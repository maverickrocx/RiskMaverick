// assets/js/ticker.js — renders the topbar live ticker
(function () {
  var TICKER = [
    { symbol: "BZUSD", label: "Brent" },
    { symbol: "GCUSD", label: "Gold" },
    { symbol: "SIUSD", label: "Silver" },
    { symbol: "^GSPC", label: "S&P 500" },
    { symbol: "^VIX",  label: "VIX" },
    { symbol: "EURUSD", label: "EUR/USD" }
  ];
  var el = document.getElementById("rmTicker");
  if (!el || !window.RM) return;
  RM.getQuotes(TICKER.map(function (t) { return t.symbol; })).then(function (quotes) {
    var html = TICKER.map(function (t, i) {
      var q = quotes[i] || {};
      var price = (q.price != null) ? Number(q.price).toLocaleString(undefined, { maximumFractionDigits: 2 }) : "—";
      var chg = Number(q.changePercentage || q.changesPercentage || 0);
      var cls = chg >= 0 ? "up" : "down";
      var sign = chg >= 0 ? "+" : "";
      return '<span class="tick"><b>' + t.label + '</b> <span class="tick-px">' + price +
             '</span> <span class="tick-chg ' + cls + '">' + sign + chg.toFixed(2) + '%</span></span>';
    }).join("");
    el.innerHTML = html + html; // duplicate for seamless marquee
  }).catch(function () { el.innerHTML = '<span class="ticker-loading">Markets unavailable</span>'; });
})();
