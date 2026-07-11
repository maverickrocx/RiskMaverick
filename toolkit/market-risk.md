---
layout: toolkit
title: Market Risk
tag: market-risk
group: "Risk Toolkit · Measurement"
emoji: "📉"
blurb: "VaR, volatility, stress testing and the Greeks."
standfirst: "The risk of loss from moving prices — and the family of measures, from VaR to Expected Shortfall, that put a single, comparable number on it."
reviewed: 2026-07-08
concepts:
  - "Value at Risk"
  - "Expected Shortfall"
  - "The Greeks"
  - "Stress testing"
methods:
  - { t: "Value at Risk (VaR)", d: "A loss threshold at a set confidence and horizon — comparable across desks, but silent about the tail beyond it." }
  - { t: "Expected Shortfall (ES)", d: "The average loss in the worst tail; coherent and tail-sensitive, now the Basel capital standard." }
  - { t: "Sensitivities (the Greeks)", d: "Delta, gamma, vega and the rest — how value responds to each individual risk factor." }
  - { t: "Stress & scenario testing", d: "What specific shocks, rather than statistical averages, would do to the book." }
regulation:
  title: "The rule that changed the measure"
  body: "The Basel Committee’s <strong>Fundamental Review of the Trading Book (FRTB)</strong> shifts the regulatory standard <strong>from 99% VaR to 97.5% Expected Shortfall</strong>, and adds <strong>liquidity horizons</strong> that recognise some positions take longer to exit."
sources:
  - { title: "Minimum capital requirements for market risk (FRTB)", publisher: "Basel Committee on Banking Supervision (BIS)", url: "https://www.bis.org/bcbs/publ/d457.htm", note_label: "Standard-setter:", note: "The global bank-capital standard-setter · bis.org" }
  - { title: "Explanatory note on the minimum capital requirements for market risk", publisher: "Basel Committee on Banking Supervision (BIS)", url: "https://www.bis.org/bcbs/publ/d457_note.pdf", note_label: "Primary:", note: "Official explanatory note · bis.org" }
  - { title: "Revised framework for market risk capital requirements (press release)", publisher: "Basel Committee on Banking Supervision (BIS)", url: "https://www.bis.org/press/p160114.htm", note: "Primary summary of the reform · bis.org" }
tool_cta_title: "Try it on the Tools page"
tool_cta_desc: "The RiskMaverick VaR & Expected Shortfall calculator lets you move the confidence level and watch the tail."
---

Market risk is the risk of loss from movements in market prices. This hub covers
how it is measured — from Value at Risk to stress testing — and how desks keep
it within appetite.

## How it works

Market risk is the risk of loss from moves in prices, rates, volatility and
spreads. It is measured in a few complementary ways: **Value at Risk (VaR)** —
the loss a portfolio is unlikely to exceed over a set horizon at a given
confidence — and, increasingly, **Expected Shortfall (ES)**, the *average* loss
in the tail beyond VaR, which captures extreme outcomes more prudently. Alongside
these sit **sensitivities** (the "Greeks" — delta, gamma, vega, etc.) that show
how value responds to each risk factor, and **stress testing / scenario
analysis** that asks what happens under specific shocks rather than statistical
averages.

<figure class="conceptviz">
<p class="conceptviz-title">VaR marks the edge of the tail — Expected Shortfall measures its depth</p>
<svg viewBox="0 0 720 280" role="img" aria-label="A bell-shaped distribution of a portfolio's one-day outcomes. A dashed line marks the 99% VaR at the edge of the loss tail; the shaded region beyond it is the worst 1%, and a second line marks Expected Shortfall as the average loss within that tail, deeper than VaR." xmlns="http://www.w3.org/2000/svg">
<defs><marker id="mrAr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#ef4444"/></marker></defs>
<line x1="60" y1="220" x2="680" y2="220" stroke="#1f2937" stroke-width="1"/>
<path d="M60 220 C 240 220 280 60 380 60 C 480 60 520 220 680 220 Z" fill="rgba(0,212,255,0.12)" stroke="#00d4ff" stroke-width="2"/>
<path d="M60 220 C 150 220 180 150 205 120 L 205 220 Z" fill="rgba(239,68,68,0.35)"/>
<line x1="205" y1="96" x2="205" y2="220" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5 4"/>
<text x="212" y="104" fill="#f59e0b" font-family="Inter,sans-serif" font-size="13" font-weight="700">99% VaR</text>
<text x="212" y="121" fill="#9ca3af" font-family="Inter,sans-serif" font-size="11">edge of the worst 1%</text>
<line x1="135" y1="150" x2="135" y2="220" stroke="#ef4444" stroke-width="2" stroke-dasharray="5 4"/>
<text x="24" y="150" fill="#ef4444" font-family="Inter,sans-serif" font-size="13" font-weight="700">ES</text>
<text x="16" y="167" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">avg of tail</text>
<path d="M92 178 L128 178" stroke="#ef4444" stroke-width="1.4" marker-end="url(#mrAr)"/>
<text x="95" y="210" fill="#ef4444" font-family="Inter,sans-serif" font-size="11">losses</text>
<text x="60" y="242" fill="#6b7280" font-family="monospace" font-size="10.5">← worse losses</text>
<text x="680" y="242" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="end">gains →</text>
<text x="380" y="150" fill="#00d4ff" font-family="Inter,sans-serif" font-size="12" text-anchor="middle" font-weight="600">most days cluster here</text>
</svg>
<figcaption class="conceptviz-src">Schematic. <strong>VaR</strong> answers “how far in does the worst 1% begin?”; <strong>Expected Shortfall</strong> answers “once you’re in that tail, how bad is it on average?” — the reason Basel moved the capital standard from VaR to ES.</figcaption>
</figure>

## In practice

For banks, market-risk capital is set by the Basel Committee's **Fundamental
Review of the Trading Book (FRTB)**, introduced after the 2008 crisis. Its
headline change is a shift in the regulatory measure **from VaR at 99% to
Expected Shortfall at 97.5%**, to better capture tail risk, plus **liquidity
horizons** that recognise some positions take longer to exit. Firms run VaR/ES
daily, **backtest** the models against actual P&L, and manage exposure to
board-approved limits and risk appetite — the discipline the RiskMaverick VaR
calculator on the Tools page illustrates.
