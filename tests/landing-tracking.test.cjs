const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const test = require('node:test');

const root = path.resolve(__dirname, '..');
const routes = [
  ['OSAT', 'landing/osat-route/osat-lot-test-traceability.html'],
  ['Fabless', 'landing/fabless-route/fabless-outsourced-wip.html'],
  ['Partner', 'landing/partner-route/semiconductor-erp-mes-ot.html'],
];

function harness(routePath, options = {}) {
  const html = fs.readFileSync(path.join(root, routePath), 'utf8');
  const scriptTags = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)];
  assert.equal(scriptTags.length, 1, `${routePath}: exactly one script block`);
  const script = scriptTags[0][1];
  assert.match(script, /^\s*\(function\s*\(/, `${routePath}: one top-level tracking IIFE`);
  assert.equal((script.match(/__dgwSectionTrackingInitialized/g) || []).length, 1, `${routePath}: one idempotent initializer`);
  assert.doesNotMatch(script, /page_view/i, `${routePath}: no inline page_view`);

  let now = 1000;
  class FakeDate extends Date {
    static now() { return now; }
  }
  class Element {
    constructor(attrs = {}) { this.attrs = attrs; this.listeners = {}; this.textContent = ''; this.style = {}; }
    getAttribute(name) { return this.attrs[name] ?? null; }
    addEventListener(name, fn) { (this.listeners[name] ||= []).push(fn); }
    fire(name) { for (const fn of this.listeners[name] || []) fn(); }
    setAttribute(name, value) { this.attrs[name] = value; }
    select() {}
  }

  const section = new Element({ 'data-section': 'hero' });
  const feedback = new Element();
  const copy = new Element({
    'data-copy': 'private-copy-value',
    'data-contact-type': 'email',
    'data-placement': 'contact',
    'data-segment': routePath.includes('osat-route') ? 'osat' : routePath.includes('fabless-route') ? 'fabless' : 'partner',
  });
  const cta = new Element({
    'data-osat-cta': routePath.includes('osat-route') ? 'hero' : null,
    'data-popup-trigger-status': 'pending',
  });
  let popupClickCalls = 0;
  const popupLookupIds = [];
  const popupTrigger = options.popupPresent === false ? null : { click() { popupClickCalls++; } };
  const documentListeners = {};
  const windowListeners = {};
  let hidden = false;
  let hasFocus = true;
  let copyResult = options.copyResult ?? 'resolve';
  let copyCalls = 0;
  const dataLayer = [];
  let observerCallback;
  let observerCount = 0;
  let observedRootMargin;

  const document = {
    get hidden() { return hidden; },
    hasFocus() { return hasFocus; },
    querySelectorAll(selector) {
      if (selector === '[data-section]') return [section];
      if (selector === '[data-copy]') return [copy];
      if (selector === '[data-consultation-cta]') return [cta];
      return [];
    },
    getElementById(id) { popupLookupIds.push(id); return id === 'OpenformWF2' ? popupTrigger : null; },
    querySelector(selector) { return selector === '[data-feedback]' ? feedback : null; },
    addEventListener(name, fn) { (documentListeners[name] ||= []).push(fn); },
    createElement() { return new Element(); },
    body: { appendChild() {}, removeChild() {} },
    execCommand() { return copyResult === 'exec-success'; },
  };
  const window = {
    dataLayer,
    addEventListener(name, fn) { (windowListeners[name] ||= []).push(fn); },
  };
  const navigator = {
    clipboard: {
      writeText() {
        copyCalls++;
        return copyResult === 'reject' ? Promise.reject(new Error('copy denied')) : Promise.resolve();
      },
    },
  };
  class IntersectionObserver {
    constructor(callback, config) { observerCount++; observerCallback = callback; observedRootMargin = config.rootMargin; }
    observe() {}
  }
  const context = vm.createContext({ window, document, navigator, IntersectionObserver, Date: FakeDate, Map, WeakSet, Promise });
  vm.runInContext(script, context, { filename: routePath });

  return {
    html, script, dataLayer, section, copy, cta, feedback, popupLookupIds,
    get copyCalls() { return copyCalls; },
    get popupClickCalls() { return popupClickCalls; },
    get observerCount() { return observerCount; },
    get observedRootMargin() { return observedRootMargin; },
    rerun() { vm.runInContext(script, context, { filename: routePath }); },
    setTime(value) { now = value; },
    intersect(isIntersecting) { observerCallback([{ target: section, isIntersecting }]); },
    blur() { hasFocus = false; for (const fn of windowListeners.blur || []) fn(); },
    focus() { hasFocus = true; for (const fn of windowListeners.focus || []) fn(); },
    hide() { hidden = true; for (const fn of documentListeners.visibilitychange || []) fn(); },
    show() { hidden = false; for (const fn of documentListeners.visibilitychange || []) fn(); },
    pagehide() { for (const fn of windowListeners.pagehide || []) fn(); },
    async copyClick(result) {
      copyResult = result;
      copy.fire('click');
      await Promise.resolve();
      await Promise.resolve();
    },
    clickCta() { cta.fire('click'); },
  };
}

for (const [name, routePath] of routes) {
  test(`${name}: initialization is idempotent`, () => {
    const h = harness(routePath);
    const before = h.observerCount;
    h.rerun();
    assert.equal(before, 1);
    assert.equal(h.observerCount, before);
    h.intersect(true);
    assert.equal(h.dataLayer.filter(e => e.event === 'section_view').length, 1);
  });

  test(`${name}: accumulates only effective-visible intervals and emits once on pagehide`, () => {
    const h = harness(routePath);
    assert.equal(h.observedRootMargin, '-45% 0px -45% 0px');

    h.setTime(1000);
    h.intersect(true);
    h.setTime(2500);
    h.intersect(false);
    h.setTime(5000); // Off-screen time is excluded.
    h.focus(); // Focus alone must not start an off-screen section.
    h.setTime(7000);
    h.intersect(true);
    h.intersect(true); // Re-entry cannot duplicate section_view.
    h.setTime(8500);
    h.blur();
    h.setTime(12000); // Blurred time is excluded.
    h.focus();
    h.setTime(12500);
    h.hide();
    h.setTime(13500); // Hidden time is excluded.
    h.show();
    h.setTime(14000);
    h.pagehide();
    h.pagehide();

    assert.equal(h.dataLayer.filter(e => e.event === 'section_view').length, 1);
    const engagement = h.dataLayer.filter(e => e.event === 'section_engagement_time');
    assert.equal(engagement.length, 1);
    assert.equal(engagement[0].engagement_seconds, 4); // 1.5s + 1.5s + 0.5s + 0.5s
  });

  test(`${name}: caps accumulated engagement at one hour`, () => {
    const h = harness(routePath);
    h.setTime(1000);
    h.intersect(true);
    h.setTime(3_700_001);
    h.pagehide();
    assert.equal(h.dataLayer.find(e => e.event === 'section_engagement_time').engagement_seconds, 3600);
  });

  test(`${name}: emits only the safe copied_contact payload after successful copy`, async () => {
    const h = harness(routePath);
    await h.copyClick('resolve');
    const events = h.dataLayer.filter(e => e.event === 'copied_contact');
    assert.equal(events.length, 1);
    assert.deepEqual(Object.keys(events[0]).sort(), ['contact_type', 'event', 'placement', 'segment']);
    assert.equal(events[0].contact_type, 'email');
    assert.equal(events[0].placement, 'contact');
    assert.equal(events[0].segment, routePath.includes('osat-route') ? 'osat' : routePath.includes('fabless-route') ? 'fabless' : 'partner');
    assert.equal(JSON.stringify(events[0]).includes('private-copy-value'), false);
    assert.equal(h.copyCalls, 1);
  });

  test(`${name}: failed copy announces failure and emits no success event`, async () => {
    const h = harness(routePath);
    await h.copyClick('reject');
    assert.equal(h.dataLayer.filter(e => e.event === 'copied_contact').length, 0);
    assert.match(h.feedback.textContent, /Không copy được/);
  });

  test(`${name}: consultation CTA opens the LadiPage-owned popup trigger once`, () => {
    const h = harness(routePath);
    assert.match(h.html, /<button[^>]*data-consultation-cta[^>]*data-popup-trigger-status="pending"/i);
    assert.equal((h.html.match(/<button[^>]*data-consultation-cta/gi) || []).length, 1);
    assert.doesNotMatch(h.html, /<form\b/i);
    assert.doesNotMatch(h.script, /accepted_form/i);
    h.clickCta();
    assert.deepEqual(h.popupLookupIds, ['OpenformWF2']);
    assert.equal(h.popupClickCalls, 1);
    assert.equal(h.cta.getAttribute('data-popup-trigger-status'), 'clicked');
    const ctaEvents = h.dataLayer.filter(e => /cta_click$/.test(e.event));
    if (routePath.includes('osat-route')) {
      assert.deepEqual(ctaEvents.map(e => ({ ...e })), [{ event: 'osat_cta_click', cta_location: 'hero' }]);
    } else {
      assert.deepEqual(ctaEvents, []);
    }
    assert.equal(h.dataLayer.some(e => e.event === 'accepted_form'), false);
  });

  test(`${name}: absent popup trigger fails safely`, () => {
    const h = harness(routePath, { popupPresent: false });
    assert.doesNotThrow(() => h.clickCta());
    assert.deepEqual(h.popupLookupIds, ['OpenformWF2']);
    assert.equal(h.popupClickCalls, 0);
    assert.equal(h.cta.getAttribute('data-popup-trigger-status'), 'missing');
    const ctaEvents = h.dataLayer.filter(e => /cta_click$/.test(e.event));
    if (routePath.includes('osat-route')) {
      assert.deepEqual(ctaEvents.map(e => ({ ...e })), [{ event: 'osat_cta_click', cta_location: 'hero' }]);
    } else {
      assert.deepEqual(ctaEvents, []);
    }
    assert.equal(h.dataLayer.some(e => e.event === 'accepted_form'), false);
  });
}
