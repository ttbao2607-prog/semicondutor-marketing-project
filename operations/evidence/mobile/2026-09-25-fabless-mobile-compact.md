# Fabless mobile compact candidate — local evidence, 2026-09-25

**Base:** `c243673` Phase 4 local closeout. **Candidate:** `slice/mobile-landing-compact-plan`. **Status:** local visual candidate; no LadiPage import, public update, form operation or account activity.

## Observed local render

Loopback HTTP preview of `landing/fabless-route/fabless-outsourced-popupx-basic-flat.html` in headless Chrome. Screenshot was visually inspected locally; no screenshot containing case imagery is committed to the public repository.

| Viewport | Baseline height | Candidate height | Horizontal overflow | Notes |
|---|---:|---:|---|---|
| 390×844 | 14,615px | about 9,987px | No | Four-step flow stays visible; full operations map opens on demand. |
| 375×812 | Not captured | about 10,133px | No | Header CTA 44px high; terminal CTA 50px high. |
| 768×1024 | Not captured | 13,467px | No | Intermediate tablet layout remains available. |
| 1024×768 | Not captured | 7,980px | No | No compact rule applies. |
| 1440×900 | 8,078px | 8,078px | No | Desktop page height unchanged; mobile controls are hidden. |

The 390px baseline's longest blocks were the operations map (2,075px section), management cards (2,251px), pain questions (2,191px), hero (1,952px) and proof (1,561px). The local page-height reduction is **31.7%** after scrolling through lazy/reveal content, not a user-engagement or conversion result. Small render-height variance was observed across captures.

## Interaction and contract checks

- At 375px, the operations map was hidden with `aria-expanded=false`; activating its control showed the detail with `aria-expanded=true`. Activating a pain card while collapsed also revealed the map.
- The source retains all 8 observed top-level sections, anchors and exactly two consultation CTA IDs. No new form, provider SDK, analytics dispatch or success event was added.
- `node --test tests/landing-tracking.test.cjs`: 12/12 pass. `21st review` on changed Fabless HTML: 0 errors, 0 warnings, 0 suggestions. `git diff --check`: pass.
- Offline PopupX bridge preparation and validation on source commit `f2d3b8f` returned `MODAL_OPENFORM_HANDOFF_READY`. Configured-domain behavior and live telemetry were **not** retested for this candidate; require the normal bridge/operator path if Bảo later authorizes deployment.

**Docs impact:** `CURRENT_STATE.md` and Fabless design override updated for the local candidate. `Pre_Ad_Readiness_Plan.md` and the tracking contract were reviewed; their live status/event contract did not change.
