'use strict';
const publicContent=__PUBLIC__, config=__CONFIG__, articles=__ARTICLES__;
let current, renderedLocale;
function show(state,scroll,focusSection=false){
  const active=document.activeElement;
  const restoreSelect=active && active.id==='source-language';
  current=state;
  const article=document.querySelector('article'),error=document.querySelector('.unavailable');
  article.hidden=!state.ok;error.hidden=state.ok;
  const notice=document.querySelector('.notice');
  if(!state.ok){notice.hidden=true;notice.textContent='';document.querySelectorAll('[data-locale]').forEach(b=>b.disabled=true);return;}
  document.querySelectorAll('[data-locale]').forEach(b=>b.disabled=false);
  const c=publicContent.locales[state.locale];
  if(renderedLocale!==state.locale){
    article.innerHTML=articles[state.locale];renderedLocale=state.locale;
    if(restoreSelect)document.getElementById('source-language').focus({preventScroll:true});
  }
  document.documentElement.lang=state.locale;document.title=c.title+' · Digiwin';
  document.querySelector('.skip').textContent=c.skip;
  document.querySelector('.languages').setAttribute('aria-label',c.language_label);
  document.querySelectorAll('[data-locale]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.locale===state.locale)));
  notice.hidden=!state.fallback;notice.textContent=state.fallback?c[state.fallback]:'';
  if(focusSection){const target=document.getElementById(state.section);if(target){target.setAttribute('tabindex','-1');target.focus({preventScroll:true});}}
  if(scroll)requestAnimationFrame(()=>{const target=document.getElementById(state.section);if(target)target.scrollIntoView({behavior:'instant',block:'start'});});
}
function toggle(locale,section){const next=CaseRoute.toggle(location.href,locale,config,section);if(next){history.pushState(null,'',next.url);show(next,true);}}
document.addEventListener('click',event=>{
  const button=event.target.closest('[data-locale]');if(button){toggle(button.dataset.locale,current.section);return;}
  const anchor=event.target.closest('.article-nav a, .skip');
  if(!anchor || event.button>0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey)return;
  const href=anchor.getAttribute('href');if(!href || !href.startsWith('#'))return;
  const next=CaseRoute.toggle(location.href,current.locale,config,href.slice(1));
  if(!next || next.section!==href.slice(1))return;
  event.preventDefault();history.pushState(null,'',next.url);show(next,true,true);
});
document.addEventListener('change',event=>{if(event.target.id==='source-language')toggle(event.target.value,'source');});
window.addEventListener('popstate',()=>{const active=document.activeElement;const control=active && (active.id==='source-language' || active.closest('[data-locale]'));show(CaseRoute.resolve(location.href,config),true,!control);});
window.addEventListener('hashchange',()=>{const state=CaseRoute.resolve(location.href,config);if(state.ok)history.replaceState(null,'',state.url);const active=document.activeElement;const control=active && (active.id==='source-language' || active.closest('[data-locale]'));show(state,false,!control);});
const initial=CaseRoute.resolve(location.href,config);if(initial.ok)history.replaceState(null,'',initial.url);show(initial,initial.ok&&initial.section!=='case-summary');
