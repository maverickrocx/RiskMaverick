---
layout: toolkit
title: Operational Risk
tag: operational
group: "Risk Toolkit · Controls"
emoji: "🧩"
blurb: "Process, controls and the three lines of defence."
standfirst: "The risk of loss from failed processes, people or systems rather than market moves — a risk you aren’t paid to take, so the goal is control, not optimisation."
reviewed: 2026-07-08
concepts:
  - "Process & people"
  - "Three lines of defence"
  - "Loss-event data"
  - "Controls"
methods:
  - { t: "Three lines of defence", d: "Business owns the risk; risk & compliance set policy and challenge; internal audit provides independent assurance." }
  - { t: "RCSA & KRIs", d: "Risk-and-control self-assessment plus key risk indicators to spot control weakness before losses occur." }
  - { t: "Loss-event data", d: "Recording internal losses and near-misses — the backbone of measurement for an infrequent, severe risk." }
  - { t: "Scenario analysis", d: "Structured what-ifs for rare but existential events (fraud, cyber, rogue trading)." }
regulation:
  title: "How bank capital is sized"
  body: "Basel’s 2017 <strong>standardised approach</strong> sizes the charge from a <strong>Business Indicator Component</strong> scaled by an <strong>Internal Loss Multiplier</strong> tied to a firm’s own loss history — directly rewarding good controls and a clean track record."
sources:
  - { title: "Principles for the Sound Management of Operational Risk", publisher: "Basel Committee on Banking Supervision (BIS)", url: "https://www.bis.org/publ/bcbs292.pdf", note_label: "Standard-setter:", note: "The foundational operational-risk principles · bis.org" }
  - { title: "Operational risk standardised approach — Executive Summary", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/fsi/fsisummaries/oprisk_sa.htm", note_label: "Primary:", note: "Official summary of the 2017 approach · bis.org" }
  - { title: "The \"four lines of defence model\" for financial institutions", publisher: "Bank for International Settlements (BIS)", url: "https://www.bis.org/fsi/fsipapers11.pdf", note: "On governance and assurance models · bis.org" }
tool_cta_title: "See the wider framework"
tool_cta_desc: "Operational risk sits inside enterprise risk management — see Frameworks & Governance."
tool_cta_url: /toolkit/frameworks-governance/
---

Operational risk is the risk of loss from failed processes, people or systems
rather than market moves. This hub covers control frameworks and the
three-lines-of-defence model that firms use to keep operational risk in check.

## How it works

Operational risk is the risk of loss from **inadequate or failed internal
processes, people and systems, or from external events** — think settlement
errors, fraud, cyber incidents, legal failures and rogue trading. It differs from
market and credit risk in that it is largely *internal* and not taken
deliberately for return; you are not paid to bear it, so the goal is control
rather than optimisation. It is inherently hard to quantify because losses are
infrequent but can be severe (a single control failure can be existential),
making loss-event data, near-miss reporting and scenario analysis central.

<figure class="conceptviz">
<p class="conceptviz-title">The three lines of defence — who owns, who challenges, who assures</p>
<svg viewBox="0 0 720 300" role="img" aria-label="A governance diagram. A governing body sits on top; below it three columns show the first line (business owns and manages risk), second line (risk and compliance set policy and challenge) and third line (internal audit provides independent assurance); regulators and external audit sit outside." xmlns="http://www.w3.org/2000/svg">
<g font-family="Inter,sans-serif">
<rect x="70" y="40" width="580" height="40" rx="9" fill="#0f1626" stroke="#00d4ff" stroke-opacity="0.5"/>
<text x="360" y="65" fill="#f9fafb" font-size="13.5" font-weight="700" text-anchor="middle">Governing body — Board &amp; Risk Committee</text>
<rect x="70" y="108" width="180" height="118" rx="10" fill="#0f1626" stroke="#1f2937"/><rect x="70" y="108" width="180" height="4" rx="2" fill="#10b981"/>
<text x="160" y="134" fill="#10b981" font-family="monospace" font-size="11" font-weight="700" text-anchor="middle">1ST LINE</text>
<text x="160" y="158" fill="#f9fafb" font-size="13" font-weight="700" text-anchor="middle">Business</text>
<text x="160" y="180" fill="#9ca3af" font-size="11" text-anchor="middle">owns &amp; manages</text><text x="160" y="195" fill="#9ca3af" font-size="11" text-anchor="middle">its own risk</text>
<rect x="270" y="108" width="180" height="118" rx="10" fill="#0f1626" stroke="#1f2937"/><rect x="270" y="108" width="180" height="4" rx="2" fill="#f59e0b"/>
<text x="360" y="134" fill="#f59e0b" font-family="monospace" font-size="11" font-weight="700" text-anchor="middle">2ND LINE</text>
<text x="360" y="158" fill="#f9fafb" font-size="13" font-weight="700" text-anchor="middle">Risk &amp; Compliance</text>
<text x="360" y="180" fill="#9ca3af" font-size="11" text-anchor="middle">set policy,</text><text x="360" y="195" fill="#9ca3af" font-size="11" text-anchor="middle">oversee &amp; challenge</text>
<rect x="470" y="108" width="180" height="118" rx="10" fill="#0f1626" stroke="#1f2937"/><rect x="470" y="108" width="180" height="4" rx="2" fill="#00d4ff"/>
<text x="560" y="134" fill="#00d4ff" font-family="monospace" font-size="11" font-weight="700" text-anchor="middle">3RD LINE</text>
<text x="560" y="158" fill="#f9fafb" font-size="13" font-weight="700" text-anchor="middle">Internal Audit</text>
<text x="560" y="180" fill="#9ca3af" font-size="11" text-anchor="middle">independent</text><text x="560" y="195" fill="#9ca3af" font-size="11" text-anchor="middle">assurance</text>
<rect x="70" y="250" width="580" height="34" rx="9" fill="#0f1626" stroke="#1f2937" stroke-dasharray="5 4"/>
<text x="360" y="271" fill="#9ca3af" font-size="12" text-anchor="middle">External audit &amp; regulators — assurance from outside</text>
</g>
</svg>
<figcaption class="conceptviz-src">Schematic. Each line is independent of the one it oversees: the business runs the controls, the second line challenges them, and <strong>internal audit assures the whole</strong> — with the board above and regulators outside.</figcaption>
</figure>

## In practice

Governance follows the **three lines of defence**: the business owns and manages
its risks (first line), independent **risk and compliance** functions set policy
and challenge (second line), and **internal audit** provides assurance (third
line), with the board and regulators above. For bank capital, Basel's 2017
**standardised approach** sizes the charge from a **Business Indicator Component**
scaled by an **Internal Loss Multiplier** tied to a firm's own loss history —
directly rewarding good controls and a clean track record.
