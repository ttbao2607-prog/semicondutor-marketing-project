# Ad artifact editorial QA gate

2026-10-02 · Bảo PO instruction after RMK R3 rejection. Applies to future paid-ad copy and finished artwork in this workspace, including awareness and RMK carousel images. Does not authorize production/live work. Canonical review loop remains LinkedIn_Awareness_Demo_and_Human_Audit_Runbook.md.

## Rule

**Mandatory message alignment, effective 2026-10-06:** [VY-CONTENT-ANCHOR](Vy_Email_Content_Anchor.md), gate **MSG-ANCHOR-01**, applies in addition to AD-ED-01 to every VN-domestic / FDI en/zh-Hans/zh-Hant content artifact. Original email evidence is now supplied by Bảo; old internal reconciliation is not the only source. Check the current anchor before pregen and reread during postcheck. A polished, accurate-looking artifact can still fail audience/persona/message alignment.

Repo/audit constraints govern what may be claimed; they are not advertising copy. Do not expose agent self-protection, proof classification, validation status or policy reasoning in caption, artwork, native headline, alt text, CTA or customer destination text. Customer copy must convey useful supplier/case information with warranted authority. This is not permission to exaggerate, fabricate or remove a qualification necessary to prevent a misleading claim.

Use concrete entity/market/result attribution to scope a claim naturally. Keep research gaps, rights decisions, uncertainty about generalization and negative mechanism boundaries in internal ledger/contract/audit. When a claim cannot be supported, narrow or replace it with a supported statement rather than append an agent disclaimer to an otherwise broad claim. If ambiguity materially persists, hold that claim internally.

| Text type | Disposition |
|---|---|
| Named case, country, exact published result, publisher/source or useful terminology definition | Customer-relevant; retain naturally where needed for truthful understanding. |
| “Case về quản trị vận hành; không chứng minh xử lý kiểm thử bất thường.” | Reject from ad: internal proof-match boundary. Keep in audit; show actual case topic/result in ad instead. |
| “Chưa xác minh”, “hypothesis”, “pending approval”, “không phải buyer validation”, “theo quy tắc repo”, “unsupported claim” | Internal process language; reject from customer surfaces. |
| “Không phải cam kết cho nhà máy khác”, “một bằng chứng để tham khảo”, repeated “được công bố” | Flag for semantic review, not universal prohibited words. Ask whether the sentence prevents a real misunderstanding or merely narrates agent caution. Prefer concise named-case attribution over boilerplate. |
| Source/market removed while an individual result is phrased as universal performance | Reject for misleading scope. Passing editorial QA cannot bypass factual/rights QA. |

## Mandatory mechanism

1. **Copy preflight before generation.** Writer examines every customer-facing field including `source`/footer and alt. Keep separate `internal_notes`/ledger so an internal note is never auto-rendered as footer. Record flagged strings and their disposition. Simple keyword search is an aid, not evidence of semantic PASS.
2. **Post-generation artwork inspection.** After assets exist, inspect every native image and visible text in the actual desktop/mobile demo. Reconcile all visible wording with exact copy, including generated labels and small print absent from copy JSON. OCR/transcription can assist, but actual image inspection is mandatory; matching an image to bad source copy does not pass this gate.
3. **Reader-purpose check for every flagged sentence.** Does it answer who Digiwin is, what it did, which case/result is relevant or how to investigate? Or is it describing agent confidence/classification/approval? Is a needed scope qualifier already carried by entity/market/attribution? Record reason to keep/rewrite/remove and source impact. Do not auto-delete all negative phrases or qualifiers.
4. **Gate receipt before handoff.** Reviewer records revision + copy/image/demo hashes, surface/card/exact string, classification, effect on supplier authority/truthfulness, action/owner and closure evidence. Use a reviewer distinct from writer when assigned; otherwise label self-review, independent audit pending. No simulated reviewer or PO acceptance.
5. **Closure on corrected artifacts.** Any leaked internal explanation on a customer surface = `EDITORIAL_QA_FAIL`, blocks ready-for-human-review content handoff. Correct exact copy, regenerate/edit affected raster, rebuild demo/manifest and inspect affected image/feed views. Deleting text in JSON while old image still displays it cannot close the finding. Missing actual artwork inspection = `INSUFFICIENT_EVIDENCE`. A semantic pass with truthful scope retained is `EDITORIAL_QA_PASS`, not content/buyer/live approval.

The current milestone may record a failed immutable revision and receipt without correcting it; do not call that artifact ready. This audit mandate adds the gate and records R3 failure only, not R4 production.

## Receipt fields

MSG-ANCHOR-01 binding is mandatory in PREGEN_SCRIPT and POSTGEN_ARTIFACT receipts: anchor path/ID/current revision/SHA256, original-email record path/hash, branch/persona/route/locale, A1–A7 findings, exact strings/scenes on all surfaces, business-value/readiness/proof/CTA mapping, per-unit and transition closure, real reviewer and independence. Use [message receipt template](templates/Message_Anchor_Review_Receipt_Template.md), linked from the editorial receipt. FDI requires persona-specific business value/ROI framing without invented returns; VN requires ERP as a preparation bridge, without automatic qualification/audit/order promises. Email budget, platform/schedule and targeting proposals are not artifact anchors.

MESSAGE_ANCHOR_FAIL => CHANGES_REQUIRED and blocks SCRIPT_REVIEW_PASS/generation plus ready/accepted handoff. Missing receipt/current anchor hash or stage-required inspection => INSUFFICIENT_EVIDENCE and also blocks those states. POSTGEN_NOT_RUN is explicit at pregen, not a failed image test. MESSAGE_ANCHOR_PASS is separate from editorial/source/rights/native/human/live verdicts; no mechanical or historical PASS overrides it. Changed anchor/persona/locale/copy/proof/order/scene/destination requires affected-scope recheck. Saving a clearly labeled failed/pending checkpoint remains allowed.

Gate ID `AD-ED-01`; revision; checkpoint/input hashes; writer/reviewer and independence; copy fields reviewed; ordered native images; desktop/mobile evidence; each flagged exact string/surface; internal-process versus customer-useful classification; source/authority impact; keep/rewrite/remove decision; correction revision/hash and rendered closure; verdict and remaining unknowns. An empty keyword finding list is not a completed image/semantic review.

## R3 observed regression

R3 at `fe5c127`, card R4 source/footer: **“Case về quản trị vận hành; không chứng minh xử lý kiểm thử bất thường.”** Appears in exact copy and final raster/demo. PO rejects this draft-style caution. Verdict `EDITORIAL_QA_FAIL`, content `AD_COPY_FAILED / CHANGES_REQUESTED`. R3 card R3 footer “Kết quả không phải cam kết cho nhà máy khác.” and explanatory “Một bằng chứng vận hành để tham khảo…” also require this editorial review before a corrected revision, without inventing a universal result.

Next revision must retain concrete proof but express authority through facts: named company/case, market, Digiwin role and attributed result. Keep adjacent-pain/non-generalization reasoning internal. Proof selection/rights/account boundaries remain unchanged.
