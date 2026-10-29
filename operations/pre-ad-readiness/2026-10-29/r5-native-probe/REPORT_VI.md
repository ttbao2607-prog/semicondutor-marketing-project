# R5 AND nhóm5 — native probe29Oct

**Kết quả: INSUFFICIENT_REACH trong cấu hình đã thử.** Native UI cho phép thêm Company Names bằng AND với R5; khi chọn đủ năm Company Pages đã đối chiếu numeric ID, Audience summary hiện “Oops! Your audience is too small. Please expand your audience.” Screenshot hiển thị cùng cảnh báo và đầy đủ expression. Đây là actual native evidence, không còn chỉ suy từ số công ty.

## Cấu hình thực quan sát

- Existing R5 validation ad set: Draft/Off, campaign VALIDATION_ONLY, đúng account đã kiểm; không tạo một draft khác.
- Vietnam recent/permanent, English.
- (Engineering OR Information Technology OR Operations OR Quality Assurance) AND (CXO OR Director OR Manager OR VP) AND R5 Company List AND (năm exact Company Pages, current jobs).
- Năm kết quả Company Names đều đối chiếu numeric ID với private R5 readback/binding28Oct; không chọn India/Europe/local alias hoặc công ty trùng tên khác.
- Expansion unchecked, LAN unchecked; không đổi placement, budget, dates, optimization hoặc bidding. Đây vẫn là validation configuration cũ, không áp production proposal.
- Full five-company Audience summary có cảnh báo too-small. Underlying forecast từng hiển thị **0+**, không có usable forecast. **Không coi0+ là exact zero people, zero demand hoặc actual delivery bằng0**. Không claim một giá trị reach cụ thể dưới ngưỡng khi UI không công bố.

Không phải ROUTE_UNAVAILABLE: phép AND có trong UI và summary ghi đúng. Cũng không phải R5 broad mất eligibility: sau cleanup, original R5 estimate trở lại470+.

## Persistence và cleanup

Chỉ thêm năm lựa chọn trong unsaved editor của owned probe tab. Không bấm Save audience, Save and exit, Next hoặc Review & Launch. Sau chụp bằng chứng, bấm Back to account; UI điều hướng về danh sách, không hiện hộp xác nhận save. Banner ghi lần save trước là28Oct. Mở lại original R5 bằng link tới editor: Company (Current Jobs) năm công ty **không còn**, bộ R5/functions/seniority/Vietnam/English vẫn giữ, estimate470+, Draft/Off và original dates/USD10 giữ nguyên. Lưu readback private, đóng owned tab. User tabs khác giữ nguyên.

No save/upload/create/enable/spend action; không đổi saved audience hay existing draft configuration. Không submit form, gửi thông điệp, nhận legal terms hoặc thay tracking/reader/creative. Readback là bằng chứng saved-state protection; không phải khẳng định quyền mua, đủ volume hay performance.

## Quyết định được thu hẹp

**Không dùng nhóm5 với bộ lọc này để dựng production P1/P2.** Không tự nới function/seniority/location, đổi AND thành OR, bỏ R5, thêm14adjacent, upload list mới hoặc điều chỉnh budget để vượt cảnh báo. Không sửa saved draft thành production.

Đề nghị bước nội bộ tiếp theo: **chuẩn bị phương án chọn/adapt nội dung cho nhóm supplier rộng hơn trong R5**, giữ giá trị planning handoff của P1 và record ownership của P2, đối chiếu cả caption/ảnh/carousel/proof/reader và actual activity mix. Bảng33 hồ sơ ngoài exact category có cả design/IP/EDA; không chỉ thay chữ equipment-component thành manufacturing rồi gọi toàn R5 là fit. So sánh với candidate sẵn có trong thư viện nếu persona khác. Trình Bảo trade-off coverage/relevance và exact copy delta trước sửa/generate creative hoặc thay lựa chọn D3; không tự thông qua một broad journey mới.

Case/translation và public reader/CTA đã duyệt không mở lại. Paid-use disposition đúng bộ asset, human/domain acceptance, processed reporting và production calendar/pacing/UI readback vẫn còn scope riêng. Proposed USD10/day02–08Nov chưa áp. Tuần1 vẫn chọn một nhóm theo plan, không tự mở VN/Chinese song song.

## Evidence / outcome

[EVIDENCE.json](EVIDENCE.json) chứa hash và sanitized booleans; private screenshots và DOM trong private evidence store. 01-five-company-too-small.png chứng minh full expression+cảnh báo;02-reopened-original.txt/png chứng minh saved R5 không có nhóm5. Không đưa screenshot chứa account/roster vào public Git. [Contract](PLAN.md), [anchor receipt](MESSAGE_ANCHOR_RECEIPT.md), [checks](CHECKS.json).

Execution **SUCCESS cho bounded native feasibility check**; audience route outcome **INSUFFICIENT_REACH**; full paid handoff **INSUFFICIENT_EVIDENCE / HOLD**. Root SELF_REVIEW, independent audit NOT_RUN. Tài liệu được local checkpoint trên approval-corrected theo yêu cầu commit trước của Bảo; chưa push/merge. Docs impact reviewed: current/readiness/build entrypoints cập nhật subgroup outcome và bước nội bộ tiếp theo; giữ historical receipts/pins và R5 scoped mapping/eligibility, không rewrite old NOT_MEASURED thành historical observed result.
