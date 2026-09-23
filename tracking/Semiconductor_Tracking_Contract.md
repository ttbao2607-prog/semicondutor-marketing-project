# Semiconductor Tracking Contract

**Status:** contract draft; dataLayer semantics are candidates until direct GTM/GA4 inventory and QA. No new container/property/event is authorized by this file.

The future awareness-oriented inventory, PopupX `modal_openform` handoff, implementation sequence and independent audit are specified in `Semiconductor_Awareness_Tracking_Execution_Plan.md`. That plan is a proposal, not evidence of deployment. Bảo selected PopupX for all three routes on 2026-09-23. Each final route must be a flat, provider-free canonical source; after tracking mutation, `$canonical-form-bridge` must generate and validate the exact prepared artifact/receipt consumed by `$ladipage-operator`.

## Local technical-document inventory boundary

- Read-only review of `digiwin_master_tracking_system.md`, `digiwin_gtm_governance_standard.md`, `digiwin_industry_landing_tracking.md`, and `digiwin_legacy_ldp_funnel_tracking.md` found dated documentation from 2026-07-09/10. This is documentary/historical evidence, not live GTM, GA4, LadiPage, consent, tag, trigger, or publication verification.
- The technical docs describe shared `section_view` and `section_engagement_time` event names with `section_name` and `engagement_seconds`; the current route contract retains hidden/unfocused-time exclusion and the 3600-second cap. This does not establish that shared tags are currently wired or deduplicated for these routes.
- `page_view` remains externally/global-tag owned; route HTML must not emit an inline `page_view`.
- The documented `industry_*` event family and its `industry` parameter belong to a separate eight-industry system. Do not automatically apply that taxonomy or parameter to the OSAT, Fabless, or Partner routes.

## Phase 1 live-inventory update (2026-09-23)

The sanitized read-only inventory is recorded in `operations/evidence/phase1/2026-09-23-inventory-and-route-ledger.md`. The existing authenticated GTM UI identified account `DigiwinVietnam` (GTM Account ID `6331240604`), container `www.digiwin.com.vn` (public container ID `GTM-NGT54TM9`). Version 49 was explicitly confirmed `Live, Latest`, published 2026-07-23; the earlier no-versions conclusion was premature and is withdrawn. Version 49 includes the All Pages section tracker plus downstream `section_view` and `section_engagement_time` GA4 Event tags and matching custom-event triggers. The tracker’s fixed legacy IDs do not intersect the frozen OSAT/Fabless source IDs, so a single route initializer may produce those events while the existing GTM tags dispatch them. The live tags also map `industry` through a DLV; route behavior for that parameter must be verified before publication. The live All Pages copy listener sends selected text through `text_copy` to GA4 `contact_info_copy` and Meta, a known privacy collision requiring route exclusion/governance before publication. No compatible OSAT CTA tag or Fabless route CTA tag was found; do not reuse Industry/Diagram click events. The correct paid-LadiPage GA4 property was observed, including the `ladipage ERP` stream, current event/custom-dimension catalogue, Enhanced Measurement and consent settings. Existing `form_start`, `generate lead` and `LeadConversionSuccess` names are visible in the GA4 catalogue, but their producers and success semantics remain unverified. The UI reported no individual consent signals despite a positive summary status; GTM per-tag consent settings were not exposed in the read-only Version snapshot. LadiPage route/receiver ownership, Ads goals and LinkedIn reporting remain unknown/blocked. OSAT and Fabless flat provider-free sources passed route-freeze/preflight and the overall §4.1 event-owner gate: `P1_PASS_OSAT` and `P1_PASS_FABLESS`. This authorizes local Phase 2 work only; it does not authorize GTM mutation, publishing, or a form operation. Supplier is `DEFERRED_BY_PRODUCT_OWNER` and excluded from Phases 2–5 until an approved source returns through Phase 1.

## Global rules

- Global `page_view` remains owned by the existing global tag; no inline `page_view`.
- Reuse `section_view` with `section_name`.
- Reuse `section_engagement_time` with `section_name`, `engagement_seconds`, capped at `<=3600`.
- Observer root margin: `-45% 0px -45% 0px`.
- Effective visibility: pause timing on `visibilitychange` and `blur`; resume only on `focus` and visible state; flush on `pagehide`.
- Initializer and listeners must be idempotent; one-time section view and duplicate prevention are required.
- UTM/gclid remain in the URL. No redirect or handoff exists in these offline pages.
- No arbitrary analytics payload, copied contact value, phone, email or address is transmitted.
- Each current OSAT/Fabless visual has exactly two primary consultation buttons: one in the header and one in the terminal contact band. The final flat artifacts expose two stable CTA IDs declared in the PopupX bridge manifest. The live operator adds the official PopupX SDK and narrow modal adapter outside the market artifact. A request does not imply popup display or form acceptance.
- A route-specific supporting demo control may invoke the same external trigger when explicitly marked, but it is not a primary CTA and emits no route event.

## Route-specific semantics

- OSAT may retain the existing candidate `osat_cta_click` with exactly `cta_location`, recording CTA intent only. The first primary button is physically in the page header but carries the existing `hero` intent label; the terminal button sends `terminal`. Do not rename its event or parameter.
- `osat_cta_click` is a local OSAT candidate only; the reviewed technical-document inventory does not substantiate it or show that it is wired in GTM/GA4.
- Fabless and Partner emit no CTA analytics event until actual GTM/container inventory authorizes reuse of an existing event. Do not create a shared CTA taxonomy for these routes.
- The offline prepared artifact contains only the bridge-marked CTA selectors/attributes and render anchors. It contains no PopupX SDK, popup URL, provider identifier, physical form reference or form configuration. The live operator resolves the environment provider at runtime and attaches only the official SDK plus narrow adapter.
- A CTA adapter request records no popup-open confirmation, form submission, lead, or conversion.
- Imported HTML contains no visible or hidden form and emits none of `Ladi_form_success`, `generate lead` (space), or `accepted_form`. The reviewed legacy docs describe `Ladi_form_success` as an internal LadiPage event and report a GA4 event named `generate lead`; its proposed direct-LadiPage source was historically inferred, not verified in this inventory. The sources do not substantiate `accepted_form`. Determine the actual successful-submit event and owner through the authorized PopupX/LadiPage runtime and live GTM/GA4 inventory; do not rename or synthesize it. A CTA adapter request is popup intent only.
- A prior OSAT route revision used `copied_contact` as a local success-only candidate with exactly `contact_type`, `placement`, and `segment`; the copied value was never included. The visually approved OSAT LDP candidate canonicalized on 2026-09-22 contains no contact-copy control and emits no `copied_contact`. The legacy docs separately describe an all-pages copy listener emitting `text_copy` with `copied_text`, followed by `contact_info_copy` carrying copied content. That legacy behavior is privacy-incompatible with this route contract: do not rename, alias, or treat these events as equivalent. Verify live listener/tag/trigger collisions and deduplication before production.
- The landing page itself has no form; a LadiPage-configured popup may display its own form only after the consultation CTA is activated.
- `section_view` and `section_engagement_time` are reused candidates, not implementation authorization.

## PopupX modal handoff boundary

- Use `$canonical-form-bridge` with an explicit `modal_openform` manifest. It pins the tracked flat source commit/tree/SHA-256, two CTA ID selectors, render anchors and non-overwriting output. Shadow DOM, embedded forms, provider bundles/references, ambiguous selectors or source drift fail closed.
- Tracking mutation occurs on the canonical flat source. Because mutation changes the hash, prepare and validate the bridge package again afterward. Hand `$ladipage-operator` only the final passed receipt and exact prepared artifact; never edit that artifact after validation.
- The live route is Basic HTML-to-LadiPage. Bảo alone selects the pinned file and creates the page. Under exact target/lifecycle authority, the operator verifies the existing four-field PopupX profile (`name`, `email`, `phone`, `industry`, Data Leads enabled), exact industry label and runtime provider resolver, then adds only the official SDK and narrow adapter.
- Verify save/reopen, desktop/mobile fidelity and that each declared CTA opens the existing modal once. A CTA request/open is not form acceptance. One synthetic submission requires separate action-time confirmation and a thank-you + Data Leads + Bảo-supplied Lark pool witness; do not retry an uncertain submission.

## Contact-copy behavior

If a future route revision contains the governed visible contact block, it must use verified company-controlled public contact values. Copy success is announced accessibly and then emits only the allowed event parameters. Copy failure announces a safe retry path without emitting success. The current visually approved Fabless and OSAT LDP candidates contain no contact-copy control.

## QA matrix

| Planned acceptance case | Desktop | Mobile | Required result |
|---|---|---|---|
| First section enters effective viewport | REQUIRED/PENDING | REQUIRED/PENDING | One `section_view` only |
| Section enters/exits effective viewport repeatedly | REQUIRED/PENDING | REQUIRED/PENDING | Visible intervals accumulate; off-screen time is excluded |
| Tab hidden / window blurred | REQUIRED/PENDING | REQUIRED/PENDING | Timer pauses and accumulates |
| Window focused / document visible | REQUIRED/PENDING | REQUIRED/PENDING | Resume only currently intersecting sections |
| Pagehide | REQUIRED/PENDING | REQUIRED/PENDING | At most one bounded engagement event per viewed section |
| Contact copy success, only if a future route has a governed copy control | NOT APPLICABLE TO CURRENT OSAT/FABLESS | NOT APPLICABLE TO CURRENT OSAT/FABLESS | `copied_contact` only after success, with three allowed params |
| Contact copy failure, only if a future route has a governed copy control | NOT APPLICABLE TO CURRENT OSAT/FABLESS | NOT APPLICABLE TO CURRENT OSAT/FABLESS | No success event; accessible failure feedback |
| Live copy-event collision and duplicate check | REQUIRED/PENDING | REQUIRED/PENDING | Inspect all-pages legacy `text_copy`/`contact_info_copy` listeners and current route handling; no copied value leaves the page; `copied_contact` wiring remains unclaimed until verified |
| Form-success source/name collision | REQUIRED/PENDING | REQUIRED/PENDING | Inspect current LadiPage/editor plus GTM/GA4; preserve actual verified success event; route HTML emits none of the legacy/synthetic success names |
| Consent and page/section duplicate inventory | REQUIRED/PENDING | REQUIRED/PENDING | Verify consent behavior, one global `page_view` owner, and no duplicate `section_view`/`section_engagement_time` path before publication |
| Each of the two declared PopupX CTA IDs before live binding | REQUIRED/PENDING | REQUIRED/PENDING | Final bridge manifest resolves each selector exactly once; prepared artifact has trigger marker and no embedded form/provider reference |
| Each declared PopupX CTA after operator binding | REQUIRED/PENDING | REQUIRED/PENDING | Each activation opens the existing four-field modal once; OSAT emits intent only if separately admitted; Fabless/Partner emit no CTA analytics event |
| Refresh/back-forward | REQUIRED/PENDING | REQUIRED/PENDING | No duplicate initialization or false success |

**Runtime status:** desktop/mobile browser acceptance is REQUIRED/PENDING. The Phase-1 read-only GA4 settings/catalogue inventory was performed on 2026-09-23; it is not browser event QA. GTM preview, GA4 DebugView, route behavior and tag-owner validation have not been executed.

**Current local test status (2026-09-23):** `node --test tests/landing-tracking.test.cjs` returned 8 pass / 16 fail. The old harness expects inline tracking and prior structure in the replaced OSAT/Fabless visuals; those two current files emit no `dataLayer` event. The passing Partner tests concern its current candidate only, not the unfinished Supplier final route. Earlier source-level pass claims applied to earlier source revisions and must not be carried forward. Revise the tests against frozen final flat PopupX artifacts during the awareness build. Browser/device and GTM/GA4 QA remain pending; no tag-container validation is implied.

## Stop conditions

Stop before production/publication if live GTM/GA4 ownership, consent behavior, global `page_view` ownership, shared section tags, the legacy all-pages copy listener, LadiPage/form integrations, event-name collisions, or duplicate prevention remain unknown. Use marked test data only. Do not resolve uncertainty by adding aliases, renaming legacy events, or synthesizing a form-success event. Keep micro-events reporting-only; never make them primary Google Ads conversions.
