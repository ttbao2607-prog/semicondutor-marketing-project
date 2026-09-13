# Pre-ad UI validation evidence

**Date:** 2026-09-13 (Asia/Ho_Chi_Minh)  
**Branch/base:** `slice/pre-ad-ui-validation` from canonical baseline `ad76af69be773ba3be8ca2804e92786f31fcdaa7`  
**Scope:** local HTML browser QA; attempted LadiPage draft import; read-only planner availability check. No publish, campaign, spend, lead, or audience action.

## Local route checks

All three exact final HTML candidates were opened as local files and checked at desktop (1280×900) and mobile (390×844) browser viewports. Screenshots were reviewed during the session; no screenshots or browser/account identifiers are retained in this public repository.

| Route | Desktop/mobile layout | Metadata/assets | Contact/CTA behavior |
|---|---|---|---|
| OSAT | Passed; no horizontal overflow; mobile grids stack | Title, canonical, `noindex,follow`; logo loaded | Hero anchor reached `#contact`; `osat_cta_click` emitted with hero location. Synthetic clipboard success emitted only approved non-PII fields; simulated failure emitted no event and exposed failure text. |
| Fabless | Passed; no horizontal overflow; mobile grids stack | Title, canonical, `noindex,follow`; logo loaded | Contact anchor passed. Synthetic clipboard success emitted approved fields with `segment=fabless`; simulated failure emitted no event. |
| ERP–MES–OT partner | Passed; no horizontal overflow; mobile grids stack | Title, canonical, `noindex,follow`; logo loaded | Contact anchor passed. Synthetic clipboard success emitted approved fields with `segment=partner`; simulated failure emitted no event. |

Clipboard checks used an invalid synthetic test value and a browser-local stub. No actual contact was copied, and no analytics/tag network or live URL was tested. The final route files contain no forms.

## Platform route limits and result

- **LadiPage:** Basic mode was visibly selected. The browser upload bridge rejected the OSAT file path before transfer because the verified worktree is outside its configured upload roots. The two other final files were not attempted. No draft was created from these final files; no workaround, alternate copy, or page-script injection was used. This is a tool-path limitation, not a demonstrated LadiPage platform failure. Import/editor preview remains pending a supported transfer route.
- **Google Ads / Keyword Planner:** no Ads tab was present in the available browser inventory; the isolated browser bridge was unavailable. No navigation or query was made. Existing six-English-seed no-metrics evidence in S02/build sheet is historical and does not cover fresh OSAT Vietnamese, Fabless, or ERP–MES–OT/partner research.

## Gate

Local HTML behavior is validated for the tested viewports. LadiPage import compatibility and preview are not validated for these three final routes. Fresh Keyword Planner research remains pending access to the already-authorized read-only surface. Publication remains unauthorized here and requires its separate action-time confirmation after draft/editor QA.

## Repository verification

- Tracking suite: 16/16 tests passed.
- Structural checks passed on all three final HTML files: doctype, title, description, canonical, `noindex,follow`, exactly one script block, and no form.
- `git diff --check` passed. Privacy-pattern review found no account identifiers, credentials, contact addresses, or private platform routes in the new evidence; the runbook retains its pre-existing generic public LadiPage entrypoint.
