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

This is a post-import configuration requirement, not part of the HTML payload. The route design remains canonical and contains no visible or hidden form. Ownership is split: HTML owns the locked page UI and consultation CTA; LadiPage owns the external popup/form configuration, field definitions and receiver/storage. The actual successful-submit source and event name remain unknown until observed in the live LadiPage/editor and GTM/GA4 inventory; preserve the verified live behavior/name once established. Do not assume or synthesize `accepted_form`, and do not move form-success tracking into the imported HTML.

1. In the LadiPage editor, configure the approved LadiPage-native popup form, its fields and receiver/storage using the separately authorized platform configuration. Verify the current successful-submit event owner/name in the live LadiPage/editor and GTM/GA4 inventory before preserving or testing it; do not infer `accepted_form` from historical documentation. Keep these responsibilities outside the imported HTML. Do not put form fields or a form element in the imported HTML.
2. Using only a supported LadiPage UI control, assign the popup's existing opener/trigger element the exact DOM ID `OpenformWF2`, available to `document.getElementById()` from the imported page. Do not invent a LadiPage API or add a custom hidden trigger.
3. If the editor cannot bind the popup through that document-level ID, stop and escalate; do not substitute a URL redirect, embedded form, custom API, or unverified integration.
4. In draft/editor preview, verify that the page itself shows no form; verify the `OpenformWF2` trigger exists; click the primary consultation CTA once and confirm the LadiPage popup opens once. OSAT may retain only its existing `osat_cta_click` / `cta_location` candidate; Fabless/Partner emit no CTA analytics event until inventory authorizes reuse. In all routes, a trigger click is not form submission/lead. Any successful-submit reporting remains unknown until the live owner and event name are verified.
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

**Slice branch:** `slice/ladipage-final-draft-import` at base `3cf7e6b82187e5c6b070a32dc28614428ff8562f`. Raw SHA-256 values differ because the D-drive copy uses different line endings. The integrity check was resolved by Git-normalized blob identity and empty EOL-insensitive diffs for all three pairs; the sources are content-equivalent to the required commit.

| Route | Git blob at required base | Normalized D-drive Git blob | Integrity result | Import/draft name |
|---|---|---|---|
| OSAT | `552cc7df2443d8911fc7d2b0cdf6e91f43482b18` | `552cc7df2443d8911fc7d2b0cdf6e91f43482b18` | Match; EOL-only raw SHA difference resolved | No file selected; no draft created/name assigned |
| Fabless | `c769c3407c9341c522a425dc6a42794204f647d1` | `c769c3407c9341c522a425dc6a42794204f647d1` | Match; EOL-only raw SHA difference resolved | No file selected; no draft created/name assigned |
| ERP–MES–OT partner | `27185e516950efd8a11f27d21252aaf43a7a873d` | `27185e516950efd8a11f27d21252aaf43a7a873d` | Match; EOL-only raw SHA difference resolved | No file selected; no draft created/name assigned |

The authenticated HTML-to-LadiPage screen was opened directly and Basic mode selected. The file chooser was not completed: no file was selected or transferred, and no draft was created or previewed. No actual LadiPage draft names exist for this slice. Before any import, the Product Owner then directed a UX-UI-Promax redesign of all landing pages; this is the current stop condition. No publication, domain assignment, popup configuration, campaign action, or other live-account change occurred. `OpenformWF2` remains intentionally unconfigured. Resume only after the redesign is approved and a new import mandate is issued.

## UX redesign candidate update (2026-09-13)

The three offline route files have since been redesigned on `slice/landing-ux-redesign`: OSAT lot trace rail, Fabless outsourced-WIP handoff, and Partner ERP–MES–OT layer map. Each route retains exactly two consultation buttons and no embedded form. This is a local candidate change only; the prior file-transfer limitation still applies, no route was imported or previewed, and `OpenformWF2` remains unconfigured. Do not import or publish without the separate approval/mandate and a supported transfer route.

## Authorized UX redesign draft-preview attempt and Coordinator follow-up (2026-09-13)

**Branch/base:** `slice/ladipage-redesign-preview` at `6ffe18a671719e87138dab2b404d96c76beeb143` (`origin/main`). Before upload, all three D-drive canonical files were checked against that commit: Git-normalized blob IDs matched and EOL-insensitive comparisons were identical.

An initial browser-connector check returned **“Could not connect to Chrome.”** The Coordinator later reported successfully opening the authenticated LadiPage account through its direct HTTPS entrypoint, navigating to **Landing Pages > Create > HTML To LadiPage**, and visibly selecting **Basic** mode. The OSAT file chooser was triggered for the verified D-drive file, but `fileChooser.setFiles` returned the visible result **“Not allowed”** before any transfer. No file was selected or uploaded, and no OSAT draft was created. Fabless and Partner were not attempted. The browser tab is preserved at the HTML-to-LadiPage Basic upload screen for user handoff.

Authorized Chrome troubleshooting guidance identifies the required file-transfer permission as **“Allow access to file URLs”** for the specific Chrome profile and extension instance. This permission was not changed in this slice. The result is a browser file-access permission blocker, not a LadiPage content-validation rejection.

| Route | Intended draft name | Creation outcome | Editor/preview outcome |
|---|---|---|---|
| OSAT | `Digiwin Semiconductor - OSAT - UXPM Draft` | Chooser attempted; `Not allowed` before transfer; no draft created | Not opened; no visual result |
| Fabless | `Digiwin Semiconductor - Fabless - UXPM Draft` | Not attempted | Not opened; no visual result |
| ERP–MES–OT partner | `Digiwin Semiconductor - ERP MES OT - UXPM Draft` | Not attempted | Not opened; no visual result |

No draft was created and no editor preview occurred. No publication, domain assignment, form/popup setup or submission, `OpenformWF2` configuration, tracking/tag change, campaign, spend, or audience action occurred. Continue only after the user provides the required extension permission/file-transfer route and the approved upload can resume from the preserved tab.
