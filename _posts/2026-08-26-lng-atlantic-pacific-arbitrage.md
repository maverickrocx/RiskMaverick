---
title: "The Atlantic–Pacific LNG Arbitrage: How Price Decides Where a Cargo Goes"
date: 2026-08-26 09:30:00 +0530
kind: analysis
markets: [natural-gas-lng]
concepts: [market-risk, hedging-derivatives]
excerpt: "JKM minus TTF is not the arbitrage. The arbitrage is JKM minus TTF minus the cost of sailing further — and in 2026 that cost changed twice."
sources:
  - { title: "Gas Market Report, Q3-2026", publisher: "International Energy Agency", url: "https://www.iea.org/reports/gas-market-report-q3-2026/executive-summary" }
  - { title: "U.S. natural gas exports to grow nearly 30% by 2027 as LNG facilities ramp up", publisher: "U.S. Energy Information Administration", url: "https://www.eia.gov/todayinenergy/detail.php?id=67484" }
  - { title: "Short-Term Energy Outlook, August 2026", publisher: "U.S. Energy Information Administration", url: "https://www.eia.gov/outlooks/steo/" }
  - { title: "Asian LNG demand to decline for a second consecutive year", publisher: "Wood Mackenzie", url: "https://www.woodmac.com/press-releases/asian-lng-demand-decline-for-second-consecutive-year/" }
  - { title: "Europe's gas prices are surging. Who will be the first to pay more?", publisher: "Euronews", url: "https://www.euronews.com/business/2026/08/26/europes-gas-prices-are-surging-who-will-be-the-first-to-pay-more" }
  - { title: "The EU will need higher LNG imports to refill gas storage ahead of winter", publisher: "ACER — EU Agency for the Cooperation of Energy Regulators", url: "https://www.acer.europa.eu/news/eu-will-need-higher-lng-imports-refill-gas-storage-ahead-winter" }
---

An LNG cargo leaving the US Gulf Coast has a choice. It can sail east to
Europe in about eleven days, or it can sail to Japan — and in 2026, with the
Strait of Hormuz effectively closed, that means going the long way round the
Cape of Good Hope, thirty-three days at sea.

The cargo goes wherever it earns more. That sounds obvious. What is not
obvious, and what trips up most people looking at this market for the first
time, is that **the higher price does not automatically win**. Asia is almost
always more expensive than Europe. That does not mean cargoes always go to
Asia. What matters is whether Asia is more expensive *by more than the extra
cost of getting there*.

That difference — the spread net of the cost of delivery — is the arbitrage.
This piece explains how it is calculated, what closes it, and what happened to
it in 2026.

<div class="rm-kf">
  <div><div class="k">TTF, 1 Jan 2026</div><div class="v">€29</div><div class="n">per MWh</div></div>
  <div><div class="k">TTF, 26 Aug 2026</div><div class="v">€66</div><div class="n">per MWh, +128%</div></div>
  <div><div class="k">EU storage</div><div class="v">63%</div><div class="n">vs 79% five-year average</div></div>
  <div><div class="k">Qatar + UAE LNG</div><div class="v">−45%</div><div class="n">year on year, IEA</div></div>
</div>

## Two basins, one fleet

The world LNG market is usually described as two basins. It is a useful
simplification, and worth stating precisely because the whole trade rests on it.

The **Atlantic basin** is the United States, Trinidad, Nigeria, Algeria, Norway
and Russia's Yamal on the supply side, selling into Europe, the UK, Turkey and
South America. Its reference price is **TTF**, the Dutch virtual trading point,
which is a pipeline hub price that LNG must compete with rather than an LNG
price as such.

The **Pacific basin** is Australia, Malaysia, Indonesia, Brunei, Papua New
Guinea, Russia's Sakhalin and now Canada's west coast, selling into Japan,
China, Korea, Taiwan and South-East Asia. Its reference price is **JKM** — the
Japan–Korea Marker, an assessment of spot cargoes delivered into North-East
Asia.

Between them sits the Middle East — Qatar above all — which physically ships
into *both* basins through the Strait of Hormuz. That is why a single military
event in one waterway repriced gas on two continents at once.

And connecting all of it is one global fleet of roughly 700 ships. A vessel
does not belong to a basin. It goes where the freight rate is best, which is
why freight is not a cost you can treat as a constant.

<div class="rm-flow">
  <div><div class="s">STEP 1</div><div class="h">Buy the molecule</div><div class="d">Feed gas at Henry Hub, plus the shrinkage burned to liquefy it</div></div>
  <div><div class="s">STEP 2</div><div class="h">Pay the tolling fee</div><div class="d">Fixed liquefaction charge, payable whether you lift or not</div></div>
  <div><div class="s">STEP 3</div><div class="h">Choose the destination</div><div class="d">Compare TTF and JKM net of the cost of reaching each</div></div>
  <div><div class="s">STEP 4</div><div class="h">Pay to get there</div><div class="d">Charter, bunkers, canal or cape, boil-off, port and regas</div></div>
  <div><div class="s">STEP 5</div><div class="h">Sell, or cancel</div><div class="d">If neither netback covers the variable cost, cancel the cargo</div></div>
</div>

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>Picture the world gas market as two large neighbourhoods sharing one fleet of
  delivery vans. Europe is one, Asia is the other, and Qatar sits between them
  delivering to both. The vans do not belong to a neighbourhood — they go wherever
  the delivery fee is best. That is why one blocked road changed prices on two
  continents at the same time.</p>
</div>

## The arithmetic

Here is the calculation an LNG desk runs several times a day. The numbers below
are illustrative but sit within 2026 market ranges, and every step is shown so
you can substitute your own.

Take a standard cargo of about **3.6 trillion British thermal units** (roughly a
174,000 cubic metre vessel), lifted free-on-board from the US Gulf.

Cargo-size conventions vary — depending on vessel and heating value you will see
anything from 3.4 to 3.8 TBtu quoted for the same class of ship. It matters less
than you would think. Charter and port costs per MMBtu scale inversely with cargo
size, while boil-off does not (it is a percentage of the cargo either way). Rerun
the whole calculation at 3.4 TBtu and the threshold below moves from USD 1.82 to
about USD 1.89 — roughly 4% on the number that decides the trade. Use your own
vessel's figure, but do not expect it to flip the answer.

<div class="rm-calc">
  <div><span class="lbl">Feed gas at Henry Hub, $3.00/MMBtu × 1.15 for shrinkage</span><span>$3.45</span></div>
  <div><span class="lbl">Liquefaction tolling fee</span><span>$2.50</span></div>
  <div class="rule"><span class="lbl">Cost of the cargo, FOB US Gulf</span><span>$5.95 /MMBtu</span></div>
</div>

That FOB cost is the same whichever way the ship turns. Everything that follows
is the cost of the voyage.

<h4>Route A — US Gulf to Northwest Europe</h4>

<div class="rm-calc">
  <div><span class="lbl">Charter, 22 days round trip at $80,000/day ÷ 3.6m MMBtu</span><span>$0.49</span></div>
  <div><span class="lbl">Bunkers and port charges</span><span>$0.20</span></div>
  <div><span class="lbl">Boil-off, 11 laden days at 0.10%/day, valued at $22/MMBtu</span><span>$0.24</span></div>
  <div class="rule"><span class="lbl">Cost of delivery to Europe</span><span>$0.93 /MMBtu</span></div>
</div>

<h4>Route B — US Gulf to Japan, via the Cape of Good Hope</h4>

<div class="rm-calc">
  <div><span class="lbl">Charter, 66 days round trip at $80,000/day ÷ 3.6m MMBtu</span><span>$1.47</span></div>
  <div><span class="lbl">Bunkers and port charges</span><span>$0.55</span></div>
  <div><span class="lbl">Boil-off, 33 laden days at 0.10%/day, valued at $22/MMBtu</span><span>$0.73</span></div>
  <div class="rule"><span class="lbl">Cost of delivery to Asia</span><span>$2.75 /MMBtu</span></div>
</div>

Subtract one from the other and you have the number that actually governs the
trade:

<div class="rm-calc">
  <div><span class="lbl">Cost of delivery to Asia</span><span>$2.75</span></div>
  <div><span class="lbl">less cost of delivery to Europe</span><span>−$0.93</span></div>
  <div class="rule"><span class="lbl">The arbitrage threshold</span><span>$1.82 /MMBtu</span></div>
</div>

<div class="rm-call">
  <div class="t">The rule</div>
  <p>A US cargo sails to Asia only when <b>JKM exceeds TTF by more than the
  freight differential</b> — here, about USD 1.82 per MMBtu. Below that, Europe
  wins even though Asia pays more. The arbitrage is "open" above the threshold
  and "shut" below it.</p>
  <p>Every one of those inputs moves. Double the charter rate and the threshold
  roughly doubles. Reopen Hormuz and the Asian voyage shortens by a fortnight,
  and the threshold collapses. That is why LNG traders watch freight and canal
  transits as closely as they watch gas prices.</p>
</div>

At a **USD 5 per MMBtu** JKM premium — which is where the spread went at the
height of the summer disruption — the trade nets USD 3.18 per MMBtu, or about
**USD 11.4 million on a single cargo**. At today's near-parity between JKM and
TTF, the same voyage loses money and the cargo discharges in Europe.

<div class="rm-fig">
  <p class="rm-fig-t">When the arbitrage opens</p>
  <p class="rm-fig-s">JKM minus TTF, against the cost of the longer voyage</p>
  <svg viewBox="0 0 800 230" role="img" aria-label="Chart showing JKM minus TTF spread against the freight differential threshold">
    <rect x="120" y="20" width="640" height="150" fill="none" stroke="var(--border)"/>
    <rect x="120" y="20" width="640" height="95.4" fill="var(--pos)" opacity=".10"/>
    <rect x="120" y="115.4" width="640" height="54.6" fill="var(--neg)" opacity=".08"/>
    <g>
      <rect x="180" y="20" width="90" height="150" fill="var(--pos)" opacity=".65"/>
      <rect x="360" y="89" width="90" height="81" fill="var(--pos)" opacity=".5"/>
      <rect x="540" y="158" width="90" height="12" fill="var(--neg)" opacity=".65"/>
    </g>
    <line x1="120" y1="115.4" x2="760" y2="115.4" stroke="var(--accent)" stroke-width="2" stroke-dasharray="6 4"/>
    <text x="756" y="111" font-family="Inter, sans-serif" font-size="11.5" fill="var(--accent-text)" text-anchor="end">threshold $1.82</text>
    <g font-family="JetBrains Mono, monospace" font-size="11" fill="var(--ink-muted)" text-anchor="end">
      <text x="110" y="24">$5.0</text><text x="110" y="119">$1.8</text><text x="110" y="174">$0.0</text>
    </g>
    <g font-family="Inter, sans-serif" font-size="12" fill="var(--ink)" text-anchor="middle">
      <text x="225" y="192">Crisis peak</text><text x="405" y="192">Mid-summer</text><text x="585" y="192">Late August</text>
    </g>
    <g font-family="JetBrains Mono, monospace" font-size="11.5" fill="var(--ink-muted)" text-anchor="middle">
      <text x="225" y="210">arb wide open</text><text x="405" y="210">arb open</text><text x="585" y="210">arb shut</text>
    </g>
    <g font-family="JetBrains Mono, monospace" font-size="11.5" fill="var(--ink)" text-anchor="middle">
      <text x="225" y="14">~$5.0</text><text x="405" y="83">~$2.7</text><text x="585" y="152">~$0.4</text>
    </g>
  </svg>
  <p class="rm-cap">Indicative spread levels through 2026 against a USD 1.82
  threshold calculated at an USD 80,000/day charter rate. In the crisis weeks
  charter rates themselves spiked toward USD 300,000/day, which pushed the
  threshold up even as the spread widened — the two moved together, which is
  exactly why the arb is harder to capture than it looks.</p>
</div>

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>A cargo does not sail to whoever pays the most. It sails to whoever pays the
  most <i>after</i> you subtract the cost of getting there. Asia nearly always pays
  more than Europe — but Asia is also far further away, so unless Asia's extra
  payment beats the extra shipping bill, the ship turns towards Europe. Here that
  break-even is about USD 1.82 per unit of gas.</p>
</div>

## What 2026 did to the price signal

Three benchmarks, three completely different years.

<div class="rm-fig">
  <p class="rm-fig-t">Three benchmarks, three different years</p>
  <p class="rm-fig-s">USD per MMBtu at three points in 2026. TTF converted at €1 = USD 1.16 and 1 MWh = 3.412 MMBtu</p>
  <div class="rm-legend">
    <span><i style="background:var(--accent)"></i>JKM (Asia)</span>
    <span><i style="background:var(--amber)"></i>TTF (Europe)</span>
    <span><i style="background:var(--pos)"></i>Henry Hub (US)</span>
  </div>
  <svg viewBox="0 0 800 270" role="img" aria-label="Grouped bar chart of JKM, TTF and Henry Hub prices at three points in 2026">
    <g stroke="var(--border)" stroke-width="1">
      <line x1="70" y1="220" x2="785" y2="220"/>
      <line x1="70" y1="180" x2="785" y2="180" opacity=".55"/>
      <line x1="70" y1="140" x2="785" y2="140" opacity=".55"/>
      <line x1="70" y1="100" x2="785" y2="100" opacity=".55"/>
      <line x1="70" y1="60"  x2="785" y2="60"  opacity=".55"/>
      <line x1="70" y1="20"  x2="785" y2="20"  opacity=".55"/>
    </g>
    <g font-family="JetBrains Mono, monospace" font-size="11" fill="var(--ink-muted)" text-anchor="end">
      <text x="60" y="224">0</text><text x="60" y="184">5</text><text x="60" y="144">10</text>
      <text x="60" y="104">15</text><text x="60" y="64">20</text><text x="60" y="24">25</text>
    </g>
    <g>
      <rect x="120" y="128"   width="48" height="92"    fill="var(--accent)"/>
      <rect x="176" y="140.8" width="48" height="79.2"  fill="var(--amber)"/>
      <rect x="232" y="196"   width="48" height="24"    fill="var(--pos)"/>
      <rect x="360" y="80"    width="48" height="140"   fill="var(--accent)"/>
      <rect x="416" y="92"    width="48" height="128"   fill="var(--amber)"/>
      <rect x="472" y="194.4" width="48" height="25.6"  fill="var(--pos)"/>
      <rect x="600" y="39.2"  width="48" height="180.8" fill="var(--accent)"/>
      <rect x="656" y="40.8"  width="48" height="179.2" fill="var(--amber)"/>
      <rect x="712" y="196.8" width="48" height="23.2"  fill="var(--pos)"/>
    </g>
    <g font-family="JetBrains Mono, monospace" font-size="11" fill="var(--ink)" text-anchor="middle">
      <text x="144" y="122">11.5</text><text x="200" y="135">9.9</text><text x="256" y="190">3.0</text>
      <text x="384" y="74">17.5</text><text x="440" y="86">16.0</text><text x="496" y="188">3.2</text>
      <text x="624" y="33">22.6</text><text x="680" y="35">22.4</text><text x="736" y="191">2.9</text>
    </g>
    <g font-family="Inter, sans-serif" font-size="12.5" fill="var(--ink)" text-anchor="middle">
      <text x="200" y="244">January 2026</text><text x="440" y="244">Q2 2026 average</text><text x="680" y="244">Late August 2026</text>
    </g>
  </svg>
  <p class="rm-cap">Asia and Europe converged as both competed for the same
  shrinking pool of flexible cargoes. Henry Hub barely moved. That gap — roughly
  <b>USD 19 per MMBtu</b> between US wellhead and Asian delivered — is the
  entire economic case for the US export build-out. Sources: IEA Gas Market
  Report Q3-2026, EIA Short-Term Energy Outlook, market assessments.</p>
</div>

Note what did *not* happen. Henry Hub sat between USD 2.87 and USD 3.44 all
year, because the United States is a closed pipeline system with abundant
domestic supply and a liquefaction bottleneck. American gas is only loosely
connected to the world price, and stays that way until export capacity
outgrows the resource base. This is why a US producer hedging in Henry Hub is
not hedged against a global gas event at all.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>American gas stayed cheap all year while European and Asian gas roughly doubled.
  That is not an error. America has plenty of gas and only a limited number of
  plants that can chill it into liquid for export, so its price sits behind a
  fence. The height of that fence — about USD 19 — is precisely why so many export
  terminals are being built.</p>
</div>

## The physical picture behind the prices

Prices are the summary. Underneath them is a straightforward supply-and-demand
story, and 2026 was a year in which supply broke and demand rationed itself.

<div class="rm-tw" markdown="0">
<table>
<thead>
<tr><th>Basin</th><th>Market</th><th>2026 position</th></tr>
</thead>
<tbody>
<tr><td rowspan="4">Atlantic<br>supply</td><td>United States</td><td>17.4 Bcf/d of LNG exports forecast for 2026, rising to 18.6 Bcf/d in 2027. Corpus Christi Stage 3 and the first two Golden Pass trains ramping this year.</td></tr>
<tr><td>Trinidad, Nigeria, Algeria</td><td>Legacy suppliers, broadly flat, feedstock-constrained.</td></tr>
<tr><td>Norway</td><td>Pipeline plus Hammerfest LNG; Europe's most reliable non-LNG lever.</td></tr>
<tr><td>Russia (Yamal)</td><td>Still flowing to Europe and Asia under sanctions carve-outs; politically fragile.</td></tr>
<tr><td rowspan="3">Atlantic<br>demand</td><td>European Union</td><td>Gas demand down more than 2% on high prices and renewables growth — but storage only 63% full against a 79% five-year average, the lowest in fifteen years outside 2021.</td></tr>
<tr><td>Germany / Netherlands</td><td>51% and 44.3% storage respectively. The weakest points in the European system going into winter.</td></tr>
<tr><td>South America</td><td>Brazil and Argentina buy on hydrology; a dry year in Brazil competes directly with Europe.</td></tr>
<tr><td rowspan="2">The swing</td><td>Qatar and UAE</td><td>Combined LNG exports forecast down 45% year on year — some 54 bcm — following the Hormuz disruption and damage at Ras Laffan. Supplies both basins, so the loss is felt on both sides.</td></tr>
<tr><td>Global fleet</td><td>Roughly 700 vessels. Longer voyages absorb ships, tightening freight independently of cargo availability.</td></tr>
<tr><td rowspan="5">Pacific<br>demand</td><td>Asia Pacific total</td><td>257 Mt forecast for 2026, down 4.1% from 268 Mt and well below the 2024 peak of 278 Mt. A second consecutive annual decline.</td></tr>
<tr><td>China</td><td>62.4 Mt, down from 66.4 Mt. Regasification terminals running at 29% of nameplate. Holds the region's largest inventory buffer and the most diversified portfolio — which makes it the marginal buyer that can simply walk away.</td></tr>
<tr><td>Japan</td><td>More than 90% of 2026 demand covered by term contracts. Structurally the least exposed to spot.</td></tr>
<tr><td>South Korea</td><td>Spot exposure above 20%, with two 2 mtpa contracts tied to the damaged Ras Laffan Train 6. The most exposed of the large Asian buyers.</td></tr>
<tr><td>India</td><td>The largest South Asian exposure by volume, with potential curtailments of up to 1.5 Mt a month forcing industrial fuel-switching and fertiliser production cuts. India is the classic price-elastic buyer: above roughly USD 12–14 per MMBtu, demand destruction starts.</td></tr>
</tbody>
</table>
</div>

The pattern is worth naming. **Europe's demand is inelastic and its storage
obligation is legal; Asia's demand is elastic and its buyers can switch to
coal.** So when the market tightens, Asia rations by price and Europe pays.
That is why the JKM–TTF spread compressed toward parity in August despite Asia
being nominally short — Asian buyers stepped back, and Europe, needing to fill
storage before winter, kept bidding.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>Europe and Asia reacted to expensive gas in opposite ways. Asian buyers, who can
  switch fuels and sit on stock, simply bought less. Europe could not — its storage
  caverns have to be filled before winter, and that is a legal obligation, not a
  preference. When one buyer can walk away and the other cannot, the one who cannot
  ends up paying.</p>
</div>

## The ceiling nobody quotes

There is a limit on how far JKM can run, and it is not set by the gas market at
all. It is set by what an Asian buyer could burn instead.

Gas competes with oil products and coal on **energy content**, not on volume. To
compare them you convert everything to dollars per million British thermal units:
divide a crude price by roughly 5.8, a fuel oil price by about 6.3, and a coal
price by about 23.8 per tonne.

<div class="rm-tw" markdown="0">
<table>
<thead>
<tr><th>Fuel</th><th class="num">Price</th><th class="num">Energy content</th><th class="num">$/MMBtu</th><th>Against JKM at $22.61</th></tr>
</thead>
<tbody>
<tr><td>LNG, JKM</td><td class="num">$22.61</td><td class="num">—</td><td class="num">22.61</td><td>the reference</td></tr>
<tr><td>Gasoil / diesel</td><td class="num">$175/bbl</td><td class="num">5.83 MMBtu/bbl</td><td class="num">30.02</td><td>33% dearer — no switching</td></tr>
<tr><td>Brent crude</td><td class="num">$92/bbl</td><td class="num">5.8 MMBtu/bbl</td><td class="num">15.86</td><td>30% cheaper</td></tr>
<tr><td>High-sulphur fuel oil</td><td class="num">$75/bbl</td><td class="num">6.29 MMBtu/bbl</td><td class="num">11.92</td><td>47% cheaper</td></tr>
<tr><td>Thermal coal, API2</td><td class="num">$130/t</td><td class="num">23.8 MMBtu/t</td><td class="num">5.46</td><td>76% cheaper</td></tr>
</tbody>
</table>
</div>

Read the bottom three rows and the whole of Asian demand behaviour in 2026
becomes obvious. At USD 22.61, LNG costs nearly twice what fuel oil costs and
more than four times what coal costs for the same heat. Any buyer with a
dual-fired boiler, an idle coal unit or a flexible industrial process stopped
buying gas.

That is what the demand numbers are describing. Asia Pacific LNG demand fell
4.1%. Chinese regasification terminals ran at 29% of nameplate. Indian buyers
faced curtailments of up to 1.5 million tonnes a month and cut fertiliser
production. None of that is a forecast about the energy transition — it is
arithmetic, executed by plant managers with a calculator.

<div class="rm-call">
  <div class="t">Why this matters for the arbitrage</div>
  <p>The switching level is a soft ceiling on JKM. Push Asian gas far above the
  price of the fuel next door and the buyers simply leave, which is exactly what
  compressed the JKM–TTF spread toward parity in August even though Asia was
  nominally short. Europe has no equivalent escape route — it has coal-plant
  closures behind it and a legal storage-filling obligation in front of it — so
  <b>Europe becomes the price setter by default</b>.</p>
  <p>Note the one row that does not switch. Gasoil at USD 30 per MMBtu is dearer
  than LNG, so nobody moves from gas to diesel. Switching runs downward into the
  cheap, dirty end of the barrel, never upward.</p>
</div>

And there is a second-order effect that connects this article to the next one.
Every tonne of gas demand that switches into fuel oil or coal becomes *additional*
demand for those fuels. In a year when refining capacity was already scarce, that
switched demand landed on top of an overloaded product market — one of the
underappreciated reasons Atlantic Basin refining margins reached all-time highs.
See [Crack Spreads Across the Barrel](/insights/product-crack-spreads/) for what
happened at the other end of that chain.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>Gas has an invisible ceiling. If it becomes dearer than the oil or coal a
  factory could burn instead, the factory switches and stops buying gas. Asian gas
  currently costs about four times what coal costs for the same heat — so the
  buyers left. That, not sentiment, is why Asia stopped competing for cargoes.</p>
</div>

## What closes the arbitrage

Five things, in roughly the order a desk worries about them.

<div class="rm-cards">
  <div>
    <h4>Freight</h4>
    <p>The fastest-moving input. Atlantic spot charter rates opened 2026 near
    USD 26,250 a day and spiked toward USD 300,000 a day during the Hormuz
    scare — a 600% move in a week. Every dollar on the charter rate raises the
    threshold the spread must clear.</p>
  </div>
  <div>
    <h4>Route availability</h4>
    <p>Suez plus Hormuz is the short way east. With Hormuz disrupted, cargoes
    go via the Cape, adding roughly three weeks round trip. The Panama Canal is
    an alternative for US Gulf cargoes but LNG carriers compete for slots with
    container ships and lose on willingness to pay.</p>
  </div>
  <div>
    <h4>Boil-off</h4>
    <p>An LNG carrier loses roughly 0.10% of cargo a day to evaporation. On an
    eleven-day run that is a rounding error. On thirty-three days it is 3.3% of
    the cargo — and at USD 22 per MMBtu, 3.3% is a real number.</p>
  </div>
  <div>
    <h4>Destination flexibility</h4>
    <p>Only cargoes with free destination rights can be diverted at all. Most
    Qatari long-term contracts historically carried destination restrictions;
    most US contracts do not. The US export model exists precisely to sell
    flexibility.</p>
  </div>
  <div>
    <h4>Regasification access</h4>
    <p>A netback assumes you can discharge. Terminal slots, send-out capacity
    and pipeline entry charges differ by country, and in a tight winter the
    binding constraint can be a berth rather than a price.</p>
  </div>
  <div>
    <h4>The cancellation option</h4>
    <p>A US offtaker paying a fixed tolling fee can decline to lift. When
    delivered prices fall below feed gas plus shipping, cancelling is rational —
    the tolling fee is sunk either way. This puts a soft floor under
    global prices at roughly the US variable cost of export.</p>
  </div>
</div>

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>Six things can kill this trade, and five have nothing to do with the gas price:
  what the ship costs, how far it must sail, how much cargo evaporates on the way,
  whether the contract even permits changing destination, and whether there is a
  free berth at the far end.</p>
</div>

## How this is traded and hedged

The spread itself is tradeable. JKM and TTF both have listed futures, so a
desk can take a view on the basin differential without owning a molecule — long
JKM, short TTF, in matched volumes. That is a pure spread position and it is
how most financial participants express a basin view.

A physical trader's problem is harder, because the position has three legs that
do not settle together: a gas price, a freight rate, and time. A cargo loaded
today and delivered to Asia in five weeks is exposed to whatever JKM does over
those five weeks, whatever the charter market does if the voyage extends, and
whatever the currency does if the sale is priced in a different unit. Hedging
the price leg while leaving freight unhedged is a common and expensive mistake —
in 2026 the freight leg moved further in percentage terms than the commodity.

<div class="rm-call">
  <div class="t">Three things worth remembering</div>
  <p><b>One.</b> The arbitrage is a spread net of delivery cost, not a price
  comparison. Asia is nearly always dearer; that alone tells you nothing.</p>
  <p><b>Two.</b> The threshold and the spread move together in a crisis. Freight
  spikes when cargoes are being diverted, which is precisely when the spread
  widens — so the visible opportunity is usually smaller than the headline
  spread implies.</p>
  <p><b>Three.</b> Henry Hub is not a global price. A US producer hedged in
  Henry Hub carries the entire international basis unhedged.</p>
</div>

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>If you sell gas in America and protect yourself using the American gas price,
  you were not protected at all this year — that price barely moved while
  everything else doubled. Insure against the thing you actually sell, not the
  thing that is easiest to insure.</p>
</div>

## Looking into 2027

The IEA expects markets to stay tighter than previously assumed for the next
two years, with cumulative supply losses of around 140 bcm over 2026–2030. But
the new-build wave is still coming: Port Arthur Phase 1 and Rio Grande Trains 1
and 2 add roughly 3 Bcf/d of US capacity in 2027, and Wood Mackenzie expects
Asian demand to recover to 279 Mt in 2027 and 297 Mt by 2028.

That sets up the interesting question. If Gulf supply returns on schedule *and*
the 2027 capacity lands *and* Asian demand only recovers to its 2024 level, the
market flips from scarcity to surplus quickly. In a surplus, the JKM–TTF spread
narrows toward the freight differential and stays there, because the marginal
cargo is always indifferent between basins. The wide, volatile spread of 2026 is
a feature of a broken market, not a normal one.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>The wild price gaps between Europe and Asia in 2026 are a symptom of a broken
  market, not a normal one. When the missing supply returns and the new export
  plants start up, those gaps should shrink back to roughly the cost of the extra
  shipping and stay there. The volatility is the anomaly, not the baseline.</p>
</div>

**Sources and further reading**

- [Gas Market Report, Q3-2026](https://www.iea.org/reports/gas-market-report-q3-2026/executive-summary) — International Energy Agency
- [U.S. natural gas exports to grow nearly 30% by 2027](https://www.eia.gov/todayinenergy/detail.php?id=67484) — U.S. Energy Information Administration
- [Short-Term Energy Outlook, August 2026](https://www.eia.gov/outlooks/steo/) — U.S. Energy Information Administration
- [Asian LNG demand to decline for a second consecutive year](https://www.woodmac.com/press-releases/asian-lng-demand-decline-for-second-consecutive-year/) — Wood Mackenzie
- [The EU will need higher LNG imports to refill gas storage ahead of winter](https://www.acer.europa.eu/news/eu-will-need-higher-lng-imports-refill-gas-storage-ahead-winter) — ACER
