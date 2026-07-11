---
layout: commodity
title: FX
group: FX
tag: fx
emoji: "💱"
blurb: "Currency pairs, drivers, and transaction/translation exposure."
standfirst: "The market beneath every cross-border trade. Rate differentials, flows and policy set the price; anyone with assets or liabilities in two currencies inherits the risk."
reviewed: 2026-07-08
benchmarks:
  - { name: "EUR/USD", region: "Majors · OTC", price: "1.0850", unit: "spot", chg: "0.2% today", dir: up }
  - { name: "USD/JPY", region: "Majors · OTC", price: "158.20", unit: "spot", chg: "0.4% today", dir: up }
  - { name: "GBP/USD", region: "Majors · OTC", price: "1.2720", unit: "spot", chg: "0.1% today", dir: dn }
benchmark_note: "Illustrative spot rates · delayed ≥15 min · interbank reference"
key_benchmarks:
  - { code: "Spot", full: "Immediate (T+2)", desc: "Delivery in two business days — the reference all other FX instruments price off." }
  - { code: "Outright forwards", full: "Fixed future date", desc: "Lock a rate today for a future settlement — the workhorse for hedging contracted cash flows." }
  - { code: "FX swaps", full: "Spot + forward legs", desc: "The largest instrument by turnover, used mainly to manage short-term funding and roll positions." }
drivers:
  - { icon: "⚖️", title: "Rate differentials", desc: "The gap between two countries’ interest rates is the primary anchor for a currency pair." }
  - { icon: "🏦", title: "Central-bank policy", desc: "Policy shifts, guidance and occasional intervention move currencies sharply." }
  - { icon: "🌍", title: "Growth & trade balances", desc: "Relative growth, current-account and capital flows set medium-term direction." }
  - { icon: "😨", title: "Risk sentiment & safe havens", desc: "In stress, flows into USD, JPY and CHF can override rate-differential logic." }
risks:
  - { title: "Transaction risk", sev: hi, sev_label: "High", desc: "Contracted foreign-currency cash flows move in home-currency terms until settled — the most direct FX exposure." }
  - { title: "Gap / intervention risk", sev: hi, sev_label: "High", desc: "Central-bank action, pegs and news can move rates discontinuously, defeating a smooth hedge." }
  - { title: "Translation risk", sev: md, sev_label: "Medium", desc: "Reporting foreign assets and earnings in the home currency swings book value with the rate." }
  - { title: "Cross-currency basis risk", sev: md, sev_label: "Medium", desc: "Funding a position across currencies carries a basis that widens in stress, raising hedging cost." }
risk_note: "<b>The dollar is on ~89% of trades.</b> Most exposure routes through USD, so a ‘hedged’ EM position can still carry USD funding and basis risk. Map the full currency chain."
specs:
  - { benchmark: "EUR/USD Future", venue: "CME", unit: "USD per EUR", size: "€125,000", settle: "Physical / cash" }
  - { benchmark: "Spot FX", venue: "OTC (interbank)", unit: "Quote ccy / base", size: "Any", settle: "T+2" }
  - { benchmark: "Japanese Yen Future", venue: "CME", unit: "USD per ¥", size: "¥12,500,000", settle: "Physical / cash" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "Triennial Central Bank Survey — OTC FX turnover, April 2025", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/statistics/rpfx25_fx.htm", note: "The definitive global FX turnover survey · bis.org" }
  - { title: "Global FX trading hits $9.6 trillion per day (press release)", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/press/p250930.htm", note: "Primary summary of the 2025 survey · bis.org" }
  - { title: "Triennial Central Bank Survey 2025", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/statistics/rpfx25.htm", note: "Full survey landing page · bis.org" }
  - { title: "Foreign Exchange Rates (H.10)", publisher: "U.S. Federal Reserve", url: "https://www.federalreserve.gov/releases/h10/", note_label: "Primary:", note: "Official reference exchange rates · federalreserve.gov" }
tool_cta_title: "Model FX risk"
tool_cta_desc: "See transaction, translation and basis exposure sized alongside VaR for an FX book."
---

Currency markets sit beneath almost every cross-border trade and investment,
turning interest-rate differentials, capital flows and policy into exposure
for anyone holding assets or liabilities in more than one currency. This hub
covers FX drivers and the transaction and translation risks that follow.

## How the market works

FX is the largest and most liquid market in the world — a decentralised,
**over-the-counter** market that trades around the clock through banks and
electronic venues rather than on a central exchange. Currencies trade in
**pairs** (EUR/USD, USD/JPY) across three main instruments: **spot**, **outright
forwards** and **FX swaps**, the last used mainly to manage short-term funding
and roll positions. Prices are driven by interest-rate differentials, capital
flows, trade balances and central-bank policy. For corporates and investors,
exposure shows up as **transaction** risk (contracted cash flows), **translation**
risk (reporting foreign assets/earnings in the home currency) and **economic**
risk (competitive position), typically hedged with forwards and options.

## Major trade flows

The BIS Triennial Survey put global FX turnover at about **US$9.6 trillion per
day** in April 2025, up 28% in three years. By instrument, **FX swaps** were the
largest at ~42% (~US$4trn/day), followed by **spot** at ~31% and **forwards** at
~19%. The **US dollar remains dominant**, on one side of roughly **89% of all
trades**, underscoring its role as the world's funding and invoicing currency;
the euro, yen and sterling follow. Trading concentrates in a few hubs — London
first, then New York, Singapore and Hong Kong — which set global liquidity and
pricing.
