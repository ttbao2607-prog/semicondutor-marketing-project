# Discovery week1 consolidated pre-upload package - 2026-10-08

## Quyết định cần Bảo chốt

Đã hoàn tất gói đề xuất giữ nguyên 424 dòng. Chưa upload và chưa khóa file để upload. Có 18 ánh xạ hiện tại sai: 3 dòng có Page thay thế được đề xuất, 15 dòng chưa có Page thay thế đủ bằng chứng. Thay đổi định danh chưa chứng minh LinkedIn sẽ ánh xạ đúng sau này.

Đề nghị giữ nguyên danh sách gốc và tạm dừng upload, xử lý một gói ngoại lệ tổng hợp. 210 dòng chưa xuất hiện trong bản capture vẫn chưa rõ nguyên nhân; không kết luận các dòng này bị mất hay không match. Chỉ tạo tập upload rút gọn nếu Bảo quyết định rõ phạm vi mới; bản này chưa xóa dòng nào. Parent audit is recorded separately in linked AUDIT.json; writer structural review is separate from audience quality.

Preparation is complete for one consolidated review. Recovery remains **PARTIAL**, audience quality **CHANGES_REQUIRED**, and upload **HOLD**. The proposed CSV preserves all424 source rows; it is not an approved or locked upload file.

| Evidence unit | Result |
|---|---|
| Source ledger |424/424 rows have a research/reconciliation disposition |
| Current captured matched entries |150 entries: 11 supported entity pairs, 18 wrong, 121 insufficient |
| Captured unmatched |93 entries:64 exact current projections,28 older/different projections,1 duplicate-source ambiguity |
| Proposed CSV changes |12 identifier cells on 11 source rows; website/Page only |
| Protected source |424 rows/order/duplicates and8 protected fields match both accepted and immutable originals |
| Source coverage |210 rows not observed in capture;11 current projections appear in both tables; causes unresolved |

These counts describe different units: source-row verdicts and150 matched-entry verdicts are reported separately in the private package.93 unmatched entries must not be treated as93 distinct companies or a current match-failure backlog. All28 different-projection entries have an observed30Sep date and explicit field differences; those dates and older local projection matches support version reconciliation, not a proven backend cause. The one duplicate ambiguity retains both source rows.

The current output audit identifies 18 known-wrong source mappings. Exact replacement Pages are proposed for 3 of those; 15 remain without an accepted replacement Page. Identifier edits do not make those current output mappings correct. The full private exception pack covers the unresolved identities, mappings and coverage together.

Recommended decision: preserve the424-row master and HOLD upload while the known-wrong cases without exact replacement Pages remain unresolved. Resolve the entire exception pack together. A reduced upload set is a possible new PO decision only; no rows were removed and no reduced file was created. After decisions are reflected in a concrete file, its exact revision/hash must be approved before a single existing-audience update.

Identity evidence is separate from supply-chain ICP, FDI/domestic classification, persona/locale and local ERP purchasing authority. No company is excluded or labeled suitable from its name, brand, language or group alone. No ROI, product capability, proof-rights, creative, CTA or journey acceptance is claimed.

Local source history supports the accepted424-row file submission once on06Oct and saved filename readback. Server bytes were not downloaded; the current aggregation, partial coverage and mixed date-added results remain unexplained. Unobserved rows are not declared dropped or unmatched. No match-rate arithmetic is inferred from150/(150+93).

The public report contains sanitized counts and hash bindings. Company/source/account details and row-level decisions remain private. [Hash bindings](hash-pins.json), [message-anchor review](message-anchor-review.json), [execution record](execution-record.json), and [parent audit](AUDIT.json) accompany this report. Parent audit is recorded separately in linked AUDIT.json; writer structural review is separate from audience quality.

All new work is local working-tree preparation on the existing checkpoint branch. Nothing in this preparation was staged, committed, merged to main or pushed. No upload, account/campaign/settings/budget/spend/support/scheduling action occurred. Earlier R5/Master203 observations and dated receipts remain unchanged; core/locale-adapter/creative/landing/tracking scopes are unchanged.
