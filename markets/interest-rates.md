---
layout: commodity
title: Interest Rates
group: Rates
tag: interest-rates
emoji: "📉"
blurb: "The curve, central banks and interest-rate swaps."
standfirst: "The discount rate under every other asset. The curve’s front end is set by central banks; its slope is the market’s verdict on growth and inflation."
reviewed: 2026-07-08
benchmarks:
  - { name: "SOFR", region: "US · NY Fed", price: "4.85%", unit: "o/n", chg: "0bp today", dir: up }
  - { name: "€STR", region: "EU · ECB", price: "3.65%", unit: "o/n", chg: "1bp today", dir: dn }
  - { name: "US 10Y Swap", region: "USD · OTC", price: "3.98%", unit: "fixed", chg: "2bp today", dir: up }
benchmark_note: "Illustrative rates · overnight benchmarks & swap reference · published source shown"
key_benchmarks:
  - { code: "Policy rates", full: "Fed · ECB · BoE", desc: "Central banks set the curve’s front end directly — the anchor for all short-dated rates." }
  - { code: "Overnight RFRs", full: "SOFR · €STR · SONIA", desc: "The post-LIBOR risk-free rates that floating legs and derivatives now reference." }
  - { code: "Interest-rate swaps", full: "Fixed vs floating", desc: "Exchange fixed for floating to reshape duration without trading the underlying bonds." }
drivers:
  - { icon: "🏦", title: "Central-bank policy path", desc: "The expected sequence of rate decisions is the single biggest driver of the curve." }
  - { icon: "📈", title: "Inflation expectations", desc: "Where inflation is headed sets real rates and the long end of the curve." }
  - { icon: "🧾", title: "QT & supply", desc: "Balance-sheet run-off and government issuance change the supply of duration the market must absorb." }
  - { icon: "⏳", title: "Term premium", desc: "The extra yield demanded to hold long bonds shifts with uncertainty and demand for safety." }
risks:
  - { title: "Level (parallel-shift) risk", sev: hi, sev_label: "High", desc: "A uniform move in rates across maturities — the primary exposure duration measures." }
  - { title: "Curve (steepener / flattener) risk", sev: hi, sev_label: "High", desc: "The curve rarely shifts in parallel; steepening and flattening are exposures a duration hedge misses." }
  - { title: "Basis risk", sev: md, sev_label: "Medium", desc: "SOFR vs Fed Funds, or swap vs bond, can diverge — leaving a hedge imperfectly matched to the exposure." }
  - { title: "Convexity risk", sev: md, sev_label: "Medium", desc: "The rate-sensitivity of duration itself changes as rates move, especially for long-dated and optioned positions." }
risk_note: "<b>The curve moves in more than one way.</b> A duration hedge covers parallel shifts but not steepening or flattening. Manage level and curve as separate risks."
specs:
  - { benchmark: "3-Month SOFR", venue: "CME", unit: "IMM index", size: "$25 × 0.01", settle: "Cash" }
  - { benchmark: "30-Day Fed Funds", venue: "CME", unit: "IMM index", size: "$41.67 × 0.01", settle: "Cash" }
  - { benchmark: "USD 10Y Swap", venue: "OTC / cleared", unit: "Fixed vs SOFR", size: "Per notional", settle: "Cash" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "OTC derivatives statistics", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/publ/otc_hy2512.htm", note: "Primary global derivatives-market statistics · bis.org" }
  - { title: "Key Trends in the Size and Composition of OTC Derivatives Markets (H2 2024)", publisher: "ISDA", url: "https://www.isda.org/a/1rjgE/Key-Trends-in-the-Size-and-Composition-of-OTC-Derivatives-Markets-in-the-Second-Half-of-2024.pdf", note: "The derivatives industry’s standard-setting body · isda.org" }
  - { title: "Secured Overnight Financing Rate (SOFR)", publisher: "Federal Reserve Bank of New York", url: "https://www.newyorkfed.org/markets/reference-rates/sofr", note_label: "Primary:", note: "The official administrator of SOFR · newyorkfed.org" }
  - { title: "Selected Interest Rates (H.15)", publisher: "U.S. Federal Reserve", url: "https://www.federalreserve.gov/releases/h15/", note_label: "Primary:", note: "Official benchmark interest-rate release · federalreserve.gov" }
tool_cta_title: "Model rate risk"
tool_cta_desc: "Separate level and curve exposure in a rates book’s VaR and Expected Shortfall."
---

Interest rates set the discount rate for nearly every other asset, and the
shape of the curve reflects central bank policy and market expectations for
growth and inflation. This hub covers rate curves, central bank drivers and the
swaps used to manage rate exposure.

## How the market works

The **yield curve** plots the interest rate across maturities, from overnight to
30 years. Its front end is anchored by **central-bank policy rates** (the Fed,
ECB, BoE), while the long end reflects the market's expectations for growth,
inflation and term premium — so the curve's slope (steep, flat or inverted) is a
core macro signal. Rate risk is managed largely through **interest-rate swaps**,
which exchange fixed for floating payments and let borrowers and investors
reshape their exposure without trading the underlying bonds. Since the retirement
of LIBOR, floating legs reference **risk-free overnight rates** such as **SOFR**
(USD), €STR and SONIA, published by central banks.

## Major trade flows

Interest-rate derivatives are the largest part of the financial system by
notional: total OTC derivatives outstanding were about **US$846 trillion** in
mid-2025, of which **interest-rate contracts are ~79%**, with **interest-rate
swaps alone around US$550 trillion** notional. Roughly **80% is centrally
cleared** through CCPs, a structural shift since the 2008 crisis that concentrates
counterparty risk in clearing houses. The dominant flows come from banks,
asset managers, insurers and corporates hedging funding and duration, plus the
huge government-bond and repo markets that the curve prices — making central-bank
policy the single biggest driver of activity.
