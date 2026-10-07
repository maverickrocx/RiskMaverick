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

The sector slugs, file naming (one file per day per wire, with a `sectors:`
list) and section headings are all specified in the skill, Step 4. They are the
contract with the chip lists in `news.html` and `general-wire.html`.

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
| EUA (both tiles) | `eua` | `https://public.eex-group.com/eex/eua-auction-report/emission-spot-primary-market-auction-report-<year>-data.xlsx` — latest successful EU ETS primary auction on EEX; an auction clearing price, not the ICE December future |

### Automated — public delayed feed, no API key

CBOT and ICE Endex publish no free feed, so these come from Yahoo Finance's
public chart endpoint (`query1.finance.yahoo.com/v8/finance/chart/<symbol>`);
the tile's source reads "… via Yahoo" so nobody mistakes it for the exchange.

| Mark | `key:` | Symbol |
|---|---|---|
| Corn · Soybeans · Wheat (CBOT front-month, ¢/bu → $/bu) | `corn` `soybeans` `wheat` | `ZC=F` `ZS=F` `ZW=F` |
| TTF (ICE Endex front-month, €/MWh) | `ttf` | `TTF=F` |

For the German power tile, publish the **average across all quarter-hours**
returned, and keep the daily min/max in the `benchmark_note` — the spread is the
point.

### Automated fallbacks for the live tiles — needs `FMP_API_KEY`

`sp500` `stoxx50` `n225` `eurusd` `usdjpy` `gbpusd` `brent` `gold` hydrate live
in the browser. The script refreshes their server-rendered fallback from the same
feed when `FMP_API_KEY` is in the environment, and silently skips them when it is
not — that is not an error, and no primary mark depends on it.

### Manual — no free feed exists

**JKM only.** Platts is proprietary and no public feed carries it. The script
prints it under *"Hand-curated tiles needing attention"* once it passes 14 days
old. The wire routine refreshes it whenever a Bloomberg article or newsletter it
read that day, or another named public report, quotes a JKM level: move
`price:` and `asof:` together in `markets/commodities/natural-gas-lng.md`,
set `source:` to the publisher, and say so in the PR body. If no source quotes
a level, leave the previous value and its date — a stale-but-true mark with a
visible date beats a fabricated one.
