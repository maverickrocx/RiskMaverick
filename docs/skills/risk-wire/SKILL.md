---
name: risk-wire
description: >
  Build and publish the daily Risk Wire and General Wire briefs for riskmaverick.com.
  Reads the morning newsletters (Economist, Bloomberg, Economic Times, Moneycontrol)
  from Gmail for curation, verifies every figure and resolves every link against the
  publisher's own article on the web, writes one markdown file per sector into _news/
  and _general/, and opens a pull request. Use when the user asks to run, build, write
  or publish the Risk Wire, the General Wire, the wires, or the daily brief.
---

# Risk Wire & General Wire

Publishes two daily briefs for riskmaverick.com from the same morning research pass:

- **Risk Wire** (`_news/`, `/news/`) — commodity and cross-asset risk.
- **General Wire** (`_general/`, `/general-wire/`) — everything else worth reading.

`docs/risk-wire-runbook.md` in the repo is the authoritative format spec. Read it
first. This skill is the operational procedure; the runbook governs the output.

---

## Step 0 — Check what channels you have

Run `date -u +%Y-%m-%d`. **Never assume the date.** If briefs for today already
exist, update them rather than duplicating.

Then establish whether Gmail is reachable in this session — look for a Gmail
search/read tool in your tool list.

- **Gmail present** → full pass. Both channels. This is the intended run.
- **Gmail absent** → *stop and tell the user* before writing anything. A web-only
  edition loses the newsletter curation that distinguishes these briefs. Ask
  whether they want it published web-only and labelled as such, or would rather
  run from a session that has Gmail. Do not decide this for them, and never
  attribute anything to a newsletter you did not read.

If Gmail is missing and you want to know why, check `cat /tmp/mcp-config-*.json`
for the servers actually provisioned, and the process's `--allowed-tools` flag for
the MCP prefixes permitted. Neither is editable from inside the session.

---

## Step 1 — Gmail: curation

Search each publisher separately over the last 24 hours. Do not use a catch-all.

```
from:economist.com newer_than:1d -is:spam
from:bloomberg.com newer_than:1d -is:spam
from:economictimes.com newer_than:1d -is:spam
from:moneycontrol.com newer_than:1d -is:spam
```

Retrieve each thread and extract the headlines and article links it leads with.
Skip billing notices and account alerts.

The newsletters decide **what is worth covering** — that editorial judgement is the
thing the open web cannot reproduce, and it is why this step comes first.

Economist links arrive as `click.e.economist.com` redirects. Resolve each to its
real `economist.com` URL before citing. Never cite the redirect.

---

## Step 2 — Web: resolution and verification

For every story taken from a newsletter, find the publisher's own article and
verify the numbers against it. **Newsletter copy is abridged and sometimes a day
stale; the article governs.**

Then sweep the web for anything market-moving the newsletters missed and fold it in.

Practical notes:
- `WebFetch` is egress-blocked for most publisher domains. `WebSearch` works. Try
  both before reporting a source unreachable.
- Where a publisher is paywalled, a major wire or official body (Reuters, FT, CNBC,
  IEA, EIA, OPEC, BIS, central banks, CME/ICE/LME, BLS) is an acceptable substitute.
  Prefer the primary body for anything statistical.

---

## Step 3 — Sourcing standard (non-negotiable)

- **Every item carries a real, working link.** No link, no item.
- **Every summary in your own words.** Figures (prices, dates, percentages) are
  fine verbatim; prose is not.
- **Never invent** a number, quote or link. Unsure of a figure → omit it. A
  shorter fully-sourced brief beats a longer shaky one.
- **Never cite** unknown blogs, SEO farms, AI-generated aggregators or forums.

---

## Step 4 — Write one file per sector

One file per sector, never a combined post — the filter chips match on `sector:`,
so a combined post cannot be filtered.

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

**Only write a file for a sector with real news.** Nine files is the ceiling, not
the target — four to six is a normal day. A quiet day in carbon means no carbon
post, not a padded one.

Front matter:

```yaml
---
title: "Risk Wire — <Chip label>, <D Month YYYY>"
date: <YYYY-MM-DD>
sector: <slug>
standfirst: "One sentence on this sector's dominant theme today."
---
```

General Wire uses `title: "General Wire — <Chip label>, <D Month YYYY>"`.

---

## Step 5 — Item format

Two or three items per file:

```markdown
**Bold one-line lede.** Two or three sentences of fact, with the actual numbers.
— [Publisher](https://url) · [Publisher](https://url)

*Risk lens:* **Bullish** — one or two lines on what this does to a risk book:
basis, volatility, liquidity, hedge effectiveness, chokepoint exposure.
```

**The lens sits below the link and opens with Bullish, Bearish or Neutral.** This
ordering is deliberate — facts and attribution first, then opinion, visibly
separate. Do not reverse it.

- **Risk Wire only.** General Wire items are plain summaries, no lens, no call.
- Name what the call is about when ambiguous: "Bearish (front-month TTF)".
- No genuine risk implication → omit the lens rather than manufacture one.
- Never phrase a call so it reads as something the cited publisher said.

**Do not put a disclaimer in the brief files.** The personal-opinion caveat renders
once at the foot of every Risk Wire page from `_layouts/news.html` (`.nws-caveat`).

---

## Step 6 — Open a pull request

Never push to `main`.

```bash
git checkout -b wire-<YYYY-MM-DD>
git add _news/<YYYY-MM-DD>-*.md _general/<YYYY-MM-DD>-*.md
git commit -m "content(wire): Risk Wire + General Wire for <D Month YYYY>"
git push -u origin wire-<YYYY-MM-DD>
```

Open the PR with `mcp__github__create_pull_request` (the `gh` CLI is unavailable in
remote sessions). In the body state:

- which sectors were covered;
- **which stories came from Gmail and which from the web sweep**;
- any sector deliberately omitted for want of news;
- if the run was web-only, say so plainly.

Commit only the brief files, plus `_data/marks.yml` and `markets/` tiles if you
refreshed them (see runbook §8). Nothing else.
