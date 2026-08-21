// assets/js/edge-guide.js — measures the header (ticker + nav) so the
// fixed overflow guide-lines in site.css can start right below it instead
// of at a guessed pixel value.
(function () {
  function measure() {
    var topbar = document.querySelector('.topbar');
    var nav = document.querySelector('.nav');
    var h = (topbar ? topbar.getBoundingClientRect().height : 0) +
            (nav ? nav.getBoundingClientRect().height : 0);
    if (h > 0) {
      document.documentElement.style.setProperty('--header-h', h + 'px');
    }
  }
  measure();
  window.addEventListener('resize', measure);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
})();
