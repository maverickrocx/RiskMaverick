// assets/js/nav.js — mobile drawer toggle + tap-to-open mega on touch +
// hover-intent mega menus on desktop.
//
// The mega panel sits a few pixels below its trigger, so a mouse moving
// diagonally toward it briefly leaves the trigger's hoverable area — plain
// CSS :hover closes the menu right then, before the pointer arrives. A
// short close delay (cleared if the pointer lands back on the trigger or
// the panel) bridges that gap so the menu stays open long enough to reach
// and click its links.
(function () {
  var toggle = document.querySelector(".nav-toggle");
  var links = document.getElementById("navLinks");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  document.querySelectorAll(".nav-item.has-mega > a").forEach(function (a) {
    a.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width:820px)").matches) {
        e.preventDefault();
        a.parentElement.classList.toggle("mega-open");
      }
    });
  });

  var CLOSE_DELAY = 300;
  function isDesktop() {
    return window.matchMedia("(min-width:821px)").matches;
  }
  document.querySelectorAll(".nav-item.has-mega").forEach(function (item) {
    var closeTimer;
    function open() {
      if (!isDesktop()) return;
      clearTimeout(closeTimer);
      item.classList.add("mega-open");
    }
    function scheduleClose() {
      if (!isDesktop()) return;
      clearTimeout(closeTimer);
      closeTimer = setTimeout(function () {
        item.classList.remove("mega-open");
      }, CLOSE_DELAY);
    }
    item.addEventListener("mouseenter", open);
    item.addEventListener("mouseleave", scheduleClose);
    item.addEventListener("focusin", open);
    item.addEventListener("focusout", scheduleClose);
  });
})();
