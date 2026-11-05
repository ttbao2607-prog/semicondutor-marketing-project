> **Current observation04/11 supersedes03/11 status below:** [Day2 receipt](READBACK_2026-11-04.md): no displayed delivery,500K remaining, CPC25K checked;3 Eligible/25 Low search volume. Bid-strategy message is not evidence of CPC-cap restriction. [Advisor](ADVISOR_2026-11-04.md) proposal only. Broader content/attribution gaps unchanged. No mutations; PARTIAL/audit NOT_RUN.

# Google Search — handoff for future agents (02/11/2026)

**HANDOFF_ONLY.** Authority: Bảo (PO). No scheduled checks, reminders or automation exist or are authorised; Bảo opens Google Ads manually and tells an agent when to read. Findings below are claims to re-verify live; nothing here grants permission to change the account.

## Current state (as recorded 03/11/2026 ~10:30 +07:00, DIGIWIN SOFTWARE VIETNAM account)
- **Live campaign:** `SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261103]_500.000d-tong_10d_end20261112` — Enabled · Eligible (Limited) (sub-label: *Limited by bid strategy*), running 03/11/2026–12/11/2026; **campaign total budget ₫500,000**; Maximize clicks, max CPC limit checked = ₫25,000 (verified in UI); Search Network only; Vietnam (presence); vi/en/zh-Hans/zh-Hant; AI Max and final URL expansion off; goal = campaign-specific `Page views` (Bảo: keep; awareness run, not lead-conversion optimisation; reporting only).
- **Content (UI counts):** 16 ad groups, 28 keywords (4 Eligible, 24 Low search volume), 16 ads (all 16 approved Eligible as of 03/11), 115 asset associations (sitelinks Eligible), 25 campaign-level phrase negatives.
- **Delivery as of morning 03/11:** 0 impressions, 0 clicks, ₫0 cost (start date lag; not a performance verdict).
- **Old campaign** `…[20261102]_50.000d-ngay_10d_end20261111`: Paused (cost ₫0). **Copy `#2`: removed.** Do not re-enable the old campaign: it would run in parallel and break the ₫500,000 envelope.
- Origin of the change: the earlier campaign only had a daily budget (monthly limit ₫1.45M, daily up to 2×) and no max CPC; the ₫500,000 PO cap was not a platform-enforced cap. Details: `POST_AUDIT_PLAN.md`, `RECEIPT.md` (follow-ups), `CURRENT_STATE.md` top banner.

## Still unknown / open
- Delivery and spend pacing across the 10-day run (03/11–12/11). Delivery just started morning 03/11 (0/0/₫0); whether the total budget behaves as a hard ₫500,000 cap in practice is **not yet fully observed**; check the Budget report and cumulative cost as delivery accumulates.
- Not diffed item-by-item vs the old campaign: ad copy, sitelink URLs, UTM suffix (`utm_source=google&utm_medium=cpc&utm_campaign=vn_semiconductor_search_p1&utm_content=<seg>_<lang>_{rsa_v1|sitelink}&utm_term={keyword}` at ad/sitelink level); the negatives (25 vs old 24: one term differs, unidentified).
- Google's current total-budget guidance was taken from the post-audit plan's 02/11 source check, not re-verified.
- MSG-ANCHOR-01 and native review (EN/zh) NOT_RUN; brand-overlap check with other account campaigns NOT_RUN; 车规级/車規級 and other flagged claims kept verbatim; 24/28 keywords had Low search volume (not zero demand); attribution/gclid/form success not verified.
- No independent audit of the remediation.

## Rules for the next agent
1. Read `AGENTS.md` (Phase A), `CURRENT_STATE.md` top banners, `DOCS_IMPACT_MAP.md`, this file. Read-only first; get a specific mandate from Bảo for any live change (pause/enable, budget, bids, new campaign, URL/copy changes).
2. Do not edit the campaign, other campaigns, tags/conversions, landing pages or forms; do not submit leads; do not create schedulers.
3. Chrome notes: Google Ads may show a "Confirm it's you" passkey prompt — only Bảo completes it. The Create-campaign wizard can show "Changes failed to save"; reload and re-check before publishing. Pasting ad groups does not carry campaign negatives. Screenshots may time out; use element/text reads. Campaign/account IDs are not stored in the repo.
4. After any change: read back saved values after reload, then sync docs (README, CURRENT_STATE, `ads/google/Google_Search_Build_Sheet.md`, `drafts/S04_Measurement_and_Budget.md`, `operations/Pre_Ad_Readiness_Plan.md`, Index S01, `RECEIPT.md`) or state: **Docs impact reviewed: no canonical update required.**

## Git
Docs were merged into local `main` (merge `3549f1c9`, from branch `slice/google-search-post-audit-plan-2026-11-02`). **Not pushed to GitHub** — a push needs Bảo's instruction.
