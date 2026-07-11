---
layout: commodity
title: Metals
group: Commodities · Metals
tag: metals
emoji: "🪙"
blurb: "Base and precious metals, LME pricing and warehousing."
standfirst: "Two markets under one name: industrial base metals priced on physical supply and demand, and precious metals that trade as much on macro and safe-haven flows."
reviewed: 2026-07-08
benchmarks:
  - { name: "Copper", region: "Base · LME", price: "$9,420", unit: "/t", chg: "0.7% today", dir: up }
  - { name: "Aluminium", region: "Base · LME", price: "$2,510", unit: "/t", chg: "0.5% today", dir: dn }
  - { name: "Gold", region: "Precious · COMEX", price: "$2,368", unit: "/oz", chg: "0.4% today", dir: up }
benchmark_note: "Illustrative values · production feed delayed ≥15 min · settlement source shown per benchmark"
key_benchmarks:
  - { code: "LME", full: "London Metal Exchange", desc: "The global base-metals benchmark; its unique prompt-date structure and warehouse network define industrial-metal pricing." }
  - { code: "COMEX", full: "CME Group", desc: "The main futures venue for gold, silver and US copper — deep, liquid and the reference for precious-metal hedging." }
  - { code: "LBMA / SGE", full: "London & Shanghai", desc: "The London OTC bullion market and Shanghai Gold Exchange complete gold’s three dominant pricing venues." }
drivers:
  - { icon: "🏭", title: "Industrial demand", desc: "Base metals track construction, manufacturing and — increasingly — electrification and the energy transition (copper)." }
  - { icon: "💵", title: "Macro & the dollar", desc: "Priced in USD, metals move inversely to the dollar; real yields drive gold in particular." }
  - { icon: "🛡️", title: "Safe-haven & official demand", desc: "Gold and silver draw flows in stress and inflation regimes, with central-bank buying now a major driver." }
  - { icon: "📦", title: "Inventories & warehousing", desc: "LME and exchange stocks, and the queues to withdraw from warehouses, signal physical tightness." }
risks:
  - { title: "Flat-price risk", sev: hi, sev_label: "High", desc: "Outright exposure to the metal price — large and cyclical for producers, fabricators and consumers." }
  - { title: "Backwardation / contango", sev: hi, sev_label: "High", desc: "The LME forward curve drives roll cost and the economics of holding inventory; tight physical markets can invert it sharply." }
  - { title: "Warehousing / delivery basis", sev: md, sev_label: "Medium", desc: "Location premiums and warehouse queues mean the exchange price and the delivered physical price can diverge." }
  - { title: "Concentration & liquidity", sev: md, sev_label: "Medium", desc: "Some metals have concentrated supply and thinner liquidity, so large positions can move the market and gap on news." }
risk_note: "<b>Base and precious behave differently.</b> Copper is an industrial-cycle bet; gold is a macro and safe-haven one. A single ‘metals’ VaR that ignores this can badly misstate diversification within the book."
specs:
  - { benchmark: "LME Copper", venue: "LME", unit: "USD / tonne", size: "25 tonnes", settle: "Physical (prompt date)" }
  - { benchmark: "Gold", venue: "COMEX (CME)", unit: "USD / troy oz", size: "100 oz", settle: "Physical delivery" }
  - { benchmark: "Silver", venue: "COMEX (CME)", unit: "USD / troy oz", size: "5,000 oz", settle: "Physical delivery" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "Metals (non-ferrous)", publisher: "London Metal Exchange", url: "https://www.lme.com/metals", note: "The primary global base-metals exchange · lme.com" }
  - { title: "Precious Metals — Contract Specs", publisher: "CME Group", url: "https://www.cmegroup.com/markets/metals.html", note_label: "Primary:", note: "Exchange rulebook for gold, silver and copper futures · cmegroup.com" }
  - { title: "The Global Gold Market", publisher: "World Gold Council", url: "https://www.gold.org/gold-market-structure/global-gold-market", note: "Reference on gold market structure and demand · gold.org" }
  - { title: "Mineral Commodity Summaries", publisher: "U.S. Geological Survey (USGS)", url: "https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries", note: "Official world production, reserves and import-reliance data · usgs.gov" }
tool_cta_title: "Model metals price risk"
tool_cta_desc: "Separate industrial (base) and macro (precious) exposures and see the diversification in a metals book."
---

“Metals” is really two markets. **Base metals** — copper, aluminium, zinc,
priced largely through the **LME** — are an industrial bet, moving with
construction, manufacturing and the energy transition. **Precious metals** —
gold and silver, traded on **COMEX** and the **LBMA** — trade as much on the
dollar, real yields and safe-haven demand as on physical supply. Because the
two behave so differently, the biggest modelling mistake is treating them as one
exposure; a metals book’s real risk lives in how those two halves interact.

## How the market works

**Base metals** — copper, aluminium, zinc, nickel, lead and tin — trade on the
**London Metal Exchange (LME)**, the world centre for industrial-metals trading,
where the LME Official Price is the global benchmark used to index physical
contracts and hedges (copper and aluminium alone average hundreds of thousands
of lots traded daily, out to ten years). Physical settlement runs through a
network of LME-approved warehouses, so warehouse stocks and delivery premiums
matter to price. **Precious metals** trade differently: gold's three main venues
— the **London OTC market, US COMEX futures and the Shanghai Gold Exchange** —
account for over 90% of global volumes (roughly US$360bn/day in 2025), and price
is driven heavily by real rates, central-bank buying and safe-haven demand.

## Major trade flows

Base-metal supply is concentrated in mining regions — Chile and Peru dominate
copper ore, Indonesia leads nickel, Guinea and Australia bauxite — while **China**
is the pivotal smelter and consumer, anchoring demand for the industrial complex.
The USGS Mineral Commodity Summaries track world production, reserves and
import-reliance for more than 90 minerals, increasingly framed around
energy-transition "critical minerals." Precious-metal flows follow investment and
official-sector demand, with vaulting hubs in London, Zurich and New York and
strong physical demand centres in China and India.

<figure class="flowviz">
<p class="flowviz-title">Base-metals trade — mine supply, pricing &amp; exchange, demand</p>
<svg viewBox="0 0 760 312" role="img" aria-label="Schematic of base-metals flows from mine supply through LME pricing to demand centres" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="mtAh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#00d4ff"/></marker></defs>
<text x="112" y="22" fill="#f59e0b" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">MINE SUPPLY</text>
<text x="380" y="22" fill="#9ca3af" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">PRICING &amp; EXCHANGE</text>
<text x="648" y="22" fill="#00d4ff" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">DEMAND</text>
<path d="M206,71 Q380,50 554,83" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#mtAh)"/>
<path d="M206,145 Q380,110 554,83" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#mtAh)"/>
<path d="M206,219 Q380,190 554,157" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#mtAh)"/>
<path d="M206,71 Q380,210 554,231" fill="none" stroke="#00d4ff" stroke-width="1.4" opacity="0.3" marker-end="url(#mtAh)"/>
<g><rect x="18" y="44" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="44" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="70" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Chile &amp; Peru</text><text x="34" y="88" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">copper ore</text></g>
<g><rect x="18" y="118" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="118" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="144" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Indonesia</text><text x="34" y="162" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">nickel</text></g>
<g><rect x="18" y="192" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="192" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="218" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Australia</text><text x="34" y="236" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">bauxite · iron ore</text></g>
<g><rect x="554" y="56" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="56" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="82" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">China</text><text x="568" y="100" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">dominant smelter &amp; buyer</text></g>
<g><rect x="554" y="130" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="130" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="156" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Rest of Asia</text><text x="568" y="174" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">India · Japan · Korea</text></g>
<g><rect x="554" y="204" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="204" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="230" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Europe &amp; US</text><text x="568" y="248" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">industrial demand</text></g>
<g><rect x="286" y="52" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="70" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">LME Official Price</text></g>
<g><rect x="286" y="106" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="124" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">LME warehouse network</text></g>
<g><rect x="286" y="160" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="178" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Shanghai (SHFE / SGE)</text></g>
<g><rect x="286" y="214" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="232" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Seaborne to Asia</text></g>
<text x="380" y="300" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="middle">Base metals on the LME · gold on London · COMEX · SGE</text>
</svg>
<figcaption class="flowviz-src">Schematic — indicative flows, not to scale. Data: <a href="https://www.lme.com/metals">London Metal Exchange</a>, <a href="https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries">USGS Mineral Commodity Summaries</a> &amp; <a href="https://www.gold.org/gold-market-structure/global-gold-market">World Gold Council</a>. Interactive: <a href="https://www.lme.com/market-data/reports-and-data">LME reports &amp; data</a>.</figcaption>
</figure>
