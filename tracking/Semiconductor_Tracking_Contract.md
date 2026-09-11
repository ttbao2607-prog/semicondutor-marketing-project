# Semiconductor Tracking Contract

**Status:** contract draft; dataLayer semantics are candidates until direct GTM/GA4 inventory and QA. No new container/property/event is authorized by this file.

## Global rules

- Global `page_view` remains owned by the existing global tag; no inline `page_view`.
- Reuse `section_view` with `section_name`.
- Reuse `section_engagement_time` with `section_name`, `engagement_seconds`, capped at `<=3600`.
- Observer root margin: `-45% 0px -45% 0px`.
- Effective visibility: pause timing on `visibilitychange` and `blur`; resume only on `focus` and visible state; flush on `pagehide`.
- Initializer and listeners must be idempotent; one-time section view and duplicate prevention are required.
- UTM/gclid remain in the URL. No redirect or handoff exists in these offline pages.
- No arbitrary analytics payload, copied contact value, phone, email or address is transmitted.

## Route-specific semantics

- OSAT may retain candidate `osat_cta_click` with `cta_location`.
- Fabless and Partner must not invent a shared general CTA event.
- `copied_contact` fires only after a successful copy and has exactly `contact_type`, `placement`, `segment`.
- There is no form; a CTA is not a lead or booking.
- `section_view` and `section_engagement_time` are reused candidates, not implementation authorization.

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
| Refresh/back-forward | REQUIRED/PENDING | REQUIRED/PENDING | No duplicate initialization or false success |

**Runtime status:** desktop/mobile browser acceptance is REQUIRED/PENDING. No browser, GTM or GA4 runtime validation has been executed.

**Executed locally:** deterministic Node.js VM tests exercise the page scripts with stubbed DOM, IntersectionObserver, visibility/focus and clipboard APIs. These verify enter/exit accumulation, pause/resume, terminal one-time flush and 3600-second cap, one-time section views, copy success/failure payloads, no inline `page_view`, and one valid script/IIFE per route. These are script-level tests, not browser/device or tag-container validation.

## Stop conditions

Stop before implementation if shared GTM/GA4 ownership, consent behavior, existing event names, duplicate state, URL/source policy or receiver scope is unknown. Use marked test data only. Keep micro-events reporting-only; never make them primary Google Ads conversions.
