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
- **Google Ads / Keyword Planner — historical executor check:** no Ads tab was present in that earlier browser inventory and its isolated browser bridge was unavailable; no account navigation or query was made in that check. This historical limitation is superseded as a description of the latest account-access evidence by the Coordinator-reported observation below. The six-English-seed no-metrics result remains historical and does not cover fresh OSAT Vietnamese, Fabless, or ERP–MES–OT/partner research.

## Gate

Local HTML behavior is validated for the tested viewports. LadiPage import compatibility and preview are not validated for these three final routes. On 2026-09-14, direct Keyword Planner navigation and its query form worked despite stale ad-blocker text in the accessibility/DOM tree; the screenshot showed no such dialog. One OSAT query returned no displayed metrics and created a Planner draft entry automatically, so the remaining cluster queries were stopped. Fresh Fabless and ERP–MES–OT/partner research remains pending. Publication remains unauthorized here and requires its separate action-time confirmation after draft/editor QA.

## Repository verification

- Tracking suite: 16/16 tests passed.
- Structural checks passed on all three final HTML files: doctype, title, description, canonical, `noindex,follow`, exactly one script block, and no form.
- `git diff --check` passed. Privacy-pattern review found no account identifiers, credentials, contact addresses, or private platform routes in the new evidence; the runbook retains its pre-existing generic public LadiPage entrypoint.

## Locked popup CTA correction (2026-09-13)

- All three hero consultation links were changed to buttons that look up/click the LadiPage-owned `OpenformWF2` trigger. OSAT retains its existing `osat_cta_click`/`cta_location` intent candidate; Fabless and Partner emit no CTA analytics event pending inventory. Missing trigger state is marked `missing` without navigation or an exception; the route markup contains no form.
- Tracking tests after this change: 21/21 passed, including one-click stub, absent-trigger fallback, OSAT-only CTA payload, no Fabless/Partner CTA event, no `accepted_form`, and no form markup per route.
- A fresh visual/browser run at 1280×900 and 390×844 could not be completed after the edit: the available browser denied local `file:` navigation by policy. No alternate browser surface, raw CDP, or workaround was used. Prior viewport screenshots predate this CTA correction and are not claimed as current verification.
- Therefore current responsive browser acceptance remains pending. The local integration logic is covered by Node tests only; LadiPage configuration/preview is also pending and was not performed.
- No `accepted_form` behavior or event name was verified; the route emitted none. The live successful-submit path remains pending LadiPage/editor and GTM/GA4 inventory. Popup/form fields and receiver/storage remain LadiPage-owned.

## LadiPage final-draft import slice (2026-09-13)

- Fresh branch `slice/ladipage-final-draft-import` was created from the required canonical base `3cf7e6b82187e5c6b070a32dc28614428ff8562f`.
- Raw SHA-256 initially differed due to line-ending normalization. Git blob hashes for all three D-drive files match the specified commit, and EOL-insensitive diffs are empty; the source integrity gate is **passed**. Exact blob IDs are recorded in `LadiPage_Draft_Runbook.md`.
- The authenticated HTML-to-LadiPage screen was opened and Basic mode selected. No file was selected or transferred; no draft was created and no editor/preview was opened. Thus no actual draft names or preview results exist for this slice.
- The Product Owner then directed that all landing pages receive a UX-UI-Promax redesign before any import. Work stopped at the pre-upload screen. No publish, domain, form submission/configuration, OpenformWF2 setup, tag/tracking, campaign, spend, or audience action occurred.
- Current resume gate: complete and approve the required redesign, then obtain a fresh import mandate. The popup/form remains LadiPage-owned and intentionally unconfigured.

## UX redesign candidate verification (2026-09-13)

- **Revision:** local changes on `slice/landing-ux-redesign`, based on the current canonical route sources. All three HTML candidates were redesigned in place using the approved design-system tokens and route overrides. Their unique static diagrams are the OSAT `LOT > TEST > QUALITY/4M1E > WIP > COST REVIEW` trace rail; the Fabless `FORECAST > OUTSOURCE > LOT/DATECODE/BIN > COST REVIEW` handoff with ownership explicitly left to confirm; and the Partner `ERP context > MES execution > OT signals` layer map labeled as an architecture hypothesis.
- **CTA and tracking contract:** each route has exactly two primary consultation buttons, hero and terminal. The external `OpenformWF2` trigger is looked up and clicked once per CTA when present; a missing trigger is non-fatal and marked `missing`. OSAT emits its existing intent event at both locations; Fabless and Partner emit no CTA event. No route contains an embedded form or emits `accepted_form`; section timing and privacy-safe copy-success events remain in place.
- **Local automated checks:** the deterministic Node.js VM suite passes 24/24, including both CTA locations with and without the external trigger, route-specific CTA event boundaries, static route diagrams, basic responsive/accessibility structure, timing, and copy success/failure behavior. `git diff --check` passes.
- **Visual and platform status:** no real browser viewport or editor preview has been completed for this redesigned revision. In the later Coordinator-reported attempt, the authenticated LadiPage account opened, Basic mode was selected, but the OSAT file chooser returned `Not allowed` before transfer; Fabless and Partner were not attempted. The tab remains at the Basic upload screen. The required Chrome extension file-URL permission has not been changed. No live form, domain, tag, campaign, spend or publication action occurred.

## Google Ads UI evidence — corrected classification (2026-09-14, Asia/Ho_Chi_Minh)

**Evidence correction from Bảo (2026-09-14):** withdraw the prior characterization of this signal as a visibly rendered modal. “Turn off ad blockers” was a DOM/accessibility-only false signal, not a historically visible dialog. Classify it as `OBSERVED_DOM_FALSE_SIGNAL_NON_BLOCKING`; the earlier report is not evidence of a rendered modal or blocker. The screenshot-backed Planner observation below shows no dialog, and Planner interaction worked. The orange Vietnamese **“Xem xét mục tiêu của chiến dịch...”** mechanism-update banner remains informational/non-blocking.

No settings, campaign, enablement, spend, lead, audience or other external mutation was reported in that 2026-09-13 session. No account identifiers, private URLs, login identity, screenshots, cookies or session details are retained.

## Google Ads Keyword Planner verification (2026-09-14, Asia/Ho_Chi_Minh)

**Evidence class:** direct executor observation in the authorized browser session. Screenshots were reviewed in-session and are not retained in the repository.

- Direct navigation to Keyword Planner reached an account chooser, the Digiwin account was selected, and the Planner page loaded. A screenshot showed no “Turn off ad blockers” dialog. The string remained in the accessibility/DOM tree, but the Planner navigation and query form worked. Classify it as `OBSERVED_DOM_FALSE_SIGNAL_NON_BLOCKING`, not a visible or functional blocker.
- The orange Vietnamese “Xem xét mục tiêu của chiến dịch...” banner was visibly rendered at the top and remained informational. It did not prevent Planner interaction.
- Planner query configuration shared by the three seed clusters: Vietnam, Vietnamese, Google network, historical window Sep 2025–Aug 2026; adult ideas excluded. The submitted seeds are the canonical OSAT, Fabless and ERP–MES–OT/partner lists in the Google Search Build Sheet; no account identifiers, private URLs or screenshots are retained here.
- OSAT results showed dashes for the displayed monthly searches, changes, competition, impression share and low/high top-of-page bid. The chart showed no data and the related-idea panel showed no results. Record `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`; do not infer demand=0.
- Fabless results contained eight seed rows; every displayed metric field was a dash. Record `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`; this is not zero demand.
- Partner results contained eight seed rows. `electronics manufacturing ERP` displayed average monthly searches 10, three-month change 0%, and year-over-year change -100%; the other displayed fields for that row were dashes. The remaining seven rows displayed dashes in all metric fields. This limited historical UI evidence is not a forecast, delivery result, demand conclusion, CPC/competition finding, or authorization to build or launch.
- **Planner side effect:** each of the three “Nhận kết quả” interactions displayed a newly created draft plan entry without an explicit save action. Bảo authorized completion of the three-query research with this side effect accepted. These entries are Planner drafts, not campaigns; none was explicitly saved, renamed or deleted.
- The three planned seed-cluster queries are complete. No campaign was created or modified; no settings changed; no campaign was enabled; no spend, export, upload, form submission or audience action occurred. Live account/campaign overlap, configuration, CPC/competition where not displayed, demand and conversion setup remain unverified.

## Authorized UX redesign draft-preview attempt (2026-09-13)

- **Integrity/base:** on `slice/ladipage-redesign-preview` at `6ffe18a671719e87138dab2b404d96c76beeb143` (`origin/main`), each specified D-drive candidate matched the commit's Git-normalized blob; EOL-insensitive comparisons also matched.
- **Superseding Coordinator-reported browser result:** after an initial connector error **“Could not connect to Chrome,”** the Coordinator successfully opened the authenticated LadiPage account through the direct HTTPS entrypoint, navigated to **Landing Pages > Create > HTML To LadiPage**, and selected **Basic**. The OSAT file chooser was triggered for the verified candidate; `fileChooser.setFiles` returned **“Not allowed”** before transfer. No file was selected/uploaded and no draft was created. Fabless and Partner were not attempted. No alternate browser surface or workaround was used.

| Route | Requested draft name | Draft created? | Desktop/mobile editor preview |
|---|---|---|---|
| OSAT | `Digiwin Semiconductor - OSAT - UXPM Draft` | No — chooser returned `Not allowed` before transfer | Not opened; no visual outcome |
| Fabless | `Digiwin Semiconductor - Fabless - UXPM Draft` | No — not attempted | Not opened; no visual outcome |
| ERP–MES–OT partner | `Digiwin Semiconductor - ERP MES OT - UXPM Draft` | No — not attempted | Not opened; no visual outcome |

Authorized Chrome troubleshooting guidance says upload requires **“Allow access to file URLs”** for the specific Chrome profile and extension instance. This permission was not changed. The tab is preserved at the HTML-to-LadiPage Basic upload screen for user handoff. No draft creation or publication occurred. No domain, form, popup, `OpenformWF2`, tracking/tag, campaign, spend, or audience action was taken. Desktop/mobile preview validation remains pending resolution of the file-access permission and successful draft creation.

## OSAT-only import retry (2026-09-14)

- **Lineage:** new owned branch `slice/ladipage-osat-draft-import-retry`, from canonical `main` at `304e1dc266bafc01365b9d399952434ec5d0b43d`. The requested OSAT source `landing/osat-route/osat-lot-test-traceability.html` matched the checked-in content exactly before use.
- **Observed:** the direct authorized LadiPage entrypoint and HTML To LadiPage workflow opened in the existing Chrome profile. Basic mode was visibly selected. The dedicated browser connector could not connect; the existing session was controlled via the available browser UI surface.
- **Transfer:** the file-selection control was clicked once, but the visible screen remained unchanged and exposed no file chooser or permission message. No file was selected or transferred. This is a UI/tool-access limitation; it is not an observed LadiPage validation result and is distinct from the prior `Not allowed` attempt.
- **Outcome:** no draft exists; the requested draft title was not assigned; editor desktop/mobile preview was not reached. No publish, domain, popup/form/receiver, `OpenformWF2`, form submit, tag/tracking, campaign, spend, audience, credential, browser permission, alternate browser/path, or script action occurred. No raw screenshot or account/session identity is retained.
- **Truth boundary:** an OSAT CTA trigger click is not a form submission or lead success. This retry generated no CTA or form evidence.
