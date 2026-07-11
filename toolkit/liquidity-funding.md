---
layout: toolkit
title: Liquidity & Funding
tag: liquidity-funding
group: "Risk Toolkit · Liquidity"
emoji: "💧"
blurb: "Margin calls, funding vs market liquidity."
standfirst: "A hedge that is right on paper can still sink a firm if the margin calls can’t be funded. This is the difference between market and funding liquidity — and why it matters."
reviewed: 2026-07-08
concepts:
  - "Market liquidity"
  - "Funding liquidity"
  - "Margin calls"
  - "LCR & NSFR"
methods:
  - { t: "Market vs funding liquidity", d: "Trading without moving price, versus meeting cash obligations as they fall due — two distinct risks that interact." }
  - { t: "Margin management", d: "Forecasting and funding variation-margin calls on derivatives, especially under stress." }
  - { t: "HQLA buffers", d: "Holding high-quality liquid assets against plausible calls rather than just marking the hedge to market." }
  - { t: "LCR & NSFR", d: "Basel III ratios for surviving a 30-day stress and for longer-term funding stability." }
regulation:
  title: "The 2022 energy-margin case"
  body: "After 2008, Basel III introduced the <strong>Liquidity Coverage Ratio (LCR)</strong> and <strong>Net Stable Funding Ratio (NSFR)</strong>. The textbook stress: in the <strong>2022 European energy crisis</strong>, TTF gas spiked ~10× and cleared <strong>initial-margin calls ran &gt;20× the pre-stress average</strong>, straining even solvent, well-hedged firms."
sources:
  - { title: "Liquidity Coverage Ratio (LCR) — Executive Summary", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/fsi/fsisummaries/lcr.htm", note_label: "Standard-setter:", note: "The Basel III liquidity standard · bis.org" }
  - { title: "Margins and liquidity in European energy markets in 2022", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/publ/bisbull77.pdf", note_label: "Primary:", note: "BIS analysis of the 2022 margin spike · bis.org" }
  - { title: "Margin dynamics in centrally cleared commodities markets in 2022", publisher: "BCBS–CPMI–IOSCO (BIS)", url: "https://www.bis.org/bcbs/publ/d550.htm", note: "Joint standard-setter review · bis.org" }
tool_cta_title: "Stress a funding position"
tool_cta_desc: "Use the Tools page to see how a price shock translates into margin calls and funding need."
---

A hedge that is right on paper can still fail if it cannot be funded through
margin calls. This hub distinguishes market liquidity from funding liquidity
and covers how firms manage the cash demands that derivatives positions create.

## How it works

There are two distinct liquidities. **Market liquidity** is the ability to trade
an asset quickly without moving its price. **Funding liquidity** is the ability
to meet cash obligations as they fall due — most sharply, the **margin calls** a
derivatives position generates. The two interact dangerously: a hedge can be
economically correct yet still sink a firm if rising **variation margin** cannot
be funded, forcing the position to be closed at the worst possible time. Managing
liquidity therefore means holding cash and high-quality liquid assets against
plausible calls, not just marking the hedge to market.

<figure class="conceptviz">
<p class="conceptviz-title">The funding spiral — how a correct hedge can still force a sale</p>
<svg viewBox="0 0 720 300" role="img" aria-label="A four-step loop showing how an adverse price move triggers a variation-margin call, which creates funding strain, which forces asset sales, which can push prices further and repeat — the liquidity spiral." xmlns="http://www.w3.org/2000/svg">
<defs><marker id="lqAr" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#f59e0b"/></marker></defs>
<g font-family="Inter,sans-serif">
<rect x="70" y="52" width="220" height="56" rx="10" fill="#0f1626" stroke="#1f2937"/><rect x="70" y="52" width="4" height="56" rx="2" fill="#00d4ff"/>
<text x="86" y="78" fill="#f9fafb" font-size="13.5" font-weight="700">1 · Adverse price move</text><text x="86" y="96" fill="#9ca3af" font-size="11">hedge moves against you (on paper)</text>
<rect x="430" y="52" width="220" height="56" rx="10" fill="#0f1626" stroke="#1f2937"/><rect x="430" y="52" width="4" height="56" rx="2" fill="#00d4ff"/>
<text x="446" y="78" fill="#f9fafb" font-size="13.5" font-weight="700">2 · Variation-margin call</text><text x="446" y="96" fill="#9ca3af" font-size="11">cash must be posted now</text>
<rect x="430" y="192" width="220" height="56" rx="10" fill="#0f1626" stroke="#1f2937"/><rect x="430" y="192" width="4" height="56" rx="2" fill="#f59e0b"/>
<text x="446" y="218" fill="#f9fafb" font-size="13.5" font-weight="700">3 · Funding strain</text><text x="446" y="236" fill="#9ca3af" font-size="11">liquidity runs short</text>
<rect x="70" y="192" width="220" height="56" rx="10" fill="#0f1626" stroke="#1f2937"/><rect x="70" y="192" width="4" height="56" rx="2" fill="#ef4444"/>
<text x="86" y="218" fill="#f9fafb" font-size="13.5" font-weight="700">4 · Forced selling</text><text x="86" y="236" fill="#9ca3af" font-size="11">position closed at the worst time</text>
<path d="M290 80 L424 80" fill="none" stroke="#f59e0b" stroke-width="1.8" marker-end="url(#lqAr)"/>
<path d="M540 108 L540 186" fill="none" stroke="#f59e0b" stroke-width="1.8" marker-end="url(#lqAr)"/>
<path d="M430 220 L296 220" fill="none" stroke="#f59e0b" stroke-width="1.8" marker-end="url(#lqAr)"/>
<path d="M180 192 L180 114" fill="none" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="5 4" marker-end="url(#lqAr)"/>
<text x="360" y="150" fill="#f59e0b" font-family="monospace" font-size="11" text-anchor="middle" font-weight="700">liquidity</text>
<text x="360" y="166" fill="#f59e0b" font-family="monospace" font-size="11" text-anchor="middle" font-weight="700">spiral</text>
</g>
</svg>
<figcaption class="conceptviz-src">Schematic. The danger isn’t being wrong on the hedge — it’s that <strong>variation margin is cash, now</strong>. If it can’t be funded, a solvent position is closed at a loss, which can push prices further and feed the loop.</figcaption>
</figure>

## In practice

After 2008, Basel III introduced two standards: the **Liquidity Coverage Ratio
(LCR)** — enough high-quality liquid assets to survive a 30-day stress — and the
**Net Stable Funding Ratio (NSFR)** for longer-term funding stability. The
textbook case for commodity firms is the **2022 European energy crisis**: the TTF
gas benchmark spiked to roughly **ten times** its prior-decade level, cleared
**initial-margin calls ran more than 20× the pre-stress average**, and intraday
variation-margin calls of hundreds of millions strained even solvent, well-hedged
firms — prompting regulatory work on margin transparency and liquidity
preparedness.
