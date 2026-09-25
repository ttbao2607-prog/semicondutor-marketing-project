# Phase 4 GTM installation and Preview ledger — 2026-09-25

## Scope and authority

Bảo authorized authenticated Phase 4 Google debugging, LadiPage mutation/republication of the three approved Semiconductor routes, and a bounded GTM workspace correction. The explicit stop condition was before GTM Submit/Publish. No form submission, campaign mutation, enablement, spend, audience action, credential handling or Git publication was authorized or performed in this cycle.

## Published route installation

The existing PopupX SDK, canonical bridge and adapter were preserved. The approved shared GTM loader for public container `GTM-NGT54TM9` was added in LadiPage page settings, saved and republished on:

- `https://solutions.digiwin.com.vn/semiconductor-osat`
- `https://solutions.digiwin.com.vn/fabless`
- `https://solutions.digiwin.com.vn/supplierecosystem`

Each publish operation returned the visible LadiPage success state for its exact route. Supplier retained exactly one declared CTA, `partner-cta-header`, labeled `Tư Vấn`; no extra CTA or form was added.

## Authenticated Preview evidence

Tag Assistant identified `GTM-NGT54TM9` and destination `G-20TL63SYLQ` from the on-page `gtm.js` snippet on all three routes. Lifecycle events reached Container Loaded, DOM Ready and Window Loaded. Global tags and the existing section tracker fired; `section_view` was visible during the route checks.

The initial authenticated checks showed the legacy `cHTML - Listener - Text Copy.` tag firing on all three pages. The owned GTM workspace was therefore changed without using Submit:

1. Added Page View trigger `EX - Semiconductor routes - no text copy`.
2. Condition: `Page Path` matches RegEx `^/(semiconductor-osat|fabless|supplierecosystem)(?:/|$)`.
3. Attached the trigger as an exception to the existing `cHTML - Listener - Text Copy.` tag; the All Pages firing trigger remains unchanged.

Workspace state after save: two pending changes, comprising the added exception trigger and modified legacy copy-listener tag. Draft Preview then showed:

| Route | Shared container/destination | Section tracking | Legacy copy listener |
|---|---|---|---|
| OSAT | Found | Fired | Not in Tags Fired |
| Fabless | Found | Fired | Not in Tags Fired |
| Supplier/Partner | Found | Fired | Explicitly listed under Tags Not Fired |

No copied text or other selected value was read, retained or transmitted during validation.

## Publication checkpoint

After Bảo independently reviewed and published the prepared GTM change, the authenticated Versions screen showed Version 51 as `Live, Latest`, published 2026-09-25. Its Version Changes listed exactly the modified `cHTML - Listener - Text Copy.` tag and added `EX - Semiconductor routes - no text copy` trigger. The OSAT public route retained the installed GTM marker on reload after publication.

## Closeout continuation

At 2026-09-25 14:28:56–14:28:58 +07:00, after Bảo's action-time confirmation, one marked OSAT synthetic lead was submitted once through the header CTA on the exact configured-domain route. The provider displayed an explicit successful-receipt thank-you state. LadiPage Data Leads then showed the matching marked row as the newest record with the same timestamp, test phone/email and selected visible industry `Linh kiện điện tử`. Raw IP and unrelated lead rows were inspected only as needed by the authenticated UI and are intentionally excluded from this sanitized ledger. No retry, receiver/profile/form mutation or second submission occurred.

Fresh 390×844 smoke loaded all three exact routes with the shared container marker, no horizontal overflow and the expected CTA IDs/counts: OSAT 2, Fabless 2, Supplier 1. A synthetic attribution URL retained `utm_source`, `utm_medium`, `utm_campaign` and `gclid` into the PopupX iframe URL without adding the legacy eight-industry parameter.

Authenticated GA4 showed the existing `section_name` event-scoped custom dimension and `engagement_seconds` event-scoped custom metric. Neither `section_view`, `section_engagement_time` nor `osat_cta_click` appears in the complete GA4 key-event list. The GA4 recent-event catalogue retains the existing provider/legacy names including `form_start` and `generate lead`; no new alias or HTML success event was created. DebugView showed zero active debug devices after the ordinary public submission, so this receipt does not claim DebugView attribution for that lead.

The Google Ads account's complete 40-action conversion inventory contained none of the three Semiconductor micro-events. The DOM-only ad-blocker warning was absent from the screenshot and navigation/data loading worked, so it is classified `OBSERVED_DOM_FALSE_SIGNAL_NON_BLOCKING`. No campaign, goal, action, setting, bid, budget or spend was changed.

GA4 Consent Settings reported `No issues detected` and `Your setup is good`, while analytics and advertising consent signals were explicitly inactive. This is recorded as `OBSERVED_CONSENT_SIGNALS_INACTIVE`; allowed/denied consent-mode behavior is not claimed. Under the closeout governance, provider thank-you plus the exact matching Data Leads row is authoritative receiver acceptance; a Lark pool notification remains an optional downstream witness rather than a prerequisite.

## Current state

`P4_PASS_OSAT`

`P4_PASS_FABLESS`

`P4_PASS_SUPPLIER`

Phase 4 is closed. Phase 5 independent audit and campaign enable/spend remain separate and unauthorized.

## Closeout checks

- `node --test tests/landing-tracking.test.cjs`: 12/12 passed.
- `git diff --check`: passed; only the repository's existing LF-to-CRLF notices were emitted.
- Correct Google routing remains in the ignored local evidence area and is excluded from this sanitized ledger.
- Documentation impact reviewed against `DOCS_IMPACT_MAP.md`; `CURRENT_STATE.md`, `README.md`, `operations/Pre_Ad_Readiness_Plan.md`, `tracking/Semiconductor_Awareness_Tracking_Execution_Plan.md`, and `tracking/Semiconductor_Tracking_Contract.md` were synchronized to the observed closeout state.
- No commit, push, campaign enablement, budget/spend change or audience action was performed.

Account-routing details and private authenticated URLs are retained only in the ignored local evidence file; they are intentionally excluded from this sanitized ledger.
