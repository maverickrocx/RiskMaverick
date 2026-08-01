// assets/js/drum.js — cylindrical component navigator.
//
// PROGRESSIVE ENHANCEMENT. Jekyll renders a normal .card-grid of real <a href> cards.
// This script MOVES those same anchors into a 3D drum — it never duplicates or recreates
// them — so search engines, screen readers with JS off, and phones all get the grid.
//
// It only engages when every one of these is true:
//   * the grid opts in with data-drum
//   * at least MIN_CARDS cards
//   * viewport at least MIN_WIDTH
//   * a fine pointer (mouse/trackpad, not touch)
//   * the user has not asked for reduced motion
//
// Geometry: the ring is pitched PITCH degrees so you look down on the cylinder. That lifts
// the front of the ring up the screen by RAD*sin(PITCH), so the selected card counter-rotates
// upright and translates back down by exactly that amount to land dead centre, then pops
// POP px toward the viewer. Change PITCH and the centring corrects itself.
(function () {
  var PITCH = 30, POP = 70, SCALE = 1.24, PULL = 0.62;
  var STEP_MS = 480, MIN_CARDS = 4, MIN_WIDTH = 1000;
  var CARD_W = 150, CARD_H = 232, STAGE_H = 420;

  if (!window.matchMedia) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!matchMedia('(pointer: fine)').matches) return;

  function radiusFor(n, w) {
    // keep the widest card on the ring inside the container
    var r = Math.min(260, Math.max(150, w * 0.26));
    return n <= 4 ? r * 0.85 : r;
  }

  function build(grid) {
    var cards = [].slice.call(grid.querySelectorAll('.card'));
    var n = cards.length;
    if (n < MIN_CARDS) return null;

    var wrap = document.createElement('div');
    wrap.className = 'rmdrum';
    var stage = document.createElement('div');
    stage.className = 'rmdrum-stage';
    stage.tabIndex = 0;
    stage.setAttribute('role', 'listbox');
    stage.setAttribute('aria-label', 'Components — use arrow keys to browse, enter to open');
    var ring = document.createElement('div');
    ring.className = 'rmdrum-ring';
    stage.appendChild(ring);

    var foot = document.createElement('div');
    foot.className = 'rmdrum-foot';
    foot.innerHTML =
      '<button class="rmdrum-nav" data-d="1" aria-label="Previous component">&#8249;</button>' +
      '<button class="rmdrum-nav" data-d="-1" aria-label="Next component">&#8250;</button>' +
      '<span class="rmdrum-cap"></span><span class="rmdrum-dots"></span>' +
      '<button class="rmdrum-exit">Grid view</button>';

    grid.parentNode.insertBefore(wrap, grid);
    wrap.appendChild(stage);
    wrap.appendChild(foot);
    grid.hidden = true;

    cards.forEach(function (c) { c.classList.add('rmdrum-card'); ring.appendChild(c); });

    var dots = foot.querySelector('.rmdrum-dots');
    for (var i = 0; i < n; i++) dots.appendChild(document.createElement('i'));

    var STEP = 360 / n, RAD = radiusFor(n, wrap.clientWidth || 900), idx = 0, lock = 0;

    function render() {
      var yc = RAD * Math.sin(PITCH * Math.PI / 180);
      ring.style.transform = 'translateZ(' + (-RAD * PULL) + 'px) rotateX(' + PITCH + 'deg) rotateY(' + (-idx * STEP) + 'deg)';
      cards.forEach(function (c, i) {
        var on = i === idx;
        c.classList.toggle('is-sel', on);
        c.setAttribute('aria-selected', on ? 'true' : 'false');
        c.tabIndex = on ? 0 : -1;
        c.style.transform = on
          ? 'rotateY(' + (i * STEP) + 'deg) translateZ(' + RAD + 'px) rotateX(' + (-PITCH) + 'deg) translateY(' + yc.toFixed(1) + 'px) translateZ(' + POP + 'px) scale(' + SCALE + ')'
          : 'rotateY(' + (i * STEP) + 'deg) translateZ(' + RAD + 'px) scale(.86)';
        c.style.zIndex = on ? 6 : 1;
      });
      [].forEach.call(dots.children, function (d, i) { d.className = i === idx ? 'on' : ''; });
      foot.querySelector('.rmdrum-cap').textContent = (cards[idx].querySelector('h3') || {}).textContent || '';
    }

    function step(d) {
      var next = idx + d;
      if (next < 0 || next > n - 1) return false;   // at an end — caller lets the page scroll
      if (lock) return true;
      lock = 1; setTimeout(function () { lock = 0; }, STEP_MS);
      idx = next; render();
      return true;
    }

    stage.addEventListener('wheel', function (e) {
      var d = (e.deltaY > 0 || e.deltaX > 0) ? -1 : 1;
      // release the wheel at either end so the page keeps scrolling
      if (step(d)) e.preventDefault();
    }, { passive: false });

    stage.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { e.preventDefault(); step(-1); }
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); step(1); }
      else if (e.key === 'Home') { e.preventDefault(); idx = 0; render(); }
      else if (e.key === 'End') { e.preventDefault(); idx = n - 1; render(); }
      else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); cards[idx].click(); }
    });

    // a click on anything but the front card selects it rather than navigating
    cards.forEach(function (c, i) {
      c.addEventListener('click', function (e) { if (i !== idx) { e.preventDefault(); idx = i; render(); } });
    });

    [].forEach.call(foot.querySelectorAll('.rmdrum-nav'), function (b) {
      b.addEventListener('click', function () { step(+b.dataset.d); });
    });

    foot.querySelector('.rmdrum-exit').addEventListener('click', function () { teardown(); });

    function teardown() {
      cards.forEach(function (c) {
        c.classList.remove('rmdrum-card', 'is-sel');
        c.removeAttribute('style'); c.removeAttribute('aria-selected'); c.removeAttribute('tabindex');
        grid.appendChild(c);
      });
      grid.hidden = false;
      wrap.parentNode.removeChild(wrap);
      grid.setAttribute('data-drum-off', '');
    }

    var rt;
    window.addEventListener('resize', function () {
      clearTimeout(rt);
      rt = setTimeout(function () {
        if (window.innerWidth < MIN_WIDTH) { teardown(); return; }
        RAD = radiusFor(n, wrap.clientWidth || 900); render();
      }, 150);
    });

    stage.style.height = STAGE_H + 'px';
    ring.style.setProperty('--cw', CARD_W + 'px');
    ring.style.setProperty('--ch', CARD_H + 'px');
    render();
    return wrap;
  }

  function init() {
    if (window.innerWidth < MIN_WIDTH) return;
    [].forEach.call(document.querySelectorAll('.card-grid[data-drum]'), function (g) {
      if (!g.hasAttribute('data-drum-off')) build(g);
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
