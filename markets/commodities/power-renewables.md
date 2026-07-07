---
title: Power & Renewables
group: Commodities
tag: power-renewables
blurb: "Non-storable power, PPAs, shape and volume risk."
---

Electricity cannot be stored economically at scale, so power prices swing
hourly with demand, weather and the generation mix. This hub covers the shape,
volume and basis risks that make power markets distinct from other commodities,
along with the PPAs and hedges used to manage them.

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

**Sources & further reading**

- [Electricity Market Design](https://www.iea.org/reports/electricity-market-design) — International Energy Agency (IEA)
- [Wholesale Electricity Markets](https://www.eia.gov/electricity/wholesalemarkets/) — U.S. Energy Information Administration
- [Electricity Mid-Year Update 2025 — wholesale price trends](https://www.iea.org/reports/electricity-mid-year-update-2025/prices-trends-in-wholesale-markets-differ-across-regions) — International Energy Agency (IEA)
