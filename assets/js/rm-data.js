// assets/js/rm-data.js — FMP quotes/sparklines with shared per-symbol cache
(function () {
const FMP_KEY = 'lq7E2T0mp2X0PAwS1txXRNdxP3aZo9lp';
const FMP = 'https://financialmodelingprep.com/stable';

// ── Instrument registry ──────────────────────────
// Trimmed to 8 key instruments to stay within FMP free tier (250 calls/day).
// Cache + 30-min refresh means ~8 calls per session, shared across visitors.
const TICKER_INSTRUMENTS = [
  { symbol: '^GSPC',  label: 'S&P 500',     prefix: '',  suffix: '',     decimals: 0, cat: 'index' },
  { symbol: '^VIX',   label: 'VIX',         prefix: '',  suffix: '',     decimals: 2, cat: 'vol'   },
  { symbol: 'BZUSD',  label: 'Brent Crude', prefix: '$', suffix: '/bbl', decimals: 2, cat: 'energy'},
  { symbol: 'GCUSD',  label: 'Gold',        prefix: '$', suffix: '/oz',  decimals: 1, cat: 'metal' },
  { symbol: 'EURUSD', label: 'EUR/USD',     prefix: '',  suffix: '',     decimals: 4, cat: 'fx'    },
  { symbol: 'USDINR', label: 'USD/INR',     prefix: '₹', suffix: '',     decimals: 2, cat: 'em'    },
  { symbol: '^N225',  label: 'Nikkei 225',  prefix: '',  suffix: '',     decimals: 0, cat: 'index' },
  { symbol: '^FTSE',  label: 'FTSE 100',    prefix: '',  suffix: '',     decimals: 0, cat: 'index' },
];

/* ── Shared per-symbol quote + sparkline cache ────────────────
   Quotes: 30-min TTL. Sparklines: 12-h TTL (end-of-day data).
   The ticker, hero snapshot and Live Markets board all read this
   same cache, so overlapping symbols are fetched only once — which
   protects the 250-call/day FMP free-tier quota. */
const QUOTE_TTL = 30 * 60 * 1000;
const SPARK_TTL = 12 * 60 * 60 * 1000;
const _qMem = {}, _sMem = {};

function _cacheGet(store, key) {
  if (store[key]) return store[key];
  try { const c = JSON.parse(localStorage.getItem(key) || 'null'); if (c) store[key] = c; return c; }
  catch(e) { return null; }
}
function _cacheSet(store, key, data) {
  const rec = { ts: Date.now(), data };
  store[key] = rec;
  try { localStorage.setItem(key, JSON.stringify(rec)); } catch(e) {}
}

async function getQuote(symbol) {
  const key = 'rmq_' + symbol;
  const c = _cacheGet(_qMem, key);
  if (c && Date.now() - c.ts < QUOTE_TTL) return c.data;
  try {
    const r = await fetch(`${FMP}/quote?symbol=${encodeURIComponent(symbol)}&apikey=${FMP_KEY}`);
    const j = await r.json();
    const d = (Array.isArray(j) && j[0]) ? j[0] : null;
    if (d) { _cacheSet(_qMem, key, d); return d; }
  } catch(e) {}
  return c ? c.data : null;                 // stale fallback on failure
}
function getQuotes(symbols) { return Promise.all(symbols.map(getQuote)); }

async function getSparkline(symbol, points) {
  points = points || 7;
  const key = 'rms_' + symbol;
  const c = _cacheGet(_sMem, key);
  if (c && Date.now() - c.ts < SPARK_TTL) return c.data.slice(-points);
  try {
    const r = await fetch(`${FMP}/historical-price-eod/light?symbol=${encodeURIComponent(symbol)}&apikey=${FMP_KEY}`);
    const j = await r.json();
    if (Array.isArray(j) && j.length) {
      const arr = j.slice(0, 14).map(o => o.price).reverse();   // oldest → newest
      _cacheSet(_sMem, key, arr);
      return arr.slice(-points);
    }
  } catch(e) {}
  return c ? c.data.slice(-points) : null;
}

async function fetchTickerData() {
  return getQuotes(TICKER_INSTRUMENTS.map(i => i.symbol));
}

window.RM = { getQuote, getQuotes, getSparkline, fetchTickerData };
})();
