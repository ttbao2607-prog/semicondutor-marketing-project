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

## Reopen / readback sau khi tạo (14:01 +07)

Mở lại audience từ danh sách Matched (trang chi tiết, chỉ đọc; không bấm "Create ad set" hay "View insights"). Đọc được: tên `RMK-SRC-F1F2-R5-EN-WAVE01-ANY-30D`; Status **Building**; Source **Single image ad**; Ownership Owned; Active ad sets không có (bảng "No records to show"); danh sách Matched 6 mục. Trang chi tiết **cũng hiển thị "Last audience count" là "<300"** khi đang Building: đây là nhãn hiển thị của LinkedIn lúc chưa xử lý xong, **không phải reachable sau xử lý** và không chứng minh dưới/trên cổng 300; reachable giữ UNKNOWN, không nâng Building thành Ready, đọc lại sau khi xử lý xong.

**Giới hạn:** trang chi tiết không in rule, lookback hay ad set nguồn đã chọn, nên ba trường này **không thể reopen-verify** trong UI. Evidence cho chúng là readback ngay trước khi tạo (option `selected` của rule và lookback, một hàng ad set được chọn, giá trị ô tên) và toast "successfully created", cùng Source = Single image ad ở trang chi tiết; chưa có xác nhận độc lập sau lưu. Nếu Bảo cần chứng minh ad set nguồn, cần nguồn khác (ví dụ khi audience Ready có thể xem insights hoặc khi gắn vào ad set) và phải có mandate riêng.

**Evidence private:** bản đọc thô lưu ngoài repo tại thư mục scratchpad của phiên (`private_readback_RMK_SRC_2026-10-29_1401.txt`), SHA256 `896d77d74c9e1d087ff69d2cc1133e777ffc9f2d84e078b4ce2894987dd73956`, observed_at 29/10/2026 14:01 +07. File này chỉ có text đọc từ DOM (không ảnh, numeric ID đã thay bằng `<id>`); thư mục phiên có thể bị xóa nên nó không phải kho lưu lâu dài. Evidence của Q1–Q4 (đọc trước đó) vẫn **không** có bundle riêng; chỉ audience readback này có private reference/hash.

## Registry

[SOURCE_REGISTRY.csv](../SOURCE_REGISTRY.csv) và pin trong [ARTIFACT_MANIFEST.json](../ARTIFACT_MANIFEST.json) đã cập nhật: rule `ANY_INTERACTIONS_SELECTED`, lookback `30_DAYS_SELECTED`, audience `RMK-SRC-F1F2-R5-EN-WAVE01-ANY-30D`, status `BUILDING_OBSERVED_2026-10-29T14:01+07`, reachable `UNKNOWN`. Các câu "NOT_VERIFIED_CREATED / NOT_SELECTED" trong [RMK_DECISION_PACK](RMK_DECISION_PACK.md) và [W2_ACTION_CARDS](W2_ACTION_CARDS.md) là snapshot lịch sử của P6/P7 (không sửa để giữ pin REVIEW.json); trạng thái source hiện hành lấy từ registry và receipt này.

## Không làm

Không tạo ad RMK, không gắn audience vào ad set/targeting, không bật gì, không đổi budget/lịch/creative của F1/F2. Readback ad set F1/F2 lúc 13:42: vẫn On / Not delivering – Scheduled.

## Trạng thái RMK sau bước này

Source: **CREATED_BUILDING** (thay NOT_VERIFIED_CREATED). Rule Any interactions, lookback 30 ngày: **SELECTED**. Reachable/kích thước: **UNKNOWN** (chưa hiển thị). Gate 300: chưa kiểm trong UI. Backfill: **chưa biết**; UI chỉ nói "can take 48 hours … to process" và ad set dùng audience chỉ chạy sau khi xử lý xong. Chỉ gán Ready/S2 sau native readback thực. Tạo source không là enable RMK; objective, release và nguồn tiền là quyết định sau.

## Đọc lại

Đọc Status/size trong Audiences ít nhất khi recheck 01/11 và sau W1 ([handoff](RECHECK_HANDOFF_2026-11-01.md)); không suy kích thước từ 470+ hoặc forecast. Quan sát lại có thể cho biết audience có backfill hay chỉ tích lũy từ lúc tạo: ghi observed_at và số liệu thực, không suy.

Docs impact reviewed: [FOLLOWUP_CLOSEOUT](FOLLOWUP_CLOSEOUT.md), [Q3](FOLLOWUP_Q3_RMK_OPTIONS.md), handoff và `CURRENT_STATE.md` được cập nhật; P6 giữ nguyên làm lịch sử.
