> **PO scope / Carousel verification · 2026-10-05:** Giữ **new cold Brand awareness + Carousel image → RMK chính new-ad cohort sau đó**; không lấy existing Digiwin Page pool. Awareness có Carousel (PO screenshot/UI), **Engagement cũng có Carousel** (selected native UI/screenshot); official guidance thêm Website visits, Website conversions, Lead generation. Format compatibility không phải native RMK source eligibility; đổi objective chưa giải quyết Carousel-source gap. Bảo không chọn Document; không đổi objective/creative. Trước delivery chưa có warm pool là expected, không phải blocker cold launch. Source CSV 424 rows chỉ name/country/city; private full review worksheet + source registry/measurement/gate templates đã chuẩn bị, identity/cleaned reach OPEN. [Current evidence/data plan](LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md).

# LinkedIn — evidence để quyết định targeting và RMK · 2026-10-05

## Mandate / acceptance

Bảo yêu cầu tiếp tục các khuyến nghị research để có đủ evidence quyết định. Tiếp tục trên `slice/linkedin-audience-ready-research`, baseline local commit `764545b`; không spawn. Outcome: đọc đủ mapping table, lập queue xác minh local, kiểm tra nguồn Website/Company Page và phân biệt source activity với matched reachable members; lưu screenshot/private report, đồng bộ canonical docs. Stop trước upload/replacement, Agree and create, publish, enable hoặc spend. Acceptance bằng table row counts, screenshot/source-editor read-back, local evidence hash/image verification và final diff/sanitization review.

## Facts mới

### Company mapping

Đã đọc cả 3 trang **50 + 50 + 17 = 117 rows**, 117 unique matched Page URLs. Bảng private giữ input name, matched name/page, industry, size và source page/row. Tất cả **117 input Domain và Page URL đều `-`** trên UI; không suy đây là toàn bộ 424 input rows.

Triage thủ công theo tên hiển thị, chưa xác minh pháp nhân/corporate relationship hoặc ICP:

| Nhóm review | Rows | Ý nghĩa |
|---|---:|---|
| Name-consistent candidate | 34 | Có cùng tên/stem nhận diện; vẫn cần official source, entity scope/location và ICP |
| Short name / group ambiguous | 8 | Tên quá ngắn hoặc group/subsidiary không đủ kết luận |
| Name-inconsistent, review required | 75 | Input và matched name không tương ứng rõ; không tự coi tất cả là false match |

Không có nhóm nào được gán VERIFIED hoặc production-approved. Không báo `75/117` là tỷ lệ match sai. Có ví dụ rõ về input doanh nghiệp điện tử ghép sang trang khác tên/ngành; **cũng có tên không tương ứng nhưng matched industry vẫn Manufacturing/electronics**. Vì vậy industry filter không giải quyết được entity identity; không đề xuất dùng nó thay việc làm sạch mapping. Raw names/URLs chỉ nằm private ngoài repo.

LinkedIn khuyến nghị bổ sung website/named Company Page URL và thông tin entity để cải thiện matching. Company-list upload có minimum **300 rows**, khác minimum **300 matched member accounts** để dùng ad set. Queue 34 candidate không phải upload-ready list; không nhân bản/padding để vượt sàn. [Official company-list guidance](https://www.linkedin.com/help/lms/answer/a423102/account-and-contact-targeting-list-templates?lang=en).

### RMK alternatives — actual source editors

| Source / cấu hình | UI output | Disposition |
|---|---|---|
| Company Page visits, 30 days | **29 unique visitors** | Không có evidence warm matched pool >=300 |
| Company Page visits, 90 days | **101 unique visitors** | Không giải quyết gate 30-day pool |
| Company Page visits, 365 days | **317 unique visitors** | Candidate source duy nhất ở đây gần sàn; chưa là matched audience và chưa lọc VN/ICP |
| Company Page header CTA clicks, 365 days | **0** | Không có source activity khả dụng được hiển thị |
| Website Buttons | 31 displayed actions; top click estimate ~40, last 30 days | Domain thử nghiệm hiển thị, chưa chứng minh production traffic |
| Website Pages | 18 displayed pages; top estimates ~80 visits/page, last 30 days | Các URL hiển thị thuộc domain thử nghiệm; không cộng thành unique members |

Website default engagement selector là 90 days nhưng column metrics ghi **last 30 days**; không gọi các page estimates là 90-day audience size. Chưa thay domain, thêm tag, nhập URL, chọn page/action hoặc tạo audience. Source editor có activity không chứng minh tag đúng production route hay real buyer traffic. Domain/raw page URLs nằm private.

Company Page source size giảm từ 317/365d xuống 29/30d; mở rộng lookback sẽ đổi recency và scope, không phải sửa nhỏ để giữ nguyên `LI-AUD-P1-ENGAGED-30D`. Chưa tạo audience để kiểm tra opt-in matching, location hoặc target size; không gán 317 thành ready members. Native editor nêu matching phụ thuộc member opt-in và processing. [Official retargeting overview](https://www.linkedin.com/help/linkedin/answer/a427551/retargeting?lang=en).

Previous source checks vẫn áp dụng: Single image source engagement total 0; Document total 0; current menu không có Carousel riêng. Không kết luận carousel engagement tự tạo warm pool.

### Metrics / prior reach

Official match rate đo source entries match trong 7 ngày; audience count là usable deduplicated reach với opt-outs. Đây là definition, **chưa reconcile được** 424 uploaded rows / 117 displayed matched / 86 unmatched / 80% của exact audience. Không chọn denominator mới. [Official match-rate definitions](https://www.linkedin.com/help/linkedin/answer/a420595/matched-audiences-match-rates?lang=en).

Saved definition `RSCH-CL-VN-LEAD-20261005` được read-back cuối phiên: **780 members**, research-only description giữ nguyên. Prior research **4,800+ functions / 780 leadership** và Vietnamese too-small là reach của **tệp chưa xác minh identity**. Chưa có cleaned-list filtered reach; không trình số 780 như verified ICP. Không thử thêm filter grid trên tệp này vì kết quả không đóng được quality gate.

## Decision pack

| Quyết định | Khuyến nghị và căn cứ | Còn cần để vận hành |
|---|---|---|
| Awareness / messages / completed carousel | **Giữ định hướng và assets**; evidence mới là audience/source quality, chưa có delivery hoặc buyer-performance evidence để đổi nội dung | Existing creative/proof/destination/tracking gates |
| Company-list production use | **Làm sạch identity trước**; enrich official named Page URL/domain, adjudicate 117 mapping queue, xử lý 86 unmatched và coverage của full source | Entity + ICP verified input; upload/match research riêng rồi đo lại VN/functions/leadership reach |
| Language / segmentation | Giữ English profile targeting làm research baseline; Vietnamese configuration đã too-small. Chưa split further theo seniority/FDI/domestic | Cleaned filtered reach; FDI/domestic evidence, không suy từ profile language |
| Immediate 30-day RMK launch | **Chưa có source đủ evidence**; Company Page 29/30d và ad-source totals 0 không hỗ trợ plan chạy RMK ngay | Eligible matched warm audience >=300 sau filters |
| Company Page 365-day fallback | Có thể là **test hypothesis sau**; 317 source visitors chỉ hơi trên minimum trước match/VN/ICP, recency khác kế hoạch | PO chọn scope/recency; actual audience processing/filter reach, không promise viability |
| Website RMK | Ưu tiên inventory production route/tag và clean traffic trước; không adopt dữ liệu domain thử nghiệm | Exact production URL/tag ownership and real route events; existing tracking contract |
| Budget / allocation | Chưa đổi budget hoặc tỷ trọng từ evidence này; không dùng default $200 unsaved form làm forecast quyết định | Approved envelope + eligible audience + launch measurement |

**Đủ evidence để chọn bước tiếp theo:** giữ creative, sửa input targeting, trì hoãn giả định immediate RMK và xác minh production tracking. **Chưa đủ evidence để launch hoặc chốt phân bổ**. Full verified input/enrichment và cleaned-list upload không được mô tả là đã hoàn thành trong research này.

## Evidence / state closeout

10 JPEG mới (15–24), ba private mapping JSON, CSV queue 117 rows, six source-editor text snapshots và hash manifest nằm ở private evidence `round2`, ngoài public repo. Images decoded/verified; screenshot 21/22 visually inspected showing exact 30/365-day selectors and 29/317 counts. Full-page table screenshots không thay thế 117-row extraction vì horizontal/viewport limits; JSON/CSV giữ row/column evidence.

Website/Company Page editors đều **Cancel**, không Agree and create. Không có persistent LinkedIn mutation mới trong round này; previous Saved Audience là object research duy nhất được tạo. Không sửa mappings/upload, không tạo ad set/ad hoặc publish/enable/spend. Browser cuối phiên ở Saved Audiences với existing research definition 780.

Docs impact reviewed: CURRENT_STATE, README, Build Pack, Pre_Ad_Readiness, S03 và prior research receipt được cập nhật/review. Discovery handover/Ready register vẫn đúng phạm vi Ready + technical size; S02/S04/proof/HTML/tracking implementation không đổi. Main worktree không bị sửa, không merge/push. Round2 report/canonical edits được lưu bằng containing local checkpoint trên branch theo mandate commit local của Bảo; không nằm trong prior checkpoint `764545b`. Commit identity được read-back sau commit.

Execution: **SUCCESS for bounded research and decision evidence**. Audit: scoped source/mapping/counts/boundary review complete; **identity/cleaned reach/RMK production eligibility OPEN**, không campaign PASS.
