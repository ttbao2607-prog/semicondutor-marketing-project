> **Decision evidence round 2 · 2026-10-05:** Đã thu đủ 117 mapping: triage tên 34 consistent candidates / 8 ambiguous / 75 name-inconsistent cần review, chưa xác minh entity/ICP và không phải tỷ lệ match sai. Input Domain/Page URL đều trống ở 117 displayed rows; industry filter không thay identity cleanup. Company Page source visitors **29/30d, 101/90d, 317/365d**; CTA clicks **0/365d**. Website editor hiển thị domain thử nghiệm; chưa có production RMK pool được chứng minh. Giữ creative, ưu tiên sạch input + production tracking; chưa immediate RMK/budget/split approval. 10 ảnh mới + queue private local; không persistent UI mutation mới. Round2 docs lưu bằng containing local checkpoint theo mandate commit của Bảo; prior `764545b` local only. [Decision pack](LinkedIn_Audience_Decision_Evidence_2026-10-05.md).

> **Local checkpoint authorization · 2026-10-05:** Bảo yêu cầu commit local các tài liệu audience/research đã sanitize trên `slice/linkedin-audience-ready-research`. Các ghi chú chưa commit bên dưới là snapshot trước checkpoint; commit identity được xác minh sau commit. Raw screenshot/private report vẫn nằm ngoài public repository. Không merge main hoặc push được yêu cầu.

# LinkedIn Audience Ready — research receipt · 2026-10-05

## Scope và kết quả

Bảo cho phép tách branch từ HEAD của worktree, mutate LinkedIn Campaign Manager để research các điều kiện còn chờ; không publish ad. Branch `slice/linkedin-audience-ready-research` được tạo từ `b70ee5a3c1b76bf6a1e29853b5698828915ca691`; các file audience update chưa commit được giữ theo branch mới. Không spawn/delegate.

Research completed with findings. Đã kiểm chứng native UI/screenshot, thử targeting trong new-ad-set form dưới campaign validation Paused, lưu một Saved Audience definition và xác minh nó tồn tại sau khi thoát form. Không lưu ad set mới; không tạo ad, publish, enable, upload, đổi account budget/tracking hoặc spend trong phiên.

## Observed evidence

| Surface / cấu hình | Kết quả |
|---|---|
| Exact Company List `TEST-AUD-COMPANY-LIST-DISCOVERY-202610` | Ready, Match rate 80%, Company List, Owned |
| Audience list đầu phiên | 752,624 members |
| Details và audience list sau refresh | **753,731** Last audience count; **117 Companies** |
| Tab counts | Matched (117), Unmatched (86) |
| Details Active ad sets | No records to show, time range 9/6/2026–10/5/2026; list Active ad sets `-` |
| Vietnam, profile language English, Company List, expansion OFF | **21,000+** target audience size observed before role filtering; this baseline is session observation, no dedicated baseline screenshot |
| Trên + Job Functions ANY Engineering / Operations / Information Technology / Quality Assurance | **4,800+** |
| Trên + AND Job Seniorities ANY Manager / Director / VP / CXO | **780+** forecast; audience summary **780**; Saved Audience table **780 members** |
| Cùng filters nhưng Profile language Vietnamese | UI báo **audience quá nhỏ để launch**; không có exact count, không tự gán số |
| Brand awareness + Carousel image | Format selectable trong current account; không tạo creative |
| Profile Language menu | English/Vietnamese có; không thấy Chinese trong menu hiện tại. Không đồng nhất language targeting với ngôn ngữ nội dung ads |
| Retargeting member sources | Company page, Conversation, Document, Event, Lead gen form, Single image, Video, Website; không có mục Carousel riêng trong menu đã kiểm tra |
| Single image source editor | Một source ad set Draft; tổng engagement row 0, per-row `-`; Any interactions hoặc chargeable clicks; 30-day lookback option có. Chưa tạo audience |
| Document source editor | Một source ad set Not delivering / Campaign on hold; tổng engagement row 0, per-row `-`; thêm tùy chọn downloaded document. Chưa tạo audience |

`AUD_STATUS_READY_VIABLE` đáp ứng **gate size kỹ thuật của discovery** (Ready + displayed member count >=300), không phải business/launch acceptance. English filtered slice 780 cũng vượt sàn 300 theo UI; không chứng minh đúng ICP, buying intent, FDI/domestic split hoặc hiệu quả phân phối. Vietnamese filtered slice không đủ theo UI.

## Discrepancy và quality hold

- Count 752,624 đầu phiên khác Details 753,731; sau refresh list cũng 753,731. Ghi đúng từng surface, không suy là lỗi hay gán nguyên nhân chưa kiểm chứng.
- Không reconcile 424 uploaded rows, 117 matched companies, 86 unmatched và 80% bằng phép tính tự đặt. Đây có thể là các denominator khác; chưa có evidence giải thích. Không ghi 117/424 là match rate hoặc suy 80% × 424 thành matched companies.
- Quan sát nhiều company-page mappings khác tên/ngành với input, có kết quả thuộc Restaurants, Veterinary Services, Retail. Đây là **mapping-quality finding cần review**, không phải proof đã audit toàn bộ 117 công ty. Chi tiết tên/raw table chỉ giữ trong evidence riêng ngoài repository; không export raw company list.
- Không sửa/xóa mappings hoặc re-upload. Company List Ready không tự giải quyết pending entity identity và ICP scope.

## Mutation thực tế và persistence

- Created Saved Audience **`RSCH-CL-VN-LEAD-20261005`**: VN AND Company List AND ANY 4 functions AND ANY 4 seniorities; English; expansion OFF. Description ghi research only / no launch approval.
- Saved Audience table sau điều hướng lại hiển thị **780 members**. Last applied date xuất hiện trên Saved table là metadata, không được suy thành live ad-set attachment.
- Draft form chọn Carousel, LAN OFF; các placement controls không thuộc Saved Audience definition. Default product listing Digiwin Thailand và daily budget $200 tồn tại trong **unsaved form**, không phải đề xuất ngân sách hay destination đã duyệt. Đã Exit without saving; không lưu ad set mới.
- Existing validation ad set vẫn Draft, switch OFF/disabled; campaign parent được observed Paused. Không chạm các existing Thai/partner campaigns.
- Hai retargeting source editors đều Cancel; không bấm Agree and create, không tạo engagement audience hoặc nhận agreement mới.

## Task closeout

| Task | Disposition |
|---|---|
| Chờ Ready/match rate/count của discovery Company List | **DONE**: Ready/80%/753,731 displayed members |
| Confirm VN + role + seniority reach | **DONE cho cấu hình research này**: 4,800+ → 780; English profile targeting |
| Confirm Vietnamese profile-filter feasibility | **DONE với finding**: too small to launch ở cấu hình đã thử |
| Account permission cho research saved targeting | **DONE trong phiên**: Saved Audience created + persistence verified; không suy toàn bộ quyền |
| Company identity / match denominator / split FDI-domestic | **OPEN**: mapping quality và denominator discrepancy; không adopt production architecture |
| RMK source menu / actual source availability | **DONE cho inventory UI**: no dedicated Carousel menu; single-image/document source rows observed |
| Actual warm RMK audience >=300 | **OPEN**: không có audience đó trong inventory được kiểm tra; sources chưa có engagement khả dụng được chứng minh |
| Production targeting / allocation / publish / delivery | **NOT RELEASED**; research không đóng các gate business |
| HTML expand, proof holds, O3 binding, route/tracking/ad→adapter | **UNCHANGED**, không phụ thuộc Ready của Company List |

## Evidence và kiểm tra

14 JPEG local giữ ngoài public repository theo yêu cầu Bảo. Private report và hash manifest trong thư mục evidence; không commit screenshot, account IDs, private URLs hoặc company table. Screenshot 02 kiểm chứng Details; 06 summary; 12 Saved Audience persistence; 05 Vietnamese finding; 09–11 source inventory; 13–14 private mapping review. Screenshot 03 chỉ ghi viewport phía trên; full configuration được ghi ở 04/06 và receipt này. Forecast spend/reach là directional với default budget của unsaved form, không dùng làm budget recommendation.

Docs impact reviewed: CURRENT_STATE, README, Build Pack, Pre_Ad_Readiness, S03, discovery plan/receipt và Ready task register được đồng bộ trên research branch. S02/S04/proof/creative/tracking không cần sửa. Local main giữ update từ ảnh PO của turn trước; research mới chưa merge main, chưa commit/push.

Execution: SUCCESS (research + evidence capture + permitted saved definition complete). Audit: AUDIT_PASS for scoped observed facts/persistence/no-publish boundary; unresolved business findings remain OPEN, not campaign PASS.
