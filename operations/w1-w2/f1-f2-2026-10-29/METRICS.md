# Định nghĩa đo và cách điền

Dùng lại cấu trúc [Week1 readback](../../linkedin-rmk-source-readiness/2026-10-08/05_Week1_Readback_Template.md). READBACK.csv mở rộng thêm check_state, planned_check, window_status, raw clicks/click definition, reader engagement definition, metric origin, extraction timestamp và VND accounting basis. Cohort key F1F2-R5-EN-WAVE01 là local key, không audience ID đã tạo. ad_id/creative_id trong bản public dùng stable key; numeric IDs resolve private tại lần đọc, không copy raw data vào Git. Trường UNKNOWN không bằng0; PLANNED_NOT_OBSERVED không phải baseline.

| Metric | Definition / evidence | Cách dùng và giới hạn |
|---|---|---|
| Phân phối đúng tệp | Report company/function/seniority, scope/filter/date; giữ counts và phần unknown/suppressed | Không lấy matched company list hoặc English để chứng minh qualified buyer; không dựng %đúng nếu thiếu mẫu số |
| Reach / impressions / frequency | Native fields cùng scope/kỳ; nếu tự tính frequency=impressions/reach phải ghi DERIVED và reach>0 | Reach unique không cộng các ad để ra cohort; không trung bình các CTR/frequency để ra tổng |
| Clicks / CTR | Giữ định nghĩa dashboard: clicks loại gì, CTR dashboard hay derived100×clicks/impressions; denominator>0 | Brand awareness/Reach không là traffic experiment; click-all khác link click; không đổi definition giữa kỳ |
| Engagement | Counts và rate theo definition native, ghi numerator/denominator nếu nguồn có | Không gọi mọi engagement là reader hoặc awareness lift |
| Spend / CPM / CPC | Dashboard currency/timezone/before-tax basis; derived CPM=1000×spend/impressions, CPC=spend/clicks khi mẫu số>0 | Shared USD10/day; cohort total không cộng lại ad+cumulative; VND dùng basis kế toán thực có ngày, không bịa FX |
| Reader engagement | Processed source UTM + treatment F1/F2, real paid sessions/engaged sessions theo nguồn có | HTTP204 không đủ; sessions không bằng clicks1:1; không thấy cohort report ghi UNAVAILABLE/PROCESSING, không số0 |
| RMK eligibility | Exact source ads/rule/lookback/objective, native status, filtered reachable và thời điểm | Registry dự kiến không chứng minh audience tạo/Ready; kiểm gate theo source contract và UI hiện hành |

## Kỳ đo, dữ liệu và độ tin cậy

Chọn daily hoặc cumulative, ghi report_period_start/end/account_timezone/extracted_at trong notes. Không cộng daily với cumulative, không cộng cumulative nhiều ngày. So sánh F1/F2 trong cùng kỳ với exposure thực; thay đổi sau đó so equal-length windows và targeting/creative revision. Không tự quy causal lift từ hai tuần khác thời điểm. Nếu 7 ngày lịch chỉ có ít giờ delivery, ghi actual eligibility days; không gọi đủ learning.

Threshold register: sample minimum=UNSET; CTR target=UNSET; CPM/CPC ceiling=UNSET; frequency warning=UNSET; acceptable demographic coverage=UNSET. Đây là khoảng trống quyết định, không mặc định PASS/FAIL. Bảo chọn criteria cho phép thử tiếp theo trước khi áp dụng; nếu chưa có, báo số thô/chi/limitations và C7 thay vì gán nhãn winner. Các lỗi đúng-sai như URL sai, targeting drift, unauthorized claim hoặc vượt budget envelope có thể nhận diện ngay mà không cần ngưỡng CTR.

## Đọc và đề xuất khi có sự cố

C1 integrity → C2 audience → C3 delivery trước C4/C5. Báo Bảo ngay nếu lỗi có thể tiếp tục gây chi sai; gói này không cấp agent quyền pause/enable mới. Lưu sanitized evidence và đề xuất pause phạm vi ảnh hưởng. Bảo ghi quyết định/owner/rollback trong log; chỉ thực thi khi mandate cụ thể. Lịch W1 hết thì để kết thúc nếu chưa chốt W2.

Raw exports/account identities/member info/lead data giữ ngoài public repo. Feedback downstream do Bảo nhận là supplemental, không cần làm CRM/receiver work. Không dùng synthetic QA làm kết quả paid.
