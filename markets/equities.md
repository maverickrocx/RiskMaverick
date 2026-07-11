---
layout: commodity
title: Equities
group: Equities
tag: equities
emoji: "📈"
blurb: "Indices vs single names, systematic vs idiosyncratic risk, beta."
standfirst: "Equity risk splits in two — the market-wide moves an index captures, and the company-specific surprises it doesn’t. That divide drives everything from beta hedging to diversification."
reviewed: 2026-07-08
benchmarks:
  - { name: "S&P 500", region: "US · CME", price: "5,620", unit: "index", chg: "0.5% today", dir: up }
  - { name: "Euro Stoxx 50", region: "EU · Eurex", price: "4,980", unit: "index", chg: "0.3% today", dir: dn }
  - { name: "Nikkei 225", region: "JP · OSE", price: "39,200", unit: "index", chg: "1.1% today", dir: up }
benchmark_note: "Illustrative index levels · delayed ≥15 min · settlement source shown per index"
key_benchmarks:
  - { code: "Index futures", full: "E-mini S&P 500 (CME)", desc: "The most liquid way to trade or hedge broad US equity beta in a single instrument." }
  - { code: "Single names", full: "Individual shares", desc: "Carry idiosyncratic, company-specific risk on top of the market beta an index captures." }
  - { code: "VIX", full: "Cboe Volatility Index", desc: "The market’s implied-volatility gauge — effectively the price of US large-cap equity risk." }
drivers:
  - { icon: "💰", title: "Earnings & fundamentals", desc: "Company profits and guidance drive single-name value and, in aggregate, the index." }
  - { icon: "🏦", title: "Rates & the discount rate", desc: "Higher risk-free rates lower the present value of future earnings — a key macro lever on valuations." }
  - { icon: "🌍", title: "Macro & growth", desc: "The economic cycle, inflation and policy set the backdrop for corporate earnings." }
  - { icon: "😨", title: "Risk sentiment & positioning", desc: "Flows, leverage and crowding can move markets well beyond fundamentals in the short run." }
risks:
  - { title: "Systematic (market / beta) risk", sev: hi, sev_label: "High", desc: "Market-wide moves that diversification cannot remove — the exposure an index and beta measure." }
  - { title: "Idiosyncratic (single-name) risk", sev: hi, sev_label: "High", desc: "Company-specific outcomes (earnings, litigation, fraud) that an index hedge leaves fully exposed." }
  - { title: "Volatility-regime risk", sev: md, sev_label: "Medium", desc: "Correlations rise and vol spikes in stress, so a book can behave very differently than its calm-market VaR." }
  - { title: "Liquidity & crowding risk", sev: md, sev_label: "Medium", desc: "Popular positions can gap on the exit; thin single names are hard to unwind at scale." }
risk_note: "<b>Beta is not the whole story.</b> An index hedge neutralises systematic risk but leaves single-name (idiosyncratic) exposure untouched. Separate the two before sizing a hedge."
specs:
  - { benchmark: "E-mini S&P 500", venue: "CME", unit: "Index points", size: "$50 × index", settle: "Cash" }
  - { benchmark: "Euro Stoxx 50", venue: "Eurex", unit: "Index points", size: "€10 × index", settle: "Cash" }
  - { benchmark: "Cboe VIX", venue: "Cboe", unit: "Vol points", size: "$1,000 × index", settle: "Cash" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "Capital Markets Fact Book", publisher: "SIFMA", url: "https://www.sifma.org/resources/research/reports/fact-book/", note: "Industry-standard capital-markets statistics · sifma.org" }
  - { title: "Market Statistics", publisher: "World Federation of Exchanges", url: "https://www.world-exchanges.org/our-work/statistics", note: "The global exchange industry’s official statistics body · world-exchanges.org" }
  - { title: "Global Financial Stability Report", publisher: "International Monetary Fund (IMF)", url: "https://www.imf.org/en/Publications/GFSR", note: "Intergovernmental financial-stability analysis · imf.org" }
  - { title: "Cboe Volatility Index (VIX) — Methodology", publisher: "Cboe", url: "https://www.cboe.com/tradable_products/vix/", note_label: "Primary:", note: "The index provider’s own methodology · cboe.com" }
tool_cta_title: "Model equity risk"
tool_cta_desc: "Run a VaR on an equity book and separate the systematic (beta) from idiosyncratic contribution."
---

Equity risk splits between **systematic** market moves and **idiosyncratic**,
company-specific outcomes — the distinction that underpins index versus
single-name exposure and beta-driven hedging. This hub covers how equity risk
is measured and managed across both.

## How the market works

Equities are shares of ownership in companies. They are created in the
**primary market** (IPOs and secondary offerings) and then trade in the
**secondary market** on exchanges, with clearing and settlement infrastructure
behind it — the mechanism that connects investors (capital providers) with
issuers (capital users). Risk decomposes into **systematic** (market-wide, the
part captured by an index and measured through **beta**) and **idiosyncratic**
(company-specific) components; diversification removes the latter, leaving
market risk that is hedged with index futures and options. Implied volatility —
the VIX for US large-caps — is the market's price of that risk.

## Major trade flows

Equity markets are large and concentrated: global equity market capitalisation
was roughly **US$127 trillion** at end-2024, and **US markets alone make up
about 49%** (~US$62 trillion), making them the deepest and most liquid in the
world, followed by Europe, China, Japan and India. Capital flows run through
primary issuance (companies raising equity) and vast secondary turnover across
exchanges tracked by the World Federation of Exchanges. Cross-border equity
investing links these pools, so global risk appetite, index rebalancing and
passive fund flows move markets well beyond any single company's fundamentals.
