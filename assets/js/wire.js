// assets/js/wire.js — Risk Wire sector filter.
// Server-rendered feed; JS only hides/shows groups, so with JS off every brief
// is still listed.
(function () {
  var bar = document.querySelector('.filterbar');
  var feed = document.getElementById('wireFeed');
  var status = document.getElementById('wireStatus');
  if (!bar || !feed) return;

  var btns = [].slice.call(bar.querySelectorAll('.filterbtn'));
  var groups = [].slice.call(feed.querySelectorAll('.wireday-group'));

  bar.addEventListener('click', function (e) {
    var btn = e.target.closest('.filterbtn');
    if (!btn) return;
    var want = btn.getAttribute('data-filter');

    btns.forEach(function (b) {
      var on = b === btn;
      b.classList.toggle('is-on', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });

    var shown = 0;
    groups.forEach(function (g) {
      var match = want === 'all' || g.getAttribute('data-sector') === want;
      g.hidden = !match;
      if (match) shown++;
    });

    if (status) {
      status.textContent = shown + ' brief' + (shown === 1 ? '' : 's') +
        (want === 'all' ? ' shown' : ' in ' + want);
    }
  });
})();
