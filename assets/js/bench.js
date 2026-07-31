// assets/js/bench.js — hydrate hub benchmark tiles with live quotes.
// Tiles carrying data-symbol are refreshed from the shared feed (rm-data.js).
// Tiles without one keep their server-rendered value and its "as of" date —
// those instruments aren't on the feed, so they're curated and dated instead.
(function () {
  var cards = document.querySelectorAll('.bcard[data-symbol]');
  if (!cards.length || !window.RM) return;

  function fmt(v, dec, pfx, sfx) {
    return (pfx || '') + Number(v).toLocaleString('en-US', {
      minimumFractionDigits: dec, maximumFractionDigits: dec
    }) + (sfx || '');
  }

  Array.prototype.forEach.call(cards, function (card) {
    var sym = card.getAttribute('data-symbol');
    var dec = parseInt(card.getAttribute('data-dec'), 10);
    if (isNaN(dec)) dec = 2;
    var pfx = card.getAttribute('data-pfx') || '';
    var sfx = card.getAttribute('data-sfx') || '';
    var pxEl = card.querySelector('.px');
    var chgEl = card.querySelector('.chg');

    RM.getQuote(sym).then(function (q) {
      chgEl.classList.remove('is-pending');
      if (!q || q.price == null) {
        // Feed unavailable — leave the rendered fallback price untouched.
        chgEl.classList.add('is-static');
        chgEl.textContent = 'feed unavailable';
        return;
      }
      var st = RM.quoteStatus(q);
      var unit = pxEl.querySelector('.unit');
      pxEl.textContent = fmt(q.price, dec, pfx, sfx);
      if (unit) pxEl.appendChild(unit);

      var pct = q.changePercentage != null ? q.changePercentage : 0;
      var up = pct >= 0;
      var asof = st.live ? 'Live'
        : (st.asOf ? 'prev close · ' + st.asOf.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
                   : 'last close');
      chgEl.classList.add(up ? 'up' : 'dn');
      if (!st.live) chgEl.classList.add('is-prev');
      chgEl.textContent = (up ? '▲ ' : '▼ ') + Math.abs(pct).toFixed(2) + '% · ' + asof;
    }).catch(function () {
      chgEl.classList.remove('is-pending');
      chgEl.classList.add('is-static');
      chgEl.textContent = 'feed unavailable';
    });
  });
})();
