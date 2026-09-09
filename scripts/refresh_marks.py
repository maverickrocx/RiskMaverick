#!/usr/bin/env python3
"""Refresh benchmark marks from free primary sources into _data/marks.yml.

Every mark endpoint here is published by the primary source, is free, and
needs no API key. The one optional extra is the live-feed fallback refresh,
which uses FMP_API_KEY if it is set and is silently skipped if it is not.
Run daily by .github/workflows/refresh-marks.yml, and again by the risk-wire
routine so the hub tiles are current before the brief goes out.

Design rules:
  * A mark is only written if it parses cleanly AND passes a sanity band.
  * On any failure the previous value is preserved untouched — a stale-but-true
    mark is always better than a wrong one, and the `asof` date makes the
    staleness visible on the page.
  * Every mark carries its own asof date and source label.
"""

import csv, io, json, os, re, sys, urllib.parse, urllib.request, datetime
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


_FRED_CACHE = {}


def fred(series_id):
    """Return {date: float} for a FRED/EIA daily series, skipping '.' gaps.

    Memoised: the crude tiles read Brent and WTI three times between them,
    and FRED is the flakiest endpoint here — one fetch per series per run."""
    if series_id not in _FRED_CACHE:
        rows = [r for r in csv.reader(io.StringIO(get(
            f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"))) if len(r) == 2]
        _FRED_CACHE[series_id] = {datetime.date.fromisoformat(d): float(v)
                                  for d, v in rows[1:] if v not in (".", "")}
    return _FRED_CACHE[series_id]


def _fred_last(series_id, key, lo, hi, pfx="$", dec=2):
    obs = fred(series_id)
    if not obs:
        raise ValueError(f"no {series_id} observations")
    d = max(obs)
    v = band(key, obs[d], lo, hi)
    return f"{pfx}{v:,.{dec}f}", fmt_date(d), "EIA"


def wti():
    """EIA Cushing WTI spot — the primary published US crude benchmark."""
    return _fred_last("DCOILWTICO", "wti", 5, 300)


def brent_spot():
    """EIA Europe Brent spot. Feeds the Brent-WTI tile; the Brent tile
    itself hydrates live in the browser from the market feed."""
    return _fred_last("DCOILBRENTEU", "brent_spot", 5, 300)


def brent_wti():
    """Transatlantic spread, derived from the two EIA spot series on the
    latest date both publish — never mix dates across the two legs."""
    b, w = fred("DCOILBRENTEU"), fred("DCOILWTICO")
    common = set(b) & set(w)
    if not common:
        raise ValueError("no common Brent/WTI date")
    d = max(common)
    v = band("brent_wti", b[d] - w[d], -30, 40)
    return f"${v:,.2f}", fmt_date(d), "derived"


def fed_target():
    """FOMC target range from the Board's own published series."""
    lo_s, hi_s = fred("DFEDTARL"), fred("DFEDTARU")
    d = max(set(lo_s) & set(hi_s))
    lo = band("fed_target_lo", lo_s[d], 0.0, 25.0)
    hi = band("fed_target_hi", hi_s[d], 0.0, 25.0)
    if hi < lo:
        raise ValueError(f"inverted fed target range {lo}-{hi}")
    return f"{lo:.2f}–{hi:.2f}%", fmt_date(d), "Federal Reserve"


def rggi():
    """Latest RGGI allowance auction clearing price. Quarterly, not a
    continuous quote, so the `asof` is the auction, not a trade date."""
    txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", get(
        "https://www.rggi.org/auctions/auction-results/prices-volumes")))
    m = re.search(r"Auction (\d+) (\d{4}-\d{2}-\d{2}) [\d,]+ [\d,]+ [\d,]+ \$([\d.]+)", txt)
    if not m:
        raise ValueError("no RGGI auction row parsed")
    v = band("rggi", float(m.group(3)), 1, 200)
    d = datetime.date.fromisoformat(m.group(2))
    return f"${v:,.2f}", f"Auction {m.group(1)}, {d:%b %Y}", "RGGI"


# ── Live-feed fallbacks ─────────────────────────────────────────────────
# The tiles carrying `symbol:` hydrate in the browser from FMP (see
# assets/js/rm-data.js). Their front-matter price is only the fallback shown
# when that feed is unavailable — so it still needs to be roughly current.
# Needs FMP_API_KEY in the environment; without it these are skipped, which
# is not an error: the tiles still hydrate live for real visitors.
FEED_TILES = {
    "sp500":   ("^GSPC",      "",  2, 20_000),
    "stoxx50": ("^STOXX50E",  "",  2, 20_000),
    "n225":    ("^N225",      "",  2, 200_000),
    "eurusd":  ("EURUSD",     "",  4, 10),
    "usdjpy":  ("USDJPY",     "",  2, 1_000),
    "gbpusd":  ("GBPUSD",     "",  4, 10),
    "brent":   ("BZUSD",      "$", 2, 300),
    "gold":    ("GCUSD",      "$", 2, 20_000),
}


def feed_marks():
    """Yield (key, (price, asof, source)) for each live tile's fallback."""
    api_key = os.environ.get("FMP_API_KEY")
    if not api_key:
        print("  skip live-feed fallbacks (no FMP_API_KEY set)")
        return
    for key, (sym, pfx, dec, hi) in FEED_TILES.items():
        try:
            d = json.loads(get("https://financialmodelingprep.com/stable/quote"
                               f"?symbol={urllib.parse.quote(sym)}&apikey={api_key}"))
            if not d or d[0].get("price") is None:
                raise ValueError("empty quote")
            q = d[0]
            v = band(key, float(q["price"]), 0, hi)
            ts = q.get("timestamp")
            when = (datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).date()
                    if ts else datetime.date.today())
            yield key, (f"{pfx}{v:,.{dec}f}", fmt_date(when), "market feed")
        except Exception as e:
            print(f"  KEEP {key:10s} (feed fallback refresh failed: {e})")


# ── Stale-tile report ───────────────────────────────────────────────────
# Some tiles have no free primary feed at all — grains, TTF, JKM, EUA. They
# are curated by hand, so the only thing automation can do is say out loud
# when one has drifted past its shelf life and needs a named published source.
STALE_AFTER_DAYS = 14
_BENCH_RE = re.compile(r'^\s*-\s*\{(?P<body>.*)\}\s*$')


def stale_tiles():
    """Report hand-curated benchmark tiles whose `asof` has gone stale."""
    today, out = datetime.date.today(), []
    for md in sorted((ROOT / "markets").rglob("*.md")):
        for line in md.read_text(encoding="utf-8").splitlines():
            m = _BENCH_RE.match(line)
            if not m:
                continue
            body = m.group("body")
            if "asof:" not in body or "key:" in body or "symbol:" in body:
                continue          # automated or live — not our problem
            name = re.search(r'name:\s*"([^"]*)"', body)
            asof = re.search(r'asof:\s*"([^"]*)"', body)
            if not (name and asof):
                continue
            try:
                d = datetime.datetime.strptime(asof.group(1), "%d %b %Y").date()
                age = (today - d).days
            except ValueError:
                age = None        # e.g. "Auction 72, Jun 2026" — not a date
            if age is None or age > STALE_AFTER_DAYS:
                out.append((md.relative_to(ROOT).as_posix(), name.group(1),
                            asof.group(1), age))
    return out


TASKS = {
    "henry_hub": henry_hub,
    "sofr": sofr,
    "estr": estr,
    "de_da": german_power,
    "lme_cu": lambda: lme("LME_Cu_cash", "lme_cu", 1000, 40000),
    "lme_al": lambda: lme("LME_Al_cash", "lme_al", 500, 15000),
    "wti": wti,
    "brent_spot": brent_spot,
    "brent_wti": brent_wti,
    "fed_target": fed_target,
    "rggi": rggi,
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

    for key, val in feed_marks():
        marks[key] = {"price": val[0], "asof": val[1], "source": val[2]}
        print(f"  ok   {key:10s} {val[0]:>12s}  as of {val[1]} ({val[2]})")

    if not marks:
        print("FATAL: no marks at all", file=sys.stderr)
        return 1

    # Deliberately no run timestamp: it would change on every run and commit a
    # no-op daily. Each mark's own `asof` records data freshness, and the git
    # commit date records when the refresh ran.
    lines = ["# Generated by scripts/refresh_marks.py — do not edit by hand.",
             "# Each mark carries the date and publisher it came from.", ""]
    for key in sorted(marks):
        lines.append(f"{key}:")
        for k, v in marks[key].items():
            lines.append(f'  {k}: "{v}"' if isinstance(v, str) else f"  {k}: {v}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)} ({len(marks)} marks, {len(failures)} failed)")

    stale = stale_tiles()
    if stale:
        print(f"\nHand-curated tiles needing attention "
              f"(no free feed, older than {STALE_AFTER_DAYS}d):")
        for path, name, asof, age in stale:
            age_s = f"{age}d" if age is not None else "not a date"
            print(f"  {name:16s} as of {asof:22s} ({age_s})  {path}")
        print("  Refresh each from a named published report and cite it, or leave\n"
              "  the value and its date rather than guessing "
              "(docs/risk-wire-runbook.md \u00a73).")
    else:
        print("\nAll hand-curated tiles are within their shelf life.")

    return 0  # partial failure is not a build failure — old values persist


if __name__ == "__main__":
    sys.exit(main())
