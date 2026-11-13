#!/usr/bin/env python3
"""Build the KPI band data for the Gas & Power Map country briefs.

For each country this writes _data/emap/<code>.json, which
_includes/emap-kpis.html renders at the top of the brief:

  * power price: year-to-date average and change on the same period last year
  * monthly power and gas prices: this year, last year and the three-year
    average of the years before that, pre-drawn as SVG polyline points
  * generation mix year to date, by source
  * installed capacity by fuel (for the infrastructure section)
  * net cross-border flows by neighbour, year to date

European data comes from Energy-Charts (Fraunhofer ISE), whose API needs no
key. The gas line is the ICE Endex TTF front month via Yahoo's public chart
feed, the same series as the hub's TTF tile. Manual inputs that no free feed
covers (gas storage, for example) live in _data/emap_manual.yml and are
merged in by the include, not here.

    python scripts/country_kpis.py            # every configured country
    python scripts/country_kpis.py deu fra    # just these

A country whose fetch fails keeps its previous JSON file untouched.
"""
import datetime as dt
import json
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_data" / "emap"
EC = "https://api.energy-charts.info"
UA = {"User-Agent": "Mozilla/5.0 (RiskMaverick country-kpis)"}

# Per-country sources. power/mix/capacity/flows default to Energy-Charts;
# Great Britain is not in Energy-Charts' price or mix data, so it reads
# Elexon (BMRS) for power and the ONS-published System Average Price for gas.
EU = {"gas": ("yahoo", "TTF=F"), "gas_label": "TTF front month", "ccy": "€"}
AGSI = {"deu": "de", "fra": "fr", "nld": "nl", "bel": "be", "ita": "it", "esp": "es",
        "dnk": "dk"}  # Norway and Finland have none; Sweden's is negligible; GB stopped reporting
COUNTRIES = {
    "deu": dict(EU, ec="de", bzn="DE-LU"),
    "fra": dict(EU, ec="fr", bzn="FR"),
    # Energy-Charts' Dutch feed files solar under "Others", so the Dutch mix
    # comes from CBS monthly statistics instead. (Belgium's nuclear series
    # has empty hours, but they match Elia's own data: reactors offline.)
    "nld": dict(EU, ec="nl", bzn="NL", mix="cbs"),
    "bel": dict(EU, ec="be", bzn="BE"),
    "ita": dict(EU, ec="it", bzn="IT-North"),
    "esp": dict(EU, ec="es", bzn="ES"),
    "nor": dict(EU, ec="no", bzn="NO2"),
    "swe": dict(EU, ec="se", bzn="SE3"),
    "dnk": dict(EU, ec="dk", bzn="DK1"),
    "fin": dict(EU, ec="fi", bzn="FI"),
    "gbr": dict(ec="uk", bzn="GB", power="elexon", mix="elexon", capacity=None,
                gas=("ons_sap", None), gas_label="NBP System Average Price", ccy="£"),
}

MIX = [  # (label, Energy-Charts production types, colour)
    ("Coal", ["Fossil brown coal / lignite", "Fossil hard coal", "Fossil coal-derived gas"], "#eb6834"),
    ("Gas", ["Fossil gas"], "#4a3aa7"),
    ("Nuclear", ["Nuclear"], "#c0392b"),
    ("Solar", ["Solar"], "#eda100"),
    ("Wind", ["Wind onshore", "Wind offshore"], "#2a78d6"),
    ("Hydro", ["Hydro Run-of-River", "Hydro water reservoir"], "#1f9aa5"),
    ("Other", ["Biomass", "Waste", "Fossil oil", "Geothermal", "Others", "Other renewables"], "#9AA8AC"),
]
RENEWABLE = {"Solar", "Wind", "Hydro"}
CAPACITY = [  # (label, Energy-Charts installed_power types)
    ("Solar", ["Solar AC"]), ("Wind onshore", ["Wind onshore"]), ("Wind offshore", ["Wind offshore"]),
    ("Gas", ["Fossil gas"]), ("Coal", ["Fossil brown coal / lignite", "Fossil hard coal"]),
    ("Nuclear", ["Nuclear"]), ("Hydro", ["Hydro"]), ("Pumped storage", ["Hydro pumped storage"]),
    ("Biomass", ["Biomass"]), ("Batteries", ["Battery storage (power)"]),
]


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
        return json.load(r)


def steps(ts):
    s = [(ts[i + 1] - ts[i]) / 3600 for i in range(len(ts) - 1)]
    return s + s[-1:]


def month_of(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m")


def power_months(bzn, start, end):
    d = get(f"{EC}/price?bzn={bzn}&start={start}&end={end}")
    acc = defaultdict(lambda: [0.0, 0.0])
    for t, p, h in zip(d["unix_seconds"], d["price"], steps(d["unix_seconds"])):
        if p is not None:
            acc[month_of(t)][0] += p * h
            acc[month_of(t)][1] += h
    return {m: v[0] / v[1] for m, v in acc.items()}, d


def gas_months(sym, y0):
    p1 = int(dt.datetime(y0, 1, 1, tzinfo=dt.timezone.utc).timestamp())
    p2 = int(dt.datetime.now(dt.timezone.utc).timestamp())
    j = get(f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}"
            f"?period1={p1}&period2={p2}&interval=1d")["chart"]["result"][0]
    acc = defaultdict(list)
    for t, c in zip(j["timestamp"], j["indicators"]["quote"][0]["close"]):
        if c:
            acc[month_of(t)].append(c)
    return {m: sum(v) / len(v) for m, v in acc.items()}


def chunks(start, end, days=7):
    a = dt.date.fromisoformat(start)
    e = dt.date.fromisoformat(end)
    while a < e:
        b = min(a + dt.timedelta(days=days), e)
        yield a, b
        a = b


ELEXON = "https://data.elexon.co.uk/bmrs/api/v1"


def elexon_prices(start, end):
    """GB day-ahead proxy: Elexon Market Index Data (APX/EPEX), half-hourly £/MWh.
    Returns [(unix_seconds, price)] sorted."""
    out = {}
    for a, b in chunks(start, end):
        d = get(f"{ELEXON}/balancing/pricing/market-index?from={a}T00:00Z&to={b}T00:00Z&dataProviders=APXMIDP")
        for r in d["data"]:
            if r["volume"] and r["volume"] > 0:
                t = int(dt.datetime.fromisoformat(r["startTime"].replace("Z", "+00:00")).timestamp())
                out[t] = r["price"]
    return sorted(out.items())


def elexon_mix(start, end):
    """Actual generation per type (AGPT), MW per half hour -> TWh by Energy-Charts-style name."""
    names = {"Biomass": "Biomass", "Fossil Gas": "Fossil gas", "Fossil Hard coal": "Fossil hard coal",
             "Fossil Oil": "Fossil oil", "Hydro Run-of-river and poundage": "Hydro Run-of-River",
             "Nuclear": "Nuclear", "Other": "Others", "Solar": "Solar", "Wind Offshore": "Wind offshore",
             "Wind Onshore": "Wind onshore"}
    twh = defaultdict(float)
    for a, b in chunks(start, end):
        d = get(f"{ELEXON}/generation/actual/per-type?from={a}T00:00Z&to={b}T00:00Z")
        for row in d["data"]:
            for x in row["data"]:
                n = names.get(x["psrType"])
                if n and x["quantity"]:
                    twh[n] += x["quantity"] * 0.5 / 1e6
    return dict(twh)


def cbs_mix(year):
    """Netherlands net production by source, CBS table 84575ENG, months of
    `year` published so far. Returns (TWh by Energy-Charts-style name, last month)."""
    base = "https://opendata.cbs.nl/ODataApi/OData/84575ENG/TypedDataSet"
    rows = get(f"{base}?$filter=substringof('{year}MM',Periods)")["value"]
    cols = {"NuclearEnergy_4": "Nuclear", "Coal_6": "Fossil hard coal", "PetroleumProducts_7": "Fossil oil",
            "NaturalGas_8": "Fossil gas", "Biomass_9": "Biomass", "OtherFuelsNonRenewable_10": "Others",
            "HydroPower_11": "Hydro Run-of-River", "WindEnergyOnShore_13": "Wind onshore",
            "WindEnergyOffShore_14": "Wind offshore", "SolarPhotovoltaic_15": "Solar", "OtherSources_16": "Others"}
    twh, last = defaultdict(float), 0
    for r in rows:
        if r.get("NetProductionTotal_3") is None:
            continue
        last = max(last, int(r["Periods"].strip()[-2:]))
        for c, n in cols.items():
            twh[n] += (r.get(c) or 0) / 1000  # GWh -> TWh
    return dict(twh), last


def agsi(cc, day):
    """Gas storage from GIE AGSI+ (needs an API key in the x-key header; set
    AGSI_KEY, or run where a proxy injects it). Latest gas day on or before
    `day`, with the same day one year earlier and the five-year average."""
    import os
    hdr = dict(UA)
    if os.environ.get("AGSI_KEY"):
        hdr["x-key"] = os.environ["AGSI_KEY"]

    def one(d):
        u = f"https://agsi.gie.eu/api?country={cc}&from={d - dt.timedelta(days=6)}&to={d}&size=7"
        with urllib.request.urlopen(urllib.request.Request(u, headers=hdr), timeout=60) as r:
            rows = [x for x in json.load(r).get("data", []) if x.get("full") not in (None, "", "-")]
        return max(rows, key=lambda x: x["gasDayStart"]) if rows else None

    now = one(day)
    if not now:
        return None
    d0 = dt.date.fromisoformat(now["gasDayStart"])
    past = [one(d0.replace(year=d0.year - k)) for k in range(1, 6)]
    past_full = [float(x["full"]) for x in past if x]
    return {"full": round(float(now["full"]), 1), "twh": round(float(now["gasInStorage"]), 1),
            "capacity_twh": round(float(now["workingGasVolume"]), 1), "gas_day": d0.strftime("%-d %b %Y"),
            "prev_year": round(past_full[0], 1) if past_full else None,
            "avg5": round(sum(past_full) / len(past_full), 1) if len(past_full) == 5 else None}


def ons_sap_months():
    """GB System Average Price of gas (National Gas Transmission, via ONS), p/kWh -> £/MWh."""
    import io, re, openpyxl
    page = urllib.request.urlopen(urllib.request.Request(
        "https://www.ons.gov.uk/economy/economicoutputandproductivity/output/datasets/systemaveragepricesapofgas",
        headers=UA), timeout=60).read().decode("utf-8", "ignore")
    href = re.search(r'href="(/file\?uri=[^"]+\.xlsx)"', page).group(1)
    raw = urllib.request.urlopen(urllib.request.Request("https://www.ons.gov.uk" + href, headers=UA), timeout=120).read()
    ws = openpyxl.load_workbook(io.BytesIO(raw), read_only=True, data_only=True)["1.Daily SAP Gas"]
    acc = defaultdict(list)
    for row in ws.iter_rows(values_only=True):
        if isinstance(row[0], dt.datetime) and isinstance(row[1], (int, float)):
            acc[row[0].strftime("%Y-%m")].append(row[1] * 10)
    return {m: sum(v) / len(v) for m, v in acc.items()}


def series(monthly, year, upto=12):
    return [monthly.get(f"{year}-{m:02d}") for m in range(1, upto + 1)]


def avg3(monthly, year):
    out = []
    for m in range(1, 13):
        v = [monthly.get(f"{y}-{m:02d}") for y in (year - 3, year - 2, year - 1)]
        v = [x for x in v if x is not None]
        out.append(sum(v) / len(v) if len(v) == 3 else None)
    return out


def chart(lines):
    """Pre-draw a 12-month line chart: returns axis ticks and polyline points
    in a 600x220 viewBox (plot area x 46..588, y 16..188)."""
    vals = [v for _, s in lines for v in s if v is not None]
    top = max(vals) * 1.08
    step = next(s for s in (5, 10, 20, 25, 50, 100, 200) if top / s <= 5)
    ymax = step * -(-top // step)
    y = lambda v: 188 - (v / ymax) * 172
    x = lambda i: 46 + i * (542 / 11)
    out = {"ticks": [{"v": int(k * step), "y": round(y(k * step), 1)}
                     for k in range(int(ymax // step) + 1)], "lines": {}}
    for key, s in lines:
        pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(s) if v is not None)
        out["lines"][key] = pts
    return out


def build(code, today):
    cfg = COUNTRIES[code]
    ec_c, bzn = cfg["ec"], cfg["bzn"]
    y = today.year
    end = today.isoformat()
    ytd_start, py_end = f"{y}-01-01", today.replace(year=y - 1).isoformat()

    def prices(s, e):
        if cfg.get("power") == "elexon":
            pts = elexon_prices(s, e)
            ts, pr = [t for t, _ in pts], [p for _, p in pts]
        else:
            d = get(f"{EC}/price?bzn={bzn}&start={s}&end={e}")
            ts, pr = d["unix_seconds"], d["price"]
        return ts, pr

    ts, pr = prices(f"{y - 3}-01-01", end)
    acc = defaultdict(lambda: [0.0, 0.0])
    for t, p, h in zip(ts, pr, steps(ts)):
        if p is not None:
            acc[month_of(t)][0] += p * h
            acc[month_of(t)][1] += h
    pm = {m: v[0] / v[1] for m, v in acc.items()}

    gsrc, gsym = cfg["gas"]
    gm = ons_sap_months() if gsrc == "ons_sap" else gas_months(gsym, y - 3)

    # Year-to-date average versus the same days last year, time-weighted.
    def avg(s, e):
        ts, pr = prices(s, e)
        num = den = neg = 0.0
        for p, h in zip(pr, steps(ts)):
            if p is not None:
                num += p * h; den += h; neg += h if p < 0 else 0
        return num / den, neg
    ytd, neg = avg(ytd_start, end)
    pytd, pneg = avg(f"{y - 1}-01-01", py_end)

    period = f"1 Jan – {today.strftime('%-d %b')} {y}"
    if cfg.get("mix") == "elexon":
        twh = elexon_mix(ytd_start, end)
    elif cfg.get("mix") == "cbs":
        twh, last = cbs_mix(y)
        period = f"Jan – {dt.date(y, last, 1).strftime('%b')} {y}"
    else:
        gen = get(f"{EC}/public_power?country={ec_c}&start={ytd_start}&end={end}")
        st = steps(gen["unix_seconds"])
        twh = {p["name"]: sum(v * h for v, h in zip(p["data"], st) if v is not None) / 1e6
               for p in gen["production_types"]}
    mix = []
    for label, names, colour in MIX:
        v = sum(max(twh.get(n, 0), 0) for n in names)
        mix.append({"label": label, "twh": round(v, 1), "colour": colour})
    total = sum(m["twh"] for m in mix)
    x = 0.0
    for m in mix:
        m["pct"] = round(100 * m["twh"] / total, 1)
        m["x"] = round(x, 2)
        m["w"] = round(m["twh"] / total * 100, 2)
        x += m["w"]

    capacity, cap_year = [], None
    if cfg.get("capacity", "ec") == "ec":
        cap = get(f"{EC}/installed_power?country={ec_c}&time_step=yearly&installation_decommission=false")
        yi = [i for i, t in enumerate(cap["time"]) if int(t) <= y]
        for label, names in CAPACITY:
            v = 0.0
            for p in cap["production_types"]:
                if p["name"] in names:
                    vals = [(cap["time"][i], p["data"][i]) for i in yi if p["data"][i] is not None]
                    if vals:
                        cap_year = cap_year or vals[-1][0]
                        v += vals[-1][1]
            if v >= 0.05:
                capacity.append({"label": label, "gw": round(v, 1)})

    flows = []
    try:
        cb = get(f"{EC}/cbpf?country={ec_c}&start={ytd_start}&end={end}")
        cst = steps(cb["unix_seconds"])
        for c in cb["countries"]:
            if c["name"].lower() == "sum":
                continue
            flows.append({"name": c["name"],
                          "twh": round(sum(v * h for v, h in zip(c["data"], cst) if v is not None) / 1000, 1)})
        flows.sort(key=lambda f: -abs(f["twh"]))
    except Exception as e:  # cross-border data is optional
        print(f"  {code}: no cross-border flows ({e})")

    storage = None
    if code in AGSI:
        try:
            storage = agsi(AGSI[code], today)
        except Exception as e:
            print(f"  {code}: no storage ({e})")

    m_now = today.month
    p_lines = [("cur", series(pm, y, m_now)), ("prev", series(pm, y - 1)), ("avg", avg3(pm, y))]
    g_lines = [("cur", series(gm, y, m_now)), ("prev", series(gm, y - 1)), ("avg", avg3(gm, y))]
    return {
        "asof": today.strftime("%-d %B %Y"),
        "period": period, "price_period": f"1 Jan – {today.strftime('%-d %b')} {y}",
        "year": y, "prev_year": y - 1, "avg_years": f"{y - 3}–{str(y - 1)[2:]}",
        "bzn": bzn, "gas_label": cfg["gas_label"], "ccy": cfg["ccy"],
        "power_ytd": round(ytd, 1), "power_pytd": round(pytd, 1),
        "power_yoy": round(100 * (ytd / pytd - 1)),
        "neg_hours": round(neg), "neg_hours_prev": round(pneg),
        "gas_ytd": round(sum(v for v in series(gm, y, m_now) if v) / len([v for v in series(gm, y, m_now) if v]), 1),
        "renewable_pct": round(sum(m["pct"] for m in mix if m["label"] in RENEWABLE)),
        "mix": mix, "mix_total": round(total),
        "capacity": capacity, "capacity_year": cap_year,
        "flows": flows, "storage": storage,
        "power_chart": chart(p_lines), "gas_chart": chart(g_lines),
        "power_months": {k: [None if v is None else round(v, 1) for v in s] for k, s in p_lines},
        "gas_months": {k: [None if v is None else round(v, 1) for v in s] for k, s in g_lines},
    }


# ── Outside Europe ──────────────────────────────────────────────────────────
# No single feed covers these markets, so each draws on its own official
# publisher. A "price series" here is a list of (date, value) points at the
# publisher's native resolution; months and year-to-date figures are simple
# averages of those points. Gas, mix and storage are optional: when a market
# publishes no free monthly series the include leaves that panel out.
EIA = "https://www.eia.gov"
WORLD = {
    "usa": dict(power=("ice", "PJM WH Real Time Peak"), bzn="PJM West hub, peak", ccy="$",
                gas=("eia_hh",), gas_label="Henry Hub spot", gas_ccy="$", gas_unit="/MMBtu",
                mix=("eia_epm",), storage=("eia_wngsr",)),
    "can": dict(power=("aeso",), bzn="Alberta pool price", ccy="C$",
                gas=("eia_hh",), gas_label="Henry Hub spot (US reference)", gas_ccy="US$", gas_unit="/MMBtu"),
    "aus": dict(power=("aemo", "NSW1"), bzn="NEM, New South Wales", ccy="A$"),
    "jpn": dict(power=("jepx",), bzn="JEPX system price", ccy="¥", power_unit="/kWh"),
}


def xl_rows(url, sheet=0):
    import io
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
    if url.endswith(".xls"):
        import xlrd
        sh = xlrd.open_workbook(file_contents=raw).sheet_by_index(sheet)
        return [sh.row_values(i) for i in range(sh.nrows)], xlrd
    import openpyxl
    ws = openpyxl.load_workbook(io.BytesIO(raw), read_only=True, data_only=True).worksheets[sheet]
    return [list(r) for r in ws.iter_rows(values_only=True)], None


def text(url, enc="utf-8"):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read().decode(enc, "ignore")


def pts_ice(hub, y0, y1):
    """EIA's daily ICE wholesale power hub prices, $/MWh (weighted average)."""
    out = []
    for y in range(y0, y1 + 1):
        name = f"ice_electric-{y}.xlsx" if y == y1 else f"archive/ice_electric-{y}final.xlsx"
        try:
            rows, _ = xl_rows(f"{EIA}/electricity/wholesale/xls/{name}")
        except Exception:
            rows, _ = xl_rows(f"{EIA}/electricity/wholesale/xls/ice_electric-{y}final.xlsx")
        for r in rows[1:]:
            if (r and r[0] and str(r[0]).strip() == hub and isinstance(r[2], dt.datetime)
                    and isinstance(r[6], (int, float))):
                out.append((r[2].date(), float(r[6])))
    return out


def pts_eia_hh(y0):
    rows, xlrd = xl_rows(f"{EIA}/dnav/ng/hist_xls/RNGWHHDd.xls", 1)
    out = []
    for r in rows[3:]:
        if isinstance(r[0], float) and isinstance(r[1], float):
            d = dt.date(*xlrd.xldate_as_tuple(r[0], 0)[:3])
            if d.year >= y0:
                out.append((d, r[1]))
    return out


def pts_aemo(region, y0, today):
    out = []
    m = dt.date(y0, 1, 1)
    while m <= today:
        try:
            for line in text(f"https://aemo.com.au/aemo/data/nem/priceanddemand/PRICE_AND_DEMAND_{m:%Y%m}_{region}.csv").splitlines()[1:]:
                f = line.split(",")
                if len(f) > 3:
                    out.append((dt.datetime.strptime(f[1][:10], "%Y/%m/%d").date(), float(f[3])))
        except Exception as e:
            print(f"  aemo {m:%Y-%m}: {e}")
        m = (m.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
    return out


def pts_aeso(y0, today):
    out = []
    m = dt.date(y0, 1, 1)
    while m <= today:
        e = min((m.replace(day=28) + dt.timedelta(days=4)).replace(day=1) - dt.timedelta(days=1), today)
        u = ("http://ets.aeso.ca/ets_web/ip/Market/Reports/HistoricalPoolPriceReportServlet"
             f"?beginDate={m:%m%d%Y}&endDate={e:%m%d%Y}&contentType=csv")
        for line in text(u).splitlines():
            f = [x.strip('"') for x in line.split('","')]
            if len(f) >= 2 and f[0][:2].isdigit():
                try:
                    out.append((dt.datetime.strptime(f[0][:10], "%m/%d/%Y").date(), float(f[1])))
                except ValueError:
                    pass
        m = e + dt.timedelta(days=1)
    return out


def pts_jepx(y0, today):
    """JEPX day-ahead system price, ¥/kWh, half-hourly; files run by fiscal year (April)."""
    out = []
    for fy in range(y0 - 1, today.year + 1):
        try:
            for line in text(f"https://www.jepx.jp/market/excel/spot_{fy}.csv", "shift_jis").splitlines()[1:]:
                f = line.split(",")
                if len(f) > 5 and f[5]:
                    out.append((dt.datetime.strptime(f[0], "%Y/%m/%d").date(), float(f[5])))
        except Exception as e:
            print(f"  jepx {fy}: {e}")
    return out


def eia_epm():
    """US net generation by source, year to date (EIA Electric Power Monthly tables 1.1 and 1.1.A)."""
    rows, _ = xl_rows(f"{EIA}/electricity/monthly/xls/table_1_01.xlsx")
    rows_a, _ = xl_rows(f"{EIA}/electricity/monthly/xls/table_1_01_a.xlsx")
    title = rows[0][0]

    def ytd(rs, year):
        i = next(k for k, r in enumerate(rs) if r[0] == "Year to Date")
        return next(r for r in rs[i + 1:i + 4] if r[0] == year)
    y = int(title.split("-")[-1].split()[-1])
    r, a = ytd(rows, y), ytd(rows_a, y)
    month = title.split("-")[-1].split()[0]
    gwh = lambda v: (v or 0) / 1e3  # thousand MWh -> TWh
    twh = {"Fossil hard coal": gwh(r[1]), "Fossil gas": gwh(r[4]) + gwh(r[5]), "Nuclear": gwh(r[6]),
           "Hydro Run-of-River": gwh(r[7]), "Solar": gwh(r[15]), "Wind onshore": gwh(a[1]),
           "Fossil oil": gwh(r[2]) + gwh(r[3]), "Biomass": gwh(a[4]) + gwh(a[5]) + gwh(a[6]) + gwh(a[7]),
           "Geothermal": gwh(a[8]), "Others": gwh(r[11])}
    return twh, f"Jan – {month[:3]} {y}"


def eia_wngsr():
    lines = text("https://ir.eia.gov/ngs/wngsr.csv", "utf-8-sig").splitlines()
    import csv
    rows = list(csv.reader(lines))
    wk = next(r for r in rows if r and r[0].startswith("Released"))
    tot = next(r for r in rows if r and r[0] == "Total")
    hdr = next(r for r in rows if len(r) > 1 and r[1] and "-" in r[1] and r[1][0].isdigit())
    num = lambda s: float(s.replace(",", ""))
    return {"bcf": num(tot[1]), "yago_bcf": num(tot[13]), "yago_pct": num(tot[16]),
            "avg5_bcf": num(tot[19]), "avg5_pct": num(tot[22]), "week": hdr[1],
            "released": wk[0].split("Released: ")[1].split(" at")[0]}


def monthly(points):
    acc = defaultdict(list)
    for d, v in points:
        acc[d.strftime("%Y-%m")].append(v)
    return {m: sum(v) / len(v) for m, v in acc.items()}


def build_world(code, today):
    cfg = WORLD[code]
    y = today.year
    kind = cfg["power"]
    if kind[0] == "ice":
        pp = pts_ice(kind[1], y - 3, y)
    elif kind[0] == "aemo":
        pp = pts_aemo(kind[1], y - 3, today)
    elif kind[0] == "aeso":
        pp = pts_aeso(y - 3, today)
    elif kind[0] == "jepx":
        pp = pts_jepx(y - 3, today)
    pm = monthly(pp)
    cut = lambda yr: [v for d, v in pp if d.year == yr and (d.month, d.day) <= (today.month, today.day)]
    ytd, pytd = cut(y), cut(y - 1)
    out = {"asof": today.strftime("%-d %B %Y"), "price_period": f"1 Jan – {today.strftime('%-d %b')} {y}",
           "year": y, "prev_year": y - 1, "avg_years": f"{y - 3}–{str(y - 1)[2:]}",
           "bzn": cfg["bzn"], "ccy": cfg["ccy"], "power_unit": cfg.get("power_unit", "/MWh"),
           "power_ytd": round(sum(ytd) / len(ytd), 2), "power_pytd": round(sum(pytd) / len(pytd), 2),
           "neg_hours": None, "flows": [], "capacity": [], "storage": None, "mix": [], "renewable_pct": None}
    out["power_yoy"] = round(100 * (out["power_ytd"] / out["power_pytd"] - 1))
    m_now = today.month
    p_lines = [("cur", series(pm, y, m_now)), ("prev", series(pm, y - 1)), ("avg", avg3(pm, y))]
    out["power_chart"] = chart(p_lines)
    out["power_months"] = {k: [None if v is None else round(v, 2) for v in s] for k, s in p_lines}
    if cfg.get("gas"):
        gm = monthly(pts_eia_hh(y - 3))
        g_lines = [("cur", series(gm, y, m_now)), ("prev", series(gm, y - 1)), ("avg", avg3(gm, y))]
        cur = [v for v in g_lines[0][1] if v]
        out.update(gas_label=cfg["gas_label"], gas_ccy=cfg["gas_ccy"], gas_unit=cfg["gas_unit"],
                   gas_ytd=round(sum(cur) / len(cur), 2), gas_chart=chart(g_lines),
                   gas_months={k: [None if v is None else round(v, 2) for v in s] for k, s in g_lines})
    if cfg.get("mix"):
        twh, period = eia_epm()
        mix = []
        for label, names, colour in MIX:
            mix.append({"label": label, "twh": round(sum(max(twh.get(n, 0), 0) for n in names), 1), "colour": colour})
        total = sum(m["twh"] for m in mix)
        x = 0.0
        for m in mix:
            m["pct"] = round(100 * m["twh"] / total, 1); m["x"] = round(x, 2); m["w"] = round(m["twh"] / total * 100, 2)
            x += m["w"]
        out.update(mix=mix, mix_total=round(total), period=period,
                   renewable_pct=round(sum(m["pct"] for m in mix if m["label"] in RENEWABLE)))
    if cfg.get("storage"):
        try:
            out["storage_us"] = eia_wngsr()
        except Exception as e:
            print(f"  {code}: no storage ({e})")
    return out


def main():
    today = dt.date.today() - dt.timedelta(days=1)  # last complete day
    codes = sys.argv[1:] or list(COUNTRIES) + list(WORLD)
    OUT.mkdir(parents=True, exist_ok=True)
    for code in codes:
        try:
            data = build_world(code, today) if code in WORLD else build(code, today)
        except Exception as e:
            print(f"KEEP {code}: {e}")
            continue
        (OUT / f"{code}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
        print(f"ok   {code}: power YTD {data['ccy']}{data['power_ytd']}{data.get('power_unit', '/MWh')} ({data['power_yoy']:+d}%), "
              f"RES {data['renewable_pct']}%")


if __name__ == "__main__":
    main()
