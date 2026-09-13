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
