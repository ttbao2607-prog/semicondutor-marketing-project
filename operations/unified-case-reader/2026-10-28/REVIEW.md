# Unified reader correction review — 2026-10-28

Execution: **SUCCESS for bounded local technical correction**. Reviewer: Codex root, **SELF_REVIEW**, not an independent agent, PO acceptance or native-market review. Overall marketing/release verdict: **INSUFFICIENT_EVIDENCE**, not ready/accepted for live handoff.

## Local checkpoint authorization

After the correction review, Bảo requested “commit đi codex.” The containing commit checkpoints the bounded correction and its evidence on the existing slice branch. Pre-commit working-file statements below record the review capture time; they are not current post-commit status. No merge, push, deployment or release acceptance is authorized or performed. Docs impact rechecked: candidate README updated for checkpoint status; bounded CURRENT_STATE and entry-mapping notices remain accurate.

## Binding and scope

- Branch/base: `slice/executive-approval-launch-2026-10-28` / `813d3fcaab993180577dac822b8ffeaa94893b75`; edits are local working files, not staged/committed/merged/pushed.
- Authority: Bảo requested “Sửa luôn codex.” [Pre-edit plan](PLAN.md). The initial audit remains historical evidence, not a new content approval.
- Anchor: `operations/Vy_Email_Content_Anchor.md`, VY-CONTENT-ANCHOR, revision 1.0, SHA256 `6621d53c845939730ebcb1f59bbf85fb8a0d9acb156e5236e7387c0e69867ac5`.
- Original email: `operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md`, VY-MAIL-USER-20261006, SHA256 `c5a6f35533e7a8b3b439ec4d9a260611fcdd2f67ddb0f046a3e33d28c6316d2b`.
- Final HTML: `deliverables/unified-case-reader/unified-case-reader.html`, SHA256 `b83cd70d8008be26b195541593298042698aa163adf7583db2af7d7a2d65f0c4`, 905146 bytes. File hash is the working-file byte hash; future newline normalization changes it and requires fresh binding.
- Stage: PREGEN_SCRIPT retained in the plan before edits; POSTGEN_ARTIFACT/package inspection here. No image generation or retrospective SCRIPT_REVIEW_PASS.
- FDI reader destinations in vi/en/zh-Hans/zh-Hant; Vietnamese is a display locale, not a new VN_DOMESTIC persona. Live audience/entity fit is unknown. OSAT quality/operations/month-end, Fabless outsourced production/planning/handoff and Partner industrial-supplier record ownership/customer questions remain separate treatment contexts.

## Findings and closure

| Finding | Observed correction | Closure evidence |
|---|---|---|
| Offline viewer return gives 404 | Removed all 11 `index.html` anchors; no invented production return URL | Source parser and 44 desktop routes show no offline link; existing case/contact/source links retained |
| Lost shell | Restored `<main id="main" class="shell">` | 44 desktop routes: main width 1180 CSS px; visual F2 screenshot confirms matching header/content margins |
| Wrong shared-reader fallback | English when locale cannot be resolved; O1 when treatment cannot be resolved | Actual Chrome blank query, `?t=F2`, invalid t/lang, explicit-over-UTM and O4-Q UTM controls |
| Font dependency | Removed Google Fonts stylesheet; embedded assets remain data URLs | Parser finds no external automatic resource, CSS import or external CSS URL; system fallback typography is intentional |
| O2 copy discrepancy | Allowlisted source entry B4/B5/B6; B4/B5 keep parameter-revision/exception question, B6 keeps handoff-source/next-step question | All 33 source packs compared in all 4 locales (132 comparisons); B4/B5/B6 each tested through en→zh-Hant toggle and reload; original source files untouched |
| Language bar ARIA not translated | Updates outer language bar label from active copy | 44 desktop routes: all data-i18n and data-i18n-attr values match the active source pack |
| Unsupported documentation claims | Removed blocker-closed/one-step publish/automatic GTM inheritance; corrected real titles, 33 entry vs 44 display count and size | Package README; canonical current-state and entry-mapping notices |

## Actual browser evidence

Chrome browser 2, local loopback only. No external account or contact form action. Checks performed against the final HTML hash above:

- Desktop matrix: 44/44 direct t/lang routes; correct html lang, nonempty title, visible body, decoded case photo, all active copy/alt/ARIA values, 1180px shell, no horizontal document overflow, no index.html links. Zero failures.
- Responsive first pass: requested viewport390 yielded **actual434 CSS px** due existing browser zoom; 44/44 geometry/image/lang checks passed. It was not reported as390.
- Responsive second pass: tool viewport351 produced **actual390 CSS px**, verified via innerWidth; 44/44 routes have correct lang, visible body, decoded photo, >=20px left margin and no document overflow. Zero failures. These are DOM/geometry checks, not a full mobile visual/native-language PASS.
- Mobile screenshot capture failed twice: Page.captureScreenshot timed out after5000ms. Desktop screenshot after viewport reset succeeded and was inspected. No mobile screenshot/whole-page visual approval is claimed; viewport reset at exit.
- O2 B4/B5/B6: each tested en→zh-Hant, entry/UTM preserved in URL, focus on zh-Hant button, same source question retained after reload.
- Invalid `entry=https://example.invalid/` selected allowlisted B4 fallback; no arbitrary navigation. Explicit F2/en overrides a conflicting O1/zh-Hant UTM.

## MSG-ANCHOR-01 observations and limits

The source ledger [SOURCE_CHECKS.json](SOURCE_CHECKS.json) binds each of the33 entry routes and all132 source-locale packs to original source hashes and exact titles. No copy string was authored or translated. This establishes retention, not semantic PASS.

| Rule | Actual unit/surface observation | Disposition |
|---|---|---|
| A1 ICP/activity | O1 title “A shared starting point for quality review”; F2 “Three questions before the next outsourcing plan”; P3 “Scope the customer question before collecting records” remain distinct operational contexts | Retained; no claim that route/locale proves ICP fit or every semiconductor company is a target |
| A2 fit/decision unit | Case entities remain references, not proof of a visitor's buying authority; source packs unchanged | Live/entity fit unverified; no new exclusion or buyer claim |
| A3 persona/locale | Every source entry matched all4locale packs; explicit incoming lang wins, toggle does not change O2 source entry | Destination retention verified; no inference FDI=nationality or Vietnamese=domestic |
| A4 business value | F2 retains questions on demand change, affected outsourced lots, partner information source and confirmation responsibility; O2 retains both source-specific roles/records questions | Useful operational content retained; no new ROI%, savings/payback or outcome guarantee |
| A5 domestic readiness | All33 inventory entries are FDI destinations, including their Vietnamese display | N/A within this package; VN domestic journey not substituted or certified |
| A6 depth/capability | F2 retains “The source states the challenges and describes the solution only as integrated; it gives no detail on specific modules”; photo/illustration labels preserved | No invented module/MES replacement claim; not a fresh primary-source/rights certification |
| A7 continuity | Removed unavailable offline-viewer step; named case→published context→questions/value→actual next step/source remain in source order. F2 still discloses Vietnamese consultation destination; Partner gains no form/CTA | Reader-local retention verified; upstream ads and live handoff untested, so whole-journey evidence remains insufficient |

Proof ledger: OSAT case06 China and authentic2020 visit-photo attribution; Bright Power China with labelled illustration and challenge-only scope; Wafer Works Taiwan–Shanghai with labelled illustration and source-limited claims. No new financial metric, capability, local implementation proof or public/paid rights is asserted. Source copy equivalence does not newly verify the external source or resolve rights.

Remaining: no complete upstream cold→explanation→proof→reader→production CTA review, no native-market/full mobile visual review, no host/import runtime, exact live tags/consent/privacy inventory, rights or campaign eligibility verification. No ready/accepted marketing handoff while these required gates lack evidence. No further technical defect was found by the bounded checks; do not turn a green matrix into marketing acceptance.

## Documentation impact and Git boundary

Reviewed DOCS_IMPACT_MAP, CURRENT_STATE, FDI destination contract/inventory, reader entry mapping, LadiPage runbook, tracking/readiness context. Updated only the candidate README and bounded candidate notices in CURRENT_STATE and entry mapping. Existing source-reader/runbook/tracking status remains unchanged; no new operational business decision. Executive launch vs corrected-branch discrepancy is recorded, not reconciled by this task. No frozen core, ad, source-reader, account, Git history or live mutation.

Auditor target: rerun `python operations/unified-case-reader/2026-10-28/verify_package.py`, compare its artifact/source hashes with this receipt, inspect the diff and repeat the specific browser behaviors if needed. Root self-inspection cannot claim independent AUDIT_PASS; overall audit **INSUFFICIENT_EVIDENCE** for release.
