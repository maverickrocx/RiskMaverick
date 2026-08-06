// assets/js/theme.js — light/dark toggle (dark is default; no-flash read happens inline in head.html)
(function () {
  function setTheme(t) {
    if (t === "light") {
      document.documentElement.setAttribute("data-theme", "light");
    } else {
      document.documentElement.removeAttribute("data-theme");
    }
    try { localStorage.setItem("rm-theme", t); } catch (e) {}
    document.querySelectorAll("[data-theme-toggle]").forEach(function (b) {
      b.setAttribute("aria-label", t === "light" ? "Switch to dark mode" : "Switch to light mode");
    });
  }
  document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var current = document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
      setTheme(current === "light" ? "dark" : "light");
    });
  });
})();
