# Q1 — Recheck F1/F2 trước launch

Revision 1 · observed 29/10/2026, kết thúc 12:26 +07 (giờ máy cục bộ) · **PARTIAL**. Authority: Bảo giao Claude thực hiện [contract](CLAUDE_EXECUTION_CONTRACT.md) (chat 29/10/2026). Executor Claude, một browser session; đọc LinkedIn Campaign Manager qua accessibility tree/DOM và text trang, không Save/Launch/Review & Launch. Audit độc lập NOT_RUN. Numeric account/ad/ad set/audience ID không ghi ở đây (private).

**Mức evidence:** đọc live DOM/accessibility, không có screenshot (chụp ảnh timeout 30 giây mọi lần thử), không lưu raw bundle riêng. Vì vậy các dòng bên dưới là observation của executor, chưa được auditor kiểm lại; không phải visual PASS.

## Expected vs actual

| Trường | Expected | Actual (đọc 29/10) | Kết luận |
|---|---|---|---|
| Parent `VALIDATION_ONLY_VN_SEMICONDUCTOR_ABM_2026-09-14` | On/Active | danh sách Campaigns: On, Active, Brand Awareness | MATCH |
| Ad set `DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH` | On, Not delivering – Scheduled | On, "Not delivering / Scheduled", Sponsored Content, key result Reach, Maximum Delivery; đọc lại sau khi rời editor vẫn như vậy | MATCH |
| Hai ad | F1/F2 On/Active cùng ad set | `LI-wave01-F1-en-COLD-v1` và `LI-wave01-F2-en-COLD-v1`: On, Active, Single Image, cùng ad set; ad set ghi "2 ads". Đọc lại lúc 12:26 sau mọi thao tác vẫn On/Active | MATCH |
| Nhãn review/hold/rejection | đọc nhãn từng ad | cả danh sách Ads lẫn trang Ads của ad set chỉ hiện "Active"; không có nhãn review, hold hay rejection nào. Trạng thái "Active" không chứng minh đã duyệt | **UNVERIFIED** (không có nguồn hiển thị review) |
| Profile language | English | combobox có option English ở trạng thái `(selected)` (giá trị chọn thật, không phải danh sách options); câu giải thích UI cũng nêu "By selecting English" | **MATCH** (đóng gap P1) |
| Company list | `TEST-AUD-CONTINGENCY-TRUE-ONLY-R5-52` | text trang chứa đúng chuỗi `TEST-AUD-CONTINGENCY-TRUE-ONLY-R5-52` làm Company List đang include; Matched Audiences cũng có đúng tên này (Ready, Company List, >90%, 1 active ad set) | **MATCH** tên đầy đủ (đóng gap P1 về prefix). Không chứng minh nội dung list |
| Location | Vietnam | text có "Vietnam" | MATCH |
| Seniority | CXO, Director, Manager, VP | text "CXO, Director, Manager, VP" | MATCH |
| Job functions | Operations, Engineering, IT, QA | không đọc được danh sách function đã chọn; chỉ thấy segment breakdown của forecast: Operations 47%, Engineering 36%, Quality Assurance 19%, Information Technology 11% (tỷ lệ chồng nhau, là phân rã forecast, không phải chọn) | **PARTIAL** (không phản bác expected; selection chưa đọc trực tiếp lượt này) |
| Audience Expansion | off | checkbox "Enable Audience Expansion": `checked=false` | MATCH |
| Placement | Feed bật; Right Rail, LAN off | Feed `true`; Right Rail `false`; LinkedIn Audience Network `false`; toggle LinkedIn manual-placement `true` | MATCH |
| Budget | USD10/ngày chung | ô Daily budget `$10.00`, currency USD; UI: "spend up to $70.00 total" | MATCH |
| Lịch | 01/11 → 07/11 (giờ VN 07:00 → 06:45 theo receipt) | radio "Set a start and end date"; Start `11/1/2026`, End `11/7/2026`; UI: "run for 7 days starting from November 1, 2026" | MATCH ngày. **Giờ trong ngày và timezone không hiển thị ở editor** → 07:00/06:45 giữ UNVERIFIED lượt này (chỉ có trong receipt). Lịch dự kiến ≠ actual first delivery |
| Frequency optimization | không quy định | radio default đang chọn | thông tin |
| Forecast | 470+ | 470+; 30-day spend $0.00–$14.00, reach 71–170, cost/1,000 reached $31.70–$37.27, frequency 1.0–1.4 | MATCH; forecast định hướng, không là kết quả hoặc cap |
| Hai probe | Draft/Off | trong nguồn của "Create single image audience" hiện bốn ad set Single Image: ad set F1/F2 (Not delivering/Scheduled) và ba ad set **Draft**: `VALIDATION_ONLY_VN_SEMICONDUCTOR_ABM_2026-09-14_AUDIENCE_TEST`, `VALIDATION_ONLY_R5_EN_ELIGIBILITY_20261028_DO_NOT_LAUNCH` và `Website visits - Oct 27, 2026`. Banner "Pick up where you left off" vẫn nhắc probe R5 ELIGIBILITY | MATCH cho hai probe (Draft). Chưa đọc cột Off/On của chúng; bộ lọc danh sách ad set đang ẩn 7/8 nên không dùng list đó |
| Delivery 30 ngày | chưa có | Spent $0.00, impressions 0, clicks 0 (range 30/09–29/10) | OBSERVED_ZERO phù hợp prelaunch; không là kết quả W1 |

## Không đọc được

- **Destination URL / UTM của ad:** trang sửa ad hiển thị ô URL nhưng công cụ đọc giá trị bị chặn ("Cookie/query string data") nên URL live **không được đọc lại**; vẫn dựa vào [SOURCE_REGISTRY](../SOURCE_REGISTRY.csv) và receipt 29/10. UNVERIFIED live.
- **Nhãn "Validation error icon":** khi mở trang Ads của ad set trong editor, accessibility tree liệt kê icon này cho cả 7 mục điều hướng (Audience, Ad format, Placement, Budget and Schedule, Conversion Tracking…) đúng lúc còn status "Loading/Saving". Không xác minh được bằng hình; ở bước Details các trường đều có giá trị. Ghi là tín hiệu chưa giải thích, **không** kết luận lỗi hay không lỗi. Đề xuất đọc lại bằng người/phiên chụp được ảnh trước 01/11.
- Review per-ad (policy) cần nguồn khác ngoài danh sách; không thấy đường vào trong lượt này.

## Tác dụng phụ và rời không lưu

Đường dẫn `…/creatives/<id>` tự chuyển sang trình sửa ad (`action=edit`); tôi chỉ đọc rồi thoát bằng "Cancel ad changes". Trình sửa ad set mở qua nút "Previous" của wizard; thoát bằng "Back to account" của app, không bấm Save/Review & Launch, không thấy hộp thoại "Leave site?". Sau khi thoát, danh sách ad set và ads vẫn On/Scheduled và On/Active. Bộ lọc danh sách ad set được mở xem rồi đóng, không đổi. Wizard có phần tử trạng thái "Saving" trong DOM; không có bằng chứng autosave thay đổi field nào (lịch, budget, audience đọc sau đó vẫn như trước). Không có thao tác nào ghi vào F1/F2 hay probe.

## Quan sát ngoài phạm vi (giữ, không mở rộng)

Danh sách ads còn các ad On/Active cũ thuộc campaign khác (Carousel Test, Partners PDF, ThaiLand Event); campaign "Test" On/Active như OBS-1 của P1; spend 30 ngày $0. Chưa đọc budget/lịch các campaign này nên không kết luận chúng có thể tiêu tiền hay không. Không dừng/đổi gì.

## Còn lại

Recheck ngay trước 01/11 07:00 VN: nhãn review, trạng thái ad/ad set, giờ bắt đầu thực tế (nếu UI nào hiển thị được), destination URL bằng phiên đọc được giá trị, icon validation. Sau 01/11: ghi actual first delivery và khoảng reject/pause riêng.

Docs impact reviewed: xem [FOLLOWUP_CLOSEOUT](FOLLOWUP_CLOSEOUT.md).
