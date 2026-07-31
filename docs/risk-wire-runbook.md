# Risk Wire — daily brief runbook

Instructions for the scheduled agent that writes the daily **Risk Wire** brief for
riskmaverick.com. Follow these steps exactly.

## 1. Learn the format

Read [`_news/2026-07-28.md`](../_news/2026-07-28.md) — it is the reference template.
Match its structure, tone and markdown conventions exactly. `news.html` and
`_layouts/news.html` show how it renders.

## 2. Get today's real date

Run `date -u +%Y-%m-%d`. **Never assume or infer the date.** If a brief for today
already exists, update it rather than creating a duplicate.

## 3. Research

Use several `WebSearch` calls to find the most significant market-moving developments
of the **last ~24 hours** across:

- Crude oil & refined products
- Natural gas & LNG
- Power & carbon
- Metals (base and precious)
- Macro / cross-asset — central banks, rates, FX, equities

Prioritise what matters to a **risk manager**: price moves *and their drivers*,
volatility, supply disruption, chokepoints, policy and regulatory change, margin and
liquidity events. Skip generic market-recap filler.

## 4. Sourcing standard (strict, non-negotiable)

- **Use only authoritative sources**: major wires and business press (Reuters,
  Bloomberg, FT, CNBC, Fortune); official bodies (IEA, EIA, OPEC, World Bank, BIS,
  central banks, CME/ICE/LME); reputable research (S&P Global, J.P. Morgan Research,
  McKinsey, Ember, Oxford Institute for Energy Studies).
- **Never cite** unknown blogs, SEO content farms, AI-generated aggregator sites or
  forums.
- **Every item must carry a real, working link** to its source. If you cannot find
  one, drop the item.
- **Write every summary in your own words.** Never copy sentences from the article.
  Short factual figures (prices, dates, percentages) are fine; prose is not.
- **Never invent** a number, quote, or link. If you are unsure of a figure, omit it.
  A shorter, fully-sourced brief is better than a longer, shakier one.

## 5. Write the brief

Create `_news/<YYYY-MM-DD>.md` with front matter:

```yaml
---
title: "Risk Wire — <D Month YYYY>"
date: <YYYY-MM-DD>
standfirst: "One sentence on the day's dominant risk theme."
---
```

Then 3–5 sections, using only those with real news (omit empty ones):

`## ⚡ Energy — oil`, `## 🔥 Gas & LNG`, `## 🔌 Power & carbon`, `## 🪙 Metals`,
`## 📊 Macro & cross-asset`

Each item follows this shape:

```markdown
**Bold one-line lede.** Two or three sentences of fact, with the actual numbers.
*Risk lens:* one line on what it means for a risk book — basis, volatility,
liquidity, hedge effectiveness, chokepoint exposure.
— [Publisher](https://url) · [Publisher](https://url)
```

Aim for 6–10 items total. The *Risk lens* line is what makes this RiskMaverick and
not a generic news feed — include it wherever there is a genuine risk implication,
and leave it out where there isn't rather than padding.

## 5b. Refresh the hub benchmark marks

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

## 6. Open a pull request

Do **not** push to `main`. Create a branch, commit only the new
`_news/<date>.md` file, and open a PR:

```bash
git checkout -b risk-wire-<YYYY-MM-DD>
git add _news/<YYYY-MM-DD>.md
git commit -m "content(news): Risk Wire brief for <D Month YYYY>"
git push -u origin risk-wire-<YYYY-MM-DD>
gh pr create --title "Risk Wire — <D Month YYYY>" --body "Automated daily brief. Review sources and merge to publish."
```

Do not modify any other file in the repository.

If research turns up genuinely little (a holiday or quiet session), still publish a
short brief and say so in the standfirst rather than padding it out.
