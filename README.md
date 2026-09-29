# Digiwin Vietnam Semiconductor Paid

Marketing operations workspace for planning and governing paid semiconductor activity. This is not an application or software project.

## Status

Canonical execution active. The three semiconductor landing routes were published under the completed Phase 3 mandate and republished on 2026-09-25 with the approved shared GTM container. The route-scoped copy-listener exclusion was Preview-verified and Bảo published it as GTM Version 51, now shown as `Live, Latest`. Phase 4 tracking/lead validation is closed for all three routes. The Phase 5 independent audit and desktop/mobile Chrome-controlled runtime matrix are recorded in the Phase 5 evidence ledger; closeout is `PASS WITH SCOPE EXCLUSION` for OSAT, Fabless and Supplier/Partner. Bảo excluded consent-behavior verification from Phase 5 and clarified LinkedIn will use native in-platform ads, so delivery reporting follows authorized campaign delivery in Campaign Manager. The scope exclusion does not verify consent behavior. Campaign enablement and spend are not authorized by this closeout. On 2026-09-27 the compact mobile UI was published on the three existing LadiPage URLs, with Save/reopen, public responsive, PopupX, CTA inventory and section tracking smoke checks recorded in `operations/evidence/mobile/2026-09-27-mobile-live-deployment.md`; the source commits remain local only.

The separate PageSpeed P4/P5 scope is closed and frozen by Bảo's 2026-09-29 **partial acceptance**. The P4 source revision `eb88b8e` is live on the same three URLs, with desktop Lighthouse scores 88/87/86. Two production Mobile runs per route scored OSAT 57/53, Fabless 48/58 and Partner 49/54, below the original ≥80 gate. This is an accepted business exception, not a technical performance PASS; the three LadiPage revision receipts remain pending formal closeout. See `operations/evidence/performance/2026-09-29-p4-p5-partial-acceptance-closeout.md`. The feature branch can be published independently of `main`; no merge is implied by this closeout.

Sanitized validation status: Google Campaigns, Ad groups, Settings and Keyword Planner are functional; the orange objective-update banner is informational/non-blocking. Keyword Planner research completed for OSAT, Fabless and Partner: OSAT/Fabless had no displayed metrics and Partner had one limited historical estimate; demand remains unvalidated. LinkedIn Research Phase 1 (sanitized external read-only validation) completed on 2026-09-14; production account/audience/object readiness remains pending.

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
