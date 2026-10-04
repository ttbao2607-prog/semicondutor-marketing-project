# AD-ED-01 copy review receipt: F2 Forecast ImageGen R1

- **Revision:** `f2-forecast-imagegen-r1`
- **Input checkpoint:** `f2-forecast-p1-copy/copy-vi.json`, SHA-256 `1eebe2873e5b1b520439512ff5f8a7f074ae771e675bd28dfc4412685f9e032c`.
- **Revised spec:** `copy-vi.json`, SHA-256 `51c2485e48b60551d0732dc1d3d96fc22949716411fd2296de1bc89154de782c` (current active alt-match revision; generation-call snapshots are preserved in `revision-history/`).
- **Writer / review status:** `/root/fabless_imagegen` self-review applies to the initial staged checks only. The parent Coordinator independently inspected all eight selected native rasters and completed current offline desktop/mobile fixture QA at the scope recorded below.
- **Fields reviewed:** caption; per-card native headline, image headline, image body, alt and destination; Card 5 regional label, context and invitation; exact prompt-visible copy in every planned call. No source/footer field exists in this schema.
- **Verdict:** Parent review of all eight selected rasters and current offline desktop/mobile fixture QA are complete at the observed scope. The first A1/B1 image remains a retained editorial failure; the separately logged correction was selected and the parent closed that native finding. The generated raster wordmark is approximate, so strict brand fidelity and the Product Owner decision remain open. This is not buyer, LinkedIn platform, content-approval or live approval.

## Flagged strings and dispositions

| Source string / location | Classification and decision | Source and authority effect |
|---|---|---|
| `không phải dữ liệu khách hàng` appended to all ten card alt records (eight distinct images) | Internal generation/evidence safeguard. Removed from alt. Replaced with a concise description of the paper records, chip tray or folders visible in the intended scene. | No claim is lost; alt remains a visual description. Reconcile with actual generated pixels during artwork QA. |
| `không phải chứng cứ triển khai Fabless` in A5/B5 alt | Internal proof boundary. Removed from the customer alt; kept in this ledger and the source-pins evidence. | Retains the truthful country/source wording `tài liệu bán dẫn Digiwin tại Đài Loan` and the ERP/MES context without implying Fabless deployment. |
| F2 A2: `Với một thay đổi dự báo giả định... Đây là phạm vi cần kiểm tra, chưa phải lịch sản xuất mới.` | Scenario disclaimer / process caution. Rewritten as `Khi dự báo thay đổi, nhóm đối chiếu sản phẩm, kỳ kế hoạch và các lô liên quan trước khi trao đổi với đối tác.` | States the useful planning action without claiming a new schedule or Digiwin product outcome. |
| F2 B4: `Câu trả lời tạo căn cứ thảo luận, không bảo đảm lịch giao hàng.` | Guarantee disclaimer. Rewritten as `Thông tin nào cần đối tác xác nhận, ai đối chiếu và khi nào trao đổi lại? Sau đó, hai bên có cơ sở bàn bước tiếp theo theo dữ liệu hiện có.` | Keeps the partner-confirmation step and bounds the discussion in available data without an ad-facing disclaimer. |

## Retained operational scope

- F2 A4 keeps the dependency on actual data and the parties' agreement; it scopes the decision a reader must make.
- F2 B3 keeps the timestamp-versus-delay distinction because an update-time difference does not by itself establish late progress; it gives the reader a useful interpretation check.
- The caption retains the first-use Fabless and WIP definitions. The ERP/MES parenthetical exemption follows the 2026-10-02 PO/session mandate; shared canonical guidance has since been reconciled. No extra source-copy change was needed for ERP/MES.
- Card 5 keeps exact Taiwan source attribution in body, alt and regional panel: `Tài liệu bán dẫn Digiwin tại Đài Loan đặt ERP và MES trong bối cảnh quản trị và sản xuất.` The Taiwan skyline is only a source-location editorial element. The source does not establish a Fabless deployment, and that boundary stays internal.

## Remaining checks

Native raster QA and current offline fixture/structural review are complete at the parent-observed scope. Product Owner decision remains open because the generated raster wordmark is approximate; touch/swipe was not checked, and no LinkedIn or buyer validation is claimed.

## Initial Card 5 native image inspection (historical staged check)

F2_CALL_A5_B5 was generated and inspected at 1254×1254. Header/category/sequence, headline/body, regional title, country-attributed source line, Fabless invitation, five folders and Taiwan skyline match the current spec; no extra text or disclaimer observed. At this historical staged check, writer self-review was complete and parent review was still pending. After viewing the actual artwork, the Card 5 alt was changed from `...trên bảng trắng...` to `...trên nền sáng...` to match the bright tabletop/background; the previous spec is retained in `revision-history/`. This alt-only adjustment does not change visible artwork.

At the initial stage, A1/B1 had `EDITORIAL_QA_FAIL_REFERENCE_TEXT_DRIFT` due to the three unplanned labels. The later correction is recorded below; the original remains preserved and excluded from the feed. At that time, full-pack native and desktop/mobile offline-demo QA was still pending; the completed current scope is recorded below. Any future internal disclaimer or unsupported visible statement is `EDITORIAL_QA_FAIL`; retain the failed artifact and use only a justified, targeted correction.


## Initial A1/B1 artifact finding (2026-10-02; original attempt)

The first native image passed main-copy/header inspection but displayed three extra, unapproved process-tile labels copied from the style anchor: `Mã lô`, `Công đoạn`, and `Thời điểm kiểm thử`. They are not present in F2 source copy and change the forecast scene toward a testing workflow. Classification: reference-derived customer-facing text drift. Verdict: `EDITORIAL_QA_FAIL_REFERENCE_TEXT_DRIFT`. The original 1254×1254 PNG remains preserved at `f2_p1_r1_a1_b1.png`, SHA-256 `64cde4a822ba5fe8907013448fc4c499188ec58859ca93ca56de2ee2592b375c`. When this finding was logged, a targeted correction awaited parent review of A5/B5; the correction was later generated and selected, and its closure is recorded in the current status below. The active prompt-lock revision explicitly restricts visible text and requires blank, unlabelled paper/process props.

## 2026-10-02 current rendered-artwork status

Parent released the staged generation gate after reviewing A5/B5. The first A1/B1 raster remains a retained editorial failure because it copied three unapproved process labels from a style anchor. The single separately logged correction removed those labels; parent reviewed the correction and closed the native finding. All eight selected rasters passed parent native-image inspection for exact visible copy, header/category/sequence, lack of extra readable text, and lack of fake values or internal disclaimers. Parent completed current-build offline desktop/mobile fixture QA at the observed scope. The generated raster wordmark remains approximate, so strict brand fidelity and the Product Owner decision remain open. No LinkedIn platform, buyer, or human content approval is asserted.

Selected A1/B1 asset: `f2_p1_r1_a1_b1-correction-1.png`, SHA-256 `c1aaab8dd26a4ee7bfee89cc561da3edc656f2093fa9167afd9444054831f17a`. It uses only the three canonical references and the strengthened blank-prop/visible-text whitelist prompt. The original `f2_p1_r1_a1_b1.png` remains unchanged and excluded from the feed.
