# Preflight chọn đúng tài khoản LinkedIn (bắt buộc trước mỗi record tuần)

**Lý do:** Chrome đăng nhập thấy hai ngữ cảnh. Tài khoản cá nhân `Digiwin ASEAN` (`businessId=personal`, trạng thái *On hold – Payment method required*, 0 ad set) hiện đầu danh sách và **sai**. Tài khoản đúng nằm dưới Business Manager **DigiwinSoft ASEAN BM**, ad account **DigiwinSoft_SEA_Performance_Bao** (Active), chứa ad set F1/F2. Bảo xác nhận 03/11/2026. Đọc nhầm tài khoản cá nhân sẽ cho số 0/rỗng giả.

Nhãn kỳ vọng nằm ở [`preflight_expectations.json`](preflight_expectations.json), theo **tên hiển thị, không có ID/URL** (ID tài khoản không đưa vào repo).

## Các bước (chỉ đọc)

1. Vào Campaign Manager. Nếu mở ra danh sách "Your ad accounts" có `Digiwin ASEAN` / `On hold`: **không chọn**; đổi sang BM đúng qua menu tiêu đề `Campaign Manager ▾` → **Business Manager** và đối chiếu tên BM. Có thể chọn ad account `DigiwinSoft_SEA_Performance_Bao` từ trang Overview/Advertise của BM đó.
2. Đối chiếu bốn dấu hiệu: BM = `DigiwinSoft ASEAN BM`; ad account = `DigiwinSoft_SEA_Performance_Bao` với trạng thái `Active`; tab Ad sets có ad set `DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH`; tab Ads có `LI-wave01-F1-en-COLD-v1` và `LI-wave01-F2-en-COLD-v1`.
3. Gặp bất kỳ hard-stop (`businessId=personal`, `On hold`, `Payment method required`, tên tài khoản `Digiwin ASEAN`) hoặc thiếu ad set/ad: **dừng, không ghi số**, báo Bảo.
4. Ghi `preflight/preflight_<start>_<end>.json` (xem file mẫu của kỳ 26/10–01/11): chỉ nhãn hiển thị, `result` = `PASS`/`FAIL`, không ID/URL/ảnh.
5. Chỉ sau PASS mới đặt time range (**lưu ý UI ghi `Time in UTC`**, ngày UTC lệch giờ VN 07:00; ghi rõ vào `date_range_applied` và `limits`) và đọc cột Performance.
6. Chạy validator (offline, không chạm tài khoản):

```
python -I scripts/check_linkedin_weekly_record.py operations/weekly-records/linkedin/linkedin_<start>_<end>.json operations/weekly-records/linkedin/preflight/preflight_<start>_<end>.json
python -I tests/test_linkedin_weekly_record.py
```

Validator trả `PASS` chỉ khi preflight khớp nhãn kỳ vọng và record đúng contract (không key/chuỗi bị cấm, tổng khớp, CTR tính lại, cờ tỷ lệ 3:1 khớp số liệu, range không khớp kỳ phải có `date_range_applied`). Không có PASS thì không commit record và không báo SHA cho Bảo.

## Giới hạn

Preflight kiểm tra **nhãn hiển thị do người/agent quan sát**; không tự động hóa trình duyệt và không thay mandate đọc của Bảo. Nếu Bảo đổi tên BM/ad account hoặc ad set, sửa `preflight_expectations.json` cùng với quyết định đó.
