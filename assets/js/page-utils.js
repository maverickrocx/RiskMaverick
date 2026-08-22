// assets/js/page-utils.js — floating back + back-to-top controls on every page.
//
// Both buttons fade in once the reader has scrolled past the fold; at the top
// of a page the main nav (and, on map pages, the sticky subnav) already covers
// navigation, so the cluster stays out of the way until it's useful.
(function () {
  var wrap = document.createElement('div');
  wrap.className = 'pageutils';

  var back = document.createElement('button');
  back.type = 'button';
  back.setAttribute('aria-label', 'Go back');
  back.title = 'Back';
  back.textContent = '←';
  back.addEventListener('click', function () { history.back(); });

  var top = document.createElement('button');
  top.type = 'button';
  top.setAttribute('aria-label', 'Back to top');
  top.title = 'Back to top';
  top.textContent = '↑';
  top.addEventListener('click', function () {
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
  });

  wrap.appendChild(back);
  wrap.appendChild(top);
  document.body.appendChild(wrap);

  var canGoBack = window.history.length > 1;
  function update() {
    var scrolled = window.scrollY > 300;
    top.classList.toggle('show', scrolled);
    back.classList.toggle('show', canGoBack && scrolled);
  }
  window.addEventListener('scroll', update, { passive: true });
  update();
})();
