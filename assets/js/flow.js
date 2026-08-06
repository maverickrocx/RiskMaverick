// assets/js/flow.js — focus one supply chain in the gas & power flow diagram.
// The SVG is server-rendered and readable as-is; this only sets data-focus,
// which CSS uses to dim the other chains.
(function () {
  var tabs = document.querySelector('.flowtabs');
  var svg = document.getElementById('flowDiagram');
  if (!tabs || !svg) return;

  tabs.addEventListener('click', function (e) {
    var btn = e.target.closest('.flowtab');
    if (!btn) return;
    var want = btn.getAttribute('data-flow');
    [].forEach.call(tabs.querySelectorAll('.flowtab'), function (b) {
      var on = b === btn;
      b.classList.toggle('is-on', on);
      b.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    if (want === 'all') svg.removeAttribute('data-focus');
    else svg.setAttribute('data-focus', want);
  });
})();
