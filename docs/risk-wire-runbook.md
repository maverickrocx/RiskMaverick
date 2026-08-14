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

The hub pages under `markets/` carry benchmark tiles. Those with a `symbol:`
field hydrate live in the browser and need no attention. Those with `asof:` and
`source:` are static and must be refreshed — update the `price:` and `asof:`
together, never one without the other.

All of these are free, need no API key, and come from the primary publisher:

| Mark | Endpoint |
|---|---|
| Henry Hub spot | `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DHHNGSP` (EIA series) |
| US Treasury par yields | `https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&_format=csv` |
| SOFR | `https://markets.newyorkfed.org/api/rates/secured/sofr/last/1.json` |
| €STR | `https://data-api.ecb.europa.eu/service/data/EST/B.EU000A2X2A25.WT?lastNObservations=1&format=csvdata` |
| German day-ahead power | `https://api.energy-charts.info/price?bzn=DE-LU` (Bundesnetzagentur/SMARD, CC BY 4.0) |
| LME copper / aluminium cash | `https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_cash` (and `LME_Al_cash`) |

For the German power tile, publish the **average across all quarter-hours**
returned, and keep the daily min/max in the `benchmark_note` — the spread is the
point. TTF, JKM, EUA, Dubai, UKA and CCA have no free primary feed; refresh
those from a named published report and cite it, or leave the previous value and
its date rather than guessing.
