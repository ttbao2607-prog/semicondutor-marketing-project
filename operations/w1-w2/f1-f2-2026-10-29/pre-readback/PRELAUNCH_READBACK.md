# P1 — Prelaunch readback F1/F2

Revision 1 · observed 29/10/2026 · COMPLETE_WITH_GAPS. Authority: Bảo cấp mandate đọc live P1–P3 ngày 29/10/2026 (chat). Chỉ đọc trong LinkedIn Campaign Manager; không bấm Save/Review & Launch/Edit campaign, không đổi trạng thái, lịch, budget hay audience. Root thực hiện và tự review; independent audit NOT_RUN. Numeric account/ad IDs và ảnh màn hình giữ private, không đưa vào Git.

Nguồn đối chiếu: [activation receipt](../../../pre-ad-readiness/2026-10-29/f1-f2-cycle/SCHEDULE_ACTIVATED.md), [saved draft](../../../pre-ad-readiness/2026-10-29/f1-f2-cycle/SAVED_DRAFT.md), [METRICS](../METRICS.md).

## Expected vs actual

| Mục | Expected (receipt) | Actual (UI đọc 29/10/2026) | Kết luận |
|---|---|---|---|
| Parent VALIDATION_ONLY_VN_SEMICONDUCTOR_ABM_2026-09-14 | On/Active | On/Active; objective Brand awareness; schedule “run continuously starting 9/14/2026” | MATCH |
| Ad set DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH | On, Not delivering – Scheduled | On, “Not delivering – Scheduled”; Sponsored Content; Reach; Maximum delivery | MATCH |
| Ads | F1/F2 On/Active, cùng ad set | LI-wave01-F1-en-COLD-v1 và LI-wave01-F2-en-COLD-v1: On/Active, Single Image, đúng ad set; ad set ghi “2 ads” | MATCH |
| Budget/currency | USD10 daily shared | ô Daily budget = $10.00; label currency USD; UI tính “spend up to $70.00 total” | MATCH |
| Lịch | 01–07/11/2026 | Start 11/1/2026, End 11/7/2026, “for 7 days”; giờ VN 07:00→06:45 không đọc lại ở lượt này (chỉ có trong receipt) | MATCH ngày; giờ UNVERIFIED lượt này |
| Location | Vietnam | Vietnam, recent/permanent | MATCH |
| Job functions / seniority | Engineering, IT, Operations, QA AND CXO/Director/Manager/VP | đúng như vậy | MATCH |
| Company list | R5 matched list (receipt chỉ ghi “R5”) | một company list tên bắt đầu TEST-AUD-CONTINGENCY-TRUE-ONLY-R5 nằm trong audience; chưa dùng tên này làm bằng chứng nội dung list | OBSERVED, cần Bảo xác nhận đây là R5 |
| Audience size | 470+ | forecast 470+; 30-day forecast spend $0.00–$14.00, reach 71–170 (ước tính định hướng, không phải kết quả) | MATCH |
| Audience expansion | off | tắt (checkbox bỏ chọn) | MATCH |
| Placement | Feed only; RightRail/LAN/Expansion off | LinkedIn feed bật; Right Rail tắt; LinkedIn Audience Network tắt | MATCH |
| Profile language | English | KHÔNG đọc được lựa chọn đã chọn (DOM chỉ liệt kê danh sách ngôn ngữ) | UNVERIFIED |
| Hai probe ad set | Draft/Off | VALIDATION_ONLY_VN_…_AUDIENCE_TEST: Draft. VALIDATION_ONLY_R5_EN_ELIGIBILITY_20261028_DO_NOT_LAUNCH: Draft. Không bị bật | MATCH |
| Delivery 30 ngày | chưa có | Spent $0.00, impressions 0, clicks 0 trên danh sách ad/ad set | EXPECTED_NO_PAID_DATA, không phải số 0 đã đo |

Review/rejection/hold: bảng ads chỉ hiện “Active”; không thấy nhãn rejected/hold trong hàng. Đây không chứng minh policy approval hoặc đủ điều kiện delivery; receipt đã ghi modal “Your ads are being reviewed”. Không đọc được trang chi tiết xét duyệt từng ad ở lượt này.

## Incident / observation list

1. **Chưa có lỗi nào làm hỏng F1/F2** trong các trường đọc được. Không có hành động đề xuất cho F1/F2.
2. **OBS-1 (ngoài phạm vi F1/F2, cần Bảo xem):** campaign “Test” (Brand Awareness) đang On/Active, bidding Maximum delivery, chứa ad “Images Carousale Test” On/Active. Spend/impressions 30 ngày = $0. Chưa đọc budget/lịch của campaign này nên chưa biết có thể tiêu tiền hay không. Đề xuất: Bảo quyết có đọc tiếp hoặc dừng; tôi không dừng.
3. **OBS-2:** campaign RSCH-TH-WEBINAR-FORECAST-1027 (draft, research only) đang On, “Campaign scheduled”. Ngoài scope F1/F2; ghi để Bảo biết.
4. **OBS-3:** có một banner “Pick up where you left off” cho VALIDATION_ONLY_R5_EN_ELIGIBILITY_20261028 (Draft). Không bấm Edit & launch.
5. **Task nhắc trên Overview:** ad set F1/F2 chỉ có 2 creatives, LinkedIn gợi ý ≥3. Chỉ là gợi ý tối ưu, không phải blocker; không thêm creative.
6. **Giới hạn kỹ thuật:** chụp ảnh màn hình trang editor bị timeout sau khi cuộn/bấm, nên các giá trị được đọc từ accessibility tree và DOM (read-only). Một lần công cụ `find` báo Right Rail/LAN “checked” sai; giá trị thật đọc từ DOM checkbox là tắt. Chỉ dùng giá trị DOM. Khi rời trang editor, hộp thoại “Leave site?” xuất hiện; tôi đã rời mà không lưu và không có chỉnh sửa nào của tôi.

## Việc còn lại / recheck

- Đọc lại ngay trước 01/11 07:00 VN: trạng thái ad/ad set, nhãn review và chọn ngôn ngữ trong audience (trong UI, không qua DOM danh sách).
- Bảo xác nhận company list đã chọn đúng R5 mong muốn.
- Sau 01/11: ghi actual first delivery và các khoảng reject/pause; không suy từ lịch.

Docs impact reviewed: no canonical update required. Đây là artifact thực thi trong gói pre-readback; không đổi audience/message, cap, lịch, creative hay tracking implementation.
