---
layout: commodity
title: Natural Gas & LNG
group: Commodities · Energy
tag: natural-gas-lng
emoji: "🔥"
blurb: "Henry Hub, TTF and JKM benchmarks, storage economics, basis and the seasonal risks that define gas markets."
standfirst: "Gas has no single global price. Three regional benchmarks — and the spreads between them — set physical flows, cargo economics and every hedging decision on the desk."
reviewed: 2026-07-08
benchmarks:
  - { name: "Henry Hub", region: "US · NYMEX",  price: "$2.84",  unit: "/MMBtu", chg: "1.7% today", dir: dn }
  - { name: "TTF",       region: "EU · ICE",    price: "€31.20", unit: "/MWh",   chg: "0.9% today", dir: up }
  - { name: "JKM",       region: "Asia · Platts",price: "$11.60", unit: "/MMBtu", chg: "2.3% today", dir: up }
benchmark_note: "Illustrative values · production feed delayed ≥15 min · settlement source shown per benchmark"
key_benchmarks:
  - { code: "Henry Hub", full: "Erath, Louisiana", desc: "The US physical & futures benchmark, settled on NYMEX. Deep, liquid, and the reference for North-American gas hedging." }
  - { code: "TTF", full: "Title Transfer Facility", desc: "The Dutch virtual hub that became Europe’s pricing anchor — the reference for pipeline gas and European LNG imports." }
  - { code: "JKM", full: "Japan-Korea Marker", desc: "Platts’ spot assessment for LNG delivered into North-East Asia — the marginal price that clears flexible cargoes." }
drivers:
  - { icon: "🌡️", title: "Weather & demand", desc: "Heating load in winter and gas-fired cooling in summer make gas the most weather-sensitive of the major commodities." }
  - { icon: "🛢️", title: "Storage & inventories", desc: "Weekly injection/withdrawal against the five-year range is the market’s primary balance signal." }
  - { icon: "🚢", title: "LNG arbitrage", desc: "When TTF or JKM rises far above Henry Hub, US export cargoes chase the spread — tightening domestic supply." }
  - { icon: "⚙️", title: "Supply & fuel-switching", desc: "Production, pipeline outages and coal-to-gas switching in power set the marginal supply stack." }
risks:
  - { title: "Seasonal risk", sev: hi, sev_label: "High", desc: "Winter demand can spike prices several-fold within weeks; the summer-to-winter spread is a position in itself." }
  - { title: "Basis (location) risk", sev: hi, sev_label: "High", desc: "A hedge at Henry Hub does not cover a physical position priced at TTF or a regional US hub — the spread is unhedged." }
  - { title: "Storage / time-spread risk", sev: md, sev_label: "Medium", desc: "The value of injecting now to sell later swings with the calendar spread and available capacity." }
  - { title: "Volume / swing risk", sev: md, sev_label: "Medium", desc: "Demand volume is itself uncertain and weather-driven, so even a price-hedged book carries quantity risk." }
risk_note: "<b>Why basis risk dominates gas.</b> Because the three benchmarks are physically separated, the single biggest modelling error is treating a Henry-Hub hedge as protection for a TTF- or JKM-priced exposure. Location spreads must be modelled explicitly."
specs:
  - { benchmark: "Henry Hub", venue: "NYMEX (CME)", unit: "USD / MMBtu", size: "10,000 MMBtu", settle: "Physical / financial" }
  - { benchmark: "TTF", venue: "ICE / EEX", unit: "EUR / MWh", size: "1 MW × period", settle: "Cash (index)" }
  - { benchmark: "JKM", venue: "ICE (swap)", unit: "USD / MMBtu", size: "10,000 MMBtu", settle: "Cash vs Platts" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "Natural Gas Explained", publisher: "U.S. Energy Information Administration (EIA)", year: 2025, url: "https://www.eia.gov/energyexplained/natural-gas/", note: "Official US energy statistics agency · eia.gov" }
  - { title: "Natural Gas Weekly Update", publisher: "U.S. EIA", url: "https://www.eia.gov/naturalgas/weekly/", note: "Weekly storage and price data — the market’s primary inventory benchmark · eia.gov" }
  - { title: "Gas Market Report", publisher: "International Energy Agency (IEA)", year: 2025, url: "https://www.iea.org/topics/natural-gas", note: "Intergovernmental energy body · iea.org" }
  - { title: "Annual Report on LNG", publisher: "GIIGNL (International Group of LNG Importers)", url: "https://www.giignl.org/annual-report", note: "Primary source on global LNG trade flows · giignl.org" }
  - { title: "LNG Outlook", publisher: "Shell", url: "https://www.shell.com/what-we-do/oil-and-natural-gas/liquefied-natural-gas-lng.html", note_label: "Industry:", note: "Widely-cited long-range LNG demand outlook · shell.com" }
  - { title: "Henry Hub Natural Gas Futures — Contract Specs", publisher: "CME Group", url: "https://www.cmegroup.com/markets/energy/natural-gas/natural-gas.contractSpecs.html", note_label: "Primary:", note: "The exchange rulebook itself · cmegroup.com" }
tool_cta_title: "Model gas price risk"
tool_cta_desc: "Run a parametric VaR on a Henry Hub / TTF book and see the basis contribution."
---

Unlike crude oil, natural gas is expensive to move, so it prices **regionally**
rather than globally. North America trades off **Henry Hub**, Europe off the
Dutch **TTF**, and Asian LNG off the **Japan-Korea Marker (JKM)**. LNG shipping
links these pools, but only imperfectly — which means the **spreads between
them**, not any single price, are what govern cargo economics and hedging
strategy.

## How the market works

Unlike oil, natural gas has no single global price. Pipeline gas is priced at
regional hubs — **Henry Hub** (US) and **TTF** (Europe) — while seaborne
**LNG** links those regions to Asia via the **JKM** benchmark. Liquefied natural
gas is chilled to a liquid, shipped, and re-gasified, so LNG turns a set of
regional markets into one increasingly connected system: European and Asian
benchmarks now move almost in lockstep. Gas is heavily seasonal (heating and
cooling demand), and **storage** plus the summer-to-winter spread are central to
how the market clears. Producers, utilities and traders hedge on ICE (TTF),
CME/NYMEX (Henry Hub) and JKM derivatives.

## Major trade flows

LNG trade is dominated by three exporters — the **United States, Qatar and
Australia**, which together supply around 60% of global LNG; the US became the
largest exporter and is expected to provide roughly a third of supply by 2030.
Demand is led by **Asia** (China is the largest importer, with India and other
emerging buyers growing), while **Europe** pivoted hard to LNG after 2022 to
replace Russian pipeline gas. Shell's outlook sees global LNG demand rising
around 65% by 2050 — a structurally growing, flexible market whose price
spreads continually redirect cargoes between the Atlantic and Pacific basins.

<figure class="flowviz">
<p class="flowviz-title">LNG trade flows — who supplies, the shipping routes, who buys</p>
<svg viewBox="0 0 760 312" role="img" aria-label="Schematic of LNG trade flows from major exporters through shipping routes to major importers" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="gasAh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#00d4ff"/></marker></defs>
<text x="112" y="22" fill="#f59e0b" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">SUPPLIERS</text>
<text x="380" y="22" fill="#9ca3af" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">SHIPPING ROUTES</text>
<text x="648" y="22" fill="#00d4ff" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">BUYERS</text>
<path d="M206,71 Q380,50 554,83" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#gasAh)"/>
<path d="M206,71 Q380,210 554,231" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#gasAh)"/>
<path d="M206,145 Q380,110 554,83" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#gasAh)"/>
<path d="M206,219 Q380,190 554,157" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#gasAh)"/>
<g><rect x="18" y="44" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="44" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="70" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">United States</text><text x="34" y="88" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">largest LNG exporter</text></g>
<g><rect x="18" y="118" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="118" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="144" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Qatar</text><text x="34" y="162" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">low-cost, via Hormuz</text></g>
<g><rect x="18" y="192" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="192" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="218" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Australia</text><text x="34" y="236" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">Pacific to Asia</text></g>
<g><rect x="554" y="56" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="56" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="82" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">China</text><text x="568" y="100" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">largest LNG importer</text></g>
<g><rect x="554" y="130" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="130" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="156" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Japan &amp; Korea</text><text x="568" y="174" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">mature Asian demand</text></g>
<g><rect x="554" y="204" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="204" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="230" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Europe</text><text x="568" y="248" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">post-2022 pull</text></g>
<g><rect x="286" y="52" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="70" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Panama Canal</text></g>
<g><rect x="286" y="106" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="124" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Strait of Hormuz</text></g>
<g><rect x="286" y="160" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="178" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Suez Canal</text></g>
<g><rect x="286" y="214" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="232" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Malacca Strait</text></g>
<text x="380" y="300" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="middle">Priced regionally: Henry Hub · TTF · JKM</text>
</svg>
<figcaption class="flowviz-src">Schematic — indicative flows, not to scale. Data: <a href="https://www.giignl.org/annual-report">GIIGNL Annual Report on LNG</a>, <a href="https://www.shell.com/what-we-do/oil-and-natural-gas/liquefied-natural-gas-lng.html">Shell LNG Outlook</a> &amp; <a href="https://www.oxfordenergy.org/gas-programme/">OIES</a>. Interactive: <a href="https://www.iea.org/data-and-statistics/data-tools/global-lng-capacity-tracker">IEA Global LNG Capacity Tracker</a>.</figcaption>
</figure>
