// assets/js/train.js — draggable, bidirectional card cylinder.
//
// Cards drift left on their own, like before, but the strip is three
// identical groups wide (prev / current / next) instead of two, so the
// user can grab it with a mouse or a finger and drag either direction —
// the loop still seams up because groups B and C (or A and B) are pixel
// identical. Letting go resumes the ambient drift.
//
// A grid opts in with data-train. Without JS (or under reduced motion) the
// original grid renders untouched — this is pure enhancement.
(function () {
  if (!window.matchMedia) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var MIN_CARDS = 4;      // fewer than this and a carousel is just noise
  var PX_PER_SEC = 34;    // ambient drift speed while not being dragged

  [].forEach.call(document.querySelectorAll('[data-train]'), function (grid) {
    var cards = [].slice.call(grid.querySelectorAll('.card'));
    if (cards.length < MIN_CARDS) return;

    var wrap = document.createElement('div');
    wrap.className = 'train';

    var view = document.createElement('div');
    view.className = 'train-view';

    var track = document.createElement('div');
    track.className = 'train-track';
    track.style.animation = 'none'; // JS drives transform directly

    var groupB = document.createElement('div');
    groupB.className = 'train-group';
    cards.forEach(function (c) { groupB.appendChild(c); });

    var groupA = groupB.cloneNode(true);
    var groupC = groupB.cloneNode(true);
    [groupA, groupC].forEach(function (g) {
      g.setAttribute('aria-hidden', 'true');
      [].forEach.call(g.querySelectorAll('a, button'), function (el) { el.tabIndex = -1; });
    });

    track.appendChild(groupA);
    track.appendChild(groupB);
    track.appendChild(groupC);
    view.appendChild(track);
    wrap.appendChild(view);

    grid.parentNode.insertBefore(wrap, grid);
    grid.hidden = true;

    var DRAG_THRESHOLD = 6; // px of movement before a tap becomes a drag

    var groupW = 0, pos = 0, dragging = false, paused = false;
    var dragStartX = 0, dragStartPos = 0, lastT = null;
    var pointerId = null;

    function measure() {
      var w = groupB.getBoundingClientRect().width;
      if (!w) return;
      groupW = w;
      if (pos === 0) pos = -groupW; // start centred on the real (B) group
    }
    measure();
    window.addEventListener('resize', measure);

    function wrapPos() {
      if (!groupW) return;
      while (pos <= -groupW * 2) pos += groupW;
      while (pos >= 0) pos -= groupW;
    }

    function frame(now) {
      if (lastT === null) lastT = now;
      var dt = Math.min((now - lastT) / 1000, 0.1);
      lastT = now;
      if (!dragging && !paused) pos -= PX_PER_SEC * dt;
      wrapPos();
      track.style.transform = 'translateX(' + pos.toFixed(1) + 'px)';
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);

    // A plain tap must resolve as a normal click on whatever was tapped (a
    // card's link, say). Pointer capture redirects that click to the
    // capturing element, so it's only engaged once real drag movement is
    // seen — not on pointerdown itself.
    function dragDown(x, id) {
      dragging = false;
      dragStartX = x;
      dragStartPos = pos;
      pointerId = id;
    }
    function dragMove(x) {
      if (pointerId === null) return;
      if (!dragging) {
        if (Math.abs(x - dragStartX) < DRAG_THRESHOLD) return;
        dragging = true;
        wrap.classList.add('is-dragging');
        if (pointerId !== undefined && view.setPointerCapture) {
          try { view.setPointerCapture(pointerId); } catch (e) {}
        }
      }
      pos = dragStartPos + (x - dragStartX);
    }
    function dragUp() {
      dragging = false;
      pointerId = null;
      wrap.classList.remove('is-dragging');
    }

    if (window.PointerEvent) {
      view.addEventListener('pointerdown', function (e) {
        if (e.button !== undefined && e.button !== 0) return;
        dragDown(e.clientX, e.pointerId);
      });
      view.addEventListener('pointermove', function (e) { dragMove(e.clientX); });
      view.addEventListener('pointerup', dragUp);
      view.addEventListener('pointercancel', dragUp);
    } else {
      view.addEventListener('mousedown', function (e) { dragDown(e.clientX, undefined); });
      window.addEventListener('mousemove', function (e) { dragMove(e.clientX); });
      window.addEventListener('mouseup', dragUp);
      view.addEventListener('touchstart', function (e) { dragDown(e.touches[0].clientX, undefined); }, { passive: true });
      view.addEventListener('touchmove', function (e) { dragMove(e.touches[0].clientX); }, { passive: true });
      view.addEventListener('touchend', dragUp);
    }

    // Pause ambient drift (not the user's own drag) while hovered or focused,
    // so a card can actually be read and clicked.
    wrap.addEventListener('mouseenter', function () { paused = true; });
    wrap.addEventListener('mouseleave', function () { paused = false; });
    wrap.addEventListener('focusin', function () { paused = true; });
    wrap.addEventListener('focusout', function () { paused = false; });
  });
})();
