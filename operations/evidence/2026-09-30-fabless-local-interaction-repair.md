# Fabless local map interaction repair — 2026-09-30

## Authority and scope

Bảo requested: “Sửa bản local trước codex.” Local repair only, based on `main` at `0dcbb939224e495111cead99f1c8ed38c6e0c9ed`. Writer: Codex. Worktree: `D:\Digiwin_Fabless_Interaction_Fix`; branch: `slice/fabless-interaction-fix`. At the local repair audit checkpoint, changes were unstaged/uncommitted and not integrated into main. Bảo subsequently authorized commit and merge into local main, followed by deployment preparation only, explicitly stopping before deploy because another Codex process is deploying the previous main. No Git push or live action is included in that instruction.

## Root cause and bounded repair

The original `fabless-outsourced-wip.html` includes `renderMap`, tab handlers and pain-card `scrollToSection`. Flat-source creation commit `51dd538` has zero scripts; PageSpeed revision `eb88b8e` and the starting main still lack those functions. Read-only production clicks reproduced focus changes without tab selection or diagram transitions.

Restore only the map data/helpers and map control bindings from the original HTML into the flat DOM. Scope queries to `dw-fabless-landing`; use an initialization guard. Reveal mobile detail before card navigation; respect the system reduced-motion preference for scrolling. Use RAF for pulse restart without the original forced layout read. Keep tab ARIA selection, tab stops and panel label synchronized. Reuse the existing locale dictionary for runtime-generated nodes/options; add translations for previously unreachable original demo strings. Existing source claims and numeric examples are carried forward, not new verified operational results.

This repair does not restore unrelated original menu, modal, replay or page-animation handlers. Those controls are not included in this acceptance or claimed as fixed.

## Observed local verification

Chrome-controlled loopback preview, same resulting HTML:

- Lot card selects `map-tab-lot`, activates only `diagram-lot`, updates inspector, and scrolls to the map.
- Cost card selects `map-tab-cost`, activates `diagram-cost`, and updates inspector. Direct Lot/Cost tab clicks work.
- ArrowLeft changes Cost to Lot; Home changes to Progress. Card Enter/Space activation works.
- At 390×844, card activation expands `fabless-mobile-map-detail` and synchronizes toggle `aria-expanded=true`. After scrolling settles, map top was about 82px and heading top about 148px; no horizontal overflow.
- Progress card returns to Progress; Lot RMA control sets genealogy RMA mode and inspector option 4. Cost MCU control updates displayed COGS to `$1.20`.
- EN, zh-Hant and zh-Hans selections translate runtime inspector text after tab changes; VI round trip works. New demo translation terminology remains subject to native editorial review, as with the existing locale candidate.
- Browser error log: no captured JavaScript errors.
- Existing `node --test tests/landing-tracking.test.cjs`: 12/12 pass.
- Independent source comparison against starting HEAD: non-script markup/CSS/CTA IDs/bridge placeholders unchanged after line-ending/adjacent-script-whitespace normalization; existing section-awareness and mobile-toggle scripts unchanged after line-ending normalization. `git diff --check` passes.

## Docs and remaining boundary

Reviewed `DOCS_IMPACT_MAP.md`, `CURRENT_STATE.md`, readiness plan, tracking contract and canonical design system/override. Updated current state, readiness and Fabless interaction requirements. Tracking contract needs no change because producer, section IDs and CTA boundaries are unchanged. Historical evidence remains intact.

Execution: `SUCCESS` for the requested local tab/card repair. Audit: `AUDIT_PASS` for these bounded criteria based on observed browser state plus separate protected-source comparison. Production remains defective until an authorized existing-page revision. No PageSpeed or live tracking acceptance is inferred from this local repair.
