// assets/js/tools.js — Risk Tools page: VaR/ES calculator, vol surface,
// correlation matrix and live markets board.
// Ported from _legacy/index-legacy.html (Live Markets board + Risk Analytics
// sections). Live prices are fetched via window.RM (assets/js/rm-data.js).
(function () {
  const root = document.getElementById('toolsRoot');
  if (!root) return;

  /* ═══════════════════════════════════════════════════
     LIVE MARKETS BOARD (ported from index-legacy.html ~2365-2515)
  ═══════════════════════════════════════════════════ */

  const MARKETS = {
    commodities: [
      { s: 'BZUSD', label: 'Brent Crude', sub: 'ICE · $/bbl',   pfx: '$', sfx: '/bbl', dec: 2 },
      { s: 'GCUSD', label: 'Gold',        sub: 'COMEX · $/oz',  pfx: '$', sfx: '/oz',  dec: 1 },
      { s: 'SIUSD', label: 'Silver',      sub: 'COMEX · $/oz',  pfx: '$', sfx: '/oz',  dec: 2 },
    ],
    fx: [
      { s: 'EURUSD', label: 'EUR / USD', sub: 'Spot FX', dec: 4 },
      { s: 'GBPUSD', label: 'GBP / USD', sub: 'Spot FX', dec: 4 },
      { s: 'USDJPY', label: 'USD / JPY', sub: 'Spot FX', dec: 2 },
      { s: 'USDINR', label: 'USD / INR', sub: 'Spot FX', pfx: '₹', dec: 2 },
    ],
    equities: [
      { s: '^GSPC', label: 'S&P 500',    sub: 'US Large Cap', dec: 0 },
      { s: '^DJI',  label: 'Dow Jones',  sub: 'US Blue Chip', dec: 0 },
      { s: '^IXIC', label: 'Nasdaq',     sub: 'US Tech',      dec: 0 },
      { s: '^FTSE', label: 'FTSE 100',   sub: 'UK',           dec: 0 },
      { s: '^N225', label: 'Nikkei 225', sub: 'Japan',        dec: 0 },
      { s: '^VIX',  label: 'VIX',        sub: 'Volatility',   dec: 2 },
    ],
  };

  function fmtNum(v, m) {
    return (m.pfx || '') + Number(v).toLocaleString('en-US',
      { minimumFractionDigits: m.dec, maximumFractionDigits: m.dec }) + (m.sfx || '');
  }

  // Build a small sparkline polyline SVG from an array of prices.
  function sparkSVG(points, w, h) {
    if (!points || points.length < 2) return '';
    w = w || 96; h = h || 34;
    const pad = 3;
    const min = Math.min(...points), max = Math.max(...points), range = (max - min) || 1;
    const step = (w - pad * 2) / (points.length - 1);
    const coords = points.map((p, i) =>
      `${(pad + i * step).toFixed(1)},${(h - pad - ((p - min) / range) * (h - pad * 2)).toFixed(1)}`).join(' ');
    const up = points[points.length - 1] >= points[0];
    const col = up ? 'var(--green)' : 'var(--red)';
    return `<svg class="spark" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" aria-hidden="true">`
         + `<polyline points="${coords}" fill="none" stroke="${col}" stroke-width="1.7" stroke-linejoin="round" stroke-linecap="round"/></svg>`;
  }

  function chgParts(q) {
    const pct = q && q.changePercentage != null ? q.changePercentage : 0;
    const up = pct >= 0;
    return { up, txt: (up ? '▲ ' : '▼ ') + Math.abs(pct).toFixed(2) + '%' };
  }

  // ── Live Markets board ──────────────────────────
  const _mktLoaded = {};

  function skeletonCards(cat) {
    return MARKETS[cat].map(inst =>
      `<div class="mkt-card mkt-skel">
         <div class="mkt-top"><span class="mkt-dot"></span><div><div class="mkt-label">${inst.label}</div><div class="mkt-sub">${inst.sub}</div></div></div>
         <div class="mkt-price">—</div>
         <div class="mkt-foot"><span class="mkt-chg">—</span></div>
       </div>`).join('');
  }

  async function loadMarketTab(cat) {
    if (_mktLoaded[cat]) return;
    _mktLoaded[cat] = true;
    const grid = document.getElementById('grid-' + cat);
    if (!grid) return;
    grid.innerHTML = skeletonCards(cat);

    const insts = MARKETS[cat];
    const [quotes, sparks] = await Promise.all([
      RM.getQuotes(insts.map(i => i.s)),
      Promise.all(insts.map(i => RM.getSparkline(i.s, 7))),
    ]);

    grid.innerHTML = insts.map((inst, i) => {
      const q = quotes[i], spark = sparks[i];
      const c = chgParts(q);
      const price = (q && q.price != null) ? fmtNum(q.price, inst) : '—';
      const flash = q ? (c.up ? 'flash-up' : 'flash-dn') : '';
      const svg = spark ? sparkSVG(spark, 96, 34) : '';
      return `<div class="mkt-card ${flash}">
         <div class="mkt-top"><span class="mkt-dot"></span><div><div class="mkt-label">${inst.label}</div><div class="mkt-sub">${inst.sub}</div></div></div>
         <div class="mkt-price">${price}</div>
         <div class="mkt-foot"><span class="mkt-chg ${c.up ? 'up' : 'dn'}">${q ? c.txt : '—'}</span><span class="mkt-spark">${svg}</span></div>
       </div>`;
    }).join('');

    updateMktStatus();
  }

  function updateMktStatus() {
    const el = document.getElementById('mktStatus');
    if (!el) return;
    const ts = new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', timeZoneName: 'short' });
    el.textContent = 'Live · ' + ts;
  }

  function showMarketTab(cat, btn) {
    document.querySelectorAll('.mkt-tab').forEach(b => b.classList.toggle('active', b === btn));
    document.querySelectorAll('.mkt-panel').forEach(p => p.classList.toggle('active', p.dataset.cat === cat));
    loadMarketTab(cat);
  }
  // showMarketTab is referenced via inline onclick= handlers in tools.html.
  window.showMarketTab = showMarketTab;

  // Lazy-load the Live Markets board when it first scrolls into view.
  (function initMarkets() {
    const section = document.getElementById('markets');
    if (!section) return;
    const start = () => loadMarketTab('commodities');
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((ents, obs) => {
        if (ents.some(e => e.isIntersecting)) { start(); obs.disconnect(); }
      }, { rootMargin: '200px' });
      io.observe(section);
    } else { start(); }
  })();

  // Refresh visible market data alongside a 30-minute cycle (matches the
  // cache TTL in rm-data.js so this simply re-renders newly cached data).
  setInterval(() => {
    const active = document.querySelector('.mkt-tab.active');
    if (active) { _mktLoaded[active.dataset.cat] = false; loadMarketTab(active.dataset.cat); }
  }, 30 * 60 * 1000);

  /* ═══════════════════════════════════════════════════
     RISK ANALYTICS — VaR calculator, vol surface,
     correlation matrix, tab switching
     (ported from index-legacy.html ~2522-2641)
  ═══════════════════════════════════════════════════ */

  function showRaTab(id, btn) {
    document.querySelectorAll('#raTabs .mkt-tab').forEach(b => b.classList.toggle('active', b === btn));
    document.querySelectorAll('.ra-panel').forEach(p => p.classList.toggle('active', p.dataset.ra === id));
  }
  // showRaTab is referenced via inline onclick= handlers in tools.html.
  window.showRaTab = showRaTab;

  // ── Interactive parametric VaR + Expected Shortfall ──
  (function initVaR() {
    const elVal = document.getElementById('vaValue');
    if (!elVal) return;
    const elVol = document.getElementById('vaVol'), elDays = document.getElementById('vaDays');
    const outVol = document.getElementById('vaVolOut'), outDays = document.getElementById('vaDaysOut');
    const conf = document.getElementById('vaConf');
    const vaVaR = document.getElementById('vaVaR'), vaES = document.getElementById('vaES');
    const vaVaRpct = document.getElementById('vaVaRpct'), vaESpct = document.getElementById('vaESpct');
    const note = document.getElementById('vaNote');
    let confLevel = 95;
    const Z = { 95: 1.6448536, 99: 2.3263479 };
    const pdf = z => Math.exp(-z * z / 2) / Math.sqrt(2 * Math.PI);

    function fmtUSD(v) {
      const a = Math.abs(v);
      if (a >= 1e9) return '$' + (v / 1e9).toFixed(2) + 'B';
      if (a >= 1e6) return '$' + (v / 1e6).toFixed(2) + 'M';
      if (a >= 1e3) return '$' + (v / 1e3).toFixed(1) + 'K';
      return '$' + Math.round(v).toLocaleString('en-US');
    }
    function countTo(el, target) {
      const start = parseFloat(el.dataset.v || '0'), t0 = performance.now(), dur = 600;
      el.dataset.v = target;
      (function tick(now) {
        const p = Math.min((now - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
        el.textContent = fmtUSD(start + (target - start) * eased);
        if (p < 1) requestAnimationFrame(tick);
      })(t0);
      // Guarantee the final value even if rAF is throttled (e.g. background tab).
      clearTimeout(el._ct);
      el._ct = setTimeout(() => { el.textContent = fmtUSD(target); }, dur + 90);
    }
    function compute() {
      const V = Math.max(0, parseFloat(elVal.value) || 0);
      const annVol = (parseFloat(elVol.value) || 0) / 100;
      const days = parseInt(elDays.value) || 1;
      outVol.textContent = (annVol * 100).toFixed(0) + '%';
      outDays.textContent = days + (days === 1 ? ' day' : ' days');
      const dailyVol = annVol / Math.sqrt(252);
      const z = Z[confLevel];
      const scale = dailyVol * Math.sqrt(days) * V;
      const varv = z * scale;
      const esv = (pdf(z) / (1 - confLevel / 100)) * scale;
      countTo(vaVaR, varv); countTo(vaES, esv);
      vaVaRpct.textContent = V ? (varv / V * 100).toFixed(2) + '% of book' : '—';
      vaESpct.textContent  = V ? (esv / V * 100).toFixed(2) + '% of book' : '—';
      note.innerHTML = `${days}-day ${confLevel}% parametric VaR on a <strong style="color:var(--white)">${fmtUSD(V)}</strong> book at ${(annVol * 100).toFixed(0)}% annualised vol. Expected Shortfall is the mean loss across the worst ${100 - confLevel}% of outcomes.`;
    }
    ['input', 'change'].forEach(ev => {
      elVal.addEventListener(ev, compute); elVol.addEventListener(ev, compute); elDays.addEventListener(ev, compute);
    });
    conf.querySelectorAll('button').forEach(b => b.addEventListener('click', () => {
      confLevel = parseInt(b.dataset.c);
      conf.querySelectorAll('button').forEach(x => x.classList.toggle('active', x === b));
      compute();
    }));
    compute();
  })();

  // ── Volatility surface heatmap (illustrative crude-oil surface) ──
  (function buildVolSurface() {
    const host = document.getElementById('volSurface');
    if (!host) return;
    const tenors = ['1M', '3M', '6M', '1Y', '2Y'];
    const money = ['80%', '90%', 'ATM', '110%', '120%'];
    const vols = [
      [42, 36, 32, 35, 41],
      [38, 33, 30, 32, 37],
      [35, 31, 28, 30, 34],
      [32, 29, 27, 28, 31],
      [30, 28, 26, 27, 29],
    ];
    const min = 26, max = 42;
    host.style.gridTemplateColumns = `40px repeat(${money.length},1fr)`;
    let html = '<div class="vs-cell vs-head"></div>';
    money.forEach(m => html += `<div class="vs-cell vs-head">${m}</div>`);
    vols.forEach((row, r) => {
      html += `<div class="vs-cell vs-head" style="display:flex;align-items:center">${tenors[r]}</div>`;
      row.forEach(v => {
        const op = (0.14 + (v - min) / (max - min) * 0.72).toFixed(2);
        html += `<div class="vs-cell" style="background:rgba(245,158,11,${op})">${v}</div>`;
      });
    });
    html += `<div style="grid-column:1/-1"><div class="vs-axis">Moneyness (strike ÷ forward) →&nbsp;&nbsp;·&nbsp;&nbsp;↓ Tenor</div></div>`;
    host.innerHTML = html;
  })();

  // ── Commodity correlation matrix (illustrative) ──
  (function buildCorr() {
    const host = document.getElementById('corrMatrix');
    if (!host) return;
    const assets = ['Brent', 'WTI', 'Gas', 'Power', 'EUA', 'Gold'];
    const M = [
      [1.00, 0.95, 0.35, 0.45, 0.30, 0.15],
      [0.95, 1.00, 0.33, 0.42, 0.28, 0.12],
      [0.35, 0.33, 1.00, 0.68, 0.22, 0.05],
      [0.45, 0.42, 0.68, 1.00, 0.55, 0.08],
      [0.30, 0.28, 0.22, 0.55, 1.00, 0.18],
      [0.15, 0.12, 0.05, 0.08, 0.18, 1.00],
    ];
    host.style.gridTemplateColumns = `46px repeat(${assets.length},1fr)`;
    let html = '<div class="cm-cell cm-head"></div>';
    assets.forEach(a => html += `<div class="cm-cell cm-head">${a}</div>`);
    M.forEach((row, r) => {
      html += `<div class="cm-cell cm-row-head">${assets[r]}</div>`;
      row.forEach(v => {
        const col = v >= 0
          ? `rgba(16,185,129,${(0.08 + v * 0.78).toFixed(2)})`
          : `rgba(239,68,68,${(0.08 + Math.abs(v) * 0.78).toFixed(2)})`;
        html += `<div class="cm-cell" style="background:${col}">${v.toFixed(2)}</div>`;
      });
    });
    host.innerHTML = html;
  })();

})();
