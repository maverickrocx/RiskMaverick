# Risk Wire — daily brief runbook

Supporting notes for the daily **Risk Wire** and **General Wire** briefs on
riskmaverick.com.

## 1. The format spec lives in the skill

The authoritative procedure and output format is the `risk-wire` skill
(`.claude/skills/risk-wire/SKILL.md`). Read it first and follow it exactly. It
covers the Gmail curation pass, the web verification pass, the sourcing
standard, file naming, front matter, item format and the pull-request step.

This runbook holds only what the skill defers to it: the benchmark marks below.

## 2. Sectors

One file per sector, never a combined post — the filter chips match on
`sector:`, so a combined post cannot be filtered.

**Risk Wire** → `_news/<YYYY-MM-DD>-<sector>.md`

| `sector:` | Chip label |
|---|---|
| `oil-products` | Oil / Products |
| `gas-power` | Gas & Power |
| `lng` | LNG |
| `carbon` | Carbon |

**General Wire** → `_general/<YYYY-MM-DD>-<sector>.md`

| `sector:` | Chip label |
|---|---|
| `business` | Business |
| `economics` | Economics |
| `finance` | Finance |
| `politics` | Politics |
| `tech-ai` | Tech / AI |

These slugs are the contract with `news.html` and `general-wire.html`. If you
change one, change all three together — a post whose `sector:` is not in the
page's list renders but cannot be filtered.

Only write a file for a sector with real news. Nine files is the ceiling, not
the target; four to six is a normal day.

## 3. Refresh the hub benchmark marks

The hub pages under `markets/` carry benchmark tiles. **Do not edit the prices by
hand unless the tile is on the manual list below.** Run:

```bash
python scripts/refresh_marks.py
```

It rewrites `_data/marks.yml`; a tile picks that up through its `key:` field. A
tile with `symbol:` also hydrates live in the browser from the market feed — its
`key:` only keeps the server-rendered fallback fresh for when that feed is down.
The same script runs unattended every day from
`.github/workflows/refresh-marks.yml`, and again as Step 5b of the risk-wire
routine.

### Automated — no API key, all primary publishers

| Mark(s) | `key:` | Endpoint |
|---|---|---|
| Henry Hub spot | `henry_hub` | `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DHHNGSP` (EIA series) |
| WTI spot | `wti` | `…?id=DCOILWTICO` (EIA Cushing) |
| Brent spot · Brent–WTI | `brent_spot` · `brent_wti` | `…?id=DCOILBRENTEU`; the spread is derived from the two spot series on the latest date **both** publish |
| US Treasury par yields | `us2y` `us10y` `us30y` | `https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&_format=csv` |
| SOFR | `sofr` | `https://markets.newyorkfed.org/api/rates/secured/sofr/last/1.json` |
| €STR | `estr` | `https://data-api.ecb.europa.eu/service/data/EST/B.EU000A2X2A25.WT?lastNObservations=1&format=csvdata` |
| Fed funds target range | `fed_target` | `…?id=DFEDTARL` and `…?id=DFEDTARU` |
| German day-ahead power | `de_da` | `https://api.energy-charts.info/price?bzn=DE-LU` (Bundesnetzagentur/SMARD, CC BY 4.0) |
| LME copper / aluminium cash | `lme_cu` `lme_al` | `https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_cash` (and `LME_Al_cash`) |
| RGGI allowance auction | `rggi` | `https://www.rggi.org/auctions/auction-results/prices-volumes` — quarterly, so `asof` is the auction, not a trade date |

For the German power tile, publish the **average across all quarter-hours**
returned, and keep the daily min/max in the `benchmark_note` — the spread is the
point.

### Automated fallbacks for the live tiles — needs `FMP_API_KEY`

`sp500` `stoxx50` `n225` `eurusd` `usdjpy` `gbpusd` `brent` `gold` hydrate live
in the browser. The script refreshes their server-rendered fallback from the same
feed when `FMP_API_KEY` is in the environment, and silently skips them when it is
not — that is not an error, and no primary mark depends on it.

### Manual — no free primary feed exists

**Corn, soybeans, wheat, TTF, JKM, EUA.** The script cannot price these; at the
end of every run it prints them under *"Hand-curated tiles needing attention"*
once they pass 14 days old. For each, either refresh from a **named published
report** — moving `price:` and `asof:` together, never one without the other, and
citing it in `source:` — or leave the previous value and its date rather than
guessing. A stale-but-true mark with a visible date beats a fabricated one.
