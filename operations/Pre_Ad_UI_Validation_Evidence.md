# Pre-ad UI validation evidence

**Date:** 2026-09-13 (Asia/Ho_Chi_Minh)
**Branch/base:** `slice/pre-ad-ui-validation` from canonical baseline `ad76af69be773ba3be8ca2804e92786f31fcdaa7`
**Scope:** local HTML browser QA; attempted LadiPage draft import; read-only planner availability check. No publish, campaign, spend, lead, or audience action.

The first local-route results below record the page revision before the locked LadiPage popup CTA correction. Its former anchor/OSAT-specific CTA observations are historical and are superseded by the correction result at the end of this file.

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

## Locked popup CTA correction (2026-09-13)

- All three hero consultation links were changed to buttons that look up/click the LadiPage-owned `OpenformWF2` trigger. OSAT retains its existing `osat_cta_click`/`cta_location` intent candidate; Fabless and Partner emit no CTA analytics event pending inventory. Missing trigger state is marked `missing` without navigation or an exception; the route markup contains no form.
- Tracking tests after this change: 21/21 passed, including one-click stub, absent-trigger fallback, OSAT-only CTA payload, no Fabless/Partner CTA event, no `accepted_form`, and no form markup per route.
- A fresh visual/browser run at 1280×900 and 390×844 could not be completed after the edit: the available browser denied local `file:` navigation by policy. No alternate browser surface, raw CDP, or workaround was used. Prior viewport screenshots predate this CTA correction and are not claimed as current verification.
- Therefore current responsive browser acceptance remains pending. The local integration logic is covered by Node tests only; LadiPage configuration/preview is also pending and was not performed.
- Existing `accepted_form` behavior was not modified. Popup/form fields, storage, and acceptance tracking remain LadiPage-owned.

## LadiPage final-draft import slice (2026-09-13)

- Fresh branch `slice/ladipage-final-draft-import` was created from the required canonical base `3cf7e6b82187e5c6b070a32dc28614428ff8562f`.
- Before upload, SHA-256 was checked for each requested D-drive canonical file against the corresponding file at that commit. All three comparisons failed; exact hashes and outcomes are recorded in `LadiPage_Draft_Runbook.md`.
- Integrity gate result: **blocked before upload**. No file was uploaded, no LadiPage draft was created, and no editor/preview was opened. Consequently there are no actual draft names or preview results to report.
- No workaround or alternate source file was substituted. No publish, domain, form submission, OpenformWF2 configuration, tag/tracking, campaign, spend, or audience action occurred.
- Resume requirement: reconcile the three D-drive canonical files with the specified commit, verify exact matching hashes, then perform only the authorized Basic-mode unpublished draft imports. The popup/form remains LadiPage-owned and intentionally unconfigured in this slice.
