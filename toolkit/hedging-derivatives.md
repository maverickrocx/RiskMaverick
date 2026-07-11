---
layout: toolkit
title: Hedging & Derivatives
tag: hedging-derivatives
group: "Risk Toolkit · Instruments"
emoji: "🛡️"
blurb: "Futures, options, swaps and structured hedges."
standfirst: "The instruments risk managers use to transfer unwanted exposure — and the art of offsetting a position so price risk falls away, leaving only basis, cost and margin."
reviewed: 2026-07-08
concepts:
  - "Futures & forwards"
  - "Options"
  - "Swaps"
  - "Basis risk"
methods:
  - { t: "Futures & forwards", d: "An obligation to buy or sell later at an agreed price — exchange-traded (futures) or bilateral OTC (forwards)." }
  - { t: "Options", d: "The right, not the obligation, to transact — protection on the downside while keeping upside, for a premium." }
  - { t: "Swaps", d: "Exchange one cash-flow stream for another (e.g. fixed for floating) to reshape exposure without trading the underlying." }
  - { t: "Hedge design", d: "Sizing the offset and managing what’s left: basis risk, cost, and the funding of margin calls." }
regulation:
  title: "How the OTC market is documented"
  body: "OTC derivatives run under the <strong>ISDA Master Agreement</strong>, with a <strong>Credit Support Annex (CSA)</strong> governing collateral. Notional outstanding was around <strong>US$846 trillion</strong> at mid-2025 — but <strong>close-out netting cuts mark-to-market exposure by roughly 86%</strong>, so headline notional badly overstates real risk."
sources:
  - { title: "ISDA Master Agreements and User Guides", publisher: "International Swaps and Derivatives Association (ISDA)", url: "https://www.isda.org/book-taxonomy/mas-and-user-guides/", note_label: "Standard-setter:", note: "The body that standardises OTC derivatives documentation · isda.org" }
  - { title: "OTC derivatives statistics at end-June 2025", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/publ/otc_hy2512.htm", note_label: "Primary:", note: "Official global derivatives-market statistics · bis.org" }
  - { title: "OTC derivatives statistics", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/statistics/derstats.htm", note: "Statistics landing page · bis.org" }
tool_cta_title: "See a hedge in numbers"
tool_cta_desc: "Use the Tools page to compare an unhedged vs hedged position and the basis that remains."
---

Derivatives — futures, options, swaps and the structured products built from
them — are the primary tools risk managers use to transfer unwanted exposure.
This hub covers how these instruments work and how hedges are designed and
sized.

## How it works

A **derivative** takes its value from an underlying — a commodity, rate, currency
or index — and lets a firm transfer risk without owning the underlying. The core
building blocks are **futures and forwards** (an obligation to buy/sell later at
an agreed price), **options** (the right, not the obligation) and **swaps**
(exchanging one cash-flow stream for another). Futures and standardised options
trade on exchanges and are centrally cleared; forwards and most swaps are
**over-the-counter (OTC)**. A hedge simply takes an offsetting position — a
producer selling futures against future output, say — trading away price risk in
exchange for basis risk, cost and margin obligations.

<figure class="conceptviz">
<p class="conceptviz-title">A hedge offsets exposure — the two legs sum to a flat result</p>
<svg viewBox="0 0 720 300" role="img" aria-label="A profit-and-loss versus price chart. A long physical exposure slopes up, a short futures position slopes down by the same amount, and their sum is a flat horizontal line — the hedged position, insensitive to price." xmlns="http://www.w3.org/2000/svg">
<line x1="70" y1="150" x2="670" y2="150" stroke="#1f2937" stroke-width="1"/>
<line x1="370" y1="40" x2="370" y2="260" stroke="#1f2937" stroke-width="1"/>
<text x="60" y="45" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="end">P&amp;L +</text>
<text x="60" y="262" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="end">P&amp;L −</text>
<text x="664" y="168" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="end">price →</text>
<line x1="90" y1="248" x2="650" y2="52" stroke="#10b981" stroke-width="2.5"/>
<text x="556" y="46" fill="#10b981" font-family="Inter,sans-serif" font-size="12" font-weight="700">Long exposure</text>
<line x1="90" y1="52" x2="650" y2="248" stroke="#ef4444" stroke-width="2.5"/>
<text x="556" y="262" fill="#ef4444" font-family="Inter,sans-serif" font-size="12" font-weight="700">Short future</text>
<line x1="90" y1="150" x2="650" y2="150" stroke="#00d4ff" stroke-width="3"/>
<rect x="410" y="118" width="150" height="24" rx="6" fill="#0f1626" stroke="#1f2937"/>
<text x="485" y="134" fill="#00d4ff" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle">Hedged = flat</text>
<text x="370" y="286" fill="#9ca3af" font-family="Inter,sans-serif" font-size="11" text-anchor="middle">Whatever the price does, the two legs cancel — leaving basis, cost &amp; margin</text>
</svg>
<figcaption class="conceptviz-src">Schematic. A perfect hedge removes <strong>price risk</strong> but never comes free — what remains is <strong>basis risk</strong> (hedge vs actual exposure), transaction cost and the obligation to fund <strong>margin calls</strong>.</figcaption>
</figure>

## In practice

OTC derivatives are documented under the **ISDA Master Agreement**, standardised
since 1987, with a **Credit Support Annex (CSA)** governing collateral (initial
and variation margin). The market is enormous — around **US$846 trillion** in
notional outstanding at mid-2025 — but that figure overstates true risk:
**close-out netting reduces mark-to-market exposure by roughly 86%**. Good hedge
design is therefore as much about managing **basis risk** and the **funding of
margin calls** as about the headline price protection.
