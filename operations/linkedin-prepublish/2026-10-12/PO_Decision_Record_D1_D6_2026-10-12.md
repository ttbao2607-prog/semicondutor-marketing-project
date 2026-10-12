# PO decision record — D1–D6, bảng build 99 ad (12/10/2026)

Record ID: **PREPUBLISH-D1D6-PO-20261012**. Nguồn: chỉ đạo trực tiếp của Bảo trong chat ngày 12/10/2026, sau khi đọc [decision pack](Decision_Pack_D1_D6_VI.md). Trạng thái package: Bảo đã gửi sếp, **sếp chưa phản hồi** nên các quyết định bên dưới chưa phải bản cuối khi Bảo nêu rõ.

## Chỉ đạo gốc của Bảo

> D1 - chốt A (ghi decision tài liệu, chừng nào sếp duyệt mới có final), D2 Chọn learn more, D3 chưa chốt, chờ sếp check library, nếu không can thiệp, Bảo sẽ chọn sau. D4. Giữ 2 carousel. D5. Dùng tên trên.

## Quyết định

| # | Trạng thái | Nội dung ghi nhận |
|---|---|---|
| D1 | **Chốt A, PROVISIONAL** | Ad cold (Single image) và ad giải thích trỏ tới cùng reader với ad proof của journey đó. Chỉ thành bản cuối khi sếp duyệt package; nếu sếp can thiệp thì mở lại. |
| D2 | **Chốt** | Nút CTA nền tảng là "Learn more" cho cả ba vai trò. Giới hạn: danh sách nút theo objective/định dạng chưa kiểm trong giao diện LinkedIn; nếu không có nút này khi tạo ad thì quay lại Bảo, không tự thay. |
| D3 | **CHƯA chốt** | Chờ sếp xem library. Nếu sếp không can thiệp, Bảo tự chọn sau. Bảng giữ nguyên 33 journey / 99 ad, không cắt. |
| D4 | **Chốt** | Giữ 2 carousel (giải thích và proof riêng), như viewer đã review. |
| D5 | **Chốt** | Dùng quy ước `LI-<wave>-<treatment>-<locale>-<role>-v1`. Phần `<wave>` vẫn là placeholder đến khi đợt chạy được định nghĩa. Nhãn UTM không thuộc quyết định này, vẫn là đề xuất cần kiểm kê tag/event trước. |
| D6 | **Chưa được nêu** | Bảo chưa trả lời mục này; giữ chờ quyết định và mandate tạo campaign. |

## Hệ quả đã áp dụng

- [`build_prepublish_packs.py`](../2026-10-08/build_prepublish_packs.py) và `03_LinkedIn_Ad_Build_Sheet.csv`: 66 dòng cold/giải thích ghi đích là reader (D1=A, PROVISIONAL), thêm cột `platform_cta_button` (D2). 0 dòng còn `DECISION_NEEDED`.
- D4/D5: cấu trúc 99 ad và `ad_key` không đổi; chỉ ghi nhận đã được chốt.
- Không đổi ngân sách, asset, verdict, audience hay nội dung copy. Không có hành động live.

## Còn mở và không bị quyết định này giải quyết

Route host reader (UNKNOWN), link "quay lại" trong reader trỏ tới viewer nội bộ, Partner reader không có CTA, quyền dùng ảnh, native review chưa có phản hồi, D3, D6, nhãn UTM, quy tắc RMK R1–R5.

Docs impact reviewed: notice trong CURRENT_STATE, bảng build và decision pack được cập nhật; không có canonical doc nào khác bị ảnh hưởng.
