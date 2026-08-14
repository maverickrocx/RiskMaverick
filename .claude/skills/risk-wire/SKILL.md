---
name: risk-wire
description: >
  Build and publish the daily Risk Wire and General Wire briefs for riskmaverick.com.
  Reads the morning newsletters (Economist, Bloomberg, Moneycontrol) from Gmail for
  curation, resolves every link to the publisher's own article on the web, and
  writes one markdown file per day into _news/ and _general/, and opens a pull request. Use when the user asks to run, build, write
  or publish the Risk Wire, the General Wire, the wires, or the daily brief.
---

# Risk Wire & General Wire

Publishes two daily briefs for riskmaverick.com from the same morning research pass:

- **Risk Wire** (`_news/`, `/news/`) — commodity and cross-asset risk.
- **General Wire** (`_general/`, `/general-wire/`) — everything else worth reading.

**This skill is the authoritative spec for both procedure and output format.**
`docs/risk-wire-runbook.md` holds only the benchmark-marks table and defers here
for everything else.

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

**Each publisher sends from more than one address — search the sending domains,
not the brand domain, or you will silently miss whole newsletters.**

```
from:e.economist.com newer_than:1d -is:spam
from:news.bloomberg.com OR from:message.bloomberg.com newer_than:1d -is:spam
from:mailer.moneycontrol.com newer_than:1d -is:spam
from:economictimesnews.com newer_than:1d -is:spam
```

**Search each domain in its own query.** Folding them into one long `OR` query
returns a mixed result set capped by page size, and a high-volume sender will
crowd the others out entirely — which is exactly how an editorial source gets
mistaken for a dead one.

| Publisher | Addresses | Newsletters |
|---|---|---|
| Economist | `noreply@e.economist.com`, `newsletters@e.economist.com` | World in Brief, Business in Brief, The Economist Today, This Week, Essential India, Asia Bulletin, The Insider |
| Bloomberg | `noreply@news.bloomberg.com`, `subscriptions@message.bloomberg.com` | Morning/Evening Briefing (Americas + Asia), Energy Daily, Markets Daily, Money Stuff, ETF IQ, John Authers |
| Moneycontrol | `alerts@mailer.moneycontrol.com` | Opening Bell, Closing Bell, PRO Panorama, Editor's Picks, Deals Stack |

| Economic Times | `newsletter@economictimesnews.com` | Morning Newsletter, Daily Brief, ET AI (twice daily), Politics & Nation, ET Markets, ET Wealth, Mutual Funds, Today's Paper |

Moneycontrol's Editor's Picks is also delivered via `newsletters-noreply@linkedin.com`.
It duplicates the `mailer.moneycontrol.com` send — dedupe, do not cite both.

**Economic Times sends from two addresses and only one is editorial.**
`newsletter@economictimesnews.com` carries the real newsletters and is the best
source in the mailbox for India politics, India markets and Indian AI/tech.
`newsletter@notifications-economictimes.com` is ETPrime sale promotions and
brand-partnership pitches only — skip it. Do not judge the editorial address by
the promotional one; they look alike in a subject-line scan, and ET mixes
genuine promos into the editorial address too.

Retrieve each thread and extract the headlines and article links it leads with.
Skip billing notices and account alerts.

The newsletters decide **what is worth covering** — that editorial judgement is the
thing the open web cannot reproduce, and it is why this step comes first.

**Newsletter links are tracking redirects. Never publish one.** They embed the
subscriber's personal token and they expire, so they become dead links on a
public page.

**Resolve redirects with `curl`, not `WebFetch`.** `WebFetch` is egress-blocked
for these domains; `curl -L` follows them fine and reports the destination:

```bash
curl -s -o /dev/null -w "%{http_code} -> %{url_effective}\n" \
  -A "Mozilla/5.0" -L --max-time 25 "<tracking-url>"
```

Strip everything after `?` from the resolved URL before citing it.

| Publisher | Link form in the email | What to publish |
|---|---|---|
| Bloomberg | real `bloomberg.com/news/...` URL with `?cmpid=…&utm_…` | same URL, query string stripped — no curl needed |
| Economist | `click.e.economist.com/?qs=…` | curl-resolved `economist.com` URL, params stripped |
| Moneycontrol | `…sendgrid.net/ls/click?upn=…` | curl-resolved `moneycontrol.com` URL |
| Economic Times | `nltrack.indiatimes.com/tracking/track/cl…` | curl-resolved `economictimes.indiatimes.com` URL |

**A 403 is fine — it means paywalled or bot-blocked, and `url_effective` is
still the real article.** A 404 is not: drop that story. Re-check every URL
before publishing.

Many newsletter items carry **no link at all** — the Economist's "In the news"
block is usually plain text. Only those need a web search to find the source
URL, and if none can be found the item cannot run: no link, no item.

Bloomberg Terminal links (`bbg://…`) are not web URLs. Where a story is
Terminal-only, cite the newsletter's own "Read in browser" URL instead.

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

## Step 4 — Write one file per day, with a section per sector

**One file per day, never one per sector.** Each brief carries a `sectors:`
list in front matter naming every sector it covers, and one `## <Chip label>`
section per sector in the body. The filter chips match against that list, so a
day tagged `[oil-products, gas-power, lng]` appears under all three.

```yaml
---
title: "Risk Wire — 14 August 2026"
date: 2026-08-14
sectors: [oil-products, gas-power, lng]
standfirst: "One or two sentences on the day's dominant themes across the sectors covered."
---

## Oil / Products {#oil-products}

*Sourced from Bloomberg's Energy Daily.*

**Bold one-line lede.** ...

## Gas & Power {#gas-power}
...
```

**Every section heading carries an explicit ID matching its slug** —
`## Gas & Power {#gas-power}`. The sector chips on the index deep-link to
`<brief-url>#<slug>`, so a missing or auto-generated ID breaks the jump.
Kramdown's auto-slug does not match: it turns "Oil / Products" into
`oil--products`, not `oil-products`. Always write the `{#slug}` yourself.

Order sections `oil-products, gas-power, lng, carbon` for Risk Wire and
`business, economics, finance, politics, tech-ai` for General Wire. Omit a
section entirely when there is no news for it — and leave the slug out of
`sectors:` too, so the chip does not promise something the brief does not
deliver.

**Risk Wire** → `_news/<YYYY-MM-DD>.md`

| Slug for `sectors:` | Chip label / section heading |
|---|---|
| `oil-products` | Oil / Products |
| `gas-power` | Gas & Power |
| `lng` | LNG |
| `carbon` | Carbon |

**General Wire** → `_general/<YYYY-MM-DD>.md`

| Slug for `sectors:` | Chip label / section heading |
|---|---|
| `business` | Business |
| `economics` | Economics |
| `finance` | Finance |
| `politics` | Politics |
| `tech-ai` | Tech / AI |

**Only write a section for a sector with real news**, and only list that sector
in `sectors:`. Two files a day is the norm — one Risk Wire, one General Wire —
each carrying however many sections the day earned. A quiet day in carbon means
no carbon section and no `carbon` in the list, not a padded one. If a whole
wire has nothing, skip that file entirely.

The `sectors:` list is the contract with the filter chips. Every slug in it
must appear in the matching page's chip list — `news.html` for `_news/`,
`general-wire.html` for `_general/`. Grep both and confirm before committing; a
slug outside the list renders but can never be filtered.

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
git add _news/<YYYY-MM-DD>.md _general/<YYYY-MM-DD>.md
git commit -m "content(wire): Risk Wire + General Wire for <D Month YYYY>"
git push -u origin wire-<YYYY-MM-DD>
```

Open the PR with `gh pr create`. In remote sessions where the `gh` CLI is
unavailable, fall back to `mcp__github__create_pull_request`. In the body state:

- which sectors were covered;
- **which stories came from Gmail and which from the web sweep**;
- any sector deliberately omitted for want of news;
- if the run was web-only, say so plainly.

Commit only the brief files, plus `_data/marks.yml` and `markets/` tiles if you
refreshed them (see runbook §3). Nothing else.
