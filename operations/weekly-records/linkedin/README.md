# Weekly LinkedIn record — snapshot cho báo cáo stakeholder

Thư mục này chứa record tuần LinkedIn (`linkedin_<start>_<end>.json`) mà agent repo Report (`Review_Ga4_GooglAd_Weekly`) đọc qua commit SHA do Bảo chuyển. Hai agent không gọi nhau.

## Contract được ghim

| Mục | Giá trị |
|---|---|
| Bản sao nguyên văn | [`CONTRACT_semi-awareness-weekly-record-v1.md`](CONTRACT_semi-awareness-weekly-record-v1.md) (không sửa nội dung; sửa = đổi hash) |
| Nguồn | repo Report, commit `89f485f9c42dc3fa62ff07952d09dd52eb3e218b`, path `Documents_File/stakeholder_dashboard/semiconductor_linkedin_weekly_record_contract.md` |
| SHA-256 | `871b1bc6563ae0a69f76c602db10fa2c7eed054adbf4d64f8b0aa1f0028a9d66` (đã đối chiếu với bản trong commit và bản sao này, 2026-11-03) |
| Schema | `semi-awareness-weekly-record-v1` |
| Trạng thái | Yêu cầu định dạng theo chỉ đạo Bảo 03/11/2026, **không phải mandate live**. Chỉ đọc (read-only) LinkedIn theo mandate đọc hiện hành. |

Cập nhật contract: Bảo chuyển SHA mới; lưu bản mới kèm hash và sửa bảng trên, không ghi đè im lặng.

## Tóm tắt nhanh cho agent (chi tiết ở contract)

- Kỳ Thứ Hai–Chủ Nhật, Asia/Ho_Chi_Minh, đã đóng ≥48h; đọc đúng date range của kỳ, không dùng số cộng dồn (vd. cửa sổ 04/10–02/11).
- Batch: 04/11 (26/10–01/11, chỉ delivery 01/11), 11/11 (02/11–08/11), 18/11 (09/11–15/11).
- `null` = không đọc được; `0` chỉ khi UI hiện 0. Không có spend/budget/CPC/CPM, audience, creative, ID, URL, PII, raw DOM/ảnh trong record.
- Không kết luận winner/hiệu quả/lead; không so F1/F2 nếu impressions lệch >3:1 (K4).
- Commit local trên nhánh Bảo chỉ định, không push; báo Bảo đường dẫn + SHA 40 ký tự + SHA-256 file; chạy documentation sync gate.
- Nội dung nội bộ (spend, receipt) vẫn ở `operations/w1-w2/f1-f2-2026-10-29/pre-readback/`, không chép vào record.

## Record đã có

Chưa có record nào (2026-11-03).
