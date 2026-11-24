/* ==========================================================================
   Baraza All Services — scripts du site
   - Mode clair / sombre
   - Langue (français / anglais)
   - Affichage des prix dans la devise du visiteur (base : USD)
   - Menu mobile, onglets, choix d'une offre, animations
   - Moyens de paiement, copie des coordonnées bancaires
   - Formulaire de devis : Netlify Forms, sinon WhatsApp
   Les textes sont dans js/i18n.js, la configuration dans js/config.js
   (tous deux générés par python/construire_site.py).
   ========================================================================== */
(function () {
  'use strict';

  var CONFIG = window.SITE_CONFIG || {};
  var I18N = window.I18N || {};
  var root = document.documentElement;
  var LANGS = ['fr', 'en'];

  function store(key, value) {
    try {
      if (value === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, value);
    } catch (e) { return null; }
    return null;
  }

  /* ======================= Langue ======================= */
  var lang = LANGS.indexOf(root.lang) >= 0 ? root.lang : 'fr';

  function tr(key) {
    var dict = I18N[lang] || {};
    return dict[key] !== undefined ? dict[key] : (I18N.fr || {})[key] || '';
  }

  function applyLanguage(newLang) {
    lang = newLang;
    root.lang = lang;
    store('lang', lang);
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var v = tr(el.getAttribute('data-i18n'));
      if (v) el.textContent = v;
    });
    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
      var v = tr(el.getAttribute('data-i18n-html'));
      if (v) el.innerHTML = v;   // contenu fixe généré par le site, pas de saisie utilisateur
    });
    document.querySelectorAll('[data-i18n-attr]').forEach(function (el) {
      el.getAttribute('data-i18n-attr').split(';').forEach(function (pair) {
        var p = pair.split(':');
        var v = tr(p[1]);
        if (v) el.setAttribute(p[0], v);
      });
    });
    var hidden = document.getElementById('langue');
    if (hidden) hidden.value = lang;
    updateThemeLabel();
    updateNavLabel();
    renderCurrencyOptions();
    renderPrices();
  }

  document.getElementById('lang-toggle').addEventListener('click', function () {
    applyLanguage(lang === 'fr' ? 'en' : 'fr');
  });

  /* ======================= Thème ======================= */
  var themeBtn = document.getElementById('theme-toggle');
  var themeMeta = document.querySelector('meta[name="theme-color"]');

  function updateThemeLabel() {
    var dark = root.getAttribute('data-theme') === 'dark';
    themeBtn.setAttribute('aria-label', tr(dark ? 'ui.theme_light' : 'ui.theme_dark'));
    themeBtn.setAttribute('title', tr(dark ? 'ui.theme_light' : 'ui.theme_dark'));
    if (themeMeta) themeMeta.setAttribute('content', dark ? '#070d1a' : '#f7faff');
  }

  themeBtn.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    store('theme', next);
    updateThemeLabel();
  });

  /* ======================= Devises ======================= */
  var rates = CONFIG.fallbackRates || { USD: 1 };
  var currency = store('currency') || 'USD';
  if (!rates[currency]) currency = 'USD';
  var selects = document.querySelectorAll('[data-currency-select]');

  function renderCurrencyOptions() {
    selects.forEach(function (sel) {
      Array.prototype.forEach.call(sel.options, function (opt) {
        var c = (CONFIG.currencies || []).filter(function (x) { return x.code === opt.value; })[0];
        if (c) opt.textContent = c.code + ' — ' + c[lang];
      });
      sel.value = currency;
    });
  }

  function formatMoney(usd) {
    var value = usd * (rates[currency] || 1);
    // Arrondi lisible : unités pour les petites devises, dizaines/centaines pour les grandes
    if (value >= 100000) value = Math.round(value / 1000) * 1000;
    else if (value >= 10000) value = Math.round(value / 100) * 100;
    else if (value >= 1000 && currency !== 'USD') value = Math.round(value / 10) * 10;
    else value = Math.round(value);
    var locale = lang === 'fr' ? 'fr-FR' : 'en-US';
    var text;
    try {
      text = new Intl.NumberFormat(locale, {
        style: 'currency', currency: currency, currencyDisplay: 'narrowSymbol', maximumFractionDigits: 0
      }).format(value);
    } catch (e) {
      text = value.toLocaleString(locale) + ' ' + currency;
    }
    // Symbole « $ » seul ambigu pour CAD : on précise le code
    if (currency === 'CAD') text = text.replace('$', 'CA$');
    return (currency === 'USD' ? '' : '≈ ') + text;
  }

  function renderPrices() {
    document.querySelectorAll('.money').forEach(function (el) {
      el.textContent = formatMoney(parseFloat(el.getAttribute('data-usd')));
    });
    var hidden = document.getElementById('devise');
    if (hidden) hidden.value = currency;
  }

  selects.forEach(function (sel) {
    sel.addEventListener('change', function () {
      currency = sel.value;
      store('currency', currency);
      renderCurrencyOptions();
      renderPrices();
    });
  });

  // Taux du jour (gratuit, sans clé). En cas d'échec, les taux de secours restent utilisés.
  function loadRates() {
    var cached = null;
    try { cached = JSON.parse(store('rates') || 'null'); } catch (e) { cached = null; }
    if (cached && Date.now() - cached.time < 12 * 3600 * 1000) {
      rates = Object.assign({}, rates, cached.rates);
      renderPrices();
      return;
    }
    if (!CONFIG.ratesUrl || !window.fetch) return;
    fetch(CONFIG.ratesUrl).then(function (r) { return r.json(); }).then(function (data) {
      if (!data || !data.rates) return;
      var keep = {};
      Object.keys(rates).forEach(function (c) { if (data.rates[c]) keep[c] = data.rates[c]; });
      rates = Object.assign({}, rates, keep);
      store('rates', JSON.stringify({ time: Date.now(), rates: keep }));
      renderPrices();
    }).catch(function () { /* taux de secours */ });
  }

  /* ======================= Menu mobile ======================= */
  var header = document.querySelector('.site-header');
  var navBtn = document.querySelector('.nav-toggle');

  function updateNavLabel() {
    navBtn.setAttribute('aria-label', tr(header.classList.contains('is-open') ? 'ui.menu_close' : 'ui.menu_open'));
  }
  function setNav(open) {
    header.classList.toggle('is-open', open);
    navBtn.setAttribute('aria-expanded', String(open));
    updateNavLabel();
  }
  navBtn.addEventListener('click', function () { setNav(!header.classList.contains('is-open')); });
  document.querySelectorAll('.main-nav a').forEach(function (a) {
    a.addEventListener('click', function () { setNav(false); });
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setNav(false); });

  /* ======================= Onglets ======================= */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tabs__btn'));
  var panels = document.querySelectorAll('.tabs__panel');
  function showTab(i) {
    tabs.forEach(function (t, j) {
      var on = i === j;
      t.classList.toggle('is-active', on);
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      panels[j].hidden = !on;
    });
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { showTab(i); });
    t.addEventListener('keydown', function (e) {
      var n = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
      if (n === undefined) return;
      e.preventDefault();
      n = (n + tabs.length) % tabs.length;
      showTab(n);
      tabs[n].focus();
    });
  });

  /* ======================= Choix d'une offre ======================= */
  var offerSelect = document.getElementById('offer');
  document.querySelectorAll('[data-offer]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      offerSelect.value = btn.getAttribute('data-offer');
      document.getElementById('devis').scrollIntoView({ behavior: 'smooth' });
      setTimeout(function () { document.getElementById('name').focus({ preventScroll: true }); }, 700);
    });
  });
  var params = new URLSearchParams(window.location.search);
  if (params.get('offre')) offerSelect.value = params.get('offre');

  /* ======================= Paiement ======================= */
  function waUrl(text) {
    return 'https://wa.me/' + (CONFIG.whatsapp || '') + (text ? '?text=' + encodeURIComponent(text) : '');
  }
  document.querySelectorAll('[data-pay]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      if (btn.getAttribute('data-pay-link')) return; // lien du prestataire configuré
      e.preventDefault();
      var method = btn.closest('.pay-card').querySelector('h3').textContent;
      window.open(waUrl(tr('payment.wa_message') + ' ' + method + ' (' + currency + ').'), '_blank', 'noopener');
    });
  });

  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var value = btn.getAttribute('data-copy');
      var done = function () {
        btn.classList.add('is-copied');
        btn.setAttribute('aria-label', tr('ui.copied'));
        setTimeout(function () { btn.classList.remove('is-copied'); btn.setAttribute('aria-label', tr('ui.copy')); }, 1500);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(value).then(done, function () {});
      else {
        var ta = document.createElement('textarea');
        ta.value = value; document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); done(); } catch (err) { /* ignore */ }
        ta.remove();
      }
    });
  });

  /* ======================= Animations ======================= */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ======================= Formulaire de devis ======================= */
  var form = document.getElementById('form-devis');
  var alertBox = document.getElementById('form-alert');
  var rules = [
    ['name', function (el) { return el.value.trim() !== ''; }, 'quote.err_name'],
    ['email', function (el) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value.trim()); }, 'quote.err_email'],
    ['offer', function (el) { return el.value !== ''; }, 'quote.err_offer'],
    ['message', function (el) { return el.value.trim().length >= 10; }, 'quote.err_message'],
    ['consent', function (el) { return el.checked; }, 'quote.err_consent']
  ];

  function clearErrors() {
    form.querySelectorAll('.field__errors').forEach(function (n) { n.remove(); });
    form.querySelectorAll('.field--error').forEach(function (n) { n.classList.remove('field--error'); });
  }
  function validate() {
    var ok = true;
    rules.forEach(function (r) {
      var el = document.getElementById(r[0]);
      if (!r[1](el)) {
        ok = false;
        var row = el.closest('.field');
        row.classList.add('field--error');
        var ul = document.createElement('ul');
        ul.className = 'field__errors';
        var li = document.createElement('li');
        li.textContent = tr(r[2]);
        ul.appendChild(li);
        row.appendChild(ul);
      }
    });
    return ok;
  }
  function showAlert(text) {
    alertBox.className = 'alert alert--success';
    alertBox.textContent = text;
    alertBox.hidden = false;
    alertBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
  function quoteText() {
    var v = function (id) { return document.getElementById(id).value.trim(); };
    return tr('quote.wa_intro') + '\n\n' +
      tr('quote.f_name') + ' : ' + v('name') + '\n' +
      tr('quote.f_email') + ' : ' + v('email') + '\n' +
      tr('quote.f_phone') + ' : ' + (v('phone') || '—') + '\n' +
      tr('quote.f_company') + ' : ' + (v('company') || '—') + '\n' +
      tr('quote.f_country') + ' : ' + (v('country') || '—') + '\n' +
      tr('quote.f_offer') + ' : ' + offerSelect.options[offerSelect.selectedIndex].text + '\n' +
      tr('ui.currency') + ' : ' + currency + '\n\n' +
      tr('quote.f_message') + ' : ' + v('message');
  }

  // Le formulaire n'existe que sur la page d'accueil (pas sur les pages légales)
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    clearErrors();
    if (!validate()) {
      form.querySelector('.field--error').scrollIntoView({ behavior: 'smooth', block: 'center' });
      return;
    }
    var button = form.querySelector('button[type=submit]');
    var name = document.getElementById('name').value.trim();
    var message = quoteText();
    button.disabled = true;

    fetch('/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(new FormData(form)).toString()
    }).then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      form.reset();
      showAlert(tr('quote.ok_sent').replace('{name}', name));
    }).catch(function () {
      // Hébergement sans gestion de formulaire (Firebase, test local) : WhatsApp.
      showAlert(tr('quote.ok_whatsapp').replace('{name}', name));
      window.open(waUrl(message), '_blank', 'noopener');
    }).then(function () {
      button.disabled = false;
    });
  });

  /* ======================= Démarrage ======================= */
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
  applyLanguage(lang);
  loadRates();
})();
