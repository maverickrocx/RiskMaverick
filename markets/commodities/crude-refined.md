---
layout: commodity
title: Crude & Refined
group: Commodities · Energy
tag: crude-refined
emoji: "🛢️"
blurb: "Brent and WTI benchmarks, crack spreads and the refining-margin risks that sit between crude and product prices."
standfirst: "The deepest commodity market in the world — but the money at a refinery is made in the spread between crude bought and product sold, not in the flat price alone."
reviewed: 2026-07-08
benchmarks:
  - { name: "Brent", region: "Global · ICE", price: "$78.40", unit: "/bbl", chg: "0.6% today", dir: up }
  - { name: "WTI",   region: "US · NYMEX",   price: "$74.10", unit: "/bbl", chg: "0.4% today", dir: up }
  - { name: "Dubai", region: "Asia · Platts",price: "$77.20", unit: "/bbl", chg: "0.3% today", dir: dn }
benchmark_note: "Illustrative values · production feed delayed ≥15 min · settlement source shown per benchmark"
key_benchmarks:
  - { code: "Brent", full: "North Sea", desc: "The waterborne global benchmark; prices roughly two-thirds of internationally traded crude and settles on ICE." }
  - { code: "WTI", full: "Cushing, Oklahoma", desc: "The US light-sweet benchmark, settled on NYMEX. Priced at an inland hub, so it carries logistics basis to the coast." }
  - { code: "Dubai / Oman", full: "Medium-sour, Asia", desc: "The reference for Middle-East crude sold into Asia — the marker for sour grades Brent and WTI don’t represent." }
drivers:
  - { icon: "🛢️", title: "OPEC+ supply policy", desc: "Coordinated production quotas are the single largest swing factor in the global supply balance." }
  - { icon: "🌍", title: "Demand & the cycle", desc: "Oil demand tracks global growth, transport and industrial activity — the demand side of the balance." }
  - { icon: "📦", title: "Inventories", desc: "Commercial stock builds and draws (EIA, IEA) signal whether the market is tightening or loosening week to week." }
  - { icon: "⚡", title: "Geopolitics", desc: "Sanctions, conflict and chokepoints (Hormuz, Suez) add a risk premium that can move price sharply and suddenly." }
risks:
  - { title: "Flat-price risk", sev: hi, sev_label: "High", desc: "Outright exposure to the level of crude — the largest and most volatile risk for producers, refiners and airlines alike." }
  - { title: "Crack-spread risk", sev: hi, sev_label: "High", desc: "Refining margin is the crude-to-product spread; it can compress even when flat price is stable, squeezing refiners." }
  - { title: "Grade / quality basis", sev: md, sev_label: "Medium", desc: "Sweet vs sour and light vs heavy differentials mean a Brent hedge imperfectly covers a differently-graded barrel." }
  - { title: "Time-spread risk", sev: md, sev_label: "Medium", desc: "Backwardation and contango change storage economics and the roll cost of maintaining a futures hedge." }
risk_note: "<b>Flat price is only half the picture.</b> A refiner can be fully hedged on crude and still lose money if the crack spread collapses. Model crude, products and the spread between them as distinct exposures."
specs:
  - { benchmark: "Brent", venue: "ICE", unit: "USD / barrel", size: "1,000 bbl", settle: "Cash (index)" }
  - { benchmark: "WTI", venue: "NYMEX (CME)", unit: "USD / barrel", size: "1,000 bbl", settle: "Physical delivery" }
  - { benchmark: "RBOB Gasoline", venue: "NYMEX (CME)", unit: "USD / gallon", size: "42,000 gal", settle: "Physical delivery" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "Oil Market Report", publisher: "International Energy Agency (IEA)", year: 2025, url: "https://www.iea.org/reports/oil-market-report", note: "Intergovernmental energy body; monthly balances · iea.org" }
  - { title: "Benchmarks play an important role in pricing crude oil", publisher: "U.S. EIA", url: "https://www.eia.gov/todayinenergy/detail.php?id=18571", note: "Official US explainer on crude benchmarks · eia.gov" }
  - { title: "Short-Term Energy Outlook", publisher: "U.S. EIA", url: "https://www.eia.gov/outlooks/steo/", note: "Official US inventory and production outlook · eia.gov" }
  - { title: "Monthly Oil Market Report (MOMR)", publisher: "OPEC", url: "https://www.opec.org/monthly-oil-market-report.html", note: "Primary source on OPEC+ supply policy · opec.org" }
  - { title: "Light Sweet Crude Oil (WTI) — Contract Specs", publisher: "CME Group", url: "https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.contractSpecs.html", note_label: "Primary:", note: "The exchange rulebook itself · cmegroup.com" }
tool_cta_title: "Model oil & margin risk"
tool_cta_desc: "Run a VaR on a crude book, or decompose crack-spread exposure into crude and product legs."
---

Crude oil is the deepest commodity market in the world, and its flat price is
the reference every other energy risk hangs off. But the risk that defines the
sector is the **crack spread** — the gap between the crude a refiner buys and
the products it sells. A barrel can be fully hedged on crude and still lose
money if that margin compresses, which is why crude and refined products are
modelled as **distinct, related exposures** rather than one price.

## How the market works

Physical crude is priced off a handful of **benchmarks**. **Brent** — four light,
sweet North Sea streams (Brent, Forties, Ekofisk, Oseberg) — is the global
reference, used to price crude across Europe, Africa and much of Asia. **WTI**, a
light sweet grade delivered at Cushing, Oklahoma, anchors US pricing, while
**Dubai/Oman** prices sour barrels flowing to Asia. Around those benchmarks sits
one of the largest financial markets anywhere: ICE Brent and CME/NYMEX WTI
futures and options let producers, refiners and traders hedge price risk.

Refiners buy crude and sell products (gasoline, diesel, jet fuel). Their margin —
the **crack spread**, often modelled as a 3:2:1 ratio — is the core of refining
risk: it widens or collapses as crude and product prices move apart. On the
supply side, **OPEC+** actively manages output through production quotas, making
its meetings a primary price driver.

## Major trade flows

The biggest exporters are the **Middle East** (Saudi Arabia, the UAE, Iraq)
alongside a fast-growing **Americas** complex — the US, Brazil, Canada, Guyana
and Argentina were at or near record output through 2025. Demand is anchored in
**Asia**, where China and India are the marginal buyers, pulling growing
long-haul flows from the Americas to markets east of Suez. Geopolitics
continually re-routes barrels: US and UK sanctions on Rosneft and Lukoil cut
Russia's exports to roughly 6.9 mb/d in late 2025, while sanctioned Iranian crude
flows almost entirely to independent Chinese refiners.

<figure class="flowviz">
<p class="flowviz-title">Crude oil trade flows — who supplies, the key routes, who buys</p>
<svg viewBox="0 0 760 312" role="img" aria-label="Schematic of crude oil trade flows from major suppliers through key shipping chokepoints to major buyers" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="crAh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#00d4ff"/></marker></defs>
<text x="112" y="22" fill="#f59e0b" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">SUPPLIERS</text>
<text x="380" y="22" fill="#9ca3af" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">KEY ROUTES &amp; CHOKEPOINTS</text>
<text x="648" y="22" fill="#00d4ff" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">BUYERS</text>
<path d="M206,71 Q380,50 554,83" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#crAh)"/>
<path d="M206,71 Q380,125 554,157" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#crAh)"/>
<path d="M206,145 Q380,210 554,231" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#crAh)"/>
<path d="M206,219 Q380,150 554,83" fill="none" stroke="#00d4ff" stroke-width="1.4" opacity="0.3" marker-end="url(#crAh)"/>
<g><rect x="18" y="44" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="44" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="70" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Middle East</text><text x="34" y="88" fill="#9ca3af" font-family="Inter,sans-serif" font-size="11">Saudi · UAE · Iraq</text></g>
<g><rect x="18" y="118" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="118" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="144" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Americas</text><text x="34" y="162" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">US · Brazil · Canada · Guyana</text></g>
<g><rect x="18" y="192" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="192" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="218" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Russia</text><text x="34" y="236" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">sanctioned barrels → Asia</text></g>
<g><rect x="554" y="56" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="56" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="82" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">China</text><text x="568" y="100" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">world's largest importer</text></g>
<g><rect x="554" y="130" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="130" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="156" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">India</text><text x="568" y="174" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">fast-growing demand</text></g>
<g><rect x="554" y="204" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="204" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="230" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Europe</text><text x="568" y="248" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">seaborne since 2022</text></g>
<g><rect x="286" y="52" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="70" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Strait of Hormuz</text></g>
<g><rect x="286" y="106" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="124" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Suez / SUMED</text></g>
<g><rect x="286" y="160" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="178" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Malacca Strait</text></g>
<g><rect x="286" y="214" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="232" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Cape of Good Hope</text></g>
<text x="380" y="300" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="middle">Physically priced off Brent · WTI · Dubai/Oman</text>
</svg>
<figcaption class="flowviz-src">Schematic — indicative flows, not to scale. Data: <a href="https://www.iea.org/reports/oil-market-report">IEA Oil Market Report</a> &amp; <a href="https://www.eia.gov/todayinenergy/detail.php?id=18571">U.S. EIA</a>. Interactive map: <a href="https://www.eia.gov/international/data/world">EIA International Energy Data</a>.</figcaption>
</figure>
