# Receipt — tạo source audience RMK (R6)

29/10/2026, quan sát ~13:40–13:42 +07 · **SUCCESS (tạo audience); audience status Building, chưa Ready**. Authority: Bảo (chat 29/10/2026): "Cho Claude tạo audience RMK-SRC-F1F2-R5-EN-WAVE01-ANY-30D: Single image, nguồn là ad set F1/F2, rule Any interactions, lookback 30 ngày, chỉ tạo audience". Executor Claude, một browser session; audit độc lập NOT_RUN. Numeric account/ad set/audience ID private, không ghi ở đây.

## Cấu hình đã tạo (đọc ngay trước khi bấm tạo)

| Mục | Giá trị |
|---|---|
| Loại | Retargeting audience → Single image (Member engagement) |
| Tên | `RMK-SRC-F1F2-R5-EN-WAVE01-ANY-30D` (giá trị ô nhập đã đọc lại) |
| Rule | "Any interactions with your ad" (option `selected`, mặc định) |
| Lookback | "30 days in the past" (option `selected`; mặc định ban đầu là 90 ngày và đã đổi) |
| Nguồn | ad set `DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH` — chỉ hàng này được chọn; ba ad set Draft không chọn. Nguồn theo ad set nên gồm tương tác của cả hai ad F1 và F2 (pool chung, không tách theo ad) |
| Đồng ý | Ads Agreement qua nút "Agree and create" theo lệnh tạo của Bảo |

## Kết quả

Toast "Your audience has been successfully created". Danh sách Matched tăng 5 → 6; dòng mới: Status **Building**, Source Single Image, Active ad sets "-", Last audience count "-", Ownership Owned, Last modified 10/29/2026. Năm audience còn lại không đổi.

## Không làm

Không tạo ad RMK, không gắn audience vào ad set/targeting, không bật gì, không đổi budget/lịch/creative của F1/F2. Readback ad set F1/F2 lúc 13:42: vẫn On / Not delivering – Scheduled.

## Trạng thái RMK sau bước này

Source: **CREATED_BUILDING** (thay NOT_VERIFIED_CREATED). Rule Any interactions, lookback 30 ngày: **SELECTED**. Reachable/kích thước: **UNKNOWN** (chưa hiển thị). Gate 300: chưa kiểm trong UI. Backfill: **chưa biết**; UI chỉ nói "can take 48 hours … to process" và ad set dùng audience chỉ chạy sau khi xử lý xong. Chỉ gán Ready/S2 sau native readback thực. Tạo source không là enable RMK; objective, release và nguồn tiền là quyết định sau.

## Đọc lại

Đọc Status/size trong Audiences ít nhất khi recheck 01/11 và sau W1 ([handoff](RECHECK_HANDOFF_2026-11-01.md)); không suy kích thước từ 470+ hoặc forecast. Quan sát lại có thể cho biết audience có backfill hay chỉ tích lũy từ lúc tạo: ghi observed_at và số liệu thực, không suy.

Docs impact reviewed: [FOLLOWUP_CLOSEOUT](FOLLOWUP_CLOSEOUT.md), [Q3](FOLLOWUP_Q3_RMK_OPTIONS.md), handoff và `CURRENT_STATE.md` được cập nhật; P6 giữ nguyên làm lịch sử.
