# Semiconductor Tracking Contract

**Status:** contract draft; dataLayer semantics are candidates until direct GTM/GA4 inventory and QA. No new container/property/event is authorized by this file.

## Local technical-document inventory boundary

- Read-only review of `digiwin_master_tracking_system.md`, `digiwin_gtm_governance_standard.md`, `digiwin_industry_landing_tracking.md`, and `digiwin_legacy_ldp_funnel_tracking.md` found dated documentation from 2026-07-09/10. This is documentary/historical evidence, not live GTM, GA4, LadiPage, consent, tag, trigger, or publication verification.
- The technical docs describe shared `section_view` and `section_engagement_time` event names with `section_name` and `engagement_seconds`; the current route contract retains hidden/unfocused-time exclusion and the 3600-second cap. This does not establish that shared tags are currently wired or deduplicated for these routes.
- `page_view` remains externally/global-tag owned; route HTML must not emit an inline `page_view`.
- The documented `industry_*` event family and its `industry` parameter belong to a separate eight-industry system. Do not automatically apply that taxonomy or parameter to the OSAT, Fabless, or Partner routes.

## Global rules

- Global `page_view` remains owned by the existing global tag; no inline `page_view`.
- Reuse `section_view` with `section_name`.
- Reuse `section_engagement_time` with `section_name`, `engagement_seconds`, capped at `<=3600`.
- Observer root margin: `-45% 0px -45% 0px`.
- Effective visibility: pause timing on `visibilitychange` and `blur`; resume only on `focus` and visible state; flush on `pagehide`.
- Initializer and listeners must be idempotent; one-time section view and duplicate prevention are required.
- UTM/gclid remain in the URL. No redirect or handoff exists in these offline pages.
- No arbitrary analytics payload, copied contact value, phone, email or address is transmitted.
- Each route has exactly two primary consultation buttons: one in the hero and one in the terminal contact band. Both invoke the external `OpenformWF2` trigger when present; neither implies popup display or form acceptance.

## Route-specific semantics

- OSAT may retain the existing candidate `osat_cta_click` with exactly `cta_location`, recording CTA intent only. The hero button sends `hero`; the terminal button sends `terminal`. Do not rename its event or parameter.
- `osat_cta_click` is a local OSAT candidate only; the reviewed technical-document inventory does not substantiate it or show that it is wired in GTM/GA4.
- Fabless and Partner emit no CTA analytics event until actual GTM/container inventory authorizes reuse of an existing event. Do not create a shared CTA taxonomy for these routes.
- The CTA handler looks up the LadiPage-owned `OpenformWF2` trigger through `document.getElementById('OpenformWF2')` and calls its `click()` method when available. The trigger is configured outside the imported HTML. If absent, the CTA must not throw or navigate; it records the local `data-popup-trigger-status="missing"` state.
- A trigger click records no popup-open confirmation, form submission, lead, or conversion.
- Imported HTML contains no visible or hidden form and emits none of `Ladi_form_success`, `generate lead` (space), or `accepted_form`. The reviewed legacy docs describe `Ladi_form_success` as an internal LadiPage event and report a GA4 event named `generate lead`; its proposed direct-LadiPage source was historically inferred, not verified in this inventory. The sources do not substantiate `accepted_form`. Determine the actual successful-submit event and owner through current LadiPage/editor and live GTM/GA4 inventory; do not rename or synthesize it. A CTA/`OpenformWF2` click is only popup intent, not popup-open, submission, lead, or conversion.
- The route HTML's `copied_contact` is a local success-only candidate with exactly `contact_type`, `placement`, and `segment`; the copied value is never included. It is not verified as wired in GTM/GA4. The legacy docs separately describe an all-pages copy listener emitting `text_copy` with `copied_text`, followed by `contact_info_copy` carrying copied content. That legacy behavior is privacy-incompatible with this route contract: do not rename, alias, or treat these events as equivalent. Verify live listener/tag/trigger collisions and deduplication before production.
- The landing page itself has no form; a LadiPage-configured popup may display its own form only after the consultation CTA is activated.
- `section_view` and `section_engagement_time` are reused candidates, not implementation authorization.

## LadiPage popup binding boundary

- After importing a route, configure the approved LadiPage-native popup separately and bind its existing opener/trigger element to the exact DOM ID `OpenformWF2` using the supported LadiPage UI.
- Do not add a form, hidden trigger, fake form target, API, or platform-specific code to the imported page. Do not rewrite the URL or add UTM parameters as part of this trigger pattern.
- If LadiPage cannot expose a document-level trigger with this ID through supported configuration, stop and escalate; do not invent a substitute integration.
- In editor preview, verify the page has no embedded form, the external trigger is present, one CTA click invokes that trigger once, and the popup behavior is visually correct. A missing trigger must leave the page in place with status `missing` and no exception.
- The runtime status `clicked` means only that the configured DOM trigger's `click()` method was invoked. It does not assert that the popup appeared or that a form was accepted.

## Contact-copy behavior

The visible block uses verified company-controlled public contact values. Copy success is announced accessibly and then emits only the allowed event parameters. Copy failure announces a safe retry path without emitting success.

## QA matrix

| Planned acceptance case | Desktop | Mobile | Required result |
|---|---|---|---|
| First section enters effective viewport | REQUIRED/PENDING | REQUIRED/PENDING | One `section_view` only |
| Section enters/exits effective viewport repeatedly | REQUIRED/PENDING | REQUIRED/PENDING | Visible intervals accumulate; off-screen time is excluded |
| Tab hidden / window blurred | REQUIRED/PENDING | REQUIRED/PENDING | Timer pauses and accumulates |
| Window focused / document visible | REQUIRED/PENDING | REQUIRED/PENDING | Resume only currently intersecting sections |
| Pagehide | REQUIRED/PENDING | REQUIRED/PENDING | At most one bounded engagement event per viewed section |
| Contact copy success | REQUIRED/PENDING | REQUIRED/PENDING | `copied_contact` only after success, with three allowed params |
| Contact copy failure | REQUIRED/PENDING | REQUIRED/PENDING | No success event; accessible failure feedback |
| Live copy-event collision and duplicate check | REQUIRED/PENDING | REQUIRED/PENDING | Inspect all-pages legacy `text_copy`/`contact_info_copy` listeners and current route handling; no copied value leaves the page; `copied_contact` wiring remains unclaimed until verified |
| Form-success source/name collision | REQUIRED/PENDING | REQUIRED/PENDING | Inspect current LadiPage/editor plus GTM/GA4; preserve actual verified success event; route HTML emits none of the legacy/synthetic success names |
| Consent and page/section duplicate inventory | REQUIRED/PENDING | REQUIRED/PENDING | Verify consent behavior, one global `page_view` owner, and no duplicate `section_view`/`section_engagement_time` path before publication |
| Each of the two consultation CTAs with stub `OpenformWF2` | REQUIRED/PENDING | REQUIRED/PENDING | Each click invokes the trigger once; OSAT sends its matching `hero` or `terminal` intent location; Fabless/Partner emit no CTA event; no embedded form |
| Each consultation CTA without `OpenformWF2` | REQUIRED/PENDING | REQUIRED/PENDING | No exception/navigation; each status becomes `missing`; same route-specific event boundary |
| Refresh/back-forward | REQUIRED/PENDING | REQUIRED/PENDING | No duplicate initialization or false success |

**Runtime status:** desktop/mobile browser acceptance is REQUIRED/PENDING. No browser, GTM or GA4 runtime validation has been executed.

**Executed locally:** deterministic Node.js VM tests exercise the page scripts with stubbed DOM, IntersectionObserver, visibility/focus, clipboard and LadiPage trigger APIs. These verify enter/exit accumulation, pause/resume, terminal one-time flush and 3600-second cap, one-time section views, copy success/failure payloads, both popup-trigger present/missing behaviors, OSAT's hero/terminal CTA intent locations, no Fabless/Partner CTA event, route-specific static diagrams, no embedded form, no inline `page_view`, and one valid script/IIFE per route. This is source-level behavior only; the dated technical-document inventory is not live tag verification. Browser/device and GTM/GA4 QA remain separate; no tag-container validation is implied.

## Stop conditions

Stop before production/publication if live GTM/GA4 ownership, consent behavior, global `page_view` ownership, shared section tags, the legacy all-pages copy listener, LadiPage/form integrations, event-name collisions, or duplicate prevention remain unknown. Use marked test data only. Do not resolve uncertainty by adding aliases, renaming legacy events, or synthesizing a form-success event. Keep micro-events reporting-only; never make them primary Google Ads conversions.
