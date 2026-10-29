# Asset và lựa chọn khi review

Đây là nguồn để Bảo chọn, không mới duyệt creative hay tạo ad. [Exact F1/F2 candidates](../../pre-ad-readiness/2026-10-29/f1-f2-cycle/BUILD_CANDIDATES.csv) vẫn là snapshot pre-build; status cold cũ được supersede bởi saved/activation receipts, không sửa hash-bound CSV cũ.

| Lựa chọn | Có gì trong repo | Khi dùng / gate còn cần |
|---|---|---|
| Giữ F1/F2 cold | Hai actual ads đã launch schedule, URL riêng t=F1/F2&lang=en; [B13 F1](../../../deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v5/index.html), [B16 F2](../../../deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B16-en-f2-v2/index.html) | C3/C7 hoặc phần có tín hiệu; lịch sauW1 cần Bảo chọn. Không giả equal delivery |
| Giải thích F1/F2 | Hai carousel6cards: partner reports/lot-stage-time-owner choF1; demand change/replanning choF2, native headlines/alt/copy trong candidates | C5/C6; exact native source eligibility/objective/URL/order/preview cần dựng và kiểm sau mandate |
| Proof F1/F2 | Hai carousel4cards, Bright Power China, manufacturing/outsourcing-management challenges; không KPI outcome | C5/C6; giữ scope case, không ngụ ý ROI%/module/outcome chưa chứng minh. [PO existing paid-asset acceptance](../../pre-ad-readiness/2026-10-29/f1-f2-cycle/PO_PAID_ASSET_ACCEPTANCE.md) giữ hiệu lực đúng set, không xin lại |
| F3/B19 English | [Journey source](../../../deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B19-en-f3-v1/index.html) và [comparison](../../pre-ad-readiness/2026-10-29/library-reselection/REPORT_VI.md); handoff lot giữa production partners | Chỉ khi evidence cần đổi tình huống và audience phù hợp. Không phải visual-only test; chưa fresh pixel/native/whole-journey/paid release choF3, cần scope review trước sử dụng |
| Hook/visual khác cùngF1/F2 | Hiện chưa có alternate cold đã được chỉ định và QA như một swap-ready variant trong gói này | C4: reuse nếu exact variant thực tồn tại và qua review; nếu thiếu chuẩn bị brief trước. Không tự generate hoặc lấy F3 giả thành alternate cùng hook |
| VN / Chinese / Search | Library và runbooks riêng đã tồn tại | Đổi segment/locale/channel là quyết định riêng, không tự chạy sauW1; VN Aplus không dùng như Bright proof choFDI |

## Continuity phải giữ

F1: chip-design Operations quản lý outsourced production → partner reports theo lot/stage/time/owner → Bright Power case đúng nguồn → readerF1 → CTA contact-vn có notice tiếng Việt. F2: Planning/Operations đổi demand → xác định lots/reports cần review trước replan → Bright Power case đúng nguồn → readerF2 → cùng contact handoff. R5 mixed-cohort là audience hypothesis đã chấp nhận, không chứng minh mọi recipient là Fabless/qualified buyer. Không biến scope paid thành kiểm purchasing authority từng account.

Chỉ đổi một phần khi có thể; giữ advertiser Digiwin/manufacturing ERP và business decision hữu ích. Không rewrite outcome hoặc claim mới để tăng CTR. Ad không bảo đảm người xem đọc tuần tự cold→explanation→proof; từng điểm chạm vẫn phải tự có ngữ cảnh.

## RMK S0–S4 áp vào F1/F2

Theo [fallback tree](../../linkedin-rmk-source-readiness/2026-10-08/03_RMK_Fallback_Decision_Tree.md): S0 cold chưa delivery; S1 source processing; S2 Ready nhưng dưới gate reachable; S3 đủ size nhưng thiếu gate khác; S4 đủ các gate để Bảo quyết release. Repository contract dùng300filtered reachable; đây không thay current UI readback/format support, không là cam kết đạt300sauW1. Rule/lookback/objective chưa chọn, không mượn Page/organic/old campaigns. Không split thành nhiều pool nhỏ chỉ vì có hai journeys; source cohort grouping phải tương thích và được chọn. Nếu chưa đủ thì giữ cold hoặc giữ tiền; Search chỉ là option riêng trong cap, không default fallback.
