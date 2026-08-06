// assets/js/train.js — continuous card train.
// Replaces the 3D cylinder: front-facing cards that scroll steadily in one
// direction and wrap seamlessly, like a ticker made of cards.
//
// Same seam maths as the price ticker: the track is width:max-content holding
// two identical groups, so translating it -50% lands group two exactly where
// group one began. The gap after the last card equals the gap between cards,
// so the rhythm never stutters at the wrap.
//
// A grid opts in with data-train. Without JS (or under reduced motion) the
// original grid renders untouched — this is pure enhancement.
(function () {
  if (!window.matchMedia) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var MIN_CARDS = 4;          // fewer than this and a marquee is just noise
  var PX_PER_SEC = 42;        // readable drift; duration is derived from width

  [].forEach.call(document.querySelectorAll('[data-train]'), function (grid) {
    var cards = [].slice.call(grid.querySelectorAll('.card'));
    if (cards.length < MIN_CARDS) return;

    var wrap = document.createElement('div');
    wrap.className = 'train';

    var view = document.createElement('div');
    view.className = 'train-view';

    var track = document.createElement('div');
    track.className = 'train-track';

    var group = document.createElement('div');
    group.className = 'train-group';
    cards.forEach(function (c) { group.appendChild(c); });

    var clone = group.cloneNode(true);
    clone.setAttribute('aria-hidden', 'true');
    // the duplicate must not be reachable by keyboard or screen readers
    [].forEach.call(clone.querySelectorAll('a, button'), function (el) { el.tabIndex = -1; });

    track.appendChild(group);
    track.appendChild(clone);
    view.appendChild(track);
    wrap.appendChild(view);

    grid.parentNode.insertBefore(wrap, grid);
    grid.hidden = true;

    function retime() {
      var w = group.getBoundingClientRect().width;
      if (!w) return;
      track.style.animationDuration = (w / PX_PER_SEC).toFixed(2) + 's';
    }
    retime();
    window.addEventListener('resize', retime);

    // Pause while a card is hovered or focused, so it can actually be read
    // and clicked — a moving target you cannot catch is not navigation.
    wrap.addEventListener('mouseenter', function () { track.style.animationPlayState = 'paused'; });
    wrap.addEventListener('mouseleave', function () { track.style.animationPlayState = 'running'; });
    wrap.addEventListener('focusin',  function () { track.style.animationPlayState = 'paused'; });
    wrap.addEventListener('focusout', function () { track.style.animationPlayState = 'running'; });
  });
})();
