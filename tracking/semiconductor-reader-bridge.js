/* Reader adapter: Blogspot-Digiwin 6802942 bridge contract, website stream only. */
(function (w, d) {
  'use strict';
  if (w.DWSemiconductorBridge) return;
  var VERSION = 'semiconductor_bridge_v1_20261028';
  var MID = 'G-MV5QWN0XVM';
  var fields = ['bridge_source', 'bridge_medium', 'bridge_campaign', 'bridge_campaign_id',
    'bridge_ad_id', 'bridge_adset_id', 'bridge_card', 'bridge_lane', 'creative_version'];
  function safe(value) {
    return typeof value === 'string' && /^[a-zA-Z0-9_-]{1,100}$/.test(value) ? value : '';
  }
  function context(search) {
    var p = new URLSearchParams(search), out = {};
    fields.forEach(function (key) { out[key] = safe(p.get(key) || ''); });
    out.bridge_source = safe(p.get('utm_source') || '');
    out.bridge_medium = safe(p.get('utm_medium') || '');
    out.bridge_campaign = safe(p.get('utm_campaign') || '');
    out.bridge_campaign_id = safe(p.get('utm_id') || '');
    // No assumed paid source/lane for a direct or unlabelled visit.
    if (!out.bridge_lane && out.bridge_source && /_rmk_/.test(out.bridge_campaign)) out.bridge_lane = 'rmk';
    if (!out.bridge_lane && out.bridge_source && /_cold_/.test(out.bridge_campaign)) out.bridge_lane = 'cold';
    if (!out.bridge_card) out.bridge_card = safe(p.get('utm_content') || '');
    return out;
  }
  function decorate(raw, ctx, now, treatment, locale) {
    try {
      var u = new URL(raw, w.location.href);
      if (u.protocol !== 'https:' || u.hostname !== 'www.digiwin.com.vn' || u.pathname !== '/contact-vn/') return raw;
      // Acquisition belongs to ad -> reader, not an internal UTM campaign.
      ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'utm_id'].forEach(function (key) { u.searchParams.delete(key); });
      u.searchParams.set('bridge_origin', 'semiconductor_reader');
      u.searchParams.set('bridge_ts', String(now));
      fields.forEach(function (key) {
        var value = safe(ctx[key] || '');
        if (value) u.searchParams.set(key, value); else u.searchParams.delete(key);
      });
      u.searchParams.set('bridge_treatment', safe(treatment));
      u.searchParams.set('bridge_locale', safe(locale));
      return u.href;
    } catch (_) { return raw; }
  }
  function acquisitionURL() {
    var original = new URL(w.location.href), clean = new URL(original.origin + original.pathname);
    ['t', 'treatment', 'lang', 'locale', 'entry', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'utm_id'].forEach(function (key) {
      var value = safe(original.searchParams.get(key) || '');
      if (value) clean.searchParams.set(key, value);
    });
    return clean.href;
  }
  function route() {
    var reader = w.unifiedReader;
    return reader ? {t: reader.getTreatment(), lang: reader.getLocale()} : {t: '', lang: d.documentElement.lang};
  }
  function refreshLink() {
    var a = d.getElementById('partner-contact-cta');
    if (!a) return;
    var r = route();
    a.href = decorate('https://www.digiwin.com.vn/contact-vn/', context(w.location.search), Date.now(), r.t, r.lang);
  }
  function start() {
    if (w.location.hostname !== 'solutions.digiwin.com.vn' || w.location.pathname !== '/semiconductor-case-reader') return;
    if (w.DWSemiconductorBridge.started) return;
    w.DWSemiconductorBridge.started = true;
    // One Google tag config owns automatic page_view and native engagement.
    // No manual page_view, GTM container, second event receiver, or consent override.
    w.dataLayer = w.dataLayer || [];
    w.gtag = w.gtag || function () { w.dataLayer.push(arguments); };
    var config = context(w.location.search);
    config.cookie_domain = 'digiwin.com.vn';
    config.page_location = acquisitionURL();
    w.gtag('js', new Date());
    w.gtag('config', MID, config);
    var loader = d.createElement('script');
    loader.async = true;
    loader.src = 'https://www.googletagmanager.com/gtag/js?id=' + MID;
    d.head.appendChild(loader);
    refreshLink();
    var root = d.getElementById('app-main');
    if (root) new MutationObserver(refreshLink).observe(root, {childList: true});
    function activate(e) {
      if (e.type === 'keydown' && e.key !== 'Enter') return;
      var el = e.target && e.target.closest && e.target.closest('#partner-contact-cta');
      if (el) refreshLink();
    }
    ['pointerdown', 'click', 'auxclick', 'contextmenu', 'keydown'].forEach(function (name) {
      d.addEventListener(name, activate, true);
    });
  }
  w.DWSemiconductorBridge = {version: VERSION, context: context, decorate: decorate, start: start};
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', start, {once: true});
  else start();
})(window, document);
