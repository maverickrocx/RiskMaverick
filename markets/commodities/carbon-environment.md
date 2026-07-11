---
layout: commodity
title: Carbon & Environment
group: Commodities · Environmental
tag: carbon-environment
emoji: "🌱"
blurb: "EU ETS, RECs, offsets and policy risk."
standfirst: "A commodity created by regulation. Supply is set by a policy cap, not a mine or a well — so the dominant risk here is the direction of climate policy itself."
reviewed: 2026-07-08
benchmarks:
  - { name: "EUA", region: "EU ETS · ICE", price: "€71.0", unit: "/t", chg: "0.8% today", dir: up }
  - { name: "UKA", region: "UK ETS · ICE", price: "£38.5", unit: "/t", chg: "1.4% today", dir: dn }
  - { name: "CCA", region: "California · ICE", price: "$38.2", unit: "/t", chg: "0.5% today", dir: up }
benchmark_note: "Illustrative values · allowance futures reference · settlement source shown per scheme"
key_benchmarks:
  - { code: "EUA", full: "EU Emission Allowance", desc: "The world’s largest compliance carbon market; one EUA permits one tonne of CO₂ under the EU ETS cap-and-trade scheme." }
  - { code: "RECs", full: "Renewable Energy Certificates", desc: "Tradable proof that one MWh of renewable power was generated — used to meet clean-energy obligations." }
  - { code: "VCM offsets", full: "Voluntary carbon market", desc: "Project-based credits (forestry, capture) traded voluntarily; quality and verification vary widely by standard." }
drivers:
  - { icon: "📜", title: "Policy & the cap", desc: "The regulator sets total supply. Tightening the cap or reforming the scheme is the single largest price driver." }
  - { icon: "🏭", title: "Industrial activity", desc: "Emissions demand for allowances rises and falls with output from power and heavy industry." }
  - { icon: "🔥", title: "Fuel switching", desc: "Gas-vs-coal economics change how many allowances the power sector needs — linking carbon to energy prices." }
  - { icon: "🏦", title: "Market stability tools", desc: "Mechanisms like the EU’s Market Stability Reserve absorb or release supply, dampening or amplifying moves." }
risks:
  - { title: "Policy / regulatory risk", sev: hi, sev_label: "High", desc: "The defining risk: a rule change, cap revision or scheme reform can revalue the entire market overnight." }
  - { title: "Liquidity & maturity risk", sev: hi, sev_label: "High", desc: "Newer and voluntary markets are thin and fragmented, so prices can gap and hedges can be hard to unwind." }
  - { title: "Quality / integrity risk", sev: md, sev_label: "Medium", desc: "In voluntary offsets, credits differ in verification and permanence — two ‘tonnes’ are not always equivalent." }
  - { title: "Basis between schemes", sev: md, sev_label: "Medium", desc: "EUA, UKA and CCA are separate, non-fungible markets; a hedge in one does not cover exposure in another." }
risk_note: "<b>Supply is a political decision.</b> Unlike a mined or drilled commodity, the amount of carbon ‘produced’ is set by the regulator. Scenario-testing policy paths matters more here than modelling physical fundamentals."
specs:
  - { benchmark: "EU Allowance (EUA)", venue: "ICE / EEX", unit: "EUR / tonne CO₂", size: "1,000 t", settle: "Physical (allowance)" }
  - { benchmark: "UK Allowance (UKA)", venue: "ICE", unit: "GBP / tonne CO₂", size: "1,000 t", settle: "Physical (allowance)" }
  - { benchmark: "California (CCA)", venue: "ICE", unit: "USD / tonne CO₂", size: "1,000 t", settle: "Physical (allowance)" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "About the EU ETS", publisher: "European Commission, Climate Action", url: "https://climate.ec.europa.eu/eu-action/carbon-markets/about-eu-ets_en", note: "The regulator of the world’s largest carbon market · europa.eu" }
  - { title: "State and Trends of Carbon Pricing", publisher: "World Bank", year: 2025, url: "https://www.worldbank.org/en/publication/state-and-trends-of-carbon-pricing", note: "Annual global survey of compliance carbon markets · worldbank.org" }
  - { title: "EU Emissions Trading System (EU ETS)", publisher: "International Carbon Action Partnership (ICAP)", url: "https://icapcarbonaction.com/en/ets/eu-emissions-trading-system-eu-ets", note: "Independent reference on ETS design worldwide · icapcarbonaction.com" }
  - { title: "Carbon Futures — Contract Specs", publisher: "Intercontinental Exchange (ICE)", url: "https://www.ice.com/products/Environmental", note_label: "Primary:", note: "Exchange rulebook for EUA, UKA and CCA futures · ice.com" }
tool_cta_title: "Model carbon price & policy risk"
tool_cta_desc: "Stress-test a compliance position against alternative policy and cap-tightening scenarios."
---

Carbon is a commodity **created by regulation**. There is no mine or well —
supply is a policy cap, and the amount of CO₂ that can be emitted is a political
decision. That makes the **direction of climate policy** the dominant price
driver and the dominant risk. Compliance markets like the **EU ETS** are the
deepest and most liquid; **renewable energy certificates** and **voluntary
offsets** sit alongside them but are thinner and more fragmented, with real
differences in quality and verification. Managing risk here is less about
physical fundamentals and more about **scenario-testing the rules themselves**.

## How the market works

Most carbon value trades in **compliance markets** built on a **cap-and-trade**
design. The flagship is the **EU Emissions Trading System (EU ETS)**: a cap is
set on total emissions from covered installations, expressed as allowances
(**EUAs**), where one allowance permits one tonne of CO₂-equivalent. Companies
must surrender enough allowances each year to cover their emissions; allowances
are auctioned and then freely traded, so the price is set by the market against a
shrinking cap (the EU cap falls ~4.3% a year, targeting −62% by 2030 versus
2005). Alongside these sit **voluntary carbon markets**, where firms buy credits
from third-party-verified emission-reduction or removal projects to meet
self-set net-zero goals — a market defined by project quality and integrity
rather than a regulated cap.

## Major trade flows

Carbon is fundamentally a **policy-created** commodity, so "flows" follow
regulation: the EU ETS is the largest and most liquid compliance market, with
other systems in the UK, California, China and elsewhere. The World Bank reports
that direct carbon pricing now covers close to a third of global emissions and
raised over US$100bn in government revenue in 2025. Because value depends on
regulatory ambition, **policy risk** — cap tightening, scope expansion (e.g. the
new EU ETS2 for buildings and road transport), and border measures like CBAM — is
the dominant driver of price.

<figure class="flowviz">
<p class="flowviz-title">How a cap-and-trade market works — allowance supply, market, compliance</p>
<svg viewBox="0 0 760 312" role="img" aria-label="Schematic of an emissions trading system: a falling cap and auctions supply allowances that trade in a market and are surrendered by covered emitters" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="cbAh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#00d4ff"/></marker></defs>
<text x="112" y="22" fill="#f59e0b" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">ALLOWANCE SUPPLY</text>
<text x="380" y="22" fill="#9ca3af" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">MARKET</text>
<text x="648" y="22" fill="#00d4ff" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">COMPLIANCE DEMAND</text>
<path d="M206,71 Q380,50 554,83" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#cbAh)"/>
<path d="M206,145 Q380,150 554,157" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#cbAh)"/>
<path d="M206,219 Q380,235 554,231" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#cbAh)"/>
<path d="M206,145 Q380,105 554,83" fill="none" stroke="#00d4ff" stroke-width="1.4" opacity="0.3" marker-end="url(#cbAh)"/>
<g><rect x="18" y="44" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="44" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="70" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Falling cap</text><text x="34" y="88" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">−62% by 2030 (EU)</text></g>
<g><rect x="18" y="118" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="118" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="144" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Govt auctions</text><text x="34" y="162" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">allowances sold</text></g>
<g><rect x="18" y="192" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="192" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="218" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Free allocation</text><text x="34" y="236" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">carbon-leakage sectors</text></g>
<g><rect x="554" y="56" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="56" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="82" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Power generators</text><text x="568" y="100" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">surrender EUAs</text></g>
<g><rect x="554" y="130" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="130" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="156" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Heavy industry</text><text x="568" y="174" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">steel · cement · chemicals</text></g>
<g><rect x="554" y="204" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="204" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="230" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Aviation</text><text x="568" y="248" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">intra-EU flights</text></g>
<g><rect x="286" y="52" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="70" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">EUA spot &amp; futures</text></g>
<g><rect x="286" y="106" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="124" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Carbon price signal</text></g>
<g><rect x="286" y="160" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="178" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Market Stability Reserve</text></g>
<g><rect x="286" y="214" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="232" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Voluntary offsets</text></g>
<text x="380" y="300" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="middle">One EUA = one tonne CO₂e · cap falls each year</text>
</svg>
<figcaption class="flowviz-src">Schematic — illustrative mechanism (EU ETS shown). Data: <a href="https://climate.ec.europa.eu/eu-action/carbon-markets/about-eu-ets_en">European Commission</a>, <a href="https://www.worldbank.org/en/publication/state-and-trends-of-carbon-pricing">World Bank</a> &amp; <a href="https://icapcarbonaction.com/en/ets/eu-emissions-trading-system-eu-ets">ICAP</a>. Interactive: <a href="https://carbonpricingdashboard.worldbank.org/">World Bank Carbon Pricing Dashboard</a>.</figcaption>
</figure>
