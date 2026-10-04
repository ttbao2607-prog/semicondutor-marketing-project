(function(root){
  'use strict';
  function resolve(raw, config) {
    const url = new URL(raw, 'http://localhost');
    const controls = ['entry', 'case', 'contract', 'lang', 'section'];
    for (const key of controls) if (url.searchParams.getAll(key).length > 1) return {ok:false, reason:'duplicate-control'};
    const identity = ['entry','case','contract'];
    const noIdentity = identity.every(key => !url.searchParams.has(key));
    if (noIdentity) {
      url.searchParams.set('entry', config.default_entry);
      url.searchParams.set('case', config.case_id);
      url.searchParams.set('contract', config.release_id);
    } else if (identity.some(key => !url.searchParams.has(key))) return {ok:false, reason:'incomplete-identity'};
    const entry = url.searchParams.get('entry');
    const compatibility=(config.compatibility||[]).find(binding=>binding.entry===entry && binding.case===url.searchParams.get('case') && binding.contract===url.searchParams.get('contract') && binding.maps_to_release===config.release_id);

    if (!config.entries.includes(entry) || url.searchParams.get('case') !== config.case_id || (url.searchParams.get('contract') !== config.release_id && !compatibility)) return {ok:false, reason:'unavailable-identity'};
    let hash;
    try { hash = decodeURIComponent(url.hash.slice(1)); } catch (_) { return {ok:false, reason:'invalid-section'}; }
    const querySection = url.searchParams.get('section');
    if (querySection !== null && hash && querySection !== hash) return {ok:false, reason:'conflicting-section'};
    const section = querySection || hash || 'case-summary';
    if (!config.sections.includes(section)) return {ok:false, reason:'invalid-section'};
    url.searchParams.delete('section');
    url.hash = section;
    const requested = url.searchParams.get('lang');
    const known = ['vi','en','zh-Hans','zh-Hant'];
    const locale = config.ready_locales.includes(requested) ? requested : 'vi';
    const fallback = requested === locale ? null : (known.includes(requested) ? 'pending' : 'fallback');
    url.searchParams.set('lang', locale);
    return {ok:true,url:url.href,entry,case_id:config.case_id,release_id:config.release_id,input_contract:url.searchParams.get('contract'),locale,section,fallback};
  }
  function toggle(raw, locale, config, section) {
    const current = resolve(raw, config);
    if (!current.ok || !config.ready_locales.includes(locale)) return null;
    const url = new URL(current.url);
    url.searchParams.set('lang',locale);
    if (section && config.sections.includes(section)) url.hash = section;
    return resolve(url.href,config);
  }
  const api = {resolve,toggle};
  if (typeof module !== 'undefined' && module.exports) module.exports=api;
  else root.CaseRoute=api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
