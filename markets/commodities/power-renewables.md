---
layout: commodity
title: Power & Renewables
group: Commodities · Energy
tag: power-renewables
emoji: "⚡"
blurb: "Non-storable power, PPAs, shape and volume risk."
standfirst: "Electricity is the only major commodity that can’t be stored, so it must be balanced every second — which makes its risks shape, timing and volume, not just flat price."
reviewed: 2026-07-08
benchmarks:
  - { name: "German Base", region: "EU · EPEX/EEX", price: "€92.5", unit: "/MWh", chg: "3.1% today", dir: up }
  - { name: "PJM West",    region: "US · PJM",      price: "$41.8", unit: "/MWh", chg: "1.2% today", dir: dn }
  - { name: "EUA Carbon",  region: "EU · ICE",      price: "€71.0", unit: "/t",   chg: "0.8% today", dir: up }
benchmark_note: "Illustrative values · day-ahead / prompt references · settlement source shown per market"
key_benchmarks:
  - { code: "Day-ahead", full: "Hourly / block auction", desc: "Most physical power clears in day-ahead auctions (EPEX, Nord Pool, PJM); the hourly shape is the core price signal." }
  - { code: "Forward / PPA", full: "Baseload & peakload", desc: "Longer-dated hedging trades as baseload and peakload blocks, or bilateral Power Purchase Agreements with generators." }
  - { code: "Ancillary / balancing", full: "Real-time", desc: "Reserve, frequency and imbalance markets price the second-by-second cost of keeping supply and demand equal." }
drivers:
  - { icon: "🌡️", title: "Demand & weather", desc: "Load follows temperature and time of day; peaks and troughs within a single day can differ several-fold." }
  - { icon: "☀️", title: "Renewable output", desc: "Wind and solar are weather-driven and near-zero marginal cost, so they reshape the price curve hour by hour." }
  - { icon: "🔥", title: "Fuel & the merit order", desc: "Gas and carbon prices set the marginal generator, and therefore the clearing power price, when renewables fall short." }
  - { icon: "🔌", title: "Grid & interconnection", desc: "Transmission limits and outages create locational price differences — the same commodity trades at different prices by node." }
risks:
  - { title: "Shape (profile) risk", sev: hi, sev_label: "High", desc: "A flat hedge can’t match a peaky physical profile; the intraday and peak/off-peak shape is an exposure in itself." }
  - { title: "Volume risk", sev: hi, sev_label: "High", desc: "Demand and renewable generation volumes are uncertain, so a price-hedged position still carries quantity risk." }
  - { title: "Basis (locational) risk", sev: md, sev_label: "Medium", desc: "Nodal and zonal prices diverge with congestion; a hub hedge leaves the node-to-hub spread open." }
  - { title: "Cannibalisation risk", sev: md, sev_label: "Medium", desc: "High renewable output depresses prices exactly when a wind or solar asset is generating most — eroding its capture price." }
risk_note: "<b>Power risk is about shape, not just level.</b> Because electricity can’t be stored, matching the hourly profile of demand and generation matters as much as the average price. A baseload hedge against a peaky load leaves real risk on the table."
specs:
  - { benchmark: "German Power", venue: "EEX", unit: "EUR / MWh", size: "1 MW × period", settle: "Cash / physical" }
  - { benchmark: "PJM Western Hub", venue: "PJM / ICE", unit: "USD / MWh", size: "Varies (nodal)", settle: "Cash (LMP)" }
  - { benchmark: "EU Allowance (EUA)", venue: "ICE / EEX", unit: "EUR / tonne CO₂", size: "1,000 t", settle: "Physical (allowance)" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "Electricity Market Design", publisher: "International Energy Agency (IEA)", url: "https://www.iea.org/reports/electricity-market-design", note: "Intergovernmental reference on power market structure · iea.org" }
  - { title: "Wholesale Electricity Markets", publisher: "U.S. EIA", url: "https://www.eia.gov/electricity/wholesalemarkets/", note: "Official map and explainer of US wholesale power markets · eia.gov" }
  - { title: "Electricity Mid-Year Update 2025 — wholesale price trends", publisher: "International Energy Agency (IEA)", year: 2025, url: "https://www.iea.org/reports/electricity-mid-year-update-2025/prices-trends-in-wholesale-markets-differ-across-regions", note: "Regional wholesale price analysis · iea.org" }
  - { title: "Energy Markets & Locational Marginal Pricing", publisher: "PJM Interconnection", url: "https://www.pjm.com/markets-and-operations", note: "Primary source on US nodal power pricing · pjm.com" }
  - { title: "EU Emissions Trading System (EU ETS)", publisher: "European Commission", url: "https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets_en", note: "The carbon price that sets the merit order · europa.eu" }
tool_cta_title: "Model power price risk"
tool_cta_desc: "Explore how shape and volume risk sit alongside flat-price VaR for a power book."
---

Electricity cannot be stored economically at scale, so it has to be balanced
in **real time** — generation must equal demand every second. That single fact
reshapes the risk. Price swings hourly with demand, weather and the generation
mix, and the exposures that matter are **shape** (matching the hourly profile),
**volume** (uncertain quantity) and **locational basis** (congestion between
nodes) — not just the average price. Power Purchase Agreements and shaped
hedges exist precisely to manage risks other commodities never face.

## How the market works

Because power is **not storable**, it trades across a layered set of markets that
tighten as delivery approaches. Longer-dated **futures and forwards** cover
years, quarters and months at a fixed price; these settle against **day-ahead
auctions** that price each hour of the following day; and **intraday** trading
(down to 15-minute blocks) balances the system in real time. To ensure enough
generation is available years ahead, many systems run **capacity markets** that
procure megawatts of firm capacity with three-to-four-year lead times.
**Power purchase agreements (PPAs)** let generators and large buyers lock in
price over the long term — important as wind and solar add intermittency, and
with it **shape** (when power is produced) and **volume** risk.

## Major trade flows

Electricity is largely a regional commodity — it flows within interconnected
grids and market zones (e.g. the US ISOs/RTOs, and European coupled day-ahead
markets) rather than trading globally like oil or LNG. The defining shift is the
rising share of variable renewables, which the IEA notes is forcing market
designs to evolve: as more wind and solar enter, wholesale prices become more
volatile and long-term markets face persistent gaps in liquidity, making PPAs
and capacity mechanisms increasingly central to managing risk and financing new
build.

<figure class="flowviz">
<p class="flowviz-title">How power trades — generation, market layers, demand</p>
<svg viewBox="0 0 760 312" role="img" aria-label="Schematic of the electricity market: generation feeding market layers that tighten toward real time, serving demand" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="pwAh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#00d4ff"/></marker></defs>
<text x="112" y="22" fill="#f59e0b" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">GENERATION</text>
<text x="380" y="22" fill="#9ca3af" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">MARKET (TIME TO DELIVERY)</text>
<text x="648" y="22" fill="#00d4ff" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">DEMAND</text>
<path d="M206,71 Q380,50 554,83" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#pwAh)"/>
<path d="M206,145 Q380,150 554,157" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#pwAh)"/>
<path d="M206,219 Q380,235 554,231" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#pwAh)"/>
<path d="M206,145 Q380,105 554,83" fill="none" stroke="#00d4ff" stroke-width="1.4" opacity="0.3" marker-end="url(#pwAh)"/>
<g><rect x="18" y="44" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="44" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="70" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Gas &amp; Coal</text><text x="34" y="88" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">dispatchable</text></g>
<g><rect x="18" y="118" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="118" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="144" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Wind &amp; Solar</text><text x="34" y="162" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">variable, weather-driven</text></g>
<g><rect x="18" y="192" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="192" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="218" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Nuclear &amp; Hydro</text><text x="34" y="236" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">baseload / flexible</text></g>
<g><rect x="554" y="56" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="56" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="82" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Industry</text><text x="568" y="100" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">large loads · PPAs</text></g>
<g><rect x="554" y="130" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="130" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="156" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Business</text><text x="568" y="174" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">commercial supply</text></g>
<g><rect x="554" y="204" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="204" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="230" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Homes &amp; EVs</text><text x="568" y="248" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">retail load</text></g>
<g><rect x="286" y="52" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="70" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Forwards (years–months)</text></g>
<g><rect x="286" y="106" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="124" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Day-ahead auction</text></g>
<g><rect x="286" y="160" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="178" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Intraday (15-min)</text></g>
<g><rect x="286" y="214" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="232" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Capacity market (3–4 yr)</text></g>
<text x="380" y="300" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="middle">Not storable — priced from years out down to real time</text>
</svg>
<figcaption class="flowviz-src">Schematic — illustrative market structure. Data: <a href="https://www.iea.org/reports/electricity-market-design">IEA Electricity Market Design</a> &amp; <a href="https://www.eia.gov/electricity/wholesalemarkets/">U.S. EIA Wholesale Electricity Markets</a>. Interactive: <a href="https://www.eia.gov/electricity/wholesalemarkets/">EIA wholesale markets map</a>.</figcaption>
</figure>
