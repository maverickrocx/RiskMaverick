---
layout: commodity
title: Fixed Income
group: Fixed Income
tag: fixed-income
emoji: "📊"
blurb: "Government and corporate bonds, yields, duration and spreads."
standfirst: "Two risks in one instrument: how far rates move (duration) and how far a borrower’s spread widens (credit). Government curves anchor the first; everything else prices above them."
reviewed: 2026-07-08
benchmarks:
  - { name: "US 10Y", region: "US · Treasury", price: "4.28%", unit: "yield", chg: "3bp today", dir: up }
  - { name: "German 10Y", region: "EU · Bund", price: "2.45%", unit: "yield", chg: "1bp today", dir: dn }
  - { name: "US 2Y", region: "US · Treasury", price: "4.05%", unit: "yield", chg: "2bp today", dir: up }
benchmark_note: "Illustrative yields · delayed ≥15 min · government benchmark curve"
key_benchmarks:
  - { code: "Government curve", full: "Treasuries · Bunds · Gilts · JGBs", desc: "The risk-free curve every other bond — and most other assets — prices off." }
  - { code: "Credit spreads", full: "Corporate · agency · EM", desc: "Non-government bonds price at a spread over govvies to compensate for default risk." }
  - { code: "Rates futures", full: "CBOT Treasury futures", desc: "The liquid instrument for hedging duration without trading the underlying cash bonds." }
drivers:
  - { icon: "🏦", title: "Central-bank policy", desc: "Policy rates and guidance anchor the front end and set the tone for the whole curve." }
  - { icon: "📈", title: "Inflation & growth", desc: "Expectations for inflation and growth drive the long end and the curve’s slope." }
  - { icon: "🧾", title: "Issuance & supply", desc: "Government funding needs and auction sizes push yields, especially at the long end." }
  - { icon: "🛡️", title: "Safe-haven flows", desc: "In stress, flight-to-quality into Treasuries and Bunds compresses yields regardless of fundamentals." }
risks:
  - { title: "Duration (rate) risk", sev: hi, sev_label: "High", desc: "Sensitivity to rate moves — the dominant risk in government and high-grade bonds." }
  - { title: "Credit-spread risk", sev: hi, sev_label: "High", desc: "The spread over the risk-free curve can widen on default fears even as rates fall, hitting corporate books." }
  - { title: "Curve / convexity risk", sev: md, sev_label: "Medium", desc: "Non-parallel curve moves and convexity mean duration alone doesn’t fully describe the exposure." }
  - { title: "Liquidity risk", sev: md, sev_label: "Medium", desc: "Most bonds trade OTC through dealers; off-the-run and credit issues can be hard to move in stress." }
risk_note: "<b>Duration and credit are separable.</b> A Treasury hedge removes rate risk but not the spread; a credit position can lose even as the risk-free curve rallies. Model them apart."
specs:
  - { benchmark: "US 10Y T-Note", venue: "CBOT (CME)", unit: "Price (32nds)", size: "$100,000 face", settle: "Physical delivery" }
  - { benchmark: "Euro-Bund (10Y)", venue: "Eurex", unit: "Price", size: "€100,000 face", settle: "Physical delivery" }
  - { benchmark: "US T-Bond", venue: "CBOT (CME)", unit: "Price (32nds)", size: "$100,000 face", settle: "Physical delivery" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "Debt securities statistics", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/statistics/secstats.htm", note: "Primary global bond-market statistics · bis.org" }
  - { title: "Capital Markets Fact Book", publisher: "SIFMA", url: "https://www.sifma.org/resources/research/reports/fact-book/", note: "Industry-standard capital-markets statistics · sifma.org" }
  - { title: "International finance through the lens of BIS statistics: bond markets", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/publ/qtrpdf/r_qt2509e.htm", note: "Analysis of global bond-market structure · bis.org" }
  - { title: "Daily Treasury Par Yield Curve Rates", publisher: "U.S. Department of the Treasury", url: "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/", note_label: "Primary:", note: "The official US benchmark curve · treasury.gov" }
tool_cta_title: "Model rate & credit risk"
tool_cta_desc: "Decompose a bond book’s VaR into its duration and credit-spread contributions."
---

Fixed income risk is driven by yield curves, duration and credit spreads,
spanning government bonds priced off risk-free rates to corporate debt priced
with an additional spread for default risk. This hub covers how bond investors
measure and manage that exposure.

## How the market works

A bond is a tradable loan: the issuer pays periodic coupons and repays principal
at maturity. Price and yield move inversely, and the two core risks are
**interest-rate risk** — measured by **duration** (sensitivity to rate moves) and
convexity — and **credit risk**, measured by the **spread** a bond pays over the
risk-free government curve to compensate for default risk. Government bonds
(Treasuries, Bunds, Gilts, JGBs) anchor the risk-free curve; corporate, agency,
mortgage-backed and emerging-market bonds price at a spread above it. Most
trading is **over-the-counter** through dealers rather than on exchange, and the
government yield curve is the reference rate for pricing almost every other
asset.

## Major trade flows

Fixed income is the largest securities market in the world — global bonds
outstanding reached about **US$145 trillion** in 2024, well over global GDP.
**Governments are now the biggest borrowers**, at roughly 52% of all debt
securities, as public debt has climbed since 2020. **US markets are the largest
single bloc** (~40%, ~US$58 trillion, over twice the size of the EU), with US
Treasuries the world's benchmark safe asset and deepest pool of collateral.
Cross-border holdings — central-bank reserves, pension and insurance portfolios —
make sovereign issuance and central-bank policy the dominant flows.
