# First-touch review anchor

## Bảo first-mention clarity instruction, 2026-10-02

For **future ad-copy revisions across all cohorts and formats**, give a short, source-checked, locale-matched explanation in parentheses at the first customer-visible occurrence of each abbreviation/acronym that is not covered by an explicit exception, and of the named industry labels **OSAT** and **Fabless**, in each independently encountered ad. Place it naturally in the caption/intro or first visible text before an unexplained acronym chain; one clear first mention is enough, not every card. Example Vietnamese wording to validate against the actual source/scope: `OSAT (dịch vụ đóng gói và kiểm thử bán dẫn thuê ngoài)`; `Fabless (doanh nghiệp thiết kế chip, không sở hữu nhà máy chế tạo)`. If WIP or another non-exempt abbreviation appears, explain that first occurrence briefly using a verified definition; do not infer product capability from a term definition. Adapt wording to language, role and channel limits by rewriting nearby copy, not silently dropping the needed explanation or exceeding native character constraints.

**Current PO exception, 2026-10-02:** ERP and MES are common industry terms and do not require parenthetical first-mention explanations under Bảo's same-day mandate. The deterministic preflight implements this exception by checking OSAT, Fabless and WIP while not requiring ERP/MES definitions (`scripts/verify_imagegen_preflight.py`, `FIRST_MENTION_TERMS`). Do not extend this exception to WIP, OSAT, Fabless or other abbreviations.

This is a PO editorial instruction for later copy, not a retroactive edit or buyer-validated rule. Current P1 and Operations/Quality copy, PNG, demo, manifests, receipts and pinned historical hashes remain their recorded revisions. Existing first-touch anchor status stays `PO_ACCEPTED_TESTING_NON_CANONICAL`; visual freeze and all content/live review gates remain. Source context: `Semiconductor - Website & Ads.md` line 19 connects OSAT with packaging/testing; line 42 names IC Design/Fabless.

## Current PO acceptance, 2026-10-01

`PO_ACCEPTED_TESTING_NON_CANONICAL`. Bảo: “Đúng ý Bảo rồi, chốt anchor này vào status là Bảo acceptance, vẫn chưa canonical do chưa test thật. Sau đó chạy pilot tiếp theo trên R2 nhé.”

Acceptance áp dụng anchor và hướng mở đầu first-touch r2: ai nói, với ai, tình huống gì, vì sao nghe tiếp. Không suy ra buyer validation, hiệu quả paid, fullchain/story3–5/content release/live acceptance. R1 vẫn NEEDS_CHANGES trong review lịch sử; r2 ảnh/copy/demo/manifest giữ nguyên. Những dòng READY/preflight phía dưới là snapshot trước acceptance này, không phải current anchor status. Tiếp theo chỉ critical pilot A3/A5 với preflight copy và human review.

2026-10-01 · TESTING_NON_CANONICAL; PO-directed editorial hypothesis, not buyer-validated performance rule. Bảo asks a new first-touch revision after r1: the opening must answer who speaks, who is addressed, what situation is discussed and why continue. Parent-relayed review: r1 feels like remarketing because consultant identity and reader situation are not explicit enough. This sentence is a paraphrase, not an invented verbatim quote.

## Four questions before procedural/detail cards

1. **Ai đang nói?** Caption introduces Digiwin and bounded ERP consulting/category scope. Logo alone does not establish that role for a cold reader.
2. **Đang nói với ai?** Cover names nhóm chất lượng OSAT, not only generic records or steps.
3. **Đang nói về việc gì?** Cover/body identify semiconductor operations and abnormal-test review/coordination, conditionally; no case/prevalence claim.
4. **Vì sao nghe tiếp?** Useful management lens: shared record/lot/result-time basis for coordination. Technical cause distinction can develop later, not a checklist invitation before orientation.

No B2C fear/curiosity hook, em/en dashes, weak meta labels, fake records/ticks/cases/years/results. Preserve Taiwan qualification and ERP/MES separation when used later. Consultant identity does not imply proven deployments/experience or guarantee. r1 and all baseline PNG/copy/demo/manifests immutable; r1 NEEDS_CHANGES for first-touch, not discarded evidence.

## Revision and review receipts

- r1 actual pilot: cold-feed-opening-pilot-r1/; technical scope safe and actualdemo observed, but PO first-touch content not accepted.
- r2: cold-feed-opening-pilot-r2/; new PO requested revision, not reset of previous correction reserves. Parent preflight accepts pilot implementation only; human acceptance remains READY.
- Common r2 opening for A/B; exact card2 A2v3/B2v2 retains first transition to lot/stage/time. Two-card fixture is partial2/5, later3-5 drafts not rendered. Compare entry/first transition, not live final ad or causal A/B performance.
- Any changed copy/image rebuilds currentdemo/source-map/manifest and invalidates old approval. Human receipt must record explanation of the four questions from cold-feed view, desktop/mobile observations and accept/edit/hold per revision, not infer understanding from source text or visual approval.

Entry: cold-feed-opening-pilot-r2/README.md and manifest.csv pin this anchor as external reference with hash. Existing canonical human audit runbook governs demo/human review. Scope outside current carousel needs separate mandate.
