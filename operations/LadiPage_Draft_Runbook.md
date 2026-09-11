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
