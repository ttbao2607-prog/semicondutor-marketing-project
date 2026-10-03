# AD-ED-01 copy review receipt: F3 Handoff ImageGen R1

- **Revision:** `f3-handoff-imagegen-r1-prompt-v2-altmatch`
- **Input checkpoint:** `f3-handoff-p1-copy/copy-vi.json`, SHA-256 `1198cae4fa03d613e8237eedfb254d1d9f9c8f97320048f98bc4cea4d1bdea5f`.
- **Revised spec:** `copy-vi.json`, SHA-256 `e7ca439e069ef3ddce00c3b6325fdb43e12ae656c56aed15f621cdd6d01c8d1e`; generation calls used the preserved prompt-lock snapshot in `revision-history/copy-vi-at-imagegen-calls-before-card5-alt-match.json`.
- **Writer / review status:** `/root/fabless_imagegen` self-review applies to the initial copy and prompt checks only. The parent Coordinator independently inspected all eight selected native rasters and completed current offline desktop/mobile fixture QA at the scope recorded below.
- **Fields reviewed:** caption; per-card native headline, image headline, image body, alt and destination; Card 5 regional label, context and invitation; exact prompt-visible copy in every planned call. No source/footer field exists in this schema.
- **Verdict:** Parent review of all eight selected rasters and current offline desktop/mobile fixture QA are complete at the observed scope. The generated raster wordmark is approximate, so strict brand fidelity and the Product Owner decision remain open. This is not buyer, platform, content-approval, or live approval.

## Flagged strings and dispositions

| Source string / location | Classification and decision | Source and authority effect |
|---|---|---|
| `không phải dữ liệu khách hàng` appended to all ten card alt records (eight distinct images) | Internal generation/evidence safeguard. Removed from alt. Replaced with a concise description of the paper records, chip tray or folders visible in the intended scene. | No claim is lost; alt remains a visual description. Reconcile with actual generated pixels during artwork QA. |
| `không phải chứng cứ triển khai Fabless` in A5/B5 alt | Internal proof boundary. Removed from the customer alt; kept in this ledger and the source-pins evidence. | Keeps the country-attributed Taiwan source in the body and regional panel and the ERP/MES context without implying Fabless deployment; alt remains a visual description. |
| F3 A2: `Không mặc định mọi sản phẩm hoặc mọi đối tác đều dùng cùng một quy trình.` | Generalization boundary expressed as negative meta-copy. Rewritten as `Chọn một điểm bàn giao cụ thể trong luồng đã được các bên xác nhận, bắt đầu với sản phẩm đang xét.` | Keeps the necessary product/confirmed-flow scope in affirmative, reader-useful wording. |
| F3 B4: `chưa coi một sơ đồ chung là quy trình cho mọi đối tác.` | Generalization boundary expressed as negative meta-copy. Rewritten as `Ai gửi, ai nhận và ai làm rõ thông tin còn thiếu? Nhóm ghi trách nhiệm theo quy trình đã được hai bên xác nhận cho luồng đang xét.` | Names the actual next task and limits it to the confirmed flow under review; does not imply one universal process. |

## Retained operational scope

- F3 A4 keeps the instruction to follow the actual process confirmed by the parties; it is useful guidance, not a statement about agent confidence.
- F3 B3 keeps the format-versus-correctness distinction because different formats alone do not establish an error; the reader is told to compare against the agreed terms.
- The caption retains the first-use Fabless definition. The ERP/MES parenthetical exemption follows the 2026-10-02 PO/session mandate; shared canonical guidance has since been reconciled. No extra source-copy change was needed for ERP/MES.
- Card 5 keeps the exact Taiwan source attribution in the body and regional panel: `Tài liệu bán dẫn Digiwin tại Đài Loan đặt ERP và MES trong bối cảnh quản trị và sản xuất.` Its alt describes the observed bright desk, chip tray and Taiwan information panel. The Taiwan skyline is only a source-location editorial element. The source does not establish a Fabless deployment, and that boundary stays internal.

## 2026-10-02 native-artwork status

All eight planned native calls completed with fresh preflight exit 0 and all three canonical references. The selected native PNGs are 1254×1254; the parent independently inspected every visible word, Vietnamese glyph, header, sequence and blank prop. Parent passed copy, category/sequence and blank-prop scope for all eight; no extra readable text, internal disclaimer, fake record value or unsupported claim was observed. Parent completed current offline desktop/mobile fixture QA at the observed scope. The generated raster wordmark is approximate rather than the exact official logo; strict brand fidelity and the Product Owner decision remain open. The feed publisher header uses the canonical logo asset. See imagegen-execution-manifest.json and execution-receipt.md for per-call hashes and local output lineage.

After those calls, F3 A5/B5 alt was adjusted in the current candidate from a whiteboard description to a bright desk and information-panel description. The call-time spec is retained at revision-history/copy-vi-at-imagegen-calls-before-card5-alt-match.json; prompt fields and raster bytes did not change. Taiwan attribution remains in the body and panel.

The current ordered feed and standalone preview include all ten records and eight selected unique images. Parent browser review passed on mobile 390×844 and desktop 1707×817; all eight unique images were mobile-inspected, desktop had no horizontal overflow, keyboard dots/pointer transitions and local actions worked, and the standalone embedded images loaded. Touch/swipe was not checked. This status does not claim LinkedIn platform rendering, buyer acceptance or Product Owner approval.
