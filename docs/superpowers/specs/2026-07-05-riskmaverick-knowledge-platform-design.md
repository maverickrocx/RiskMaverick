# RiskMaverick — Knowledge Platform Redesign (Design Spec)

**Date:** 2026-07-05
**Status:** Draft for review
**Owner:** maverickrocx / riskmaverick.com

---

## 1. Purpose & positioning

Re-orient RiskMaverick.com from an advisory/consulting-led site into a **knowledge-first, article-led magazine** on financial risk management, with **commodities as the flagship specialism** and broad cross-asset coverage as the supporting library.

- **Audience:** risk managers, traders, treasury/CFO teams, and learners building risk expertise.
- **Advisory/consulting is de-emphasised** — reduced to contact details and an enquiry form on a single About page. It is no longer a headline pillar.
- **Tone:** authoritative, institutional, educational. Every claim is sourced (see §8).

### Non-goals (out of scope)
- Advisory/consulting as a marketed service line (contact only).
- Local build tooling / npm / React — the site stays statically hosted on GitHub Pages.
- Netlify or any non-GitHub-Pages host.
- A visual redesign — the existing RiskMaverick logo, dark palette and typography are **reused as-is** (see §9). New magazine templates (hubs, cards, post) inherit those tokens; only their page-level layout is new.

---

## 2. Information architecture

### Navigation
```
[RM]  Home   Markets ▾   Risk Toolkit ▾   Insights   Tools   About
      ── Topbar: live ticker (Brent · Gold · S&P · VIX) + "Get in touch" ──
```

### Page map
```
Home            featured piece + latest across markets + "browse by market" grid
│
Markets/  (flagship spine — cross-asset)
│   ├── Commodities  ★
│   │     ├── Crude & Refined     ├── Metals
│   │     ├── Natural Gas & LNG   ├── Agriculture
│   │     └── Power & Renewables  └── Carbon & Environment
│   ├── Equities
│   ├── Fixed Income (Bonds)
│   ├── FX
│   └── Interest Rates
│
Risk Toolkit/  (broad, cross-asset concept hubs)
│   ├── Market Risk            ├── Liquidity & Funding
│   ├── Hedging & Derivatives  ├── Operational Risk
│   └── Credit & Counterparty  └── Frameworks & Governance
│
Insights        full magazine feed (basics + analysis + curated web links);
│               filter by market/toolkit tag
Tools           VaR/ES calculator + volatility surface + correlation matrix + live board
About           RiskMaverick story + contact details + advisory enquiry
```

Individual articles render as standard Jekyll post pages with their own URLs; the post template is a behind-the-scenes layout, not a listed page.

### Dual-tagging mechanic (the glue)
Every post carries a **market tag** and a **concept tag** plus a `kind`:
```yaml
markets:  [natural-gas]
concepts: [hedging, market-risk]
kind: analysis        # basics | analysis | wire
```
Hubs filter the global post list with plain Liquid (GitHub-Pages-safe, **no custom plugins**):
```liquid
{% assign posts = site.posts | where_exp: "p", "p.markets contains 'natural-gas'" %}
```
One article therefore appears automatically on its market hub *and* its concept hub(s). Related-article links derive from shared tags. Insights filtering is client-side JS over `data-` attributes.

---

## 3. Jekyll repository structure

```
riskmaverick/
├── _config.yml              site config, path-scoped layout defaults
├── CNAME                    riskmaverick.com   (unchanged)
├── index.html               home layout
│
├── _layouts/
│   ├── default.html         topbar ticker + nav + footer shell
│   ├── home.html            featured + latest + market grid + toolkit strip
│   ├── hub.html             market/toolkit hub: intro + auto-listed articles
│   ├── post.html            single article (byline, tags, sources, related)
│   └── page.html            simple pages (About)
│
├── _includes/
│   ├── head.html   nav.html   ticker.html   footer.html
│   ├── article-card.html     related.html    sources.html
│
├── _posts/                  the magazine — YYYY-MM-DD-title.md
│
├── markets/                 hub pages (front-matter drives auto-listing)
│   ├── commodities/ crude-refined.md · natural-gas-lng.md · power-renewables.md
│   │                metals.md · agriculture.md · carbon-environment.md
│   ├── equities.md   fixed-income.md   fx.md   interest-rates.md
│
├── toolkit/                 market-risk.md · hedging-derivatives.md ·
│                            credit-counterparty.md · liquidity-funding.md ·
│                            operational.md · frameworks-governance.md
│
├── insights.html   tools.html   about.md
│
├── _data/
│   ├── markets.yml   toolkit.yml   wires.yml (curated external links)
│
└── assets/
    ├── css/site.css         theme extracted from today's inline CSS
    └── js/  ticker.js · tools.js · insights.js
```

**Constraints honoured:** GitHub Pages native Jekyll (no local build), whitelisted features only (no custom plugins), FMP API and key retained, CNAME preserved, dark-theme + mobile-responsive baseline (Galaxy Z Fold 7 / iPhone 17 Pro Max) carried over from current site.

---

## 4. Migration of existing content

Today's single `index.html` becomes the seed corpus — nothing is discarded.

| Today | Becomes |
|---|---|
| Commodity Knowledge Hub cards (crude / gas / power / environmental) | intro copy for matching **Commodities** sub-hubs |
| Deep pages: market / credit / operational / liquidity / framework | **Toolkit** hub copy + first "basics" posts |
| Trades page | seed posts under **Hedging & Derivatives** |
| VaR calculator + vol surface + correlation matrix + analytics | **Tools** page (logic → `tools.js`) |
| Live markets board + ticker | topbar **ticker** include + board on Tools |
| About section | **About** page (with contact + enquiry) |
| `:root` palette, Inter/JetBrains type, GSAP, inline CSS/JS | `assets/css/site.css` + `assets/js/*` |
| CNAME, FMP key/usage, per-symbol cache | preserved unchanged |

---

## 5. Insights feed composition

Insights blends three post kinds, all in one filterable feed:
1. **`basics`** — evergreen 101 explainers (markets & risk fundamentals).
2. **`analysis`** — original explanatory/analytical articles.
3. **`wire`** — curated links to authoritative external articles.

**"Around the web" (latest from the internet):** implemented as **curated link-posts** (recommended). A worthwhile external piece becomes a small `kind: wire` post + a line in `_data/wires.yml` (title · source · url · date · one-line take), surfaced in an "Around the web" module. Reliable, editorial, no API dependency.
- *Optional future add-on:* a client-side RSS widget in `insights.js` pulling an authoritative feed live. A clean hook is left for this; not built at launch.

---

## 6. Content inventory

Legend: **★** flagship · **[L]** = written in full at launch (core set) · others = titled backlog stubs.

### A. Fundamentals — basics (all [L])
Markets: What Are Commodity Markets? · How Commodity Futures Work · Reading the Forward Curve · The Commodity Value Chain · **A Map of the Financial Markets** (equities·bonds·FX·rates·commodities) · **How Markets Connect: the Cross-Asset View**
Risk: What Is Risk Management? · The Four Financial Risks · What Is Value at Risk? · Hedging 101

### B. Markets — hub overview [L] + seed articles
| Hub | Seed articles (~2/hub [L], rest backlog) |
|---|---|
| Crude & Refined ★ | Crack Spreads Explained [L] · Managing Refining-Margin Risk [L] · OPEC+ and Price Risk |
| Natural Gas & LNG ★ | The Global Gas Trinity HH·TTF·JKM [L] · Hedging LNG Cargo Risk [L] · Storage & Seasonal Spreads |
| Power & Renewables | Why Power Is the Hardest Commodity to Hedge [L] · PPAs & Renewable Risk [L] · Shape & Volume Risk |
| Metals | Base vs Precious Risk Drivers [L] · Hedging Copper Exposure [L] · Gold as a Risk Asset |
| Agriculture | Weather Risk in Ag [L] · Hedging Grain Price Risk [L] · Softs: Coffee·Sugar·Cocoa |
| Carbon & Environment | How the EU ETS Works [L] · Carbon Price Risk for Emitters [L] · Compliance vs Voluntary Markets |
| Equities | Equity Market Risk & Beta [L] · Hedging Equity Portfolios [L] · Volatility & the VIX |
| Fixed Income (Bonds) | Duration & Convexity Explained [L] · Interest-Rate Risk in Bonds [L] · Credit-Spread Risk |
| FX | Managing FX Transaction Risk [L] · Hedging FX with Forwards & Options [L] · FX in Commodity Trading |
| Interest Rates | The Yield Curve Explained [L] · Interest-Rate Swaps 101 [L] · Managing Rate Risk in Treasury |

### C. Risk Toolkit — hub overview [L] + seed articles
| Hub | Seed articles |
|---|---|
| Market Risk | VaR: Parametric·Historical·Monte Carlo [L] · Expected Shortfall & why it beats VaR [L] · Volatility & the Vol Surface · Stress Testing & Scenarios · Greeks for Commodity Options |
| Hedging & Derivatives | Futures vs Forwards vs Swaps [L] · Commodity Option Strategies [L] · Building a Hedging Programme · Hedge Accounting (IFRS 9) |
| Credit & Counterparty | Counterparty Risk in Physical Trading [L] · Credit Support: Margin·LCs·Guarantees [L] · CVA in a Nutshell |
| Liquidity & Funding | Margin Calls & the 2022 Energy Liquidity Crunch [L] · Funding vs Market Liquidity [L] · Liquidity Risk in Trading |
| Operational | Operational Risk in Commodity Trading [L] · Rogue Trading & Controls [L] · Three Lines of Defence |
| Frameworks & Governance | Building a Risk Framework [L] · Risk Appetite & Limits [L] · Basel for Commodity Firms · Model Risk Management |

### D. Tools page
VaR/ES calculator · volatility surface · correlation matrix · live markets board (all ported from current site).

### E. Around the web
Seeded with ~6 curated links to approved sources (see §8).

**Launch core set ≈ 58 fully written pieces** (16 hub overviews + 10 fundamentals + ~2 flagship articles per hub = 32); remaining titles ship as "coming soon" backlog stubs. Full inventory ≈ 78 pieces.

---

## 7. Tools page

Ports today's interactive machinery, content-secondary:
- Parametric VaR / Expected Shortfall calculator (existing math retained).
- Volatility surface heatmap + correlation matrix.
- Live markets board (FMP; live-supported symbols only — Brent, Gold, Silver, FX, indices).
- Reuses the shared per-symbol FMP cache (localStorage + in-memory) to protect the free-tier quota.

---

## 8. Sourcing & attribution standard

**Every piece of knowledge content must be grounded in credible, authoritative sources, with credit and links to the original.**

### Approved-source whitelist (only these classes)
- **Official / multilateral:** IEA, EIA, IMF, World Bank, OECD, BIS & Basel Committee, central banks (Fed, ECB, BoE), EU Commission, national energy/statistics agencies.
- **Exchanges & price-reporting agencies:** CME, ICE, LME, S&P Global Platts, Argus.
- **Tier-1 media/data:** Bloomberg, Reuters, Financial Times.
- **Major consultancies:** McKinsey, BCG, Bain, Oliver Wyman, Deloitte, PwC, EY, KPMG.
- **Standards/professional bodies:** IFRS Foundation, GARP, ISDA.
- **Academic:** university/journal publications and working papers.

**Excluded:** unknown blogs, content farms, low-authority or anonymous sources.

### Attribution rules
- Each article ends with a **"Sources & further reading"** block; each entry names the publisher and links to the original.
- Structured front-matter `sources: [{title, publisher, url}]` on every post.
- Content is original explanation; sources are paraphrased and credited, never copied.

### Integrity commitment
- **No fabricated citations.** During the build, each link is verified via web search.
- Where a specific deep URL cannot be verified, cite the institution at a stable landing level (e.g., the IEA Oil Market Report page) rather than invent a precise link.

---

## 9. Brand & visual identity (locked)

Reuse the existing RiskMaverick identity — no redesign:
- **Logo:** `logo-falcon-blue.png` (the falcon mark; also the favicon). Carried into `assets/` and used in nav + footer.
- **Palette (unchanged):** bg `#0a0f1e` · surface `#111827` · border `#1f2937` · cyan `#00d4ff` · amber `#f59e0b` · green `#10b981` · red `#ef4444` · text `#f9fafb` / `#9ca3af`.
- **Typography (unchanged):** Inter (800 headlines / 400 body / 600 uppercase labels) + JetBrains Mono for data/prices.
- **Theme:** dark only; "Bloomberg-grade" aesthetic retained.

Templates and per-page layout are new (magazine hubs/cards/post), but they inherit these tokens from `assets/css/site.css`, extracted from today's inline CSS `:root`.

## 10. Deferred decisions (next discussion)

- Optional live RSS widget for "Around the web".
- Author identity/bylines and any multi-author setup.

---

## 11. Success criteria

- Static Jekyll site builds cleanly on GitHub Pages with no custom plugins; `riskmaverick.com` (CNAME) preserved.
- Navigation exposes both spines; every hub auto-lists its tagged articles.
- ~58 fully-written, sourced pieces at launch; backlog titles visible as stubs.
- Every article carries a verifiable "Sources & further reading" block from the approved whitelist.
- Tools (VaR/ES, heatmaps, live board) function using the retained FMP integration and shared cache.
- Responsive (Galaxy Z Fold 7 / iPhone 17 Pro Max) with no horizontal overflow; dark theme baseline.
