# Closeout — bốn việc follow-up trước readback W1

29/10/2026 · revision 1 · **Overall execution status: PARTIAL**. Executor Claude theo [contract](CLAUDE_EXECUTION_CONTRACT.md) do Bảo giao trong chat; một browser session; không spawn/delegate. Audit độc lập: **NOT_RUN** (không tự gọi independent PASS). Worktree `D:/Digiwin_F1F2_W1W2_2026-10-29`, nhánh `slice/f1-f2-w1-w2-decision-pack-2026-10-29`, base HEAD `dec94ed7`; git-state-recovery chạy trước khi bắt đầu, HEAD không đổi, worktree sạch. Không push/merge, không ghi `main`.

## Bảng Q1–Q4

| Task | Status | Evidence thực | Gap / impact |
|---|---|---|---|
| [Q1](FOLLOWUP_Q1_READBACK.md) | **PARTIAL** | parent, ad set, hai ad, English (option selected), tên đầy đủ list R5-52, Expansion off, placement, USD10, ngày 01–07/11, forecast, hai probe Draft; hai ad vẫn On/Active khi đọc lại 12:26 | nhãn review không hiển thị (Active ≠ duyệt); giờ trong ngày 07:00/06:45 và timezone không hiển thị; destination URL live không đọc được; job functions chỉ thấy breakdown forecast; tín hiệu "Validation error icon" trong accessibility tree chưa giải thích |
| [Q2](FOLLOWUP_Q2_REPORT_MAP.md) | **PARTIAL** | LinkedIn có Reach, Average frequency, Clicks, Clicks to landing page, Total engagement; GA4 stream/Measurement ID `G-MV5QWN0XVM` khớp bridge; Session campaign dùng được, `fdi_` 01–28/10 = no data; GA4 timezone Vietnam GMT+07:00 | timezone LinkedIn UNVERIFIED; không có Session manual ad content/utm_content trong báo cáo chuẩn (Explore chưa thử); không chứng minh attribution |
| [Q3](FOLLOWUP_Q3_RMK_OPTIONS.md) | **PARTIAL** | form thật: rule Any/Chargeable, lookback 7–365 (có 30), nguồn theo ad set, F1/F2 chung ad set → pool chung; danh sách Matched 5 Company List, không có retargeting audience; Cancel, không tạo gì | gate 300, reachable, backfill, ghép carousel RMK chưa thấy trong UI; chọn per-ad không có |
| [Q4](FOLLOWUP_Q4_VISUAL_QA.md) | **PARTIAL** | 16 ảnh duy nhất đọc trực tiếp, headline/alt/thứ tự/hash khớp; reader F1/F2 đo 390 và 360 px không tràn, notice tiếng Việt có | không có screenshot trình duyệt; B16 thiếu viewer desktop; native NOT_RUN; transition public/return không re-test (tránh traffic không đánh dấu) |

## Đã xác minh / đề xuất

- **Đã xác minh (executor đọc live):** các dòng MATCH ở Q1–Q3; số liệu 0 ở prelaunch là OBSERVED_ZERO, không là kết quả W1.
- **Mới so với P1–P7:** English đã chọn thật; tên list R5-52 đầy đủ; hai probe Draft; Reach/frequency/click columns có thật; nguồn RMK theo ad set nên pool F1/F2 chung; không có retargeting audience hiện hữu; `utm_content` không có trong picker chuẩn.
- **Đề xuất (chưa quyết):** mặc định R1=A, R2=30 ngày, R3 giữ pool chung theo ad set, R6 cần mandate hẹp.
- **Không đổi:** metric/threshold; W2 funding vẫn NOT_DECIDED; forecast không là RMK size hay KPI; không có winner/ROI.

## Input cụ thể Bảo cần chọn

1. R1 (Any / Chargeable), R2 (lookback), R3 (giữ pool chung hay tách ad set — tách thay cấu trúc cold đang scheduled), R5.
2. **R6:** có cấp mandate hẹp tạo source audience (chỉ audience, không ad/RMK) trước 01/11 không. Form tạo được mở; chưa biết backfill.
3. Có muốn một recheck trước 01/11 07:00 VN bằng phiên chụp được ảnh/đọc được URL để đóng review label, giờ chạy, destination URL, icon validation không.
4. Có cần viewer desktop riêng cho B16 (F2) không.

## Protected invariants readback

- F1/F2 và probe: sau khi mở/rời các editor, danh sách vẫn ad set On/Not delivering–Scheduled và hai ad On/Active; lịch/budget/audience đọc trước khi rời đúng như expected. Không Save/Launch/pause/enable, không đổi budget/ngày/targeting/creative/analytics.
- Audience: danh sách Matched trước/sau 5 mục; dialog tạo audience chỉ mở và Cancel (một lần bước nhầm sang form video cũng Cancel).
- GA4: chỉ đổi dimension/search trong phiên xem; không lưu report, không đổi config.
- Reader/tracking source, public runtime, ảnh và `main`: không đổi. Reader chỉ mở trên loopback (không GA4). Không gửi form, không tạo lead, không scheduler.
- Một tab Chrome do phiên mở đã đóng cuối phiên.

## Rủi ro báo ngay

Không phát hiện reject, target drift, link lỗi hay budget risk đo được. Hai lưu ý: nhãn review không đọc được (Active ≠ duyệt) và tín hiệu "Validation error icon" chưa giải thích; đề xuất đọc lại bằng phiên chụp được ảnh trước 01/11, không dừng/đổi gì.

## Evidence và audit

Public chỉ có observation đã sanitize; không numeric ID, credential hay URL phiên riêng. Không có raw screenshot/DOM bundle (chụp ảnh timeout) nên **không có SHA256 cho raw evidence**; auditor không thể kiểm lại từ tệp. Audit target nếu có: đọc lại từng trường Q1 trên UI, từng cột Q2, form Q3, ảnh/reader Q4, đối chiếu diff với `main` và không đổi tài khoản.

## Docs impact

Đọc `DOCS_IMPACT_MAP.md`. Observed truth thay đổi ở: English/list R5-52/probe/Reach-frequency columns/nguồn RMK theo ad set. Đã thêm pointer vào `CURRENT_STATE.md`; P1/P2/P6 giữ nguyên làm lịch sử và được bổ sung bằng các tệp follow-up này (không sửa số baseline cũ). Không đổi scope, lịch, budget, creative, tracking implementation hay anchor; README/readiness/build/S04 không cần đổi nội dung vận hành. Fresh MSG-ANCHOR receipt ở [Q4](FOLLOWUP_Q4_VISUAL_QA.md).

## Next action

Bảo chọn mục 1–4 ở trên. Chưa có hành động live nào được đề xuất cho F1/F2. Hold W2 decisions tới khi có metric/funding thực.
