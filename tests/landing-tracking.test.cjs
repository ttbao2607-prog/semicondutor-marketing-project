const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const test = require('node:test');
const root = path.resolve(__dirname, '..');
const routes = [
  { name: 'OSAT', file: 'landing/osat-route/osat-lot-test-traceability.html', sections: ['top','operations-questions','lot-map','management-layers','cas-ic-case','industry-delivery','resources'], ctas: ['osat-cta-header','osat-cta-terminal'] },
  { name: 'Fabless', file: 'landing/fabless-route/fabless-outsourced-popupx-basic-flat.html', sections: ['top','operations-questions','fabless-map','management-layers','relationship-proof','bright-power-case','industry-delivery','resources'], ctas: ['fabless-cta-header','fabless-cta-terminal'] },
  { name: 'Supplier/Partner', file: 'landing/partner-route/supplier-ecosystem-flat.html', sections: ['top','audience-context','ecosystem-architecture','operations-questions','product-evidence','supply-chain','local-delivery','resources'], ctas: ['partner-cta-hero','partner-cta-architecture'] },
];
function setup(route) {
  const html = fs.readFileSync(path.join(root, route.file), 'utf8');
  const match = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)].find(([, body]) => body.includes('__dgwAwarenessSectionInitV1'));
  assert.ok(match, `${route.name}: route initializer exists`);
  const script = match[1];
  let time = 1000, hidden = false, focused = true;
  const elements = new Map(route.sections.map(id => [id, { id }]));
  const observers = [], docEvents = {}, winEvents = {}, dataLayer = [];
  const document = {
    get hidden() { return hidden; }, hasFocus: () => focused,
    getElementById: id => elements.get(id) || null,
    addEventListener: (name, fn) => (docEvents[name] ||= []).push(fn),
  };
  const window = { dataLayer, addEventListener: (name, fn) => (winEvents[name] ||= []).push(fn) };
  class IO { constructor(cb, options) { this.cb = cb; this.options = options; observers.push(this); } observe(el) { (this.targets ||= []).push(el); } }
  class FakeDate extends Date { static now() { return time; } }
  const context = vm.createContext({ window, document, IntersectionObserver: IO, Date: FakeDate, Map, Array, Object, Math });
  const run = () => vm.runInContext(script, context, { filename: route.file });
  run();
  return {
    html, script, dataLayer, observers, docEvents, winEvents,
    setTime: n => { time = n; },
    intersect(id, isIntersecting = true) { observers[0].cb([{ target: elements.get(id), isIntersecting }]); },
    hidden(value) { hidden = value; for (const fn of docEvents.visibilitychange || []) fn(); },
    focused(value) { focused = value; for (const fn of winEvents[value ? 'focus' : 'blur'] || []) fn(); },
    fire(name) { for (const fn of winEvents[name] || []) fn(); },
    rerun: run,
  };
}
for (const route of routes) {
  test(`${route.name}: exact IDs, idempotency, observer band and unique view`, () => {
    const h = setup(route);
    assert.equal(h.observers.length, 1);
    assert.deepEqual({ ...h.observers[0].options }, { threshold: 0, rootMargin: '-45% 0px -45% 0px' });
    assert.deepEqual(h.observers[0].targets.map(e => e.id), route.sections);
    h.rerun(); assert.equal(h.observers.length, 1);
    h.hidden(true); h.intersect('top'); assert.equal(h.dataLayer.length, 0);
    h.hidden(false); assert.deepEqual(h.dataLayer.map(x => x.event), ['section_view']);
    h.intersect('top', false); h.intersect('top');
    assert.equal(h.dataLayer.filter(x => x.event === 'section_view').length, 1);
    assert.deepEqual(Object.keys(h.dataLayer[0]).sort(), ['event','section_name']);
    assert.equal(h.dataLayer[0].section_name, 'top');
  });
  test(`${route.name}: visible and focused intervals only; pagehide flushes once with bounded integer`, () => {
    const h = setup(route);
    h.setTime(1000); h.intersect('top'); // initially active
    h.setTime(2500); h.focused(false);
    h.setTime(7000); h.focused(true); // 1.5 sec accumulated; resumes
    h.setTime(8000); h.hidden(true);
    h.setTime(12000); h.hidden(false); // 2.5 sec accumulated
    h.setTime(13000); h.intersect('top', false);
    h.setTime(18000); h.intersect('top'); // resume
    h.setTime(19000); h.fire('pagehide'); h.fire('pagehide');
    const events = h.dataLayer.filter(x => x.event === 'section_engagement_time');
    assert.equal(events.length, 1);
    assert.deepEqual(Object.keys(events[0]).sort(), ['engagement_seconds','event','section_name']);
    assert.equal(events[0].section_name, 'top');
    assert.equal(events[0].engagement_seconds, 4);
    assert.ok(Number.isInteger(events[0].engagement_seconds) && events[0].engagement_seconds >= 1 && events[0].engagement_seconds <= 3600);
    h.setTime(30000); h.intersect('operations-questions'); h.setTime(40000); h.fire('pagehide');
    assert.equal(h.dataLayer.filter(x => x.event === 'section_engagement_time').length, 1);
  });
  test(`${route.name}: one-hour cap and sub-second interval omitted`, () => {
    const h = setup(route); h.setTime(1000); h.intersect('top'); h.setTime(9_000_000); h.fire('pagehide');
    assert.equal(h.dataLayer.find(x => x.event === 'section_engagement_time').engagement_seconds, 3600);
    const short = setup(route); short.intersect('top'); short.setTime(1500); short.fire('pagehide');
    assert.equal(short.dataLayer.some(x => x.event === 'section_engagement_time'), false);
  });
  test(`${route.name}: inert CTAs and allowlist N/A produce no other tracking`, () => {
    const h = setup(route);
    assert.doesNotMatch(h.html, /semiconductor_content_click|potential_viewer|osat_cta_click|accepted_form|page_view|OpenformWF2|PopupX|navigator\.clipboard|fetch\s*\(/i);
    const buttons = [...h.html.matchAll(/<button\b[^>]*id="([^"]+)"[^>]*>/gi)].map(([, id]) => id).filter(id => route.ctas.includes(id));
    assert.deepEqual(buttons, route.ctas);
    for (const id of route.ctas) {
      const tag = h.html.match(new RegExp(`<button\\b[^>]*id="${id}"[^>]*>`, 'i'))?.[0] || '';
      assert.match(tag, /type="button"/i);
      assert.doesNotMatch(tag, /onclick|data-ldp-native-form-popup-trigger|data-popup/i);
    }
    h.intersect('resources'); h.fire('pagehide');
    assert.ok(h.dataLayer.every(event => ['section_view','section_engagement_time'].includes(event.event)));
    assert.ok(h.dataLayer.every(event => Object.keys(event).every(k => ['event','section_name','engagement_seconds'].includes(k))));
  });
}
