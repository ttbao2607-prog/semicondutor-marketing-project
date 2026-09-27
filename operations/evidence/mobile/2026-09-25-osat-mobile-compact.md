# OSAT mobile compact candidate — local evidence, 2026-09-25

**Base:** `c243673` Phase 4 local closeout. **Candidate:** `slice/mobile-landing-compact-plan`. **Status:** local visual candidate; no LadiPage import, public update, form operation or account activity.

## Observed local render

Loopback HTTP preview of `landing/osat-route/osat-lot-test-traceability.html` in headless Chrome. Screenshot was visually inspected locally; no screenshot containing case imagery is committed to the public repository.

| Viewport | Baseline height | Candidate height | Horizontal overflow | Notes |
|---|---:|---:|---|---|
| 390×844 | 16,914px | about 10,247px | No | Main lot simulation is closed by default; five-step rail and explicit open control remain visible. |
| 375×812 | Not captured | about 10,520px | No | Header CTA 44px high; terminal CTA 50px high. |
| 768×1024 | Not captured | 12,845px | No | Tablet layout uses the existing intermediate breakpoint. |
| 1024×768 | Not captured | 9,482px | No | No compact rule applies. |
| 1440×900 | 7,872px | 7,872px | No | Every page-level section has the same top and height before/after; desktop layout geometry is preserved. |

At 390px the baseline section heights were hero 2,138px, questions 2,511px, lot map 4,168px, management layers 1,744px, case 1,518px, delivery 3,095px, resources 1,532px. The first compact pass lowered the total to 12,577px; placing the detailed simulation behind an explicit open control lowered it to about 10,247px after scrolling through lazy/reveal content. This is a **39.4% local page-height reduction**, not a user-engagement or conversion result. Small render-height variance was observed across captures.

## Interaction and contract checks

- At 375px, the map detail was hidden with `aria-expanded=false`; activating its control showed the detail with `aria-expanded=true`. Activating a pain card while collapsed also revealed the target simulation. The inspector has a separate native button inside the expanded simulation.
- The page retains 7 observed top-level sections, the same IDs/anchors and exactly two consultation CTA IDs. No new form, provider SDK, analytics dispatch or success event was added.
- `node --test tests/landing-tracking.test.cjs`: 12/12 pass. `21st review` on changed OSAT HTML: 0 errors, 0 warnings, 0 suggestions. `git diff --check`: pass.
- Offline PopupX bridge preparation and validation on source commit `f2d3b8f` returned `MODAL_OPENFORM_HANDOFF_READY`. Configured-domain behavior and live telemetry were **not** retested for this candidate; require the normal bridge/operator path if Bảo later authorizes deployment.

**Docs impact:** `CURRENT_STATE.md`, OSAT route source of truth and OSAT design override updated for the new local candidate. `Pre_Ad_Readiness_Plan.md` and the tracking contract were reviewed; their live status/event contract did not change.
