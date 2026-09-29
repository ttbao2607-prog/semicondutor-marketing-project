# P4 offline audit — PageSpeed candidate (2026-09-29)

**Current terminal:** `P4_OFFLINE_PASS` after the bounded OSAT anchor fix and re-audit below. The first-pass failure remains recorded for traceability. This is a local candidate audit. No LadiPage Builder action, publication, form submission, GTM change, or Git synchronization occurred.

## Candidate identity

Branch `slice/landing-pagespeed-optimization`, commit `72ee6a711bd9d16e117cdb7edb06a722682c26a9`, clean working tree at audit start. The branch has no upstream and these commits are local only. SHA-256 of the exact HTML files:

| Route | Canonical path | SHA-256 |
|---|---|---|
| OSAT | `landing/osat-route/osat-lot-test-traceability.html` | `458e340a73393103af2b97f670783dce51bfd492b64f0015656a252001dd810a` |
| Fabless | `landing/fabless-route/fabless-outsourced-popupx-basic-flat.html` | `8fad9ea264655aa3d49cdd784a827286192fd4a6f14eff80a6fd1fe554eee893` |
| Supplier/Partner | `landing/partner-route/supplier-ecosystem-flat.html` | `7eb55fbe67e2ec2cc7be5e2ba75315dd12ecaa729ef04f2d3b0f2c0376ea94b7` |

## Lighthouse local candidate

Lighthouse 13.5.0 through headless Chrome against Python static HTTP server bound to `127.0.0.1`. One run per route and form factor. Raw JSON reports are local-only at `%TEMP%/semiconductor-p4-offline-20260929/`. Values below are one-run lab results, not PSI measurements of published LadiPage pages and not a like-for-like performance delta from the P0 live baseline.

| Route | Mode | Score | FCP ms | LCP ms | TBT ms | CLS | Speed Index ms |
|---|---|---:|---:|---:|---:|---:|---:|
| OSAT | Mobile | 84 | 2295 | 3563 | 222 | 0 | 2295 |
| OSAT | Desktop | 96 | 416 | 1364 | 52 | 0 | 562 |
| Fabless | Mobile | 92 | 1832 | 3253 | 0 | 0 | 1832 |
| Fabless | Desktop | 97 | 375 | 1207 | 24 | 0 | 535 |
| Supplier/Partner | Mobile | 93 | 2189 | 2799 | 46 | 0 | 2189 |
| Supplier/Partner | Desktop | 100 | 530 | 708 | 0 | 0 | 607 |

All six single runs exceed the plan's score threshold of 80. This does not establish the same scores after Builder normalization, PopupX/GTM runtime, or publication.

## Regression and bridge checks

- `node --test tests/landing-tracking.test.cjs`: **12/12 pass** at the candidate HEAD. This verifies source tracking behavior and CTA inventory (2/2/1), not a live PopupX open.
- Offline `modal_openform_handoff.inspect_artifact` against the candidate source and previously declared route CTA/anchor sets: **valid for all three routes**. All CTA IDs and anchors match once; no form, inline provider bundle, physical reference, or Shadow DOM signal. This is source compatibility only. Older final prepared artifacts/receipts bind older hashes and do not bind this candidate. Existing-page revision remains the deployment route.
- Chrome local preview at desktop and 390px: hero content rendered on each route; at 390px document width equaled viewport width for the inspected Partner route. OSAT and Fabless narrow screenshots showed their hero layouts; the inspection was bounded and does not prove every lower section or every image loaded on every run. Some CDN images appeared incomplete on first preview and loaded after reload; direct checks returned HTTP 200 for two sampled original and transformed URLs. Image delivery needs a repeat visual/network check before a PASS.
- **OSAT navigation defect:** Clicking the hero anchor in the local preview logged `TypeError: root.getElementById is not a function` at the click handler. The same expression is present in local `main` before P1–P3, so it is an existing defect rather than a regression introduced by this branch. The P4 navigation check cannot pass while it persists. Do not claim the `content-visibility:auto` scroll behavior is validated by this incomplete check.

## First-pass closeout, superseded by re-audit

Execution status: `FAILURE` for the P4 acceptance gate. Audit verdict: `AUDIT_FAIL`. Lighthouse and deterministic source checks passed, but the required route navigation check failed. The broad `content-visibility:auto; contain-intrinsic-size:1px 700px` rule still needs a complete scroll/anchor/observer check on all three routes. No candidate-specific `PENDING` `revise_existing_page` receipts or production preflight were prepared in this offline P4 scope. Do not start deployment from this record.

Next local step: resolve or explicitly scope the OSAT anchor defect, complete browser regression at desktop and 390px including CDN image load and all section anchors, then rerun the affected P4 checks. A later deployment decision requires exact per-page `PENDING` receipts, baseline hashes, authority, and the `revise_existing_page` preflight under `$ladipage-operator`.

## Final offline re-audit

The OSAT local anchor handler now looks up the target in `document` and verifies it belongs to the route root before scrolling. This is a bounded source fix for the pre-existing `root.getElementById` error. No CTA, tracking initializer, form, provider or tag code was changed. The three route tracking initializer script bodies match local `main` exactly.

Final candidate SHA-256: OSAT `19fb86f7fee3cfcf8e0da46b1c38ca14ba5273592bd3f382e54c5b7f2943b20c`; Fabless and Supplier/Partner remain at the hashes in the candidate identity table above. The OSAT source fix is an uncommitted working-tree change on the named branch; deployment must pin these final bytes, not the old `72ee6a7` OSAT blob.

Lighthouse 13.5.0 rerun against the final OSAT bytes: Mobile **82** (FCP 2278 ms, LCP 3646 ms, TBT 240 ms, CLS 0); Desktop **95** (FCP 551 ms, LCP 1537 ms, TBT 0 ms, CLS 0). Raw reports: `%TEMP%/semiconductor-p4-offline-20260929/osat-mobile-final.json` and `osat-desktop-final.json`. Fabless and Supplier/Partner files did not change after their initial six-run matrix; their four reports and scores above remain tied to final bytes. All six final route/mode scores are >=80. These local lab results do not predict the exact published LadiPage scores.

Because OSAT Mobile was close to the threshold, one focused repeat on the same final bytes scored **84** (LCP 3594 ms, TBT 208 ms, CLS 0); raw report `osat-mobile-final-repeat.json` in the same local-only directory. This is repeat lab evidence, not a guaranteed live score.

- Tracking gate rerun: **12/12 pass**. CTA inventory remains 2/2/1. Offline modal bridge source inspection rerun against final bytes: **READY** for all three declared CTA/anchor sets, with no forbidden provider/form signal. This is compatibility inspection, not a new prepared import receipt or live PopupX proof.
- Desktop Chrome preview: OSAT hero link reached `#lot-map` with its top 94px below the viewport top after scroll and no console error. Fabless navigation reached `#fabless-map` (top 0px); Supplier/Partner reached `#ecosystem-architecture` (top 91px). Desktop hero imagery rendered after load, and no horizontal overflow was observed.
- Narrow breakpoint interaction: OSAT map and nested inspector toggles, Fabless map toggle, and Supplier/Partner map toggle each reached `aria-expanded=true`; document width remained within viewport at the tested narrow breakpoint. Exact 390px CDP viewport readback showed `documentElement.scrollWidth === innerWidth === 390` on all three routes. Hero layouts were visually inspected at desktop and narrow width. Browser control did not reliably dispatch clicks under the exact 390px touch emulation; link interaction was checked in desktop and narrow non-touch contexts. This limits the mobile link claim but does not alter the source behavior verified by those contexts.
- CDN media check: all **46 distinct `lh3.googleusercontent.com` image URLs** present in the three final HTML sources returned HTTP 200 with an image content type. Initial Chrome preview frames occasionally preceded image completion; repeat screenshots showed hero images loaded. This confirms current URL availability, not future CDN uptime.
- The P2 `content-visibility` rule remains in the candidate. Section links in the three desktop routes reached their targets after scroll. Lighthouse reported CLS 0 for all six local runs; narrow detail disclosures expanded without horizontal overflow. The audit does not claim full live Builder/PopupX/GTM runtime behavior.

**Execution status:** `SUCCESS` for the defined offline P4 scope. **Audit verdict:** `AUDIT_PASS` for the final local candidate under the evidence and limits above. Ready for a separate, exact-target `revise_existing_page` deployment decision and preflight; **not yet authorized or preflight-cleared for publication**. The old Phase 2 prepared import artifacts and their receipts are bound to older source hashes and are not deploy inputs for this existing-page revision.
