# LadiPage OSAT draft runbook

**Status:** import/preview **PENDING**; this file does not assert that a cloud page exists.
**Owner:** paid executor; report to coordinator. **Scope:** one draft HTML upload only.

## Preconditions and boundary

- Use only the already authenticated Chrome route `https://app.ladipage.com/`; do not enter credentials or follow an auth prompt.
- The **Basic mode** and HTML-to-LadiPage GUI are user-provided authenticated UI evidence. GUI upload/import and cloud draft creation are external state changes.
- Upload exactly `landing/osat-route/index.html`; title must clearly say draft-only (for example, `DRAFT — OSAT vận hành — mechanism review`).
- Never publish, submit a form, create a lead, preview a created cloud page, or change tags/containers.

## Controlled sequence

1. Navigate to the HTML-to-LadiPage workflow.
2. Select the supplied HTML file and choose **Basic** mode.
3. Verify the file name and draft-only title.
4. Stop immediately before the final button that creates the cloud landing-page draft. Record the UI state and report `LADIPAGE_CREATE_CONFIRMATION_REQUIRED`; do not click it without a new confirmation.

## Audit fields to fill after an authorized import

| Field | Value |
|---|---|
| Timestamp / timezone | PENDING |
| Workflow URL (public/non-private only) | PENDING |
| Authenticated workspace identity | PENDING; do not record account ID |
| Uploaded filename / local revision | `landing/osat-route/index.html` / PENDING |
| Mode selected | Basic / PENDING |
| Draft-only title | PENDING |
| Import result/message | PENDING |
| Sections visibly present | PENDING |
| Desktop/mobile render check | PENDING |
| Final create button label and enabled state | PENDING |
| Publish/form/tag/container actions | Not performed |
| Reviewer and evidence location | PENDING; no private URL or PII |
