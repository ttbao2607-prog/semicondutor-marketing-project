# Matched Audience — nhập task, lịch sử và docs vào main

Bảo yêu cầu merge nhánh vừa hoàn tất. Merge này giữ nguyên **4commit** (`c5c38c93`, `db8b0ddd`, `811c34ad`, `d478d12c`) trong lịch sử và **29hồ sơ sanitize**: recheck, R5 retry, Discovery recovery, consolidated research/plan, quyết định cách ly15, hậu kiểm409, upload receipt. Main trước tích hợp `ef183ffb`; source `d478d12c`. Không nhập CSV/company rows, raw account/browser data hoặc ảnh riêng tư.

| Luồng | Trạng thái hiện hành theo evidence08/10 | Việc còn lại |
|---|---|---|
| Tệp công ty Week1 / Discovery | Master424 bảo toàn; Bảo duyệt cách ly15. File409x10/hash `ca12a1c8a7a0439b5fd9f755f8400814910c90e4f92b78041dea27a150c40985` submit một lần08/10 lúc16:20; success toast, reload Updating, filename409persisted. | Đề xuất hậu kiểm10/10 sau16:20 giờ Việt Nam (T+48h): capture đầy đủ matched/unmatched, đối chiếu exact409/ledger và mapping sai/sửa. Nếu còn xử lý, T+72h chỉ đọc lại. **CHANGES_REQUIRED**, chưa quality PASS. |
| R5-52 backup riêng | Upload lại một lần08/10 khoảng14:25. Reload Ready/>90% nhưng immediate Details0Companies/Matched0/Unmatched0; filename52persisted. | Đề xuất recheck09/10 sau14:25; nếu xử lý xong mà vẫn trắng, áp dụng chỉ đạo Bảo xem xét LinkedIn Support. **INSUFFICIENT_EVIDENCE**, chưa gửi Support. |

Chưa tạo lịch tự động. Discovery đã có lần upload424 ngày06/10 và lần cập nhật409 ngày08/10; “một lần” ở checkpoint mới chỉ nói tới **lần cập nhật409**, không phủ nhận lịch sử06/10. Chưa có kết quả matching mới đã ổn định; không gọi409 sạch/all matched. Historical150=11đúng/18sai/121chưa đủ; retained135 BEFORE_UPLOAD=11đúng/3sai/121chưa đủ không được coi là hậu kiểm mới. Identity không chứng minh ICP/FDI/persona hay quyền mua ERP.

[Upload409](../upload409/README.md) · [R5 retry](../r5-reupload.md) · [Plan một lần upload và hậu kiểm](../PLAN_SINGLE_UPLOAD_2026-10-08.md) · [409 preparation audit](../approved-quarantine409/AUDIT.json) · [Manifest/preservation và SELF review](receipt.json).

Docs impact reviewed:7canonical/current entrypoints đã được đối chiếu và thêm current notice. Giữ nguyên toàn bộ body main trước merge, kể cả cập nhật FDI33/33/creative/package; giữ nguyên29file lịch sử/hash-bound evidence. Các bảng tiến độ và receipt cũ vẫn đúng tại thời điểm/revision ghi, không phải current whole-project status; notice hiện hành này thay thế riêng phần Matched Audience. Không sửa lịch sử để nâng PASS, không kéo trạng thái pending-upload của checkpoint cũ thành current hold.

Main integration chỉ local, chưa push GitHub. Source branch/checkpoints được giữ; merge không rebase/rewrite/delete. Đây là hợp nhất tài liệu/task, không thực hiện thêm upload hoặc campaign/settings/enable/spend, không chứng nhận audience ready. Source histories và private evidence tiếp tục dùng cho vòng hậu kiểm kế tiếp.
