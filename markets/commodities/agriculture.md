---
layout: commodity
title: Agriculture
group: Commodities · Agriculture
tag: agriculture
emoji: "🌾"
blurb: "Grains and softs, weather and seasonality risk."
standfirst: "The one commodity complex where the crop is grown to a calendar — so weather and the planting-to-harvest cycle drive price in a way no other market shares."
reviewed: 2026-07-08
benchmarks:
  - { name: "Corn", region: "US · CBOT", price: "$4.28", unit: "/bu", chg: "1.1% today", dir: dn }
  - { name: "Soybeans", region: "US · CBOT", price: "$10.85", unit: "/bu", chg: "0.6% today", dir: up }
  - { name: "Wheat", region: "US · CBOT", price: "$5.62", unit: "/bu", chg: "0.9% today", dir: up }
benchmark_note: "Illustrative values · production feed delayed ≥15 min · CBOT (CME) reference"
key_benchmarks:
  - { code: "CBOT grains", full: "Chicago Board of Trade", desc: "The global reference for corn, soybeans and wheat futures — the deepest and most-watched ag benchmarks." }
  - { code: "ICE softs", full: "Coffee, sugar, cocoa, cotton", desc: "The ‘softs’ complex trades on ICE, driven by tropical weather and concentrated growing regions." }
  - { code: "Cash / basis", full: "Local elevator", desc: "Physical grain trades as a basis to the futures — the local cash-to-futures spread is where merchandisers live." }
drivers:
  - { icon: "🌦️", title: "Weather", desc: "Drought, heat and excess rain at key growth stages are the dominant price mover — a single forecast can move the market." }
  - { icon: "🌱", title: "Planting & harvest cycle", desc: "Acreage decisions and the seasonal supply flush at harvest give ag its characteristic annual price pattern." }
  - { icon: "🚢", title: "Trade flows & policy", desc: "Export demand, tariffs and shipping (e.g. Black Sea, Mississippi) shift where and at what price crops clear." }
  - { icon: "📋", title: "USDA reports", desc: "WASDE and crop-progress reports reset supply/demand expectations and regularly trigger limit moves." }
risks:
  - { title: "Weather / yield risk", sev: hi, sev_label: "High", desc: "The defining risk: a growing-season weather shock can swing prices dramatically and is fundamentally unhedgeable at source." }
  - { title: "Seasonality risk", sev: hi, sev_label: "High", desc: "Prices follow a repeatable planting-to-harvest pattern; the old-crop / new-crop spread is a core ag position." }
  - { title: "Basis risk", sev: md, sev_label: "Medium", desc: "Local cash prices move against futures with logistics and local supply, leaving elevators and processors exposed." }
  - { title: "Policy / trade risk", sev: md, sev_label: "Medium", desc: "Tariffs, export bans and biofuel mandates can reroute global flows overnight." }
risk_note: "<b>Weather is the risk you can’t hedge at source.</b> Futures let you hedge price, but not the yield on your own acres. Ag risk management is as much about basis and quantity as it is about the flat price."
specs:
  - { benchmark: "Corn", venue: "CBOT (CME)", unit: "USc / bushel", size: "5,000 bu", settle: "Physical delivery" }
  - { benchmark: "Soybeans", venue: "CBOT (CME)", unit: "USc / bushel", size: "5,000 bu", settle: "Physical delivery" }
  - { benchmark: "Wheat (SRW)", venue: "CBOT (CME)", unit: "USc / bushel", size: "5,000 bu", settle: "Physical delivery" }
specs_note: "Specifications summarised for orientation; confirm current terms with the exchange rulebook before trading."
sources:
  - { title: "World Agricultural Supply & Demand Estimates (WASDE)", publisher: "U.S. Department of Agriculture (USDA)", url: "https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report", note: "The primary global ag supply/demand report · usda.gov" }
  - { title: "Grain: World Markets and Trade", publisher: "USDA Foreign Agricultural Service", url: "https://www.fas.usda.gov/data/grain-world-markets-and-trade", note: "Primary source on world grain trade and balances · usda.gov" }
  - { title: "Food Outlook", publisher: "UN Food and Agriculture Organization (FAO)", url: "https://www.fao.org/giews/reports/food-outlook/en/", note: "Intergovernmental crop and price monitoring · fao.org" }
  - { title: "Agricultural Futures — Contract Specs", publisher: "CME Group", url: "https://www.cmegroup.com/markets/agriculture.html", note_label: "Primary:", note: "Exchange rulebook for grains and oilseeds · cmegroup.com" }
tool_cta_title: "Model agricultural price risk"
tool_cta_desc: "See how basis and seasonal spreads sit alongside flat-price VaR for a grain book."
---

Agriculture is the one major complex grown to a **calendar**. Corn, soybeans
and wheat are planted, grown and harvested on an annual cycle, so **weather**
and **seasonality** drive price in a way energy and metals never see: a single
drought forecast can move the whole curve. Futures on the **CBOT** let a farmer
or processor hedge the flat price — but not the yield on their own acres, nor
the **local basis** between cash and futures. That gap between what you can and
can’t hedge is what defines risk management across the agricultural supply chain.

## How the market works

Ags divide into **grains and oilseeds** (corn, wheat, soybeans), **softs**
(coffee, sugar, cocoa, cotton) and livestock. Benchmark price discovery happens
on futures exchanges — principally **CBOT/CME** for grains and oilseeds and ICE
for softs — where producers, processors and merchants hedge. The defining driver
is the **crop cycle**: prices react to planting intentions, weather through the
growing season, and harvest yields, so a single drought or frost in a key region
can reset the balance. Because production is seasonal but consumption is
year-round, **stocks-to-use** ratios and the USDA's monthly supply-and-demand
balances are central to how the market prices risk.

## Major trade flows

Trade is regionally concentrated and politically sensitive. In **wheat**, Russia
is the largest exporter, followed by the EU, Canada, Australia and the US, with
the **Black Sea** a critical swing region. In **corn**, the US, Brazil, Argentina
and Ukraine lead exports; in **soybeans**, Brazil and the US dominate supply
while **China** is by far the largest importer, making the US–Brazil–China axis
pivotal to global oilseed pricing. The USDA's WASDE and Grain: World Markets and
Trade reports are the reference for these balances and flows.

<figure class="flowviz">
<p class="flowviz-title">Grain &amp; oilseed trade — exporters, routes, importers</p>
<svg viewBox="0 0 760 312" role="img" aria-label="Schematic of grain and oilseed trade flows from major exporters through shipping routes to major importers" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="agAh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#00d4ff"/></marker></defs>
<text x="112" y="22" fill="#f59e0b" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">EXPORTERS</text>
<text x="380" y="22" fill="#9ca3af" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">ROUTES</text>
<text x="648" y="22" fill="#00d4ff" font-family="Inter,sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="1">IMPORTERS</text>
<path d="M206,71 Q380,50 554,83" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#agAh)"/>
<path d="M206,145 Q380,110 554,83" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#agAh)"/>
<path d="M206,219 Q380,190 554,157" fill="none" stroke="#00d4ff" stroke-width="1.6" opacity="0.45" marker-end="url(#agAh)"/>
<path d="M206,71 Q380,210 554,231" fill="none" stroke="#00d4ff" stroke-width="1.4" opacity="0.3" marker-end="url(#agAh)"/>
<g><rect x="18" y="44" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="44" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="70" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">United States</text><text x="34" y="88" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">corn · soybeans</text></g>
<g><rect x="18" y="118" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="118" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="144" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Brazil</text><text x="34" y="162" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">soybeans · corn</text></g>
<g><rect x="18" y="192" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="18" y="192" width="4" height="54" rx="2" fill="#f59e0b"/><text x="34" y="218" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">Black Sea</text><text x="34" y="236" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">Russia · Ukraine wheat</text></g>
<g><rect x="554" y="56" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="56" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="82" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">China</text><text x="568" y="100" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">top soybean importer</text></g>
<g><rect x="554" y="130" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="130" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="156" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">MENA</text><text x="568" y="174" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">major wheat buyer</text></g>
<g><rect x="554" y="204" width="188" height="54" rx="9" fill="#0f1626" stroke="#1f2937"/><rect x="738" y="204" width="4" height="54" rx="2" fill="#00d4ff"/><text x="568" y="230" fill="#f9fafb" font-family="Inter,sans-serif" font-size="14" font-weight="700">SE Asia</text><text x="568" y="248" fill="#9ca3af" font-family="Inter,sans-serif" font-size="10.5">feed &amp; food grains</text></g>
<g><rect x="286" y="52" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="70" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Black Sea corridor</text></g>
<g><rect x="286" y="106" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="124" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">US Gulf / Mississippi</text></g>
<g><rect x="286" y="160" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="178" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Paraná / Santos</text></g>
<g><rect x="286" y="214" width="188" height="28" rx="14" fill="#0a0f1e" stroke="#1f2937"/><text x="380" y="232" fill="#cbd5e1" font-family="Inter,sans-serif" font-size="12" text-anchor="middle">Panama Canal</text></g>
<text x="380" y="300" fill="#6b7280" font-family="monospace" font-size="10.5" text-anchor="middle">Priced on CBOT/CME (grains) · ICE (softs)</text>
</svg>
<figcaption class="flowviz-src">Schematic — indicative flows, not to scale. Data: <a href="https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report">USDA WASDE</a> &amp; <a href="https://www.fas.usda.gov/data/grain-world-markets-and-trade">Grain: World Markets and Trade</a>; <a href="https://www.fao.org/giews/reports/food-outlook/en/">FAO</a>. Interactive: <a href="https://apps.fas.usda.gov/psdonline/app/index.html">USDA PSD Online</a>.</figcaption>
</figure>
