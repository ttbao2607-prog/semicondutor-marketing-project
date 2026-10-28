> **Git consolidation / active handoff — 28/10/2026:** Main tích hợp hồ sơ điều hành/audience đã commit tại `c8e9d00c` và unified reader candidate từ `eaf805a1`. R5 draft eligibility, readiness index và shortlist mới hơn đang được phiên khác hoàn thiện trên `slice/executive-approval-corrected-2026-10-28`; Bảo yêu cầu giữ nguyên worktree đó. Các nhận định eligibility trong checkpoint bên dưới là snapshot, không đại diện kết quả mới nhất của phiên đang làm. Chưa nhập phần working docs đó hoặc chốt journey/D6/release. [Trạng thái Git, nguồn và bước bàn giao](../../git-consolidation/2026-10-28/README.md).

# PO decision record — D1–D6, bảng build 99 ad (12/10/2026)

> **Cập nhật 28/10/2026:** Bảo xác nhận chạy đúng Package v2 sau chỉ đạo khởi động từ tháng 11. D1=A FINAL theo xác nhận của Bảo; D3 chốt nguyên tắc một nhóm và vài journey đại diện, Bảo còn chọn nhóm/journey/locale tuần 1. Thư viện 33 journey / 99 ad / 339 card không đồng nghĩa chạy toàn bộ. Audience là blocker trước chạy. [Hồ sơ](../../source-evidence/Daphne_Tsai_Executive_Approval_2026-10-28.md).

Record ID: **PREPUBLISH-D1D6-PO-20261012**. Nguồn: chỉ đạo trực tiếp của Bảo trong chat ngày 12/10/2026, sau khi đọc [decision pack](Decision_Pack_D1_D6_VI.md). Lịch sử 12/10: sếp chưa phản hồi; trạng thái hiện hành theo notice 28/10 ở trên.

## Chỉ đạo gốc của Bảo

> D1 - chốt A (ghi decision tài liệu, chừng nào sếp duyệt mới có final), D2 Chọn learn more, D3 chưa chốt, chờ sếp check library, nếu không can thiệp, Bảo sẽ chọn sau. D4. Giữ 2 carousel. D5. Dùng tên trên.

## Quyết định

| # | Trạng thái | Nội dung ghi nhận |
|---|---|---|
| D1 | **Chốt A, FINAL** | Ad cold (Single image) và ad giải thích trỏ tới cùng reader với ad proof của journey đó. FINAL theo xác nhận của Bảo chạy đúng plan ngày 28/10; ảnh chat không nêu D1. |
| D2 | **Chốt** | Nút CTA nền tảng là "Learn more" cho cả ba vai trò. Giới hạn: danh sách nút theo objective/định dạng chưa kiểm trong giao diện LinkedIn; nếu không có nút này khi tạo ad thì quay lại Bảo, không tự thay. |
| D3 | **Nguyên tắc chốt; lựa chọn tuần 1 CHƯA chốt** | Chạy đúng plan: một nhóm phù hợp, vài journey đại diện; Bảo chọn nhóm, journey và locale. Bảng giữ 33 journey / 99 ad làm thư viện, không có nghĩa chạy toàn bộ. |
| D4 | **Chốt** | Giữ 2 carousel (giải thích và proof riêng), như viewer đã review. |
| D5 | **Chốt** | Dùng quy ước `LI-<wave>-<treatment>-<locale>-<role>-v1`. Phần `<wave>` vẫn là placeholder đến khi đợt chạy được định nghĩa. Nhãn UTM không thuộc quyết định này, vẫn là đề xuất cần kiểm kê tag/event trước. |
| D6 | **Chưa được nêu** | Bảo chưa trả lời mục này; giữ chờ quyết định và mandate tạo campaign. |

## Hệ quả đã áp dụng

- [`build_prepublish_packs.py`](../2026-10-08/build_prepublish_packs.py) và `03_LinkedIn_Ad_Build_Sheet.csv`: 66 dòng cold/giải thích ghi đích là reader (D1=A, FINAL theo xác nhận của Bảo), thêm cột `platform_cta_button` (D2). 0 dòng còn `DECISION_NEEDED`.
- D4/D5: cấu trúc 99 ad và `ad_key` không đổi; chỉ ghi nhận đã được chốt.
- Không đổi ngân sách, asset, verdict, audience hay nội dung copy. Không có hành động live.

## Còn mở và không bị quyết định này giải quyết

Route host reader (UNKNOWN), link "quay lại" trong reader trỏ tới viewer nội bộ, Partner reader không có CTA, quyền dùng ảnh, native review chưa có phản hồi, lựa chọn D3 tuần 1, D6, nhãn UTM, quy tắc RMK R1–R5 và audience blocker.

Docs impact reviewed: đồng bộ notice hiện hành, decision pack, build sheet và hồ sơ package; lịch sử 12/10 giữ nguyên theo ngày.
