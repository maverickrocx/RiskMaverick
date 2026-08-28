---
title: "The Intermittency Problem: Why Adding Renewables Is the Easy Part"
date: 2026-08-26 11:00:00 +0530
kind: analysis
markets: [power-renewables]
concepts: [market-risk, operational]
excerpt: "Solar and wind produce when the weather says so, not when demand says so. What that costs, at four different timescales, and what batteries and pumped hydro can and cannot fix."
sources:
  - { title: "Electricity 2026 — Flexibility", publisher: "International Energy Agency", url: "https://www.iea.org/reports/electricity-2026/flexibility" }
  - { title: "Solar and wind power curtailments are increasing in California", publisher: "U.S. Energy Information Administration", url: "https://www.eia.gov/todayinenergy/detail.php?id=65364" }
  - { title: "Europe's record solar output drives surge in negative electricity prices", publisher: "pv magazine", url: "https://www.pv-magazine.com/2026/07/15/europes-record-solar-output-drives-surge-in-negative-electricity-prices/" }
  - { title: "EnergyWatts — monthly update on India's energy storage market, July 2026", publisher: "Institute for Energy Economics and Financial Analysis", url: "https://ieefa.org/sites/default/files/2026-08/ESSjmk-0626.pdf" }
  - { title: "Batteries and Secure Energy Transitions", publisher: "International Energy Agency", url: "https://iea.blob.core.windows.net/assets/cb39c1bf-d2b3-446d-8c35-aae6b1f3a4a0/BatteriesandSecureEnergyTransitions.pdf" }
---

Electricity is the only major commodity that must be produced at the exact
instant it is consumed. There is no warehouse. Supply and demand have to match
continuously, every second, or the frequency drifts and equipment starts
tripping offline.

For a century that was manageable, because generation was dispatchable — you
told a coal or gas plant what to produce and it produced it. Solar and wind
are not dispatchable. They produce what the weather allows. Building them is
now cheap and fast; the difficulty has moved entirely to the question of what
the rest of the system does around them.

That question is what "intermittency" means, and it is worth being precise: it
is not one problem. It is four problems with different timescales, different
costs and different solutions.

<div class="rm-kf">
  <div><div class="k">Negative price hours</div><div class="v">596</div><div class="n">Spain, first half of 2026</div></div>
  <div><div class="k">European Q2 solar output</div><div class="v">129 TWh</div><div class="n">~20% above any prior Q2</div></div>
  <div><div class="k">Global battery capacity</div><div class="v">124 GW</div><div class="n">utility-scale, after a record year</div></div>
  <div><div class="k">Demand response used</div><div class="v">~100 GW</div><div class="n">globally — a fraction of the potential</div></div>
</div>

## Four problems, not one

<div class="rm-tw" markdown="0">
<table>
<thead>
<tr><th>Timescale</th><th>The problem</th><th>What it looks like</th><th>What solves it</th></tr>
</thead>
<tbody>
<tr><td>Seconds</td><td>Inertia and frequency</td><td>Spinning turbines physically resist frequency change. Inverter-connected solar and wind do not, so the grid becomes twitchier as thermal plant retires</td><td>Synthetic inertia from inverters, synchronous condensers, fast frequency response from batteries</td></tr>
<tr><td>Minutes to hours</td><td>Ramping</td><td>Solar falls away over the evening while demand climbs. The rest of the fleet has to make up the gap at a rate it was never designed for</td><td>Batteries, flexible gas, demand response, interconnection</td></tr>
<tr><td>Days</td><td>Surplus and shortfall</td><td>A sunny, windy, mild weekend produces more than anyone needs. A still, overcast week produces almost nothing</td><td>Longer-duration storage, pumped hydro, cross-border trade, curtailment</td></tr>
<tr><td>Seasons</td><td>Adequacy</td><td>Northern winters have peak demand and minimum solar at the same time. No amount of four-hour storage bridges December</td><td>Firm dispatchable capacity, hydro reservoirs, hydrogen or long-duration chemistries, capacity markets</td></tr>
</tbody>
</table>
</div>

Conflating these is the most common mistake in the debate. A battery that
solves the evening ramp brilliantly contributes almost nothing to winter
adequacy. A capacity market that solves adequacy does nothing for frequency.
Each timescale needs its own instrument.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>Electricity is the one thing you cannot keep in a warehouse — it has to be made
  at the exact second it is used. That was manageable while we could tell power
  stations what to produce. Solar and wind do not take instructions; they produce
  when the weather allows. The problem is not that they are unreliable. It is that
  they are unschedulable, and those are different things.</p>
</div>

## The duck, and what it became

The single most useful picture in power systems is the **net load curve** —
total demand minus whatever wind and solar happen to produce. It is what the
dispatchable fleet actually has to serve.

<div class="rm-fig">
  <p class="rm-fig-t">Total demand versus net load, on a spring day</p>
  <p class="rm-fig-s">Illustrative shape for a solar-heavy system. The gap between the lines is renewable output</p>
  <div class="rm-legend">
    <span><i style="background:var(--ink-muted)"></i>Total demand</span>
    <span><i style="background:var(--accent)"></i>Net load (what thermal plant must serve)</span>
    <span><i style="background:var(--amber);opacity:.35"></i>Solar and wind output</span>
  </div>
  <svg viewBox="0 0 800 340" role="img" aria-label="Duck curve chart showing total demand and net load across a day with a steep evening ramp">
    <g stroke="var(--border)" stroke-width="1" opacity=".55">
      <line x1="70" y1="260" x2="785" y2="260"/>
      <line x1="70" y1="194" x2="785" y2="194"/>
      <line x1="70" y1="128" x2="785" y2="128"/>
      <line x1="70" y1="62"  x2="785" y2="62"/>
    </g>
    <path d="M70,108.9 L158.75,128.6 L247.5,128.6 L306.7,154.9 L365.8,187.7 L425,207.4 L454.6,210.7 L484.2,207.4 L543.3,177.6 L602.5,102.3 L632.1,69.4 L661.7,62.9 L691.25,76 L780,102.3
             L780,102.3 L691.25,69.4 L632.1,49.7 L602.5,56.3 L513.75,76 L425,82.6 L336.25,95.7 L247.5,122 L158.75,128.6 L70,108.9 Z"
          fill="var(--amber)" opacity=".22"/>
    <path d="M70,108.9 L158.75,128.6 L247.5,122 L336.25,95.7 L425,82.6 L513.75,76 L602.5,56.3 L632.1,49.7 L691.25,69.4 L780,102.3"
          fill="none" stroke="var(--ink-muted)" stroke-width="2"/>
    <path d="M70,108.9 L158.75,128.6 L247.5,128.6 L306.7,154.9 L365.8,187.7 L425,207.4 L454.6,210.7 L484.2,207.4 L543.3,177.6 L602.5,102.3 L632.1,69.4 L661.7,62.9 L691.25,76 L780,102.3"
          fill="none" stroke="var(--accent)" stroke-width="2.5"/>
    <g stroke="var(--neg)" stroke-width="1.3" stroke-dasharray="5 4" fill="none" opacity=".85">
      <line x1="484.2" y1="210.7" x2="484.2" y2="55"/>
      <line x1="661.7" y1="62.9"  x2="661.7" y2="55"/>
      <line x1="484.2" y1="55"    x2="661.7" y2="55"/>
    </g>
    <circle cx="484.2" cy="210.7" r="3.5" fill="var(--neg)"/>
    <circle cx="661.7" cy="62.9"  r="3.5" fill="var(--neg)"/>
    <text x="573" y="44" font-family="Inter, sans-serif" font-size="12.5" fill="var(--neg)" text-anchor="middle">the evening ramp — about 22 GW in six hours</text>
    <text x="425" y="232" font-family="Inter, sans-serif" font-size="12" fill="var(--accent-text)" text-anchor="middle">midday belly</text>
    <g font-family="JetBrains Mono, monospace" font-size="11" fill="var(--ink-muted)" text-anchor="end">
      <text x="60" y="264">0</text><text x="60" y="198">10</text><text x="60" y="132">20</text><text x="60" y="66">30</text>
    </g>
    <g font-family="JetBrains Mono, monospace" font-size="11" fill="var(--ink-muted)" text-anchor="middle">
      <text x="70" y="282">00:00</text><text x="247.5" y="282">06:00</text><text x="425" y="282">12:00</text>
      <text x="602.5" y="282">18:00</text><text x="780" y="282">24:00</text>
    </g>
    <text x="30" y="160" font-family="Inter, sans-serif" font-size="11.5" fill="var(--ink-muted)" text-anchor="middle" transform="rotate(-90 30 160)">gigawatts</text>
  </svg>
  <p class="rm-cap">Shape is illustrative, not a specific system's data. The
  belly deepens every year that solar is added; the ramp steepens with it. In
  California, solar now supplies close to half of demand between 08:00 and
  16:00.</p>
</div>

Two things happen as the belly deepens.

Midday power becomes worthless, and then worse than worthless. If more is being
produced than consumed and nothing can absorb it, someone must be paid to take
it — which is what a negative price is. Generators with subsidies tied to output
will keep running through negative prices rather than lose the subsidy, which
pushes the price lower still.

And the evening ramp gets brutal. The fleet that has to close that gap runs for
a few hours a day at increasing cost per hour, because a plant that starts and
stops daily is expensive to run and expensive to maintain.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>Draw a day of electricity demand, then subtract whatever the sun and wind
  happened to provide. What is left is the shape everything else has to fill. As
  more solar is added, the middle of the day sags towards zero and the evening turns
  into a cliff. Around lunchtime nobody needs your power; by seven in the evening
  everybody does, all at once.</p>
</div>

## What it looked like in 2026

Europe gave a clean demonstration. Second-quarter solar output hit **129 TWh**,
about 20% above any previous second quarter. The consequences were immediate:

- **Spain recorded 596 hours of negative prices in the first half of 2026** —
  the most in Europe. Portugal had 462. France had 370.
- By late April, exchanges had to lower the minimum price floor from −€500 to
  **−€600 per MWh**, because the existing floor was being hit.
- In the same month as those negative prices, German afternoon prices exceeded
  **€600 per MWh** on days when the sun went down and demand did not.

<div class="rm-fig">
  <p class="rm-fig-t">Hours of negative day-ahead prices, first half of 2026</p>
  <svg viewBox="0 0 800 175" role="img" aria-label="Bar chart of negative electricity price hours in Spain, Portugal and France in the first half of 2026">
    <g font-family="Inter, sans-serif" font-size="13.5" fill="var(--ink)" text-anchor="end">
      <text x="140" y="38">Spain</text><text x="140" y="78">Portugal</text><text x="140" y="118">France</text>
    </g>
    <g>
      <rect x="150" y="20" width="596" height="26" fill="var(--accent)"/>
      <rect x="150" y="60" width="462" height="26" fill="var(--accent)" opacity=".72"/>
      <rect x="150" y="100" width="370" height="26" fill="var(--accent)" opacity=".55"/>
    </g>
    <g font-family="JetBrains Mono, monospace" font-size="12.5" fill="var(--ink)">
      <text x="756" y="38">596</text><text x="622" y="78">462</text><text x="530" y="118">370</text>
    </g>
    <line x1="150" y1="14" x2="150" y2="132" stroke="var(--border)" stroke-width="1"/>
    <g stroke="var(--border)" stroke-width="1" opacity=".45">
      <line x1="350" y1="14" x2="350" y2="132"/><line x1="550" y1="14" x2="550" y2="132"/><line x1="750" y1="14" x2="750" y2="132"/>
    </g>
    <g font-family="JetBrains Mono, monospace" font-size="11" fill="var(--ink-muted)" text-anchor="middle">
      <text x="150" y="150">0</text><text x="350" y="150">200</text><text x="550" y="150">400</text><text x="750" y="150">600</text>
    </g>
    <text x="450" y="168" font-family="Inter, sans-serif" font-size="11" fill="var(--ink-muted)" text-anchor="middle">Roughly one hour in seven was priced below zero in Spain</text>
  </svg>
  <p class="rm-cap">The Iberian peninsula has abundant solar and comparatively
  thin interconnection to the rest of Europe. Denmark and South Australia hit
  negative net load more often than Germany or Brazil for the same structural
  reason — small, high-renewable systems with limited ability to export.</p>
</div>

California shows the other consequence: **curtailment**. In 2024, CAISO curtailed
3.4 million MWh — 29% more than the previous year — and 93% of it was solar.
That is clean electricity that was generated and thrown away, and it happens
mostly in spring, when output is high and cooling and heating demand are both
low.

<div class="rm-call">
  <div class="t">The economics people miss</div>
  <p>Curtailment and negative prices are not signs of failure. They are signs of
  a system with more zero-marginal-cost supply than it can currently use — which
  is the intended destination. The problem is that they wreck the business case
  for the next solar farm, because the hours it generates are exactly the hours
  nobody wants power. This is <b>value deflation</b> or <b>capture rate decline</b>,
  and it is what limits renewable build long before engineering does.</p>
</div>

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>When there is more electricity than anyone wants, the price goes below zero —
  you have to pay somebody to take it. Spain had 596 such hours in six months. On
  some of those same days, once the sun set, German prices went above €600. That is
  not a broken market. It is a market saying very loudly that the valuable thing is
  no longer electricity — it is electricity <i>at the right moment</i>.</p>
</div>

## What the ramp actually costs

The evening ramp has to be served by something, and in most European systems that
something is a gas turbine. Whether it runs is decided by the **clean spark
spread** — the power price, less the cost of the gas burned, less the cost of the
carbon emitted.

`Clean spark = Power price − (Gas price × heat rate) − (Carbon price × emissions intensity)`

For a modern combined-cycle plant at 55% efficiency, the heat rate is 1.82
megawatt-hours of gas per megawatt-hour of electricity and the emissions intensity
is about 0.367 tonnes of CO₂ per megawatt-hour. At August 2026 levels — TTF at
€66/MWh and EU allowances at €75 a tonne — the plant needs:

<div class="rm-calc">
  <div><span class="lbl">Gas: €66/MWh × 1.82</span><span>€120.1</span></div>
  <div><span class="lbl">Carbon: 0.367 t/MWh × €75</span><span>€27.5</span></div>
  <div class="rule"><span class="lbl">Break-even power price</span><span>€147.6 /MWh</span></div>
</div>

<div class="rm-tw" markdown="0">
<table>
<thead>
<tr><th>Power price</th><th class="num">Clean spark spread</th><th>What the plant does</th></tr>
</thead>
<tbody>
<tr><td>Negative, midday surplus</td><td class="num neg">−€150 and worse</td><td>Off. Batteries and exports absorb the surplus</td></tr>
<tr><td>€90/MWh, ordinary baseload</td><td class="num neg">−€57.6</td><td>Off. Running would lose money on fuel alone</td></tr>
<tr><td>€147.6/MWh</td><td class="num">€0</td><td>At the margin — the switch-on price</td></tr>
<tr><td>€600/MWh, German June evening</td><td class="num pos">+€452.4</td><td>Runs, and earns a large share of its annual margin in a few hours</td></tr>
</tbody>
</table>
</div>

That table is the whole economics of a modern peaking plant. It is switched off for
the overwhelming majority of the year and makes its money in a few dozen evenings.
It is not really a power station any more — it is **a strip of call options on the
evening ramp**, and it should be valued and hedged that way rather than as a
baseload asset.

<div class="rm-call">
  <div class="t">Why the battery wins these hours</div>
  <p>A battery competes for exactly the same scarcity, without a fuel bill. Charge
  at −€10/MWh in the midday surplus, discharge into the €600 evening at 85%
  round-trip efficiency, and the economics are:</p>
  <p><code>600 − (−10 ÷ 0.85) = €611.8 per MWh discharged</code> — against the gas
  plant's €452.4, on the same evening, with no gas and no carbon to buy.</p>
  <p>This is why battery build has outrun every forecast. It is also why the
  business is self-limiting: every battery added flattens the very spread it lives
  on. A fleet large enough to fill the ramp is a fleet that has competed away its
  own revenue — which is why systems that want a lot of storage end up paying for
  availability through capacity mechanisms rather than relying on arbitrage.</p>
</div>

Two things follow for anyone modelling this. First, the carbon price sits inside
the switch-on price, so a change in EU allowance policy moves the dispatch order
without a single physical change — the arithmetic is set out in
[Two Carbon Markets](/insights/voluntary-vs-compliance-carbon-markets/). Second,
the gas price in that calculation is set half a world away by the LNG market
described in
[The Atlantic–Pacific LNG Arbitrage](/insights/lng-atlantic-pacific-arbitrage/).
A European battery's revenue in December depends on a shipping lane in the Gulf.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>The gas plant that covers the evening is not really a power station any more.
  It is an insurance policy that sits switched off almost all the time and earns its
  entire year in a handful of expensive evenings. That is a hard thing to finance —
  and it is exactly the money a battery is now competing for, without burning
  anything at all.</p>
</div>

## The mitigation toolkit

There are six ways to deal with a mismatch between when power is produced and
when it is wanted. Storage is only one.

<div class="rm-cards">
  <div>
    <h4>1 · Move it in time</h4>
    <p>Storage. Charge in the belly, discharge on the ramp. Batteries for hours,
    pumped hydro for days, other chemistries for longer.</p>
  </div>
  <div>
    <h4>2 · Move it in space</h4>
    <p>Interconnection. The wind is always blowing somewhere. Transmission is
    often the cheapest flexibility available — and always the slowest to permit.</p>
  </div>
  <div>
    <h4>3 · Move the demand</h4>
    <p>Demand response. Only about 100 GW is actively used globally, against 600
    GW of residential air conditioning and 160 GW of aluminium smelting that
    could in principle respond.</p>
  </div>
  <div>
    <h4>4 · Keep firm capacity</h4>
    <p>Flexible gas, hydro reservoirs, nuclear. Expensive to hold for a few
    hundred hours a year, which is why capacity markets exist to pay for
    availability rather than energy.</p>
  </div>
  <div>
    <h4>5 · Throw it away</h4>
    <p>Curtailment. Genuinely the right answer sometimes — storing every surplus
    megawatt-hour costs more than losing the few percent that arrive at the worst
    possible moment.</p>
  </div>
  <div>
    <h4>6 · Change the product</h4>
    <p>Convert surplus power into hydrogen, heat or desalinated water — anything
    storable. Round-trip efficiency is poor, so this only works when the input
    power is nearly free.</p>
  </div>
</div>

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>There are only six ways to fix a mismatch between when power is made and when it
  is wanted: move it in time (storage), move it in space (cables), move the demand,
  keep some old-fashioned plant on standby, throw the surplus away, or convert it
  into something storable. Storage gets all the attention, but the cheapest answer
  is very often just a bigger cable.</p>
</div>

## What batteries actually do

Grid-scale lithium-ion has scaled faster than almost anyone forecast. A record
63 GW was added globally in 2024, taking installed utility-scale capacity to
124 GW, while costs fell about 40% in a single year to roughly USD 150 per kWh.
China alone added 42 GW in 2024 and had 145 GW cumulative by the end of 2025.

Penetration is already meaningful in the systems that needed it most: batteries
equate to nearly 25% of peak load in California and around 15% in South
Australia and Great Britain.

What they are good at is precise and limited:

- **Sub-second response.** Nothing else on a grid responds faster, which makes
  batteries the natural provider of frequency regulation.
- **The daily arbitrage.** Buy in the belly, sell on the ramp. This is the core
  revenue stream and it depends entirely on the spread between the two.
- **Deferring network investment.** A battery at a constrained substation can
  postpone a transmission upgrade for years.

What they are not good at is duration. A four-hour battery is a four-hour
battery. It shifts energy within a day; it does nothing for a week of low wind
and nothing at all for a season. Durations are lengthening — Australia's average
is expected to rise from 1.5 hours in 2024 to 2.5 hours by 2027, and California
concentrates on four-hour systems because its resource-adequacy rules pay for
them — but the technology is fundamentally a diurnal tool.

There is also a self-limiting quality to battery economics that is not widely
appreciated. Batteries earn on the intraday spread. Adding batteries flattens
the intraday spread. **A battery fleet large enough to solve the duck curve is a
battery fleet that has destroyed its own arbitrage revenue** — which is why
markets that want a lot of storage end up paying for capacity or availability
rather than relying on energy arbitrage alone.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>A battery is superb at one job — buying cheap power at lunchtime and selling it
  dearly at dinner time — and useless at another: getting a country through a still,
  cloudy week in January. A four-hour battery is a four-hour battery. There is also
  a catch: every battery you add narrows the very gap it feeds on, so a fleet big
  enough to fix the problem has competed away its own income.</p>
</div>

## Pumped hydro and the longer end

Pumped storage hydro is old technology and still by far the largest store of
electricity on earth — roughly 9,000 GWh of global capacity against about 120 GW
of batteries. Water is pumped uphill when power is cheap and released through
turbines when it is dear.

<div class="rm-tw" markdown="0">
<table>
<thead>
<tr><th>Technology</th><th>Typical duration</th><th>Round-trip efficiency</th><th>Asset life</th><th>Best used for</th></tr>
</thead>
<tbody>
<tr><td>Lithium-ion battery</td><td>2–8 hours</td><td>80–95%</td><td>15–20 years</td><td>Frequency response, daily arbitrage, network deferral</td></tr>
<tr><td>Pumped hydro</td><td>12–30 hours</td><td>70–82%</td><td>60–100+ years</td><td>Multi-day shifting, inertia, bulk capacity</td></tr>
<tr><td>Compressed air</td><td>12–24 hours</td><td>42–75%</td><td>40–60 years</td><td>Bulk storage where geology allows</td></tr>
<tr><td>Flow batteries</td><td>4–12 hours</td><td>65–80%</td><td>20–25 years</td><td>Longer daily cycles without degradation</td></tr>
<tr><td>Iron-air and similar</td><td>100+ hours</td><td>40–55%</td><td>Emerging</td><td>Multi-day outage cover, where efficiency matters less than cost</td></tr>
<tr><td>Hydrogen</td><td>Seasonal</td><td>25–40%</td><td>25–40 years (cavern 80+)</td><td>Seasonal balancing — only viable with near-free surplus power</td></tr>
</tbody>
</table>
</div>

<p class="rm-cap">Indicative industry ranges. Efficiency and duration trade off
against each other almost perfectly: the longer you want to store energy, the
more of it you accept losing.</p>

Pumped hydro's advantages are duration, an asset life measured in generations,
and real spinning inertia. Its disadvantages are that it needs specific
topography, takes the better part of a decade to build, and attracts every
planning objection available. Which is exactly why it is chronically
under-built relative to what systems need.

Policy is starting to reach past the four-hour battery. Italy's MACSE auction is
contracting 10 GWh of storage by 2028, including 1.3 GWh with durations of eight
hours or more. Great Britain's long-duration scheme targets 2.7–7.7 GWh by 2035.
These are small numbers deliberately aimed at a gap the market will not fill on
its own.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>Pumping water uphill when power is cheap and letting it run back down through
  turbines when power is dear is a hundred-year-old idea, and it is still by far the
  largest store of electricity on the planet — roughly seventy times everything held
  in the world's grid batteries. It lasts for generations. It also needs a mountain,
  a decade, and a very patient planning department.</p>
</div>

## India: a very large pipeline and a very small fleet

India is the clearest live case study, and the numbers are striking.

<div class="rm-fig">
  <p class="rm-fig-t">India's storage pipeline versus what is actually running</p>
  <p class="rm-fig-s">Gigawatts, as at mid-2026</p>
  <svg viewBox="0 0 800 200" role="img" aria-label="Bar chart comparing India's tendered, awarded and commissioned energy storage capacity">
    <g font-family="Inter, sans-serif" font-size="13" fill="var(--ink)" text-anchor="end">
      <text x="190" y="38">Tendered</text><text x="190" y="82">Awarded</text><text x="190" y="126">Commissioned</text>
    </g>
    <g>
      <rect x="200" y="20" width="526" height="28" fill="var(--ink-muted)" opacity=".4"/>
      <rect x="200" y="64" width="254.5" height="28" fill="var(--amber)" opacity=".75"/>
      <rect x="200" y="108" width="52.4" height="28" fill="var(--accent)"/>
    </g>
    <g font-family="JetBrains Mono, monospace" font-size="12.5" fill="var(--ink)">
      <text x="736" y="39">103.4</text><text x="465" y="83">~50</text><text x="263" y="127">10.3</text>
    </g>
    <line x1="200" y1="14" x2="200" y2="142" stroke="var(--border)" stroke-width="1"/>
    <g font-family="JetBrains Mono, monospace" font-size="11" fill="var(--ink-muted)" text-anchor="middle">
      <text x="200" y="160">0</text><text x="404" y="160">40</text><text x="608" y="160">80</text><text x="760" y="160">110</text>
    </g>
    <text x="480" y="184" font-family="Inter, sans-serif" font-size="11.5" fill="var(--ink-muted)" text-anchor="middle">Commissioned capacity is under 10% of what has been tendered</text>
  </svg>
  <p class="rm-cap">Of the 10.3 GW running, 7.4 GW is pumped hydro (36 GWh) and
  2.9 GW is batteries (8.3 GWh). Source: IEEFA, July 2026.</p>
</div>

The economics have moved fast. Standalone battery projects supported by
viability gap funding cleared at **INR 2.10–2.12 lakh per MW per month** in June
2026 — roughly USD 2,200 per MW per month. Renewable-plus-storage packages have
been contracted at **INR 5.51 per kWh** on 25-year terms. Viability gap funding
runs up to INR 18 lakh per MWh for standalone projects.

The Central Electricity Authority's target for FY2030 is **60.63 GW** of
storage: 41.65 GW of batteries and 18.98 GW of pumped hydro. Getting from 10.3
GW to 60 GW in four years requires the commissioning rate, not the tendering
rate, to change — and the constraints are land, grid connection and offtaker
credit rather than technology or cost. The 16.4 GW Madhya Pradesh pumped-hydro
tender is already delayed on land and site identification.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>India has ordered a great deal of storage and built very little of it — about a
  tenth of what has been tendered. The prices are now workable and the targets are
  clear. What is missing is not money or technology: it is land, grid connections,
  and buyers whose credit a lender will accept.</p>
</div>

## What a risk manager should take from this

Four points that matter if you are pricing, hedging or lending against these
assets.

**Shape risk is now the dominant risk in a power book.** A renewable generator
sells at the average price of the hours it happens to generate, which is
systematically below the period average and falling. Hedging with a flat
baseload swap leaves that gap entirely open — and it is widening every year.

**Volatility is the product, not the noise.** Spain's 596 negative hours and
Germany's €600 afternoons are the same phenomenon. Flexible assets earn from the
spread between them, so an intermittency-heavy system makes flexibility more
valuable, not less. Markets are already responding by shifting activity from
day-ahead auctions toward intraday and balancing.

**Correlation breaks the diversification assumption.** Solar assets across one
country are almost perfectly correlated at noon. A portfolio of ten solar farms
in the same market is a concentrated position, not a diversified one. Real
diversification requires different technologies, different weather regimes, or
different timezones.

**Storage revenue is a policy variable.** Battery cash flow comes from energy
arbitrage, ancillary services and capacity payments in a mix set by market
design. Change the resource-adequacy rules, the ancillary product definitions
or the viability-gap terms, and the asset reprices without a single physical
thing changing. Model the regulation as carefully as the price.

The engineering question — can a grid run on mostly variable renewables? — is
largely settled: yes, with enough flexibility. The open questions are who pays
for that flexibility, through which market design, and on what timetable. Those
are commercial and political questions, and they are where the risk now lives.

<div class="rm-pe">
  <div class="t">In plain English</div>
  <p>The engineering argument is settled — a grid can run mostly on wind and solar if
  you buy enough flexibility to go alongside it. What is not settled is who pays for
  that flexibility, and through which market. If you own or lend against these
  assets, remember that the revenue comes from rules as much as from physics, and
  rules can be rewritten without a single wire being moved.</p>
</div>

**Sources and further reading**

- [Electricity 2026 — Flexibility](https://www.iea.org/reports/electricity-2026/flexibility) — International Energy Agency
- [Solar and wind power curtailments are increasing in California](https://www.eia.gov/todayinenergy/detail.php?id=65364) — U.S. Energy Information Administration
- [Europe's record solar output drives surge in negative electricity prices](https://www.pv-magazine.com/2026/07/15/europes-record-solar-output-drives-surge-in-negative-electricity-prices/) — pv magazine
- [EnergyWatts — India's energy storage market, July 2026](https://ieefa.org/sites/default/files/2026-08/ESSjmk-0626.pdf) — IEEFA
- [Batteries and Secure Energy Transitions](https://iea.blob.core.windows.net/assets/cb39c1bf-d2b3-446d-8c35-aae6b1f3a4a0/BatteriesandSecureEnergyTransitions.pdf) — International Energy Agency
