#!/usr/bin/env python3
"""Refresh benchmark marks from free primary sources into _data/marks.yml.

Every endpoint here is published by the primary source, is free, and needs no
API key. Run daily by .github/workflows/refresh-marks.yml.

Design rules:
  * A mark is only written if it parses cleanly AND passes a sanity band.
  * On any failure the previous value is preserved untouched — a stale-but-true
    mark is always better than a wrong one, and the `asof` date makes the
    staleness visible on the page.
  * Every mark carries its own asof date and source label.
"""

import csv, io, json, re, sys, urllib.request, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_data" / "marks.yml"
UA = {"User-Agent": "RiskMaverick-marks-refresh/1.0 (+https://riskmaverick.com)"}
TIMEOUT = 45


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read().decode("utf-8", errors="replace")


def fmt_date(d):
    """Portable '5 Jul 2026' — %-d is glibc-only and fails on Windows."""
    return f"{d.day} {d:%b %Y}"


def band(name, value, lo, hi):
    """Reject implausible values — a parser that silently grabs the wrong
    column is more dangerous than no update at all."""
    if not (lo <= value <= hi):
        raise ValueError(f"{name} out of band: {value} not in [{lo}, {hi}]")
    return value


# ── Fetchers: each returns (price_string, asof_string, source) ───────────

def henry_hub():
    rows = [r for r in csv.reader(io.StringIO(get(
        "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DHHNGSP"))) if len(r) == 2]
    for date, val in reversed(rows[1:]):
        if val not in (".", ""):
            v = band("henry_hub", float(val), 0.5, 40)
            d = datetime.date.fromisoformat(date)
            return f"${v:.2f}", fmt_date(d), "EIA"
    raise ValueError("no Henry Hub observation")


def treasury():
    year = datetime.date.today().year
    txt = get("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
              f"daily-treasury-rates.csv/{year}/all?type=daily_treasury_yield_curve&_format=csv")
    rdr = list(csv.DictReader(io.StringIO(txt)))
    if not rdr:
        raise ValueError("empty treasury csv")
    row = rdr[0]  # newest first
    d = datetime.datetime.strptime(row["Date"], "%m/%d/%Y").date()
    out = {}
    for key, col in (("us2y", "2 Yr"), ("us10y", "10 Yr"), ("us30y", "30 Yr")):
        v = band(key, float(row[col]), 0.0, 20.0)
        out[key] = (f"{v:.2f}%", fmt_date(d), "US Treasury")
    return out


def sofr():
    d = json.loads(get("https://markets.newyorkfed.org/api/rates/secured/sofr/last/1.json"))
    r = d["refRates"][0]
    v = band("sofr", float(r["percentRate"]), 0.0, 20.0)
    dt = datetime.date.fromisoformat(r["effectiveDate"])
    return f"{v:.2f}%", fmt_date(dt), "NY Fed"


def estr():
    txt = get("https://data-api.ecb.europa.eu/service/data/EST/B.EU000A2X2A25.WT"
              "?lastNObservations=1&format=csvdata")
    row = list(csv.DictReader(io.StringIO(txt)))[-1]
    v = band("estr", float(row["OBS_VALUE"]), -2.0, 20.0)
    dt = datetime.date.fromisoformat(row["TIME_PERIOD"])
    return f"{v:.3f}%", fmt_date(dt), "ECB"


def german_power():
    d = json.loads(get("https://api.energy-charts.info/price?bzn=DE-LU"))
    px = [x for x in d["price"] if x is not None]
    if len(px) < 20:
        raise ValueError("too few German price points")
    avg = band("de_da", sum(px) / len(px), -500, 3000)
    lo, hi = min(px), max(px)
    dt = datetime.datetime.fromtimestamp(d["unix_seconds"][len(d["unix_seconds"]) // 2], datetime.timezone.utc).date()
    return (f"€{avg:,.2f}", fmt_date(dt), "SMARD",
            {"low": round(lo, 2), "high": round(hi, 2), "points": len(px)})


def lme(field, key, lo, hi):
    html = get(f"https://www.westmetall.com/en/markdaten.php?action=table&field={field}")
    cells = re.findall(r"<td[^>]*>([^<]{3,16})</td>", html)
    for i, c in enumerate(cells):
        m = re.match(r"^\s*(\d{1,2})\.\s*([A-Za-z]+)\s*(\d{4})\s*$", c)
        if m and i + 1 < len(cells):
            v = float(cells[i + 1].strip().replace(",", ""))
            v = band(key, v, lo, hi)
            dt = datetime.datetime.strptime(
                f"{m.group(1)} {m.group(2)[:3]} {m.group(3)}", "%d %b %Y").date()
            return f"${v:,.0f}", fmt_date(dt), "LME"
    raise ValueError(f"no {key} row parsed")


TASKS = {
    "henry_hub": henry_hub,
    "sofr": sofr,
    "estr": estr,
    "de_da": german_power,
    "lme_cu": lambda: lme("LME_Cu_cash", "lme_cu", 1000, 40000),
    "lme_al": lambda: lme("LME_Al_cash", "lme_al", 500, 15000),
}


def load_existing():
    """Parse the previous marks.yml well enough to preserve failed entries."""
    if not OUT.exists():
        return {}
    out, cur = {}, None
    for line in OUT.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\w+):\s*$", line)
        if m:
            cur = m.group(1); out[cur] = {}
        elif cur:
            kv = re.match(r'^\s+(\w+):\s*"?(.*?)"?\s*$', line)
            if kv:
                out[cur][kv.group(1)] = kv.group(2)
    return out


def main():
    marks = load_existing()
    failures = []

    for key, fn in TASKS.items():
        try:
            res = fn()
            extra = res[3] if len(res) > 3 else {}
            marks[key] = {"price": res[0], "asof": res[1], "source": res[2], **extra}
            print(f"  ok   {key:10s} {res[0]:>12s}  as of {res[1]} ({res[2]})")
        except Exception as e:
            failures.append(f"{key}: {e}")
            kept = marks.get(key, {}).get("price", "—")
            print(f"  KEEP {key:10s} {kept:>12s}  (refresh failed: {e})")

    try:
        for key, val in treasury().items():
            marks[key] = {"price": val[0], "asof": val[1], "source": val[2]}
            print(f"  ok   {key:10s} {val[0]:>12s}  as of {val[1]} ({val[2]})")
    except Exception as e:
        failures.append(f"treasury: {e}")
        print(f"  KEEP treasury curve (refresh failed: {e})")

    if not marks:
        print("FATAL: no marks at all", file=sys.stderr)
        return 1

    lines = ["# Generated by scripts/refresh_marks.py — do not edit by hand.",
             "# Each mark carries the date and publisher it came from.",
             f"# Last run: {datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d %H:%M} UTC", ""]
    for key in sorted(marks):
        lines.append(f"{key}:")
        for k, v in marks[key].items():
            lines.append(f'  {k}: "{v}"' if isinstance(v, str) else f"  {k}: {v}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)} ({len(marks)} marks, {len(failures)} failed)")
    return 0  # partial failure is not a build failure — old values persist


if __name__ == "__main__":
    sys.exit(main())
