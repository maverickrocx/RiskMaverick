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

### Both channels, every run

Gmail and the web are **not alternatives** — they do different jobs, and a full
run uses both:

| Channel | Job |
|---|---|
| **Gmail** | Discovery and curation. The morning newsletters decide *what is worth covering* — that editorial selection is the thing the open web cannot reproduce. |
| **Web** | Resolution and verification. Turn each selected story into a canonical, citable publisher URL, and confirm every figure against the article or the primary body. |

Run order:

1. **Gmail first.** Search the inbox for the day's newsletters from the four
   publishers. Extract the headlines and the stories each one leads with.
   Economist links arrive as `click.e.economist.com` redirects — resolve them
   to real `economist.com` URLs before citing.
2. **Web second.** For every story taken from a newsletter, find the publisher's
   article and verify the numbers. Newsletter copy is often abridged and
   sometimes a day stale; the article governs. Also sweep the web for anything
   market-moving the newsletters missed, and fold it in.
3. **State the provenance.** In the PR body, note which stories came from
   Gmail and which from the web sweep.

**If Gmail is not available in the session, stop. Do not publish.**

Check before writing anything: look for a Gmail search tool in the tool list. If
there isn't one, this run cannot produce a brief to standard, because the
newsletter curation is not an optional enhancement — it is what decides what gets
covered. A web-only edition is a different, lesser product wearing the same name.

On abort: write nothing, open no pull request, and notify the user that the run
stopped and why. A missed edition is recoverable; a published edition that
quietly lost its curation layer is not. See §7 for how to diagnose the cause.

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

Whether Gmail is reachable depends on how the session was launched. Check the
tool list rather than assuming, and do not spend a run re-diagnosing this.

**When Gmail tools are absent**, the cause is the launch configuration, not a
broken connector and not a setting the agent can change from inside:

- The MCP servers available to the session come from the file named by the
  process's `--mcp-config` flag, which the host generates at launch. Inspect it
  with `cat /tmp/mcp-config-*.json`. If it lists only `github`, no claude.ai
  connector is reachable in that session.
- The process's `--allowed-tools` flag independently gates MCP tools by prefix.
  If it permits only `mcp__github__*`, then Gmail tools would be rejected even
  if they were configured.
- Both are set at launch and are not editable from inside the container. A
  connector toggled on in the claude.ai UI does not feed either one.

**To get Gmail into a run**, launch `claude` from a local session where
`mcpServers` in `~/.claude.json` is yours to configure and no host allowlist is
imposed. Verify before relying on it: if Gmail tools appear in the tool list,
the run is Gmail-enabled; if not, it is web-only and §2 applies.

Also environmental, in every session type:

- `WebFetch` is egress-blocked for most publisher domains. `WebSearch` is not.
- `gh` CLI is unavailable. Use the `mcp__github__*` tools.

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
