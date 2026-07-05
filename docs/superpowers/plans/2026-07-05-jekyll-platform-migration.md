# Jekyll Platform & Theme Migration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the single-file RiskMaverick site into a Jekyll static site (magazine structure: cross-asset Markets spine + Risk Toolkit + Insights + Tools + About) that builds on GitHub Pages, reusing the existing brand and porting the existing FMP/tools JavaScript.

**Architecture:** Jekyll (via the `github-pages` gem, so GitHub Pages auto-builds server-side; local dev uses the Ruby toolchain just installed). Two content spines are stitched by dual tags on every post (`markets:` + `concepts:`); hub pages filter `site.posts` with core Liquid — **no custom plugins**. Theme CSS/JS is extracted from today's inline `index.html` into `assets/`. This plan builds the *platform* and proves it with a handful of sample posts; full article authoring is a separate plan (Plan B).

**Tech Stack:** Ruby 3.3.11, Jekyll (via `github-pages` gem), Bundler, kramdown, Liquid. Vanilla JS for ticker/tools (no framework). FMP REST API for live data. GitHub Pages hosting.

## Global Constraints

- Host: **GitHub Pages only** (no Netlify). Production builds server-side; no local build tooling required to deploy.
- Generator: **Jekyll via the `github-pages` gem**; **NO custom plugins** — core Liquid filters only (`where_exp`, `where`, etc.).
- Preserve `CNAME` → `riskmaverick.com` unchanged.
- Brand reused as-is: logo `logo-falcon-blue.png`; palette `--bg #0a0f1e` / `--surface #111827` / `--border #1f2937` / `--cyan #00d4ff` / `--amber #f59e0b` / `--green #10b981` / `--red #ef4444` / `--white #f9fafb` / `--gray2 #9ca3af`; fonts **Inter** (800 headline / 400 body / 600 uppercase label) + **JetBrains Mono** (data). Dark theme only.
- Keep the existing **FMP API key and shared per-symbol cache** (quotes 30-min TTL, sparklines 12-h TTL; localStorage + in-memory).
- Every post's front-matter carries: `markets: [...]`, `concepts: [...]`, `kind: basics|analysis|wire`, and optional `sources: [{title, publisher, url}]`.
- Responsive: no horizontal overflow at **344px** (Z Fold 7 cover), **440px** (iPhone 17 Pro Max), **1280px** (desktop).
- Run Jekyll from **PowerShell** (Ruby is on the Windows PATH; it is not on the bash PATH). Content assertions use the Grep/Read tools against the generated `_site/`.

---

### Task 1: Project scaffold & baseline build

**Files:**
- Create: `Gemfile`
- Create: `_config.yml`
- Create: `.gitignore`
- Create: `.claude/launch.json`
- Preserve (do not modify): `index.html`, `logo-falcon-blue.png`, `M Falcon B.png`, `CNAME`

**Interfaces:**
- Produces: a buildable Jekyll project. Existing `index.html` has no front-matter, so Jekyll copies it verbatim — the live homepage is untouched until Task 8.

- [ ] **Step 1: Create the migration branch**

Run (PowerShell): `git checkout -b feat/jekyll-platform`
Expected: `Switched to a new branch 'feat/jekyll-platform'`

- [ ] **Step 2: Write `Gemfile`**

```ruby
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "webrick", "~> 1.8"   # Ruby 3+ no longer bundles webrick; needed for `jekyll serve`
```

- [ ] **Step 3: Write `_config.yml`**

```yaml
title: RiskMaverick
tagline: Commodity & Cross-Asset Risk Intelligence
description: >-
  Institutional-grade risk-management knowledge across commodities, equities,
  fixed income, FX and interest rates.
url: "https://riskmaverick.com"
baseurl: ""
lang: en

markdown: kramdown
highlighter: rouge
permalink: /insights/:title/

exclude:
  - Gemfile
  - Gemfile.lock
  - docs/
  - vendor/
  - .claude/
  - "M Falcon B.png"

defaults:
  - scope: { path: "", type: "posts" }
    values: { layout: "post" }
  - scope: { path: "markets" }
    values: { layout: "hub", spine: "markets" }
  - scope: { path: "toolkit" }
    values: { layout: "hub", spine: "toolkit" }
```

- [ ] **Step 4: Write `.gitignore`**

```gitignore
_site/
.jekyll-cache/
.jekyll-metadata
vendor/
```

- [ ] **Step 5: Write `.claude/launch.json`**

```json
{
  "version": "0.0.1",
  "configurations": [
    {
      "name": "jekyll",
      "runtimeExecutable": "bundle",
      "runtimeArgs": ["exec", "jekyll", "serve", "--livereload", "--port", "4000"],
      "port": 4000
    }
  ]
}
```

- [ ] **Step 6: Install dependencies**

Run (PowerShell): `bundle install`
Expected: `Bundle complete!` (creates `Gemfile.lock`).

- [ ] **Step 7: Build to verify it succeeds**

Run (PowerShell): `bundle exec jekyll build`
Expected: ends with `done in N.NN seconds`. Confirm `_site/index.html` and `_site/CNAME` exist (the old homepage copied verbatim).

- [ ] **Step 8: Commit**

```powershell
git add Gemfile Gemfile.lock _config.yml .gitignore .claude/launch.json
git commit -m "chore: scaffold Jekyll project (github-pages gem), preserve existing site"
```

---

### Task 2: Theme CSS extraction

**Files:**
- Create: `assets/css/site.css`
- Source: `index.html:12-517` (the entire `<style>…</style>` block)

**Interfaces:**
- Produces: `/assets/css/site.css` exposing the palette CSS variables on `:root` and all base/component styles, consumed by every layout via `head.html` (Task 3).

- [ ] **Step 1: Extract the stylesheet**

Copy the contents **between** `<style>` (line 12) and `</style>` (line 517) of `index.html` verbatim into `assets/css/site.css` (exclude the `<style>`/`</style>` tags themselves). Do not edit rules yet — this is a lift-and-shift so the theme tokens and existing components survive intact.

- [ ] **Step 2: Append magazine component styles**

Append the following new component styles (used by later tasks) to the end of `assets/css/site.css`:

```css
/* ---- Magazine components ---- */
.site-main{max-width:1180px;margin:0 auto;padding:0 20px 80px;}
.eyebrow{font:600 12px/1 Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--cyan);margin:0 0 10px;}
.card-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:28px;}
.card{display:flex;flex-direction:column;gap:8px;padding:20px;background:var(--surface);border:1px solid var(--border);border-radius:10px;text-decoration:none;color:var(--white);transition:border-color .18s,transform .18s;}
.card:hover{border-color:var(--cyan);transform:translateY(-2px);}
.card h3{font:800 18px/1.25 Inter,sans-serif;margin:0;}
.card p{color:var(--gray2);font:400 14px/1.5 Inter,sans-serif;margin:0;}
.card-date{color:var(--gray3);font:500 12px/1 "JetBrains Mono",monospace;margin-top:auto;}
.card-kind{align-self:flex-start;font:600 10px/1 Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase;padding:4px 8px;border-radius:4px;background:var(--bg3);color:var(--gray1);}
.kind-basics{color:var(--green);} .kind-analysis{color:var(--cyan);} .kind-wire{color:var(--amber);}
.hub-head{padding:48px 0 8px;} .hub-head h1{font:800 40px/1.1 Inter,sans-serif;margin:0 0 12px;}
.hub-blurb{color:var(--gray1);font:400 18px/1.5 Inter,sans-serif;max-width:720px;}
.empty{color:var(--gray2);font-style:italic;padding:24px 0;}
.post{max-width:760px;margin:0 auto;} .post-head{padding:48px 0 24px;border-bottom:1px solid var(--border);}
.post-head h1{font:800 36px/1.15 Inter,sans-serif;margin:8px 0 12px;}
.post-meta{color:var(--gray2);font:500 14px/1 "JetBrains Mono",monospace;}
.post-tags{margin-top:14px;display:flex;flex-wrap:wrap;gap:8px;}
.tag{font:600 11px/1 Inter,sans-serif;text-transform:uppercase;letter-spacing:.08em;padding:5px 9px;border-radius:4px;background:var(--bg3);color:var(--cyan);}
.tag.concept{color:var(--amber);}
.post-body{font:400 17px/1.7 Inter,sans-serif;color:var(--gray1);padding:28px 0;}
.post-body h2{font:800 24px/1.3 Inter,sans-serif;color:var(--white);margin:32px 0 12px;}
.post-body a{color:var(--cyan);}
.sources{border-top:1px solid var(--border);padding-top:24px;margin-top:24px;}
.sources h2{font:800 18px/1 Inter,sans-serif;} .sources li{color:var(--gray2);margin:8px 0;} .sources a{color:var(--cyan);}
.related{border-top:1px solid var(--border);padding-top:24px;margin-top:32px;}
@media(max-width:820px){.card-grid{grid-template-columns:1fr 1fr;}}
@media(max-width:560px){.card-grid{grid-template-columns:1fr;} .hub-head h1{font-size:30px;} .post-head h1{font-size:28px;}}
```

- [ ] **Step 3: Build to verify no CSS breakage**

Run (PowerShell): `bundle exec jekyll build`
Expected: `done in …`; confirm `_site/assets/css/site.css` exists and contains `--cyan:#00d4ff` (Grep the file).

- [ ] **Step 4: Commit**

```powershell
git add assets/css/site.css
git commit -m "style: extract theme CSS to assets/css/site.css + magazine components"
```

---

### Task 3: Site shell — layouts & includes (nav, ticker, footer)

**Files:**
- Create: `_layouts/default.html`
- Create: `_includes/head.html`
- Create: `_includes/nav.html`
- Create: `_includes/ticker.html`
- Create: `_includes/footer.html`
- Create: `_data/markets.yml`
- Create: `_data/toolkit.yml`
- Create: `_pages-test.md` (temporary probe page, deleted in Step 7)

**Interfaces:**
- Consumes: `assets/css/site.css` (Task 2).
- Produces: `default` layout wrapping `{{ content }}` with ticker + nav + footer; `site.data.markets` / `site.data.toolkit` (arrays of `{slug,label,group,icon,url,tag,blurb}`) consumed by nav mega-menus and hubs (Tasks 5, 7, 8).

- [ ] **Step 1: Write `_data/markets.yml`**

```yaml
- { slug: crude-refined,      label: "Crude & Refined",     group: Commodities, icon: "🛢️", url: /markets/commodities/crude-refined/,      tag: crude-refined,      blurb: "Brent & WTI benchmarks, crack spreads and refining-margin risk." }
- { slug: natural-gas-lng,    label: "Natural Gas & LNG",   group: Commodities, icon: "🔥", url: /markets/commodities/natural-gas-lng/,    tag: natural-gas-lng,    blurb: "Henry Hub, TTF and JKM, storage, basis and seasonal risk." }
- { slug: power-renewables,   label: "Power & Renewables",  group: Commodities, icon: "⚡", url: /markets/commodities/power-renewables/,   tag: power-renewables,   blurb: "Non-storable power, PPAs, shape and volume risk." }
- { slug: metals,             label: "Metals",              group: Commodities, icon: "🪙", url: /markets/commodities/metals/,             tag: metals,             blurb: "Base and precious metals, LME pricing and warehousing." }
- { slug: agriculture,        label: "Agriculture",         group: Commodities, icon: "🌾", url: /markets/commodities/agriculture/,        tag: agriculture,        blurb: "Grains and softs, weather and seasonality risk." }
- { slug: carbon-environment, label: "Carbon & Environment",group: Commodities, icon: "🌱", url: /markets/commodities/carbon-environment/, tag: carbon-environment, blurb: "EU ETS, RECs, offsets and policy risk." }
- { slug: equities,           label: "Equities",            group: Equities,    icon: "📈", url: /markets/equities/,                        tag: equities,           blurb: "Indices vs single names, systematic vs idiosyncratic risk, beta." }
- { slug: fixed-income,       label: "Fixed Income",        group: Fixed Income,icon: "📊", url: /markets/fixed-income/,                    tag: fixed-income,       blurb: "Government and corporate bonds, yields, duration and spreads." }
- { slug: fx,                 label: "FX",                  group: FX,          icon: "💱", url: /markets/fx/,                              tag: fx,                 blurb: "Currency pairs, drivers, and transaction/translation exposure." }
- { slug: interest-rates,     label: "Interest Rates",      group: Rates,       icon: "📉", url: /markets/interest-rates/,                  tag: interest-rates,     blurb: "The curve, central banks and interest-rate swaps." }
```

- [ ] **Step 2: Write `_data/toolkit.yml`**

```yaml
- { slug: market-risk,           label: "Market Risk",            url: /toolkit/market-risk/,           tag: market-risk,           blurb: "VaR, volatility, stress testing and the Greeks." }
- { slug: hedging-derivatives,   label: "Hedging & Derivatives",  url: /toolkit/hedging-derivatives/,   tag: hedging-derivatives,   blurb: "Futures, options, swaps and structured hedges." }
- { slug: credit-counterparty,   label: "Credit & Counterparty",  url: /toolkit/credit-counterparty/,   tag: credit-counterparty,   blurb: "Counterparty exposure, credit support and CVA." }
- { slug: liquidity-funding,     label: "Liquidity & Funding",    url: /toolkit/liquidity-funding/,     tag: liquidity-funding,     blurb: "Margin calls, funding vs market liquidity." }
- { slug: operational,           label: "Operational Risk",       url: /toolkit/operational/,           tag: operational,           blurb: "Process, controls and the three lines of defence." }
- { slug: frameworks-governance, label: "Frameworks & Governance",url: /toolkit/frameworks-governance/, tag: frameworks-governance, blurb: "ERM, risk appetite, Basel and model risk." }
```

- [ ] **Step 3: Write `_includes/head.html`**

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% if page.title %}{{ page.title }} — {{ site.title }}{% else %}{{ site.title }} — {{ site.tagline }}{% endif %}</title>
  <meta name="description" content="{{ page.blurb | default: page.excerpt | default: site.description | strip_html | truncate: 160 }}">
  <link rel="icon" type="image/png" href="{{ '/logo-falcon-blue.png' | relative_url }}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ '/assets/css/site.css' | relative_url }}">
</head>
```

- [ ] **Step 4: Write `_includes/ticker.html`**

```html
<div class="topbar">
  <div class="ticker" id="rmTicker" aria-label="Live market prices"><span class="ticker-loading">Loading markets…</span></div>
  <a class="topbar-cta" href="{{ '/about/' | relative_url }}#contact">Get in touch</a>
</div>
```

- [ ] **Step 5: Write `_includes/nav.html`**

```html
<header class="nav">
  <div class="nav-inner">
    <a class="logo" href="{{ '/' | relative_url }}">
      <span class="logo-icon"><img src="{{ '/logo-falcon-blue.png' | relative_url }}" alt="RiskMaverick"></span>
      <span class="logo-word">Risk<strong>Maverick</strong></span>
    </a>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">&#9776;</button>
    <nav class="nav-links" id="navLinks">
      <div class="nav-item has-mega">
        <a href="{{ '/markets/' | relative_url }}">Markets</a>
        <div class="mega mega-markets">
          {% for m in site.data.markets %}
          <a href="{{ m.url | relative_url }}"><span class="mega-ico">{{ m.icon }}</span>{{ m.label }}</a>
          {% endfor %}
        </div>
      </div>
      <div class="nav-item has-mega">
        <a href="{{ '/toolkit/' | relative_url }}">Risk Toolkit</a>
        <div class="mega">
          {% for t in site.data.toolkit %}
          <a href="{{ t.url | relative_url }}">{{ t.label }}</a>
          {% endfor %}
        </div>
      </div>
      <a href="{{ '/insights/' | relative_url }}">Insights</a>
      <a href="{{ '/tools/' | relative_url }}">Tools</a>
      <a href="{{ '/about/' | relative_url }}">About</a>
    </nav>
  </div>
</header>
```

- [ ] **Step 6: Write `_includes/footer.html`**

```html
<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <span class="logo-icon"><img src="{{ '/logo-falcon-blue.png' | relative_url }}" alt="RiskMaverick"></span>
      <p>Institutional-grade risk intelligence across commodities and cross-asset markets.</p>
    </div>
    <div><h4>Markets</h4>{% for m in site.data.markets %}<a href="{{ m.url | relative_url }}">{{ m.label }}</a>{% endfor %}</div>
    <div><h4>Risk Toolkit</h4>{% for t in site.data.toolkit %}<a href="{{ t.url | relative_url }}">{{ t.label }}</a>{% endfor %}</div>
    <div><h4>More</h4>
      <a href="{{ '/insights/' | relative_url }}">Insights</a>
      <a href="{{ '/tools/' | relative_url }}">Tools</a>
      <a href="{{ '/about/' | relative_url }}">About &amp; Contact</a>
    </div>
  </div>
  <div class="footer-legal">© {{ 'now' | date: "%Y" }} RiskMaverick. Educational content only — not investment advice.</div>
</footer>
```

- [ ] **Step 7: Write `_layouts/default.html`**

```html
<!DOCTYPE html>
<html lang="{{ site.lang | default: 'en' }}">
{% include head.html %}
<body>
  {% include ticker.html %}
  {% include nav.html %}
  <main class="site-main">
    {{ content }}
  </main>
  {% include footer.html %}
  <script src="{{ '/assets/js/rm-data.js' | relative_url }}"></script>
  <script src="{{ '/assets/js/ticker.js' | relative_url }}"></script>
</body>
</html>
```

- [ ] **Step 8: Add a temporary probe page**

Create `_pages-test.md`:

```markdown
---
layout: default
title: Shell Test
permalink: /shell-test/
---
Shell probe.
```

- [ ] **Step 9: Build and assert the shell renders**

Run (PowerShell): `bundle exec jekyll build`
Then Grep `_site/shell-test/index.html` for: `Risk<strong>Maverick</strong>`, `mega-markets`, `Natural Gas & LNG`, `rmTicker`, and `Get in touch`.
Expected: all present (nav, mega-menu from data, ticker, footer all rendered).

- [ ] **Step 10: Remove the probe page and commit**

```powershell
git rm _pages-test.md
git add _layouts/default.html _includes/head.html _includes/nav.html _includes/ticker.html _includes/footer.html _data/markets.yml _data/toolkit.yml
git commit -m "feat: site shell — default layout, nav mega-menus, ticker, footer, data files"
```

*(Note: `rm-data.js`/`ticker.js` are referenced but created in Task 4; missing scripts 404 harmlessly until then.)*

---

### Task 4: FMP data module & live ticker

**Files:**
- Create: `assets/js/rm-data.js`
- Create: `assets/js/ticker.js`
- Source: `index.html:2277-2363` (`getQuote`, `getQuotes`, `getSparkline`, `fetchTickerData` + the `_cacheGet`/`_cacheSet` helpers and the FMP API-key/base-URL constants that precede `getQuote` — scan upward from line 2277 to include them).

**Interfaces:**
- Produces: global `window.RM` with `getQuote(symbol)`, `getQuotes(symbols)`, `getSparkline(symbol, points)`, and the cache helpers; consumed by `ticker.js` and by `tools.js` (Task 10).

- [ ] **Step 1: Create `assets/js/rm-data.js` from the existing cache/fetch code**

Copy from `index.html`: the FMP API-key constant, base-URL constant, `_cacheGet`, `_cacheSet`, `getQuote` (2277), `getQuotes` (2289), `getSparkline` (2291), and `fetchTickerData` (2308) through its closing brace (~2363). Wrap them in an IIFE that assigns the public functions to `window.RM`:

```javascript
// assets/js/rm-data.js — FMP quotes/sparklines with shared per-symbol cache
(function () {
  // <-- paste API-key const, base-URL const, _cacheGet, _cacheSet here -->
  // <-- paste getQuote, getQuotes, getSparkline, fetchTickerData here -->
  window.RM = { getQuote, getQuotes, getSparkline, fetchTickerData };
})();
```

Preserve the cache keys (`rmq_<symbol>`, `rms_<symbol>`) and TTLs (quotes 30 min, sparklines 12 h) exactly.

- [ ] **Step 2: Create `assets/js/ticker.js`**

```javascript
// assets/js/ticker.js — renders the topbar live ticker
(function () {
  var TICKER = [
    { symbol: "BZUSD", label: "Brent" },
    { symbol: "GCUSD", label: "Gold" },
    { symbol: "SIUSD", label: "Silver" },
    { symbol: "^GSPC", label: "S&P 500" },
    { symbol: "^VIX",  label: "VIX" },
    { symbol: "EURUSD", label: "EUR/USD" }
  ];
  var el = document.getElementById("rmTicker");
  if (!el || !window.RM) return;
  RM.getQuotes(TICKER.map(function (t) { return t.symbol; })).then(function (quotes) {
    var html = TICKER.map(function (t, i) {
      var q = quotes[i] || {};
      var price = (q.price != null) ? Number(q.price).toLocaleString(undefined, { maximumFractionDigits: 2 }) : "—";
      var chg = Number(q.changePercentage || q.changesPercentage || 0);
      var cls = chg >= 0 ? "up" : "down";
      var sign = chg >= 0 ? "+" : "";
      return '<span class="tick"><b>' + t.label + '</b> <span class="tick-px">' + price +
             '</span> <span class="tick-chg ' + cls + '">' + sign + chg.toFixed(2) + '%</span></span>';
    }).join("");
    el.innerHTML = html + html; // duplicate for seamless marquee
  }).catch(function () { el.innerHTML = '<span class="ticker-loading">Markets unavailable</span>'; });
})();
```

- [ ] **Step 3: Add ticker styles to `assets/css/site.css`**

```css
.topbar{display:flex;align-items:center;justify-content:space-between;gap:16px;background:var(--bg2);border-bottom:1px solid var(--border);padding:6px 20px;overflow:hidden;}
.ticker{display:flex;gap:26px;white-space:nowrap;overflow:hidden;flex:1;font:500 13px/1 "JetBrains Mono",monospace;}
.tick b{color:var(--gray1);font-weight:600;} .tick-px{color:var(--white);} .tick-chg.up{color:var(--green);} .tick-chg.down{color:var(--red);}
.topbar-cta{flex-shrink:0;color:var(--cyan);font:600 12px/1 Inter,sans-serif;text-transform:uppercase;letter-spacing:.08em;text-decoration:none;}
.ticker-loading{color:var(--gray3);}
```

- [ ] **Step 4: Build and verify the scripts are served**

Run (PowerShell): `bundle exec jekyll build`
Then confirm `_site/assets/js/rm-data.js` and `_site/assets/js/ticker.js` exist; Grep `rm-data.js` for `window.RM` and the cache-key prefix `rmq_`.

- [ ] **Step 5: Preview the live ticker**

Start server: `preview_start` name `jekyll`. Then `preview_snapshot` and confirm `#rmTicker` contains at least one `.tick` with a numeric price; check `preview_console_logs` (level error) is clean. If FMP is rate-limited, the "Markets unavailable" fallback is acceptable — verify the fallback path instead.

- [ ] **Step 6: Commit**

```powershell
git add assets/js/rm-data.js assets/js/ticker.js assets/css/site.css
git commit -m "feat: port FMP cache module + live topbar ticker"
```

---

### Task 5: Hub layout + auto-listing (proven on one market hub)

**Files:**
- Create: `_layouts/hub.html`
- Create: `_includes/article-card.html`
- Create: `markets/commodities/natural-gas-lng.md`
- Create: `_posts/2026-07-05-global-gas-trinity.md` (sample `analysis` post)
- Create: `_posts/2026-07-04-what-is-var.md` (sample `basics` post — tagged to a toolkit concept, not this market)

**Interfaces:**
- Consumes: `default` layout (Task 3); `site.data` (Task 3).
- Produces: `hub` layout that lists `site.posts` filtered by `page.tag` against `markets`/`concepts` depending on `page.spine`; `article-card.html` include taking `include.post`.

- [ ] **Step 1: Write `_includes/article-card.html`**

```html
<a class="card" href="{{ include.post.url | relative_url }}">
  <span class="card-kind kind-{{ include.post.kind | default: 'analysis' }}">{{ include.post.kind | default: 'analysis' }}</span>
  <h3>{{ include.post.title }}</h3>
  <p>{{ include.post.excerpt | strip_html | truncate: 120 }}</p>
  <span class="card-date">{{ include.post.date | date: "%b %-d, %Y" }}</span>
</a>
```

- [ ] **Step 2: Write `_layouts/hub.html`**

```html
---
layout: default
---
<section class="hub-head">
  <p class="eyebrow">{{ page.group | default: page.spine }}</p>
  <h1>{{ page.title }}</h1>
  <p class="hub-blurb">{{ page.blurb }}</p>
</section>
<div class="post-body">{{ content }}</div>
<section class="hub-body">
  {% assign tag = page.tag %}
  {% if page.spine == "markets" %}
    {% assign posts = site.posts | where_exp: "p", "p.markets contains tag" %}
  {% else %}
    {% assign posts = site.posts | where_exp: "p", "p.concepts contains tag" %}
  {% endif %}
  <div class="card-grid">
    {% for post in posts %}
      {% include article-card.html post=post %}
    {% else %}
      <p class="empty">In-depth articles on this topic are coming soon.</p>
    {% endfor %}
  </div>
</section>
```

- [ ] **Step 3: Write the market hub `markets/commodities/natural-gas-lng.md`**

```markdown
---
title: Natural Gas & LNG
group: Commodities
tag: natural-gas-lng
blurb: "Henry Hub, TTF and JKM benchmarks, storage economics, basis and the seasonal risks that define gas markets."
---

Natural gas is priced regionally — Henry Hub in North America, TTF in Europe,
JKM for Asian LNG — and the spreads between them drive both physical flows and
hedging strategy. This hub collects our coverage of gas and LNG price risk.
```

- [ ] **Step 4: Write sample post `_posts/2026-07-05-global-gas-trinity.md`**

```markdown
---
title: "The Global Gas Trinity: Henry Hub, TTF and JKM"
kind: analysis
markets: [natural-gas-lng]
concepts: [market-risk]
excerpt: "Why three regional benchmarks — not one global gas price — govern LNG risk."
sources:
  - { title: "Natural Gas Explained", publisher: "U.S. EIA", url: "https://www.eia.gov/energyexplained/natural-gas/" }
---

Unlike oil, natural gas has no single global price. Three benchmarks dominate…

## Why the spreads matter
Arbitrage between Henry Hub, TTF and JKM sets LNG cargo economics…
```

- [ ] **Step 5: Write sample post `_posts/2026-07-04-what-is-var.md`**

```markdown
---
title: "What Is Value at Risk?"
kind: basics
markets: []
concepts: [market-risk]
excerpt: "A plain-English introduction to VaR and what it does — and does not — tell you."
sources:
  - { title: "Messages from the Academic Literature on Risk Measurement", publisher: "Bank for International Settlements", url: "https://www.bis.org/publ/bcbs_wp19.htm" }
---

Value at Risk (VaR) estimates the loss a portfolio is unlikely to exceed over a
set horizon at a given confidence level…
```

- [ ] **Step 6: Build and assert auto-listing works**

Run (PowerShell): `bundle exec jekyll build`
Grep `_site/markets/commodities/natural-gas-lng/index.html` for `The Global Gas Trinity`.
Expected: present (the analysis post auto-listed via its `natural-gas-lng` market tag). Confirm `What Is Value at Risk?` is **absent** from this page (it has no market tag) — proves filtering is correct.

- [ ] **Step 7: Commit**

```powershell
git add _layouts/hub.html _includes/article-card.html markets/commodities/natural-gas-lng.md _posts/2026-07-05-global-gas-trinity.md _posts/2026-07-04-what-is-var.md
git commit -m "feat: hub layout with tag-based auto-listing + sample posts"
```

---

### Task 6: Post layout, sources & related includes

**Files:**
- Create: `_layouts/post.html`
- Create: `_includes/sources.html`
- Create: `_includes/related.html`

**Interfaces:**
- Consumes: `default` layout; post front-matter `kind/markets/concepts/sources` (Task 5).
- Produces: `post` layout (set as default for `_posts` in `_config.yml` Task 1); renders body, sources block, related-by-tag list.

- [ ] **Step 1: Write `_includes/sources.html`**

```html
{% if page.sources %}
<section class="sources">
  <h2>Sources &amp; further reading</h2>
  <ul>
    {% for s in page.sources %}
    <li><a href="{{ s.url }}" target="_blank" rel="noopener">{{ s.title }}</a> — <span>{{ s.publisher }}</span></li>
    {% endfor %}
  </ul>
</section>
{% endif %}
```

- [ ] **Step 2: Write `_includes/related.html`**

```html
{% assign firsttag = page.markets | first %}
{% if firsttag == nil %}{% assign firsttag = page.concepts | first %}{% assign field = 'concepts' %}{% else %}{% assign field = 'markets' %}{% endif %}
{% if field == 'markets' %}
  {% assign pool = site.posts | where_exp: "p", "p.markets contains firsttag" %}
{% else %}
  {% assign pool = site.posts | where_exp: "p", "p.concepts contains firsttag" %}
{% endif %}
<section class="related">
  <h2>Related</h2>
  <div class="card-grid">
    {% assign shown = 0 %}
    {% for post in pool %}
      {% unless post.url == page.url %}{% if shown < 3 %}
        {% include article-card.html post=post %}
        {% assign shown = shown | plus: 1 %}
      {% endif %}{% endunless %}
    {% endfor %}
  </div>
</section>
```

- [ ] **Step 3: Write `_layouts/post.html`**

```html
---
layout: default
---
<article class="post">
  <header class="post-head">
    <p class="eyebrow">{{ page.kind | default: 'analysis' }}</p>
    <h1>{{ page.title }}</h1>
    <p class="post-meta">{{ page.date | date: "%B %-d, %Y" }}{% if page.author %} · {{ page.author }}{% endif %}</p>
    <div class="post-tags">
      {% for m in page.markets %}<span class="tag">{{ m | replace: '-', ' ' }}</span>{% endfor %}
      {% for c in page.concepts %}<span class="tag concept">{{ c | replace: '-', ' ' }}</span>{% endfor %}
    </div>
  </header>
  <div class="post-body">{{ content }}</div>
  {% include sources.html %}
  {% include related.html %}
</article>
```

- [ ] **Step 4: Build and assert the post renders**

Run (PowerShell): `bundle exec jekyll build`
Grep `_site/insights/global-gas-trinity/index.html` for: `Sources &amp; further reading`, `U.S. EIA`, and `class="related"`.
Expected: all present.

- [ ] **Step 5: Preview the article**

`preview_start` (if not running) → navigate via `preview_eval` to `/insights/global-gas-trinity/` → `preview_snapshot`: confirm headline, tags, sources list, and related section render with the dark theme.

- [ ] **Step 6: Commit**

```powershell
git add _layouts/post.html _includes/sources.html _includes/related.html
git commit -m "feat: post layout with sources + related-by-tag includes"
```

---

### Task 7: All market & toolkit hub pages

**Files:**
- Create: `markets/index.html`, `toolkit/index.html`
- Create the 9 remaining market hubs: `markets/commodities/crude-refined.md`, `power-renewables.md`, `metals.md`, `agriculture.md`, `carbon-environment.md`; `markets/equities.md`, `markets/fixed-income.md`, `markets/fx.md`, `markets/interest-rates.md`
- Create the 6 toolkit hubs: `toolkit/market-risk.md`, `hedging-derivatives.md`, `credit-counterparty.md`, `liquidity-funding.md`, `operational.md`, `frameworks-governance.md`

**Interfaces:**
- Consumes: `hub` layout (Task 5), `site.data.markets`/`toolkit` (Task 3).
- Produces: every hub URL referenced by nav/footer/mega-menus.

- [ ] **Step 1: Write each remaining market hub**

For each entry in `_data/markets.yml` not yet created, create the file at its `url` path (drop leading/trailing slashes, add `.md`). Front-matter uses the data row's `label`, `group`, `slug`→`tag`, `blurb`, plus one real intro paragraph. Example — `markets/commodities/crude-refined.md`:

```markdown
---
title: Crude & Refined
group: Commodities
tag: crude-refined
blurb: "Brent and WTI benchmarks, crack spreads and the refining-margin risks that sit between crude and product prices."
---

Crude oil is the deepest commodity market in the world, and the spread between
crude and refined products — the crack spread — is where much refining risk
lives. This hub collects our coverage of oil price and margin risk.
```

Repeat for `power-renewables` (tag `power-renewables`), `metals`, `agriculture`, `carbon-environment` (all under `markets/commodities/`), and `equities`, `fixed-income`, `fx`, `interest-rates` (directly under `markets/`). Each gets a 1–2 sentence real intro paragraph — no placeholder text.

- [ ] **Step 2: Write each toolkit hub**

For each `_data/toolkit.yml` entry, create `toolkit/<slug>.md`. Example — `toolkit/market-risk.md`:

```markdown
---
title: Market Risk
tag: market-risk
blurb: "Measuring and managing the risk of loss from moves in prices, rates and volatility — VaR, stress testing and the Greeks."
---

Market risk is the risk of loss from movements in market prices. This hub covers
how it is measured — from Value at Risk to stress testing — and how desks keep
it within appetite.
```

Repeat for the other five toolkit slugs, each with its own real intro paragraph. (`layout: hub`, `spine: toolkit` come from `_config.yml` defaults.)

- [ ] **Step 3: Write `markets/index.html` (grouped directory of market hubs)**

```html
---
layout: default
title: Markets
permalink: /markets/
---
<section class="hub-head"><p class="eyebrow">Cross-asset</p><h1>Markets</h1>
<p class="hub-blurb">Commodities are our flagship, backed by equities, fixed income, FX and rates.</p></section>
{% assign groups = site.data.markets | group_by: "group" %}
{% for g in groups %}
<h2 class="group-h">{{ g.name }}</h2>
<div class="card-grid">
  {% for m in g.items %}
  <a class="card" href="{{ m.url | relative_url }}"><span class="card-kind">{{ m.icon }}</span><h3>{{ m.label }}</h3><p>{{ m.blurb }}</p></a>
  {% endfor %}
</div>
{% endfor %}
```

- [ ] **Step 4: Write `toolkit/index.html`**

```html
---
layout: default
title: Risk Toolkit
permalink: /toolkit/
---
<section class="hub-head"><p class="eyebrow">Concepts</p><h1>Risk Toolkit</h1>
<p class="hub-blurb">The cross-asset methods for measuring and managing risk.</p></section>
<div class="card-grid">
  {% for t in site.data.toolkit %}
  <a class="card" href="{{ t.url | relative_url }}"><h3>{{ t.label }}</h3><p>{{ t.blurb }}</p></a>
  {% endfor %}
</div>
```

- [ ] **Step 5: Add `.group-h` style**

Append to `assets/css/site.css`: `.group-h{font:800 22px/1 Inter,sans-serif;margin:36px 0 4px;color:var(--white);}`

- [ ] **Step 6: Build and assert all hubs exist**

Run (PowerShell): `bundle exec jekyll build`
Confirm these built: `_site/markets/commodities/crude-refined/index.html`, `_site/markets/equities/index.html`, `_site/markets/interest-rates/index.html`, `_site/toolkit/market-risk/index.html`, `_site/toolkit/frameworks-governance/index.html`, `_site/markets/index.html`, `_site/toolkit/index.html`.
Grep `_site/markets/index.html` for `Interest Rates` and `Commodities` (grouped listing).

- [ ] **Step 7: Commit**

```powershell
git add markets/ toolkit/ assets/css/site.css
git commit -m "feat: all market & toolkit hub pages + directory indexes"
```

---

### Task 8: Home page

**Files:**
- Create: `_layouts/home.html`
- Overwrite: `index.html` (replaces the legacy single-file homepage)

**Interfaces:**
- Consumes: `default` layout, `site.posts`, `site.data` (Tasks 3–7).
- Produces: the new homepage at `/`.

- [ ] **Step 1: Write `_layouts/home.html`**

```html
---
layout: default
---
<section class="home-hero">
  <p class="eyebrow">Commodity &amp; Cross-Asset Risk Intelligence</p>
  <h1 class="home-h1">Risk management, explained by practitioners.</h1>
  <p class="home-sub">Deep coverage of commodity and cross-asset markets, and the tools and frameworks used to manage their risk.</p>
</section>

{% assign featured = site.posts | first %}
{% if featured %}
<section class="home-featured">
  {% include article-card.html post=featured %}
</section>
{% endif %}

<section class="home-latest">
  <h2 class="group-h">Latest</h2>
  <div class="card-grid">
    {% for post in site.posts limit: 6 %}
      {% unless post.url == featured.url %}{% include article-card.html post=post %}{% endunless %}
    {% endfor %}
  </div>
</section>

<section class="home-browse">
  <h2 class="group-h">Browse by market</h2>
  <div class="card-grid">
    {% for m in site.data.markets %}
    <a class="card" href="{{ m.url | relative_url }}"><span class="card-kind">{{ m.icon }}</span><h3>{{ m.label }}</h3><p>{{ m.blurb }}</p></a>
    {% endfor %}
  </div>
</section>

<section class="home-toolkit">
  <h2 class="group-h">From the Risk Toolkit</h2>
  <div class="card-grid">
    {% for t in site.data.toolkit %}
    <a class="card" href="{{ t.url | relative_url }}"><h3>{{ t.label }}</h3><p>{{ t.blurb }}</p></a>
    {% endfor %}
  </div>
</section>

<section class="home-tools-cta">
  <div><h2>Interactive risk tools</h2><p>VaR &amp; Expected Shortfall calculator, volatility surface, correlation matrix and a live markets board.</p></div>
  <a class="btn-primary" href="{{ '/tools/' | relative_url }}">Open Tools</a>
</section>
```

- [ ] **Step 2: Preserve the legacy source, then replace `index.html`**

The Tools port (Task 10) still needs to extract JS/markup from the original file, so preserve it **before** overwriting (theme CSS and the FMP module were already extracted in Tasks 2 and 4):

```powershell
New-Item -ItemType Directory -Force _legacy | Out-Null
git mv index.html _legacy/index-legacy.html
```

Then create a new `index.html` whose entire contents are:

```html
---
layout: home
---
```

`_legacy/` is underscore-prefixed, so Jekyll never builds or serves it, but it stays in git as the extraction source for Task 10. Line numbers in `_legacy/index-legacy.html` are identical to the original `index.html`.

- [ ] **Step 3: Add home styles to `assets/css/site.css`**

```css
.home-hero{padding:64px 0 24px;} .home-h1{font:800 clamp(32px,5vw,52px)/1.08 Inter,sans-serif;margin:0 0 16px;max-width:14ch;}
.home-sub{color:var(--gray1);font:400 19px/1.55 Inter,sans-serif;max-width:640px;}
.home-featured .card{border-color:var(--cyan);} .home-featured .card h3{font-size:24px;}
.home-tools-cta{display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap;margin-top:56px;padding:28px;border:1px solid var(--border);border-radius:12px;background:var(--surface);}
.home-tools-cta h2{font:800 22px/1.2 Inter,sans-serif;margin:0 0 6px;} .home-tools-cta p{color:var(--gray2);margin:0;max-width:520px;}
.btn-primary{background:var(--cyan);color:#06121f;font:700 14px/1 Inter,sans-serif;padding:14px 22px;border-radius:8px;text-decoration:none;white-space:nowrap;}
```

- [ ] **Step 4: Build and assert the home renders**

Run (PowerShell): `bundle exec jekyll build`
Grep `_site/index.html` for: `Browse by market`, `From the Risk Toolkit`, `Open Tools`, and `The Global Gas Trinity` (featured/latest).
Expected: all present.

- [ ] **Step 5: Preview home at three widths**

`preview_start` → `preview_snapshot`. Then `preview_resize` to 344, 440, 1280; after each, `preview_eval` `document.documentElement.scrollWidth <= window.innerWidth + 1` → expect `true` (no horizontal overflow). `preview_screenshot` at 1280 for the record.

- [ ] **Step 6: Commit**

```powershell
git add _layouts/home.html index.html assets/css/site.css
git commit -m "feat: new magazine home page; retire legacy single-file index"
```

---

### Task 9: Insights feed + client-side filter + "Around the web"

**Files:**
- Create: `insights.html`
- Create: `assets/js/insights.js`
- Create: `_data/wires.yml`

**Interfaces:**
- Consumes: `site.posts`, `site.data.markets/toolkit`.
- Produces: `/insights/` feed page with tag filtering and a curated external-links module.

- [ ] **Step 1: Write `_data/wires.yml` (curated external links, approved sources only)**

```yaml
- { title: "Oil Market Report", publisher: "IEA", url: "https://www.iea.org/topics/oil-market-report", date: 2026-07-01 }
- { title: "Short-Term Energy Outlook", publisher: "U.S. EIA", url: "https://www.eia.gov/outlooks/steo/", date: 2026-07-01 }
- { title: "Commodity Markets Outlook", publisher: "World Bank", url: "https://www.worldbank.org/en/research/commodity-markets", date: 2026-06-01 }
```

- [ ] **Step 2: Write `insights.html`**

```html
---
layout: default
title: Insights
permalink: /insights/
---
<section class="hub-head"><p class="eyebrow">Knowledge &amp; commentary</p><h1>Insights</h1>
<p class="hub-blurb">Fundamentals, analysis and the latest from authoritative sources.</p></section>

<div class="filters" id="filters">
  <button class="filter active" data-tag="all">All</button>
  {% for m in site.data.markets %}<button class="filter" data-tag="{{ m.tag }}">{{ m.label }}</button>{% endfor %}
  {% for t in site.data.toolkit %}<button class="filter" data-tag="{{ t.tag }}">{{ t.label }}</button>{% endfor %}
</div>

<div class="card-grid" id="feed">
  {% for post in site.posts %}
  <a class="card" href="{{ post.url | relative_url }}" data-tags="{{ post.markets | join: ' ' }} {{ post.concepts | join: ' ' }}">
    <span class="card-kind kind-{{ post.kind | default: 'analysis' }}">{{ post.kind | default: 'analysis' }}</span>
    <h3>{{ post.title }}</h3>
    <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
    <span class="card-date">{{ post.date | date: "%b %-d, %Y" }}</span>
  </a>
  {% endfor %}
</div>

<section class="wires">
  <h2 class="group-h">Around the web</h2>
  <ul class="wire-list">
    {% for w in site.data.wires %}
    <li><a href="{{ w.url }}" target="_blank" rel="noopener">{{ w.title }}</a> <span>— {{ w.publisher }}</span></li>
    {% endfor %}
  </ul>
</section>
```

- [ ] **Step 3: Write `assets/js/insights.js`**

```javascript
// assets/js/insights.js — client-side tag filtering for the Insights feed
(function () {
  var filters = document.getElementById("filters");
  var feed = document.getElementById("feed");
  if (!filters || !feed) return;
  filters.addEventListener("click", function (e) {
    var btn = e.target.closest(".filter");
    if (!btn) return;
    filters.querySelectorAll(".filter").forEach(function (b) { b.classList.remove("active"); });
    btn.classList.add("active");
    var tag = btn.getAttribute("data-tag");
    feed.querySelectorAll(".card").forEach(function (card) {
      var tags = " " + (card.getAttribute("data-tags") || "") + " ";
      card.style.display = (tag === "all" || tags.indexOf(" " + tag + " ") > -1) ? "" : "none";
    });
  });
})();
```

- [ ] **Step 4: Reference `insights.js` on this page**

Append this script include at the very end of `insights.html` (after the `.wires` section):

```html
<script src="{{ '/assets/js/insights.js' | relative_url }}"></script>
```

- [ ] **Step 5: Add filter/wire styles to `assets/css/site.css`**

```css
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0;}
.filter{background:var(--bg3);border:1px solid var(--border);color:var(--gray1);font:600 12px/1 Inter,sans-serif;padding:8px 12px;border-radius:20px;cursor:pointer;}
.filter.active{background:var(--cyan);color:#06121f;border-color:var(--cyan);}
.wires{margin-top:48px;border-top:1px solid var(--border);padding-top:24px;}
.wire-list li{margin:10px 0;color:var(--gray2);} .wire-list a{color:var(--cyan);}
```

- [ ] **Step 6: Build, assert, and preview the filter**

Run (PowerShell): `bundle exec jekyll build`
Grep `_site/insights/index.html` for `data-tags=` and `Around the web`.
`preview_start` → navigate to `/insights/` → `preview_click` the `Market Risk` filter → `preview_eval` that the VaR "basics" card is visible and the gas "analysis" card is hidden (it has no `market-risk`? it does — pick a filter that separates them, e.g. `natural-gas-lng`: gas card visible, VaR card hidden). Confirm.

- [ ] **Step 7: Commit**

```powershell
git add insights.html assets/js/insights.js _data/wires.yml assets/css/site.css
git commit -m "feat: Insights feed with client-side tag filter + Around-the-web module"
```

---

### Task 10: Tools page (VaR/ES calculator, heatmaps, live board)

**Files:**
- Create: `tools.html`
- Create: `assets/js/tools.js`
- Source markup: `_legacy/index-legacy.html` VaR calculator + volatility-surface + correlation-matrix + live-board sections (within the Risk Analytics / Live Markets blocks, body between ~line 545 and ~2205). *(This is the legacy homepage preserved in Task 8; line numbers match the original `index.html`.)*
- Source JS: `_legacy/index-legacy.html:2365-2646` (`MARKETS`, `loadMarketTab`, `showMarketTab`, `loadHeroSnapshot`, `showRaTab` incl. nested `countTo`, plus the VaR math helpers) — extract the tools-related functions; exclude router (`showPage` 2647), `goToSection` (2686) and `initGSAP` (2748) which are not needed on this page.

**Interfaces:**
- Consumes: `window.RM` (Task 4) for live prices.
- Produces: `/tools/` page.

- [ ] **Step 1: Create `tools.html` shell**

```html
---
layout: default
title: Tools
permalink: /tools/
---
<section class="hub-head"><p class="eyebrow">Interactive</p><h1>Risk Tools</h1>
<p class="hub-blurb">Parametric VaR &amp; Expected Shortfall, a volatility surface, a correlation matrix and a live markets board.</p></section>

<div id="toolsRoot">
  <!-- PASTE the VaR calculator markup (inputs #vaValue/#vaVol/#vaDays/#vaConf, outputs
       #vaVaR/#vaES/#vaVaRpct/#vaESpct/#vaNote), #volSurface, #corrMatrix and the live
       markets board markup extracted from index.html here, unchanged. -->
</div>

<script src="{{ '/assets/js/tools.js' | relative_url }}"></script>
```

- [ ] **Step 2: Extract tool markup from `_legacy/index-legacy.html` into `#toolsRoot`**

Copy the VaR calculator panel, `#volSurface`, `#corrMatrix`, and the live markets board (`#grid-commodities`/`#grid-fx`/`#grid-equities` + `showMarketTab` tabs + `mkt-status`) markup from `_legacy/index-legacy.html` into the `#toolsRoot` div, preserving all element IDs the JS depends on.

- [ ] **Step 3: Create `assets/js/tools.js`**

Copy the tools-related functions from `_legacy/index-legacy.html:2365-2646` (`MARKETS`, `loadMarketTab`, `showMarketTab`, `loadHeroSnapshot`→adapt to the board, `showRaTab`, `countTo`, the VaR/ES compute helpers, `sparkSVG`, `fmtNum`, `fmtUSD`, `chgParts`) into an IIFE. Replace any calls to the old `getQuotes`/`getQuote`/`getSparkline` with `RM.getQuotes`/`RM.getQuote`/`RM.getSparkline`. Preserve the VaR math exactly (`z95=1.6448536`, `z99=2.3263479`, `dailyVol=annualVol/√252`) and keep the `countTo` rAF + `setTimeout` fallback intact.

- [ ] **Step 4: Build and assert**

Run (PowerShell): `bundle exec jekyll build`
Grep `_site/tools/index.html` for `vaVaR`, `volSurface`, `corrMatrix`.

- [ ] **Step 5: Preview and functionally verify the calculator**

`preview_start` → `/tools/` → `preview_fill` `#vaValue`=`1000000`, `#vaVol`=`30`, `#vaDays`=`1`, `#vaConf`=`95` → trigger recompute (`preview_click` the calc button or dispatch input) → `preview_eval` that `#vaVaR` text is non-zero and finite. Confirm `#volSurface` and `#corrMatrix` render cells; check console for errors.

- [ ] **Step 6: Commit**

```powershell
git add tools.html assets/js/tools.js
git commit -m "feat: Tools page — port VaR/ES calculator, heatmaps, live board"
```

---

### Task 11: About & Contact page

**Files:**
- Create: `_layouts/page.html`
- Create: `about.md`

**Interfaces:**
- Consumes: `default` layout.
- Produces: `/about/` with story + contact + enquiry.

- [ ] **Step 1: Write `_layouts/page.html`**

```html
---
layout: default
---
<article class="post">
  <header class="post-head"><h1>{{ page.title }}</h1></header>
  <div class="post-body">{{ content }}</div>
</article>
```

- [ ] **Step 2: Write `about.md`**

```markdown
---
layout: page
title: About & Contact
permalink: /about/
---

RiskMaverick is an educational platform on commodity and cross-asset risk
management, written for risk managers, traders and treasury teams.

## Contact
<div id="contact">
Email: <a href="mailto:hello@riskmaverick.com">hello@riskmaverick.com</a>
</div>

For advisory or training enquiries, email us with a short description of your
requirement and we will respond.
```

- [ ] **Step 3: Build, assert, commit**

Run (PowerShell): `bundle exec jekyll build`; Grep `_site/about/index.html` for `mailto:hello@riskmaverick.com`.

```powershell
git add _layouts/page.html about.md
git commit -m "feat: About & Contact page"
```

---

### Task 12: Responsive nav (mega-menu behaviour + mobile toggle)

**Files:**
- Create: `assets/js/nav.js`
- Modify: `_layouts/default.html:end` (add nav.js script tag before `</body>`)
- Modify: `assets/css/site.css` (nav + mega + mobile rules)

**Interfaces:**
- Consumes: nav markup (Task 3).
- Produces: hover/click mega-menus on desktop; a working hamburger drawer ≤820px.

- [ ] **Step 1: Write `assets/js/nav.js`**

```javascript
// assets/js/nav.js — mobile drawer toggle + tap-to-open mega on touch
(function () {
  var toggle = document.querySelector(".nav-toggle");
  var links = document.getElementById("navLinks");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  document.querySelectorAll(".nav-item.has-mega > a").forEach(function (a) {
    a.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width:820px)").matches) {
        e.preventDefault();
        a.parentElement.classList.toggle("mega-open");
      }
    });
  });
})();
```

- [ ] **Step 2: Add nav.js to `_layouts/default.html`**

Add before `</body>` (after ticker.js): `<script src="{{ '/assets/js/nav.js' | relative_url }}"></script>`

- [ ] **Step 3: Add nav + mega + responsive rules to `assets/css/site.css`**

```css
.nav{position:sticky;top:0;z-index:50;background:rgba(10,15,30,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--border);}
.nav-inner{max-width:1180px;margin:0 auto;display:flex;align-items:center;gap:22px;padding:12px 20px;}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--white);} .logo-word{font:800 18px/1 Inter,sans-serif;} .logo-word strong{color:var(--cyan);}
.nav-links{display:flex;align-items:center;gap:22px;margin-left:auto;}
.nav-links > a,.nav-item > a{color:var(--gray1);font:600 14px/1 Inter,sans-serif;text-decoration:none;}
.nav-item{position:relative;} .nav-item .mega{position:absolute;top:130%;left:0;display:none;grid-template-columns:1fr 1fr;gap:2px;min-width:340px;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:8px;}
.nav-item:hover .mega{display:grid;} .mega a{display:flex;align-items:center;gap:8px;padding:8px 10px;border-radius:6px;color:var(--gray1);text-decoration:none;font:500 13px/1.2 Inter,sans-serif;} .mega a:hover{background:var(--bg3);color:var(--white);}
.nav-toggle{display:none;background:none;border:0;color:var(--white);font-size:22px;cursor:pointer;margin-left:auto;}
@media(max-width:820px){
  .nav-toggle{display:block;}
  .nav-links{display:none;position:absolute;top:100%;left:0;right:0;flex-direction:column;align-items:flex-start;gap:4px;background:var(--surface);border-bottom:1px solid var(--border);padding:12px 20px;}
  .nav-links.open{display:flex;}
  .nav-item{width:100%;} .nav-item .mega{position:static;display:none;grid-template-columns:1fr;min-width:0;border:0;padding:0 0 0 12px;}
  .nav-item.mega-open .mega{display:grid;}
}
@media(max-width:640px){ .footer-grid{grid-template-columns:1fr 1fr;} }
```

- [ ] **Step 4: Build and verify responsive nav**

Run (PowerShell): `bundle exec jekyll build`. `preview_start` → `preview_resize` mobile (375) → `preview_click` `.nav-toggle` → `preview_snapshot`: confirm `#navLinks` is visible with Markets/Toolkit/Insights/Tools/About. `preview_eval` no horizontal overflow at 344/440. At 1280, confirm `.mega` shows on hover (`preview_eval` computed `display` of `.nav-item:hover .mega` or check markup present).

- [ ] **Step 5: Commit**

```powershell
git add assets/js/nav.js _layouts/default.html assets/css/site.css
git commit -m "feat: responsive nav — hover mega-menus + mobile drawer"
```

---

### Task 13: Final integration, deploy config & verification

**Files:**
- Verify: `CNAME` present in `_site/`
- Modify: `_config.yml` (only if the full-site build surfaces a needed exclude)
- Create: `README.md` (build/run notes)

**Interfaces:**
- Produces: a clean full-site build ready for GitHub Pages.

- [ ] **Step 1: Clean full build**

Run (PowerShell): `bundle exec jekyll build --trace`
Expected: `done in …`, zero warnings about missing includes/layouts. Confirm `_site/CNAME` contains `riskmaverick.com`.

- [ ] **Step 2: Link/asset sanity sweep**

Grep `_site` for any literal unrendered Liquid (`{{` or `{%`) in built HTML — expect none. Confirm `_site/logo-falcon-blue.png` exists and `_site/assets/css/site.css`, `_site/assets/js/{rm-data,ticker,tools,insights,nav}.js` all exist.

- [ ] **Step 3: Full responsive pass**

`preview_start` → for each of `/`, `/markets/commodities/natural-gas-lng/`, `/insights/`, `/tools/`, `/about/`: `preview_resize` to 344, 440, 1280 and `preview_eval` `document.documentElement.scrollWidth <= window.innerWidth + 1` → expect `true` each time. Screenshot `/` and `/insights/` at 1280.

- [ ] **Step 4: Write `README.md`**

```markdown
# RiskMaverick

Jekyll site (magazine) deployed via GitHub Pages to riskmaverick.com.

## Local development
Requires Ruby 3.3+ with DevKit.
```powershell
bundle install
bundle exec jekyll serve --livereload
```
Open http://localhost:4000. Production builds automatically on GitHub Pages from the default branch.

## Adding an article
Create `_posts/YYYY-MM-DD-slug.md` with front-matter: `title`, `kind` (basics|analysis|wire), `markets: []`, `concepts: []`, `excerpt`, and `sources: [{title, publisher, url}]`. It appears automatically on matching hubs and in Insights.
```

- [ ] **Step 5: Commit and open PR**

```powershell
git add README.md _config.yml
git commit -m "docs: build/run README; finalize platform migration"
git push -u origin feat/jekyll-platform
```
Then open a PR from `feat/jekyll-platform` to `main` (via the GitHub web UI, since `gh` is not installed). Merging triggers the GitHub Pages build.

---

## Self-Review

**Spec coverage:**
- IA (nav, Markets spine w/ Commodities group + Equities/Bonds/FX/Rates, Toolkit, Insights, Tools, About) → Tasks 3, 5, 7, 8, 9, 10, 11. ✔
- Dual market/concept tagging + auto-listing → Tasks 5, 6, 9. ✔
- Jekyll structure (layouts/includes/data/posts) → Tasks 1, 3, 5, 6, 8. ✔
- Migration of CSS/JS/tools/FMP cache → Tasks 2, 4, 10. ✔
- Insights: basics + analysis + curated wires → Tasks 5, 9. ✔
- Sourcing standard (per-post `sources`, "Sources & further reading") → Tasks 5, 6. ✔
- Brand reuse (logo + palette + fonts, dark theme) → Tasks 2, 3, 8. ✔ (Global Constraints)
- CNAME preserved, GitHub Pages, no plugins → Tasks 1, 13. ✔
- Responsive 344/440/1280 → Tasks 8, 12, 13. ✔
- Deferred (live RSS, bylines) → intentionally out of scope. ✔
- Full article authoring (~58 pieces) → **Plan B** (out of scope here; hubs ship with real intro copy + sample posts + graceful empty states). ✔

**Placeholder scan:** hub intro paragraphs are real one-liners, not "TODO"; the only "paste from index.html" steps are precise extractions of existing code with exact source line ranges — acceptable, not placeholders.

**Type consistency:** `RM.getQuote/getQuotes/getSparkline` used consistently (Tasks 4, 10); `page.tag`+`page.spine` drive `hub.html` filtering matching `_config.yml` defaults and `_data` `tag` fields; `include.post` naming consistent across `article-card.html` consumers (Tasks 5, 6, 8, 9).

**Gap fixes applied:** added `markets/index.html` + `toolkit/index.html` (Task 7) so the nav "Markets"/"Risk Toolkit" top links resolve; added graceful empty-state to `hub.html` (Task 5) so hubs render before Plan B content lands.
