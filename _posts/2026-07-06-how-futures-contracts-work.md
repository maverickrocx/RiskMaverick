---
title: "How Futures Contracts Work"
kind: basics
markets: []
concepts: [hedging-derivatives]
excerpt: "Futures explained — the contract, long vs short, margin, mark-to-market, and how they turn into a hedge."
sources:
  - { title: "Margin: Know What's Needed (Introduction to Futures)", publisher: "CME Group", url: "https://www.cmegroup.com/education/courses/introduction-to-futures/margin-know-what-is-needed" }
  - { title: "The Benefits of Futures Margins", publisher: "CME Group", url: "https://www.cmegroup.com/education/courses/understanding-the-benefits-of-futures/the-benefits-of-futures-margins" }
  - { title: "Hedging with E-mini S&P 500 Futures", publisher: "CME Group", url: "https://www.cmegroup.com/education/whitepapers/hedging-with-e-mini-sp-500-future" }
---

A **futures contract** is an agreement to buy or sell a defined quantity of an
underlying — a barrel of oil, a bushel of corn, an equity index — at a set price
on a future date. Standardised and exchange-traded, futures are the workhorse of
commodity and financial risk transfer.

## Long, short and mark-to-market

Every contract has two sides. The **long** agrees to buy and profits if the price
rises; the **short** agrees to sell and profits if it falls. Positions are
**marked to market daily**: gains and losses are settled every day through the
clearing house, so profit or loss accrues continuously rather than only at expiry.

## Margin — leverage and its cost

You don't pay the full contract value. Instead you post **initial margin** (often
only ~3–12% of notional) as a good-faith deposit, and must keep your balance above
a **maintenance margin** level. If losses erode it, you get a **margin call** for
more cash. This leverage makes futures capital-efficient — but it is also why
liquidity risk and margin funding matter so much (see [Liquidity & Funding](/toolkit/liquidity-funding/)).

## Turning a futures position into a hedge

Used on their own, futures are directional bets. Used against an existing
exposure, they *reduce* risk: a producer who will sell oil later can **short**
oil futures today, locking in a price — losses on falling physical barrels are
offset by gains on the short. That is the essence of hedging, explored further in
[Hedging & Derivatives](/toolkit/hedging-derivatives/).

**Sources & further reading**

- [Margin: Know What's Needed (Introduction to Futures)](https://www.cmegroup.com/education/courses/introduction-to-futures/margin-know-what-is-needed) — CME Group
- [The Benefits of Futures Margins](https://www.cmegroup.com/education/courses/understanding-the-benefits-of-futures/the-benefits-of-futures-margins) — CME Group
- [Hedging with E-mini S&P 500 Futures](https://www.cmegroup.com/education/whitepapers/hedging-with-e-mini-sp-500-future) — CME Group
