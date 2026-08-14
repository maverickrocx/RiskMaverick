# Risk Wire & General Wire — daily brief runbook

Instructions for the scheduled agent that writes the two daily briefs for
riskmaverick.com. Follow these steps exactly.

There are two collections, built from the same morning research pass:

- **Risk Wire** (`_news/`, `/news/`) — commodity and cross-asset risk.
- **General Wire** (`_general/`, `/general-wire/`) — everything else worth
  reading that isn't a commodity or cross-asset risk story.

## 1. Get today's real date

Run `date -u +%Y-%m-%d`. **Never assume or infer the date.** If briefs for today
already exist, update them rather than creating duplicates.

## 2. Sources

Four publishers, in this order of preference:

| Publisher | Notes |
|---|---|
| Economist | `click.e.economist.com` redirects resolve to citable `economist.com` URLs |
| Bloomberg | |
| Economic Times | |
| Moneycontrol | |

**On Gmail.** When this runbook is executed by a *scheduled* task it runs in a
headless cloud container, where claude.ai connectors (Gmail included) are not
available — see §7. Scheduled runs therefore source these four publishers from
the open web via `WebSearch`. A human running this interactively from a local
session may read the same publishers' newsletters from Gmail instead; the
format below is identical either way. Note which channel was used in the PR
body so the provenance is on the record.

Note that `WebFetch` is blocked by the egress proxy for most publisher domains.
`WebSearch` works. Do not report a source as unavailable without trying both.

## 3. Sourcing standard (strict, non-negotiable)

- **Every item must carry a real, working link** to its source. If you cannot
  find one, drop the item.
- **Write every summary in your own words.** Never copy sentences from the
  article. Short factual figures (prices, dates, percentages) are fine; prose
  is not.
- **Never invent** a number, quote, or link. If you are unsure of a figure, omit
  it. A shorter, fully-sourced brief is better than a longer, shakier one.
- **Never cite** unknown blogs, SEO content farms, AI-generated aggregator sites
  or forums.
- Where one of the four publishers is paywalled or unreachable, a major wire or
  official body (Reuters, FT, CNBC, IEA, EIA, OPEC, BIS, central banks,
  CME/ICE/LME, BLS) is an acceptable substitute. Prefer the primary body for
  anything statistical.

## 4. Sectors — one post per sector

Write **one file per sector**, not one combined post. The filter chips on
`news.html` and `general-wire.html` match on the `sector:` field, so a combined
post cannot be filtered.

**Risk Wire** — `_news/<YYYY-MM-DD>-<sector>.md`

| `sector:` | Chip label |
|---|---|
| `oil-products` | Oil / Products |
| `gas-power` | Gas & Power |
| `lng` | LNG |
| `carbon` | Carbon |

**General Wire** — `_general/<YYYY-MM-DD>-<sector>.md`

| `sector:` | Chip label |
|---|---|
| `business` | Business |
| `economics` | Economics |
| `finance` | Finance |
| `politics` | Politics |
| `tech-ai` | Tech / AI |

**Only create a file for a sector that has real news.** A quiet day in carbon
means no carbon post — not a padded one. Do not invent coverage to fill the
grid. Nine files is the ceiling, not the target; four to six is a normal day.

## 5. Front matter

```yaml
---
title: "Risk Wire — <Chip label>, <D Month YYYY>"
date: <YYYY-MM-DD>
sector: <slug from the table above>
standfirst: "One sentence on this sector's dominant theme today."
---
```

General Wire uses `title: "General Wire — <Chip label>, <D Month YYYY>"` and the
same shape otherwise.

## 6. Item format

Two or three items per sector file. Each item:

```markdown
**Bold one-line lede.** Two or three sentences of fact, with the actual
numbers.
— [Publisher](https://url) · [Publisher](https://url)

*Risk lens:* **Bullish** — one or two lines on what this does to a risk book:
basis, volatility, liquidity, hedge effectiveness, chokepoint exposure.
```

The **Risk lens sits below the source link**, and opens with a one-word call:
**Bullish**, **Bearish** or **Neutral**. This ordering is deliberate and must not
be reversed — the facts and their attribution come first, then the opinion,
clearly marked as a separate thing.

Rules for the lens:

- **Risk Wire only.** General Wire items are plain summaries with no lens and no
  directional call.
- Name what the call is *about* when it isn't obvious — "Bearish (front-month
  TTF)" beats a bare "Bearish" on a story that touches four instruments.
- Leave the lens off an item that has no genuine risk implication rather than
  padding one on. A missing lens is better than a manufactured one.
- The call is a judgement. Never phrase it so it reads as something the cited
  publisher said.

**Do not add a disclaimer to individual brief files.** The personal-opinion
caveat is rendered once at the foot of every Risk Wire page by
`_layouts/news.html` (`.nws-caveat`). Adding it per-file duplicates it.

## 7. Environment constraints (read before diagnosing a failure)

Scheduled runs execute in a remote Claude Code container. Known and expected:

- `mcpServers` is empty in `~/.claude.json`; MCP servers are injected by the
  host. Only `github` is present. **claude.ai connectors — Gmail, Drive,
  Calendar — do not bridge into this container**, and no config change from
  inside it will make them appear. This is environmental, not a broken setting.
- `WebFetch` is egress-blocked for most publisher domains. `WebSearch` is not.
- `gh` CLI is unavailable. Use the `mcp__github__*` tools.

If Gmail-sourced content is required, that run has to happen interactively from
a local session, not from the schedule.

## 8. Refresh the hub benchmark marks

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

## 9. Open a pull request

Do **not** push to `main`. Create one branch carrying both wires:

```bash
git checkout -b wire-<YYYY-MM-DD>
git add _news/<YYYY-MM-DD>-*.md _general/<YYYY-MM-DD>-*.md
git commit -m "content(wire): Risk Wire + General Wire for <D Month YYYY>"
git push -u origin wire-<YYYY-MM-DD>
```

Then open the PR with `mcp__github__create_pull_request`. In the body, list the
sectors covered, the sourcing channel used (web or Gmail), and any sector
deliberately omitted for want of real news.

Commit only the brief files and, if refreshed, `_data/marks.yml` and the
`markets/` tiles. Do not modify anything else.

If research turns up genuinely little (a holiday or quiet session), publish the
sectors that do have news and say so in the PR body rather than padding.
