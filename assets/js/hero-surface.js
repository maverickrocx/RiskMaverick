// assets/js/hero-surface.js — the hero risk surface.
// A rotating wireframe mesh drawn on a canvas behind the hero copy: a payoff
// surface that breathes, drifts with the pointer, and fades out as the reader
// scrolls past it. Decorative only — aria-hidden, and skipped entirely under
// prefers-reduced-motion.
(function () {
  if (!window.matchMedia) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var cv = document.querySelector('[data-surface]');
  if (!cv || !cv.getContext) return;

  var N = 22, mx = 0, my = 0, tx = 0, ty = 0, t = 0, raf;

  window.addEventListener('pointermove', function (e) {
    tx = (e.clientX / window.innerWidth - 0.5) * 2;
    ty = (e.clientY / window.innerHeight - 0.5) * 2;
  }, { passive: true });

  function fit() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var r = cv.getBoundingClientRect();
    cv.width = Math.max(1, r.width * dpr);
    cv.height = Math.max(1, r.height * dpr);
    var ctx = cv.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: r.width, h: r.height };
  }

  // Height field: a central ridge with a travelling wave across it.
  function height(u, v, time) {
    return Math.exp(-u * u * 1.7) * 0.42
         + 0.22 * Math.cos(v * 2.1 + time * 0.35) * Math.exp(-Math.abs(u) * 0.9)
         + 0.10 * Math.sin(u * 3.1 - time * 0.5);
  }

  function draw() {
    var f = fit(), ctx = f.ctx, w = f.w, h = f.h;
    ctx.clearRect(0, 0, w, h);
    mx += (tx - mx) * 0.05; my += (ty - my) * 0.05;
    t += 0.008;

    // Once scrolled past, keep the loop alive but stop painting — cheaper than
    // tearing the rAF down and rebuilding it on the way back up.
    var fade = Math.max(0, 1 - window.scrollY / 520);
    if (fade <= 0.01) { raf = requestAnimationFrame(draw); return; }

    var cx = w * 0.26, cy = h * 0.56;
    var scale = Math.min(w, h) * 0.62;
    var yaw = t * 0.18 + mx * 0.35;
    var tilt = 0.42 + my * 0.10;
    var ca = Math.cos(yaw), sa = Math.sin(yaw);

    var pts = [];
    for (var i = 0; i <= N; i++) {
      pts[i] = [];
      for (var j = 0; j <= N; j++) {
        var u = (i / N) * 2 - 1, v = (j / N) * 2 - 1;
        var z = height(u, v, t);
        var rx = u * ca - v * sa, rz = u * sa + v * ca;
        pts[i][j] = {
          x: cx + rx * scale,
          y: cy + rz * scale * tilt - z * scale * 0.78,
          d: (rz + 1) / 2,
          z: z
        };
      }
    }

    ctx.lineWidth = 1;
    function stroke(a, b) {
      var depth = (a.d + b.d) / 2;
      var lift = Math.max(0, (a.z + b.z) / 2);
      var alpha = (0.05 + depth * 0.20 + lift * 0.30) * fade;
      ctx.strokeStyle = 'rgba(255,122,26,' + alpha.toFixed(3) + ')';
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.stroke();
    }
    for (var a = 0; a <= N; a++) {
      for (var b = 0; b < N; b++) {
        stroke(pts[a][b], pts[a][b + 1]);
        stroke(pts[b][a], pts[b + 1][a]);
      }
    }
    raf = requestAnimationFrame(draw);
  }

  window.addEventListener('resize', function () {
    cancelAnimationFrame(raf); raf = requestAnimationFrame(draw);
  });
  raf = requestAnimationFrame(draw);
})();
