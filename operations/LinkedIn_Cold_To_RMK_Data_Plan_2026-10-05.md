> **Latest PO closeout · 2026-10-05:** Phase 1 ưu tiên cold; RMK concept campaign/new-ad cohort → interaction window → Engagement hoặc click LDP được ghi nhận, không tự suy account hỗ trợ native Carousel interaction source. Defer implementation gap tới preparation Phase 2; chưa đổi objective/creative, chưa launch. PO yêu cầu local checkpoint + main integration.

# Cold awareness mới → engagement RMK: evidence và data plan · 2026-10-05

## PO scope correction

Bảo xác nhận luồng ban đầu: **chạy cold awareness mới trước, sau đó remarketing những người tương tác với chính ads awareness mới**. Không lấy existing Digiwin Company Page audience làm nguồn RMK. Không có warm pool trước delivery là trạng thái bình thường của sequence này, không phải lý do đổi chiến lược hoặc đánh giá cold campaign thất bại.

Company Page/Website test-domain inventory ở round2 chỉ là research phụ. Đề xuất dùng Page 365-day fallback trong report trước **không được adopt và bị loại khỏi current campaign plan** theo latest PO scope. Historical screenshots/receipts giữ nguyên. Website click pool từ *ads mới* là một lựa chọn khác về semantics, không thay thế tất cả ad interactions nếu chưa được Bảo chọn.

## Execution contract và actual findings

Outcome của round3: xác minh native engagement rules + format/objective compatibility; chuẩn bị source registry, collection sheet và RMK gate; kiểm tra actual local source quality/enrichment queue. Research UI/unsaved form được phép; dừng trước save ad set/ad, upload, agreement, publish/enable/spend. Acceptance: selected native rule/read-back, Document selected dưới existing Brand awareness validation campaign Paused, Exit without saving và không có new ad set, CSV/source counts + screenshot hashes, canonical diff review. Không spawn.

| Check | Actual evidence | Meaning |
|---|---|---|
| Retargeting source menu | Member types có Single image, Document, Video; không có Carousel type trong menu đã kiểm tra | Không có verified native Carousel-image engagement route trong scope này |
| Single image 30-day rule | `Any interactions with your ad` hoặc `People who performed chargeable clicks on your ad`; có thể chọn exact ad set | Rule definition/source selection được chứng minh, không phải production pool |
| Single image source row | Existing validation Draft; total 0 / row `-` | Không dùng test ad set làm nguồn campaign mới; không gọi là performance baseline |
| Document 30-day rule | Any interactions, chargeable clicks, downloaded document | Có native source phù hợp với mục tiêu RMK theo ads mới |
| Document objective compatibility | Existing validation campaign **Brand awareness / Paused**; new unsaved form cho chọn **Document**, checked state observed | Account hỗ trợ lựa chọn này; chưa tạo/upload creative hoặc adopt format |
| Targeting imported into unsaved form | Prior Saved Audience reach vẫn **780+** sau load | Reach của unverified company input, chưa phải sạch/ICP accepted |
| Saved audience composition | Summary: Operations **68%**, Manager **57%**, Computers and Electronics Manufacturing **47%**, company size 10,001+ **53%** | Descriptive UI insights của current definition; không phải tỷ lệ delivered audience hay kiểm chứng identity |

Saved detail DOM có side-panel placeholder `<300` khi load, trong khi imported ad-set form sau load hiển thị 780+. Không coi placeholder đó là actual size regression; giữ hai surfaces trong private snapshots, không thêm suy luận nguyên nhân. Insights percentages không được nhân thành precise member counts hoặc cộng qua facets.

Official LinkedIn retargeting documentation xác định nguồn Single image/Document và tương ứng engagement triggers, không liệt kê Carousel image source. Đây là **implementation gap**, không phải statement mọi account vĩnh viễn không có capability. [Official engagement types/triggers](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/advertising-targeting/engagement-retargeting?view=li-lms-2026-09).

## Format decision — proposal, not adopted

| Route | Giữ được điều gì | Trade-off / gate |
|---|---|---|
| **Document nhiều trang + Brand awareness → Document interactions 30d → RMK** | Chuỗi kể chuyện nhiều trang; native engagement source từ chính cold ads mới | Khuyến nghị nghiên cứu tiếp. Cần PO chọn format adapter, PDF/export/native readability QA; không tự đổi accepted Carousel artwork. Links trong document chỉ clickable sau download; không giả định destination/card-link behavior giữ nguyên |
| Single image + Brand awareness → Single-image interactions 30d → RMK | Native interaction pool đúng cold nguồn mới | Cần concept/copy adaptation; một hình không giữ nguyên toàn bộ story nhiều card |
| Carousel image → click sang route mới được gắn nguồn → website RMK | Giữ native Carousel assets và destination links | Chỉ retarget được subset có website visit/match, không bao gồm all likes/swipes/engagement. Cần production route/Insight Tag/attribution inventory riêng, không dùng historical Page/test traffic |

Document hỗ trợ Brand awareness; quảng cáo được đọc/download trong feed. CTA/link behavior khác Carousel và là material trade-off cần quyết định. [Official Document ad guidance](https://www.linkedin.com/help/lms/answer/a737898/linkedin-document-ads?lang=en). Carousel ad sets không mix format khác trong cùng ad set, nên thêm Single image companion cũng không thu native Carousel engagers. [Official Carousel FAQ](https://www.linkedin.com/help/linkedin/answer/a423082/carousel-ads-faqs?lang=en).

**Latest PO response:** Bảo không chọn Document cho cold awareness; yêu cầu điều tra Carousel images với Engagement và các ad objectives. Giữ cold Carousel awareness đã chốt. Document ở bảng trên chỉ là research alternative không được adopt; không tạo PDF/adapter mới. Các collection templates độc lập format và không tự release live action.

## Carousel image objective matrix — verified follow-up

| Objective | Carousel image | Evidence / operating role |
|---|---|---|
| **Brand awareness** | **Có** | PO screenshot 35 + account UI options; giữ original cold direction |
| **Engagement** | **Có** | Actual unsaved form selected Carousel, screenshot 34; tối ưu engagement, không tự tạo eligible RMK source |
| Website visits | Có theo official guidance | Traffic objective; chưa test bằng account form trong round này |
| Website conversions | Có theo official guidance | Cần website conversion measurement/eligibility riêng; chưa adopt |
| Lead generation | Có theo official guidance | Có thể kèm Lead Gen Form; form open/submit pool là subset riêng, không phải all Carousel interactions |

Carousel image là **Sponsored Content format**, objective là mục tiêu tối ưu riêng. [Official create-Carousel prerequisites](https://www.linkedin.com/help/lms/answer/a421188/create-a-linkedin-carousel-ad-campaign?lang=en) liệt kê cả 5 objective. Không ghi Brand awareness thiếu Carousel. PO screenshot hiển thị 5 format choices; existing validation/Engagement research surfaces hiện nhiều choices hơn. Ghi đúng từng context, chưa gán nguyên nhân/version/campaign type cho khác biệt.

Engagement test chỉ mở **new unsaved form** dưới existing unrelated Engagement campaign với ended schedule/Not delivering; không edit existing campaign/ad set, không đổi switch/budget/schedule, không save/enable. Đã Exit without saving và Create later. Forecast/default targeting/budget trong form không được dùng làm campaign data hoặc proposal.

**Đổi Awareness sang Engagement không chứng minh sẽ thu native audience của Carousel engagers.** Native retargeting source menu và official supported source types vẫn không có dedicated Carousel image source. Engagement metric reporting và Matched Audience eligibility là hai capability khác. Không đổi objective để chữa source gap khi chưa có route evidence.

Giữ phương án campaign: cold **Brand awareness + Carousel image**. Cần resolve source-to-RMK path trước production: native Carousel source nếu LinkedIn/account xác nhận thêm; hoặc PO chọn new-ad website-click/form-open subset và chấp nhận semantics khác. Không tự chuyển sang Document, Single image, existing Page pool hoặc Engagement.

## Cold input quality — actual source và prepared review

Đã đọc đúng local sanitized source CSV, hash giữ private. **424 rows**, headers chỉ `companyname,country,city`; 424 country values, 346 city values; không có domain/website/LinkedIn Page field. **421 exact names / 419 case-insensitive normalized names**: hai definition khác nhau, không gọi 419 là exact uniqueness. Không khẳng định file hash hiện tại là exact historical uploaded bytes khi historical receipt không pin hash.

Private full-source review worksheet có **424 rows**, original source-row traceability; giữ nguyên original CSV. Hai priority mapping findings đã có official-name/source leads để enrich, nhưng **0 correct named LinkedIn Page verified / 0 rows upload-ready** trong worksheet này. Một lead có exact VN entity trong official group network; không gán group domain thành subsidiary website. Lead cơ khí có about-page name nhưng homepage mixed naming/direct-page retrieval issue, nên vẫn HOLD. Raw names/official URLs chỉ ở private worksheet, không đưa customer table vào repo.

Existing 117 matched-page queue và 86 Unmatched UI count vẫn giữ OPEN. Hai leads không giải quyết toàn bộ 424 rows và không chứng minh đủ semiconductor/FDI/domestic scope. Next substantive cold task: verify exact entity + official named Page URL + VN/corporate scope + ICP for full source, adjudicate mappings, then remeasure cleaned VN/functions/leadership reach. Không dùng industry filter làm substitute, không padding list để vượt upload minimum.

## Data collection contract

Ba CSV header-only đã chuẩn bị private; **không có invented delivery rows**. Baseline của new cold campaign/ad set/ad IDs, spend, impressions, engagements và RMK members đều **UNKNOWN / NOT CREATED**, không gán số 0 của historical test rows sang campaign mới.

1. **Source registry trước launch:** pin campaign/ad-set/creative IDs của *new cold release*, content/targeting revision, format, rule/lookback, owner, approved source scope. Default proposed rule: **Any interactions, 30 days**, chỉ exact new cold source IDs. Chargeable-click/download pools là alternatives riêng; không silently union với Page, organic hoặc unrelated campaign. Chưa tạo matched audience vì chưa có exact production source và chưa cần nhận agreement trong research.
2. **Daily snapshot khi authorized delivery bắt đầu:** calendar date + account timezone + eligible delivery day, spend/currency, impressions, native reach/frequency, metric-defined engagement/click counts; Document view/download metrics nếu format đó được chọn. Pin source IDs và revision để không gộp các slices khác scope. Synthetic visits/test records không vào kết quả paid.
3. **Pool check:** source rule/lookback, exact IDs, processing/Ready status, displayed matched member count, actual filtered reachable count/eligibility. Source engagements không phải unique matched people; không dự đoán pool size bằng CTR × reach hoặc cộng unique audiences qua creatives.
4. **Cadence proposal:** daily integrity/pacing recording; check ở eligible delivery day 3 và 7, sau đó weekly trên cấu hình ổn định. Đây là lịch lấy mẫu đề xuất, không mandate scheduler và không hứa RMK ready sau 7 ngày. Native audience processing có latency; lấy fresh status khi đánh giá.
5. **RMK release gate:** đúng source cohort mới + rule/window được PO chọn + actual Ready/eligible + **>=300 reachable members sau filters theo UI** + proof/destination/HTML/tracking/pacing/budget gates. Chưa đủ thì tiếp tục cold theo approved envelope hoặc báo decision về scope/recency; không tự lấy Page users hoặc enable RMK theo calendar.

Prior 780 is targetable research slice, không phải sufficient warm-pool forecast. Không chia thêm 11 tiny pools theo creative/scenario ngay từ đầu; đề xuất pool theo approved compatible source cohort, vẫn lưu per-creative metrics để đọc story performance. Không adopt pooling/budget architecture trước cleaned reach và owner decision.

Website Insight Tag không phải prerequisite cho native Single image/Document engagement RMK. Nó chỉ đi vào critical path nếu PO chọn website-click route. HTML click-expand, route/ad-adapter pair và destination/tracking vẫn có gate riêng; scope correction không tự PASS các assets/routes đó.

## State / evidence / closeout

11 screenshots mới (25–34 agent + 35 PO-provided), source editors/format/detail/exit DOM snapshots, full-source review 424, source-quality summary và 3 collection templates nằm private `round3` ngoài repo. Images decode verified; screenshot 34 được visual read-back: Engagement header + selected Carousel image cùng viewport. Screenshot 30 hiển thị Brand awareness format options nhưng còn Single image selected khi capture; không dùng ảnh đó làm proof Document selected. Document checked state chỉ giữ trong DOM snapshot; không cần further Document test theo PO rejection. Existing ad set vẫn Draft/OFF; unsaved format form Exit without saving, không có new ad set. Saved-tab Create audience ban đầu mở New audience form; đã thoát bằng **Do not save**, không lưu thêm definition. Retargeting editors đều Cancel.

Docs impact reviewed: CURRENT_STATE, README, Build Pack, Pre_Ad_Readiness, S03, S04 và prior decision report được đồng bộ/reconciled. Tracking implementation/runbook/source brief không đổi; latest PO scope bổ sung operational source contract ở đây, không rewrite HISTORY. Containing local checkpoint theo prior commit mandate; main không sửa, không merge/push/live.

Execution: **SUCCESS for bounded format/source/data-contract research**. Audit: evidence/CSV/source-count/no-save/docs inspection complete. **Cold Carousel awareness giữ nguyên theo PO; native Carousel engagement-to-RMK route, full identity cleanup, cleaned reach và actual new-cold delivery data còn OPEN**; không campaign-ready PASS.
