# Digiwin Vietnam Semiconductor Paid

**Carousel awareness decision (2026-10-01):** Bảo chọn carousel images + introductory copy, kể chuyện theo card để định vị Digiwin là ERP có chuyên môn và kinh nghiệm ngành semiconductor. Anchor audit/spec/artifact: [LinkedIn_Carousel_Constraints_and_Awareness_Anchor.md](operations/LinkedIn_Carousel_Constraints_and_Awareness_Anchor.md). Điều này supersede static mặc định và format-open trong wave tối ưu awareness, cùng Company-Page-only destination baseline cho carousel này: mỗi ad chọn một trong ba LDP đúng route để đọc thêm; URL vẫn required nhưng mục tiêu native awareness không click-driven. Đây là positioning intent, không tự xác nhận claim kinh nghiệm/capability hoặc brand lift. Cohort/POV pair/locale/C, budget và live authority chưa chốt; chưa sản xuất hoặc upload. Format/anchor docs đã được checkpoint local tại 67067c4; chưa merge main hoặc push GitHub.

Marketing operations workspace for planning and governing paid semiconductor activity. This is not an application or software project.

## Status

**2026-09-30 Fabless interaction checkpoint:** local main now includes repair `2e52bf1` for map tabs and pain-card navigation, with local browser evidence and tracking regression 12/12. Deployment preparation is held before live action while another Codex process deploys the previous main, as requested by Bảo. The source is pinned and the bounded delta is prepared in `operations/deploy/fabless-interaction-2026-09-30/PROCESS.md`; the request template is not production-authorized. Reconcile the other process's completed live baseline before resuming. No live repair or GitHub push is claimed by this checkpoint.

Canonical execution active. The three semiconductor landing routes were published under the completed Phase 3 mandate and republished on 2026-09-25 with the approved shared GTM container. The route-scoped copy-listener exclusion was Preview-verified and Bảo published it as GTM Version 51, now shown as `Live, Latest`. Phase 4 tracking/lead validation is closed for all three routes. The Phase 5 independent audit and desktop/mobile Chrome-controlled runtime matrix are recorded in the Phase 5 evidence ledger; closeout is `PASS WITH SCOPE EXCLUSION` for OSAT, Fabless and Supplier/Partner. Bảo excluded consent-behavior verification from Phase 5 and clarified LinkedIn will use native in-platform ads, so delivery reporting follows authorized campaign delivery in Campaign Manager. The scope exclusion does not verify consent behavior. Campaign enablement and spend are not authorized by this closeout. On 2026-09-27 the compact mobile UI was published on the three existing LadiPage URLs, with Save/reopen, public responsive, PopupX, CTA inventory and section tracking smoke checks recorded in `operations/evidence/mobile/2026-09-27-mobile-live-deployment.md`; the source commits remain local only.

The separate PageSpeed P4/P5 scope is closed and frozen by Bảo's 2026-09-29 **partial acceptance**. The P4 source revision `eb88b8e` is live on the same three URLs, with desktop Lighthouse scores 88/87/86. Two production Mobile runs per route scored OSAT 57/53, Fabless 48/58 and Partner 49/54, below the original ≥80 gate. This is an accepted business exception, not a technical performance PASS; the three LadiPage revision receipts remain pending formal closeout. See `operations/evidence/performance/2026-09-29-p4-p5-partial-acceptance-closeout.md`. The feature branch can be published independently of `main`; no merge is implied by this closeout.

Sanitized validation status: Google Campaigns, Ad groups, Settings and Keyword Planner are functional; the orange objective-update banner is informational/non-blocking. Keyword Planner research completed for OSAT, Fabless and Partner: OSAT/Fabless had no displayed metrics and Partner had one limited historical estimate; demand remains unvalidated. LinkedIn Research Phase 1 (sanitized external read-only validation) completed on 2026-09-14; production account/audience/object readiness remains pending.

**2026-09-29 offline planning update:** Bảo chose `vi/en/zh-Hans/zh-Hant` (three languages, four locale variants) on the three existing URLs, with one HTML per route, a top switch and non-PII `lang` query for initial paid entry. All three route HTML/copy files are complete offline four-locale candidates combined with the 2026-09-29 PageSpeed source in local integration commit `6fa842e`, with tracking and 320px/desktop four-locale runtime checks passing. LinkedIn four-locale source copy is registered, and Stage A has rendered and visually checked nine localized static SVG/PNG assets and three localized six-page PDFs offline. The localized carousel candidate batch has 12/12 offline 1254×1254 cards with QA; localized CAR-01/02 omit the `200+`/`700+` metrics. Nine planned B2B v2 variants (`vi`/`zh-Hans`/`zh-Hant` across the three concepts) are rendered offline; no new EN B2B image is claimed. The published LadiPage routes remain Vietnamese; a separate 2026-09-29 PageSpeed revision was published at the same URLs. Its scope closed as `P4_P5_CLOSED_PARTIAL_ACCEPTANCE_FROZEN` with live Mobile below 80 and revision receipts still PENDING; locale behavior is not live. The PageSpeed production closeout above remains unchanged by these offline locale candidates. Bảo approved full use/translation of case/claim already in the Vietnamese source, subject to exact scope and translation QA; this does not approve new claims or named/logo proof on abstract CAR-03. Bảo set a 35 million VND ceiling through Scale 1 over eight calendar weeks; the paid-day schedule and Scale 2 approval are separate. This is no authority to enable campaigns or spend. These integrated files are committed locally as `6fa842e`; no GitHub push or live locale publication is evidenced. The original workspace local `main` reached docs commit `2099d9e` after integration `6fa842e`; use `git worktree list` for the current checkout count.

## Source hierarchy

Current instruction from Bảo > `Semiconductor_Work_Kickoff.md` v2.0 > `Semiconductor - Website & Ads.md` > `AGENTS.md`.

## File map

- `AGENTS.md` — workspace rules and trust boundaries.
- `Semiconductor_Work_Kickoff.md` — paid operating plan and slice contracts.
- `Semiconductor - Website & Ads.md` — source brief and website context.
- `drafts/` — S01–S04 research and planning drafts.
- `operations/Pre_Ad_Readiness_Plan.md` — canonical pre-ad execution plan and launch gates.
- `operations/Public_Source_Register.md` — public source and sanitized UI-status register.
- `tracking/Semiconductor_Tracking_Contract.md` — candidate event/UTM contract and QA matrix.
- `ads/` — offline Google and LinkedIn build packs.
- `landing/` — canonical local route sources; the three existing LadiPage routes include the 2026-09-27 compact mobile update and the 2026-09-29 frozen PageSpeed P4 revision. Later publication changes require a new scope and mandate.
- `assets/linkedin/` and `output/pdf/` — offline creative deliverables.

## Public boundary

Only sanitized marketing material belongs in this repository. Do not commit credentials, tokens, cookies, browser/session state, PII, raw lead/audience/contact exports, private account data, or unverified proof presented as fact. Public-source observations remain distinct from authenticated account evidence.

## Collaboration model

`main` is canonical. The initial baseline is the sole direct-main exception. Future executor work uses an isolated worktree and an owned `slice/<slice>-<short-name>` branch. One writer owns each shared file; avoid direct shared-file conflicts. The Coordinator audits diffs and merges approved work.

This repository has no CI, application code, product architecture, issue bureaucracy, or automatic campaign execution.

## Four-locale production deployment (2026-09-30)

The `vi`, `en`, `zh-Hans` and `zh-Hant` revisions are published and publicly verified on the existing OSAT, Fabless and Supplier/Partner URLs. This supersedes the 2026-09-29 planning note above where it says the routes remain Vietnamese and locale behavior is not live; that note records the pre-deployment snapshot. The separate PageSpeed partial-acceptance result is unchanged. See [the route-by-route deployment checkpoint](operations/evidence/locale/2026-09-30-four-locale-production-deployment.md) for readback hashes, receipts and responsive evidence. No campaign or spend authority is implied.
