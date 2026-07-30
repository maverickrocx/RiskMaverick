// assets/js/energy-map.js — Gas & Power Map: region tabs + country selection.
// Content is server-rendered by Liquid; this only toggles visibility, so the
// page still works with JS disabled (all panels render, first one active).
(function () {
  var root = document.querySelector('.emap');
  if (!root) return;

  function activate(nodes, match) {
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].classList.toggle('active', match(nodes[i]));
    }
  }

  // ── Region tabs ──
  var tabs = root.querySelectorAll('.emap-tab');
  var panels = root.querySelectorAll('.emap-panel');
  for (var i = 0; i < tabs.length; i++) {
    tabs[i].addEventListener('click', function () {
      var slug = this.getAttribute('data-region');
      activate(tabs, function (n) { return n.getAttribute('data-region') === slug; });
      activate(panels, function (n) { return n.getAttribute('data-region') === slug; });
    });
  }

  // ── Country selection (scoped to the region panel it lives in) ──
  for (var p = 0; p < panels.length; p++) {
    (function (panel) {
      var btns = panel.querySelectorAll('.emap-country');
      var details = panel.querySelectorAll('.emap-detail');
      for (var j = 0; j < btns.length; j++) {
        btns[j].addEventListener('click', function () {
          var key = this.getAttribute('data-country');
          activate(btns, function (n) { return n.getAttribute('data-country') === key; });
          activate(details, function (n) { return n.getAttribute('data-country') === key; });
        });
      }
    })(panels[p]);
  }
})();
