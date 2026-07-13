/* Open external links in a new tab.
   Any anchor pointing to a different host than the current site gets
   target="_blank" + rel="noopener noreferrer". Internal navigation is
   left untouched so it stays in the same tab. */
(function () {
  var host = window.location.hostname;
  var anchors = document.querySelectorAll('a[href]');
  for (var i = 0; i < anchors.length; i++) {
    var a = anchors[i];
    var href = a.getAttribute('href');
    if (!href || !/^https?:\/\//i.test(href)) continue; // skip relative / mailto / anchors
    var u;
    try { u = new URL(href, window.location.href); } catch (e) { continue; }
    if (u.hostname === host) continue; // same-site link — leave alone
    a.setAttribute('target', '_blank');
    var rel = (a.getAttribute('rel') || '').split(/\s+/).filter(Boolean);
    if (rel.indexOf('noopener') === -1) rel.push('noopener');
    if (rel.indexOf('noreferrer') === -1) rel.push('noreferrer');
    a.setAttribute('rel', rel.join(' '));
  }
})();
