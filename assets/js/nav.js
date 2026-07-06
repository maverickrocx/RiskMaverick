// assets/js/nav.js — mobile drawer toggle + tap-to-open mega on touch
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
})();
