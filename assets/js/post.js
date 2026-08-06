// assets/js/post.js — reading progress bar + sticky TOC with scrollspy.
// Progressive enhancement: without JS the article reads normally and the TOC
// simply stays empty (it is hidden by CSS when it has no items).
(function () {
  var body = document.getElementById('postBody');
  var list = document.getElementById('tocList');
  var fill = document.getElementById('readbarFill');
  if (!body) return;

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── Build the TOC from the article's own h2s ──
  var heads = [], links = [];
  if (list) {
    heads = [].slice.call(body.querySelectorAll('h2'));
    heads.forEach(function (h, i) {
      if (!h.id) h.id = 'sec-' + i;
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent.trim();
      li.appendChild(a); list.appendChild(li); links.push(a);
    });
    if (heads.length) list.parentNode.classList.add('has-items');
  }

  function onScroll() {
    // Progress across the article body only, not the whole document.
    if (fill) {
      var r = body.getBoundingClientRect();
      var total = r.height - window.innerHeight;
      var done = total > 0 ? Math.min(Math.max(-r.top / total, 0), 1) : (r.top <= 0 ? 1 : 0);
      fill.style.width = (done * 100).toFixed(2) + '%';
    }
    // Scrollspy: last heading whose top has passed the reading line.
    if (links.length) {
      var active = 0;
      for (var i = 0; i < heads.length; i++) {
        if (heads[i].getBoundingClientRect().top <= 120) active = i; else break;
      }
      for (var j = 0; j < links.length; j++) links[j].classList.toggle('active', j === active);
    }
  }

  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    (reduce ? function (f) { f(); } : window.requestAnimationFrame)(function () { onScroll(); ticking = false; });
  }, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();
})();
