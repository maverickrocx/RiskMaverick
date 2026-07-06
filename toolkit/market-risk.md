---
title: Market Risk
tag: market-risk
blurb: "VaR, volatility, stress testing and the Greeks."
---

Market risk is the risk of loss from movements in market prices. This hub covers
how it is measured — from Value at Risk to stress testing — and how desks keep
it within appetite.

## How it works

Market risk is the risk of loss from moves in prices, rates, volatility and
spreads. It is measured in a few complementary ways: **Value at Risk (VaR)** —
the loss a portfolio is unlikely to exceed over a set horizon at a given
confidence — and, increasingly, **Expected Shortfall (ES)**, the *average* loss
in the tail beyond VaR, which captures extreme outcomes more prudently. Alongside
these sit **sensitivities** (the "Greeks" — delta, gamma, vega, etc.) that show
how value responds to each risk factor, and **stress testing / scenario
analysis** that asks what happens under specific shocks rather than statistical
averages.

## In practice

For banks, market-risk capital is set by the Basel Committee's **Fundamental
Review of the Trading Book (FRTB)**, introduced after the 2008 crisis. Its
headline change is a shift in the regulatory measure **from VaR at 99% to
Expected Shortfall at 97.5%**, to better capture tail risk, plus **liquidity
horizons** that recognise some positions take longer to exit. Firms run VaR/ES
daily, **backtest** the models against actual P&L, and manage exposure to
board-approved limits and risk appetite — the discipline the RiskMaverick VaR
calculator on the Tools page illustrates.

**Sources & further reading**

- [Minimum capital requirements for market risk (FRTB)](https://www.bis.org/bcbs/publ/d457.htm) — Basel Committee on Banking Supervision (BIS)
- [Revised framework for market risk capital requirements (press release)](https://www.bis.org/press/p160114.htm) — Basel Committee on Banking Supervision (BIS)
- [Explanatory note on the minimum capital requirements for market risk](https://www.bis.org/bcbs/publ/d457_note.pdf) — Basel Committee on Banking Supervision (BIS)
