---
layout: toolkit
title: Credit & Counterparty
tag: credit-counterparty
group: "Risk Toolkit · Credit"
emoji: "🤝"
blurb: "Counterparty exposure, credit support and CVA."
standfirst: "Every trade carries the risk that the other side fails to perform. This is how that exposure is measured over a trade’s life — and pulled down with netting, collateral and CVA."
reviewed: 2026-07-08
concepts:
  - "Credit risk"
  - "Counterparty risk (CCR)"
  - "CVA"
  - "Netting & collateral"
methods:
  - { t: "Netting", d: "Offsetting positive and negative exposures to one counterparty into a single net amount — the biggest exposure reducer." }
  - { t: "Collateral (CSA)", d: "Posting initial and variation margin as exposures move, under an ISDA Credit Support Annex." }
  - { t: "Credit Valuation Adjustment (CVA)", d: "The market price of counterparty default risk — an adjustment to a derivative’s value." }
  - { t: "Central clearing (CCP)", d: "Novating trades to a clearing house that mutualises and margins counterparty risk." }
regulation:
  title: "How regulators capitalise it"
  body: "The <strong>Standardised Approach for Counterparty Credit Risk (SA-CCR)</strong> measures exposure, while <strong>SA-CVA / BA-CVA</strong> capitalise CVA risk itself. <strong>Central clearing</strong> concentrates counterparty risk in CCPs — cutting bilateral risk but raising the importance of margin and clearing-house resilience."
sources:
  - { title: "The standardised approach for measuring counterparty credit risk exposures (SA-CCR)", publisher: "Basel Committee on Banking Supervision (BIS)", url: "https://www.bis.org/publ/bcbs279.pdf", note_label: "Standard-setter:", note: "The Basel measure for counterparty exposure · bis.org" }
  - { title: "Counterparty credit risk in Basel III (Executive Summary)", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/fsi/fsisummaries/ccr_in_b3.htm", note_label: "Primary:", note: "Official summary of the CCR framework · bis.org" }
  - { title: "Standardized Approach to Counterparty Credit Risk (SA-CCR)", publisher: "International Swaps and Derivatives Association (ISDA)", url: "https://www.isda.org/tag/standardized-approach-to-counterparty-credit-risk-sa-ccr/", note: "Industry implementation resources · isda.org" }
tool_cta_title: "Explore counterparty risk"
tool_cta_desc: "The Tools page’s counterparty-credit panel shows how exposure and CVA respond to collateral."
---

Every hedge or trade carries the risk that the counterparty on the other side
fails to perform. This hub covers how counterparty exposure is measured and
mitigated — from credit support annexes and collateral to CVA.

## How it works

Two related risks sit here. **Credit risk** is the risk a borrower or bond issuer
defaults, priced through the spread over the risk-free curve. **Counterparty
credit risk (CCR)** is the risk that the party on the other side of a derivative
defaults *before* the trade settles — an exposure that changes as the trade moves
in or out of the money. The market price of that risk is the **Credit Valuation
Adjustment (CVA)**: an adjustment to a derivative's value for the expected cost of
counterparty default. CVA moves with both the counterparty's credit spread and
the size of the exposure.

<figure class="conceptviz">
<p class="conceptviz-title">Exposure builds over a trade’s life — collateral pulls it back down</p>
<svg viewBox="0 0 720 300" role="img" aria-label="An exposure-versus-time chart over the life of a derivative. An uncollateralised expected-exposure curve rises then falls to zero at maturity; a lower curve shows exposure after netting and collateral. The gap between them, priced as CVA, is shaded." xmlns="http://www.w3.org/2000/svg">
<line x1="70" y1="240" x2="670" y2="240" stroke="#1f2937" stroke-width="1"/>
<line x1="70" y1="40" x2="70" y2="240" stroke="#1f2937" stroke-width="1"/>
<text x="62" y="50" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="end">exposure</text>
<text x="70" y="258" fill="#6b7280" font-family="monospace" font-size="10.5">today</text>
<text x="670" y="258" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="end">maturity →</text>
<path d="M70 240 C 220 90 320 70 400 95 C 500 126 590 200 670 240 L 70 240 Z" fill="rgba(0,212,255,0.10)" stroke="#00d4ff" stroke-width="2.5"/>
<path d="M70 240 C 200 205 340 198 430 205 C 540 214 610 228 670 240" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 4"/>
<text x="300" y="80" fill="#00d4ff" font-family="Inter,sans-serif" font-size="12" font-weight="700">Potential future exposure</text>
<text x="360" y="228" fill="#f59e0b" font-family="Inter,sans-serif" font-size="12" font-weight="700">with netting &amp; collateral</text>
<rect x="452" y="120" width="150" height="22" rx="6" fill="#0f1626" stroke="#1f2937"/>
<text x="527" y="135" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">gap ≈ CVA</text>
<line x1="470" y1="142" x2="470" y2="205" stroke="#6b7280" stroke-width="1" stroke-dasharray="3 3"/>
</svg>
<figcaption class="conceptviz-src">Schematic. Counterparty exposure isn’t a single number — it’s a <strong>profile over time</strong>. <strong>Netting and collateral</strong> compress it, and the residual expected loss from default is priced as <strong>CVA</strong>.</figcaption>
</figure>

## In practice

CCR is mitigated by **netting**, **collateral** and hedging. The ISDA **Credit
Support Annex (CSA)** governs collateral — posting **initial and variation
margin** as exposures move — which can reduce or even neutralise CVA. Regulators
require capital against it: the **Standardised Approach for Counterparty Credit
Risk (SA-CCR)** measures exposure, while **SA-CVA/BA-CVA** capitalise CVA risk
itself. **Central clearing** further concentrates and mutualises counterparty
risk through CCPs — reducing bilateral risk but raising the importance of margin
and clearing-house resilience.
