# LadiPage OSAT draft runbook

**Status:** draft created and preview-validated; unpublished.
**Owner:** paid executor; report to coordinator. **Scope:** one draft HTML upload only.

## Preconditions and boundary

- Use only the already authenticated Chrome route `https://app.ladipage.com/`; do not enter credentials or follow an auth prompt.
- The **Basic mode** and HTML-to-LadiPage GUI were observed in the authenticated session. Upload/import and cloud draft creation are external state changes and were completed only for this approved draft.
- Upload exactly `landing/osat-route/osat-route-draft.html`; LadiPage rejects the filename `index.html`. Title must clearly say draft-only (for example, `DRAFT — OSAT vận hành — mechanism review`).
- Never publish, submit a form, create a lead, set a domain, or change tags/containers. Preview was limited to the created draft editor.

## Controlled sequence

1. Navigate to the HTML-to-LadiPage workflow.
2. Select the supplied HTML file and choose **Basic** mode.
3. Verify the file name and draft-only title.
4. After creation, inspect the draft editor in desktop and mobile modes and record only sanitized visual evidence. Do not publish.

## Required popup binding after import — all three final routes

This is a post-import configuration requirement, not part of the HTML payload. The route design remains canonical and contains no visible or hidden form. Ownership is split: HTML owns the locked page UI and consultation CTA; LadiPage owns the external popup/form configuration, field definitions and data storage, and the successful-submit behavior/tracking.

1. In the LadiPage editor, configure the approved LadiPage-native popup form, its fields and receiver/storage using the separately authorized platform configuration. LadiPage's existing accepted-submit behavior and tracking remain authoritative; do not move these responsibilities into the imported HTML. Do not put form fields or a form element in the imported HTML.
2. Using only a supported LadiPage UI control, assign the popup's existing opener/trigger element the exact DOM ID `OpenformWF2`, available to `document.getElementById()` from the imported page. Do not invent a LadiPage API or add a custom hidden trigger.
3. If the editor cannot bind the popup through that document-level ID, stop and escalate; do not substitute a URL redirect, embedded form, custom API, or unverified integration.
4. In draft/editor preview, verify that the page itself shows no form; verify the `OpenformWF2` trigger exists; click the primary consultation CTA once and confirm the LadiPage popup opens once. OSAT may retain only its existing `osat_cta_click` / `cta_location` candidate; Fabless/Partner emit no CTA analytics event until inventory authorizes reuse. In all routes, a trigger click is not form submission/lead and only the existing accepted-form flow can report acceptance.
5. If the trigger is absent, verify there is no exception or navigation and the CTA reports `data-popup-trigger-status="missing"`. A `clicked` status means only that the trigger's `click()` method was invoked, not that a form was accepted.

No final-route import or popup setup is authorized by this runbook update. Do not import yet, publish, assign domains, submit test forms, change campaign state, spend, or upload audiences.

## Audit fields to fill after an authorized import

| Field | Value |
|---|---|
| Timestamp / timezone | 2026-09-11 / Asia/Ho_Chi_Minh |
| Workflow URL (public/non-private only) | Authenticated HTML-to-LadiPage route; URL omitted |
| Authenticated workspace identity | Observed; identity omitted |
| Uploaded filename / local revision | `landing/osat-route/osat-route-draft.html` / branch revision |
| Mode selected | Basic |
| Draft-only title | `DRAFT — OSAT vận hành — mechanism review` |
| Import result/message | Accepted; draft created and editor opened |
| Sections visibly present | Hero, mechanism cards, operating-view steps, CTA band, footer |
| Desktop/mobile render check | Passed visually in editor modes |
| Final create button label and enabled state | Creation completed; no publish action |
| Publish/form/tag/container actions | Not performed |
| Reviewer and evidence location | Coordinator review; sanitized evidence only |

## Current final-route import attempt (2026-09-13)

The earlier OSAT draft evidence above concerns `osat-route-draft.html` only. It does not establish import or preview compatibility for the three current final offline candidates.

- Basic mode was visibly selected in the HTML-to-LadiPage workflow.
- Upload of `landing/osat-route/osat-lot-test-traceability.html` was rejected by the browser bridge before file selection because the worktree path is outside its configured upload roots. No file reached LadiPage and no new draft was created.
- The Fabless and partner route uploads were not attempted after this first-route tooling boundary was confirmed.
- This is a local browser-tool path restriction, not an observed LadiPage validation/authentication error. No alternate copy location, page-script injection, credential flow, or workaround was used.
- Result: all three final candidates remain local-only and unimported in this validation slice. Import/editor preview is pending a supported, approved file-transfer route. No publication, domain, form, tracking, or campaign action occurred.

## Final-route import gate check (2026-09-13)

**Slice branch:** `slice/ladipage-final-draft-import` at base `3cf7e6b82187e5c6b070a32dc28614428ff8562f`. **Outcome:** stopped before opening the upload flow because all three requested D-drive sources failed the required SHA-256 comparison against that commit's worktree files.

| Route | SHA-256 at branch base | SHA-256 at requested D-drive path | Result / draft name |
|---|---|---|---|
| OSAT | `2C57D5B17096B4B30B3C660D3485AB0F2948A0E21F77E8F36E326F8F1D54C58E` | `7E84FC55325B2E78F6A060D04D6B2A39C63011022B1DFD895FD1360E45EC675D` | Mismatch; upload not attempted; no draft name assigned |
| Fabless | `CA6A9453E620F19C62826BCA56B20CEA3D2CEF637BE7845B8F079CD830A9CBAA` | `B0F87BFDBCFF6A554CAE9B5E100CD4A76A4E71866A805BBC8FFDAFA6928C0988` | Mismatch; upload not attempted; no draft name assigned |
| ERP–MES–OT partner | `178A45866AF92F050DF021CE04260496510EC425DE1554FDBE4A47D92AF7D2C7` | `383EAE7F9FA97AE84E47395D9EFBC083C75F706CD6BA0F51500DECD5ACEE2546` | Mismatch; upload not attempted; no draft name assigned |

No LadiPage upload, draft creation, editor preview, publication, domain assignment, popup configuration, or campaign action occurred in this slice. The existing `OpenformWF2` requirement remains pending and intentionally unconfigured. Resume only after the canonical D-drive files are reconciled to the approved commit and all three hashes match; then rerun the pre-upload gate.
