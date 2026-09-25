# Supplier/Partner mobile compact candidate — local evidence, 2026-09-25

**Base:** `c243673` Phase 4 local closeout. **Candidate:** `slice/mobile-landing-compact-plan`. **Status:** local visual candidate; no LadiPage import, public update, form operation or account activity.

## Observed local render

Loopback HTTP preview of `landing/partner-route/supplier-ecosystem-flat.html` in headless Chrome. Screenshot was visually inspected locally; no screenshot containing case imagery is committed to the public repository.

| Viewport | Baseline height | Candidate height | Horizontal overflow | Notes |
|---|---:|---:|---|---|
| 390×844 | 14,353px | 9,325px | No | ERP → MES → OT summary stays visible; full architecture opens on demand. |
| 375×812 | Not captured | 9,471px | No | Sole `partner-cta-header` is 44px high and labeled `Tư Vấn`. |
| 768×1024 | Not captured | 11,421px | No | Intermediate tablet layout remains available; header CTA enlarged to at least 44px. |
| 1440×900 | 8,232px | 8,232px | No | Desktop page height unchanged; mobile controls are hidden. |

The 390px baseline's longest sections were architecture (2,516px), hero (2,088px), audience (1,754px), local delivery (1,711px) and Wafer Works proof (1,640px). The local page-height reduction is **35.0%**, not a user-engagement or conversion result.

## Interaction and contract checks

- At 375px, the architecture detail was hidden with `aria-expanded=false`; activating its control showed the detail with `aria-expanded=true`. Activating an audience card while collapsed also revealed the architecture. The control is a native button with visible focus and accepted Enter in the local browser check.
- The source retains all 8 observed top-level sections, anchors and exactly one consultation CTA ID: `partner-cta-header`, labeled `Tư Vấn`. No new form, provider SDK, analytics dispatch or success event was added.
- `node --test tests/landing-tracking.test.cjs`: 12/12 pass. `21st review` on changed Partner HTML: 0 errors, 0 warnings, 0 suggestions. `git diff --check`: pass.
- Browser screenshots and height measurements are local candidate evidence. PopupX binding compatibility, configured-domain behavior and live telemetry were **not** retested for this candidate; require the normal bridge/operator path if Bảo later authorizes deployment.

**Docs impact:** `CURRENT_STATE.md` and Partner design override updated for the local candidate. `Pre_Ad_Readiness_Plan.md` and the tracking contract were reviewed; their live status/event contract did not change.
