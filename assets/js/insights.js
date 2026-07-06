// assets/js/insights.js — client-side tag filtering for the Insights feed
(function () {
  var filters = document.getElementById("filters");
  var feed = document.getElementById("feed");
  if (!filters || !feed) return;
  filters.addEventListener("click", function (e) {
    var btn = e.target.closest(".filter");
    if (!btn) return;
    filters.querySelectorAll(".filter").forEach(function (b) { b.classList.remove("active"); });
    btn.classList.add("active");
    var tag = btn.getAttribute("data-tag");
    feed.querySelectorAll(".card").forEach(function (card) {
      var tags = " " + (card.getAttribute("data-tags") || "") + " ";
      card.style.display = (tag === "all" || tags.indexOf(" " + tag + " ") > -1) ? "" : "none";
    });
  });
})();
