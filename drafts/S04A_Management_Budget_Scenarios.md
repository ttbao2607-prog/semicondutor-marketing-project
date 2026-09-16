# S04A — Đề xuất ngân sách và giả thuyết đo lường để trình quản lý

**Trạng thái:** đề xuất nội bộ; **DRAFT / MANAGEMENT APPROVAL PENDING**  
**Ngày:** 2026-09-16 · Asia/Ho_Chi_Minh  
**Chủ sở hữu vận hành:** Bảo — Paid Product Owner  
**Phạm vi:** media paid. Tài liệu này không cấp quyền tạo/sửa account, tag, form, audience hay campaign; không cho phép publish, enable, spend hoặc submit form.

## 1. Đề nghị quyết định

Đề nghị quản lý phê duyệt **envelope media trung bình 1.000.000 VNĐ cho mỗi ngày delivery đủ điều kiện**, sau khi chốt ngày chạy và cách tính thuế/phí. Đây là mốc pacing và trần lập kế hoạch, không phải platform daily cap tự động hay quyền chi tiêu.

Trong envelope được duyệt, Bảo tự giữ, test hoặc tái phân bổ phần linh hoạt theo evidence. Scale cấp 2 đề nghị nâng envelope lên **tối đa 1.250.000 VNĐ/ngày delivery đủ điều kiện**; vì tăng tổng ngân sách nên chỉ làm khi quản lý phê duyệt lại.

Campaign là awareness dài hạn. Tín hiệu yếu hoặc chưa kết luận **không phải fail-close**: quay về observation/test có kiểm soát. Chỉ lỗi nghiêm trọng về claim, privacy, tracking, URL/route hoặc form receiver mới dừng tactic/route bị ảnh hưởng.

| Nội dung | Fact / proposal / unknown |
|---|---|
| Ưu tiên | **Fact:** OSAT/factory là ưu tiên nội dung; Fabless và Partner theo dải brief. Content mix không phải quota spend. |
| Mốc budget | **Fact:** `1.000.000 VNĐ/ngày` là working reference trong chỉ đạo Bảo; canonical vẫn ghi management-approval pending. |
| Allocation, ngưỡng và phản ứng | **Proposal:** là khuyến nghị vận hành, không phải forecast, benchmark ngành hay KPI sếp đã giao. |
| Thuế/phí, ngày delivery, audience/query khả dụng, account history, tracking/form inventory | **Unknown:** phải xác minh trước launch; không tự đưa vào mẫu số/envelope. |

Nếu `1.000.000 VNĐ/ngày` bao gồm thuế, agency/service fee hoặc production, phải tách các khoản đó trước khi áp dụng plan media. Tổng media = `ngày delivery đủ điều kiện × average daily envelope`; không mặc định thành 60 triệu vì brief bao phủ hai tháng lịch.

## 2. Allocation khởi đầu

| Bucket | Kế hoạch / ngày delivery | Vai trò | Quy tắc trước khi có evidence |
|---|---:|---|---|
| LinkedIn prospecting / awareness | 600.000 VNĐ | Độ phủ/frequency đúng account–role; test OSAT-led expert message | Chỉ dùng sau audience/objective/placement readiness. Native LinkedIn engagement báo riêng với landing traffic. |
| Google Search | 250.000 VNĐ | Bắt operating intent bằng exact/phrase và query control | Không mua query rộng/sai intent để tiêu tiền. Planner hiện không chứng minh demand bằng 0. |
| Reserve linh hoạt / retargeting đủ điều kiện | 150.000 VNĐ | Một test có hypothesis, winner đã validate, hoặc retargeting đủ điều kiện | Giữ không chi khi chưa có lý do rõ. LinkedIn retargeting chưa launchable dưới `>=300` reachable members. |
| **Tổng trần** | **1.000.000 VNĐ** | Envelope media | Bucket chưa ready/không eligible thì giữ lại; không ép tiêu đủ trần. |

Reserve không phải quyền phải dùng, không tự chuyển thành retargeting và có thể không chi cả campaign.

## 3. Giả thuyết đo lường

Campaign không tuyên bố đo trực tiếp việc người xem đã coi Digiwin là chuyên gia. Chuỗi evidence cần xây là: phân phối đúng tệp hoặc Search relevance → attention vào thông điệp vận hành bán dẫn → progression tùy chọn. Lead/commercial signal là chỉ số cộng thêm, không là KPI awareness chính.

| Giả thuyết | Evidence có thể ủng hộ | Metric/mẫu số quyết định | Không chứng minh được |
|---|---|---|---|
| H0 — đường đo đáng tin | Route đúng; UTM/click ID còn khi có; một owner `page_view`; không duplicate đã biết; không PII | QA evidence theo route/platform; không dùng composite score | Business value hay awareness lift |
| H1 — LinkedIn vào đúng population | Delivery distribution, account/role coverage quan sát được, reach/frequency cùng scope, interaction phù hợp format | Báo riêng theo platform, period, audience definition | Identity cá nhân, cross-platform unique reach, changed perception |
| H2 — Search bắt relevant intent | Search term theo rubric viết trước; exact/phrase; paid landing attention | `relevant observed-query clicks / observed-query clicks`, kèm visible-query share | Tổng demand hoặc query ẩn |
| H3 — ad promise và landing cùng intent tạo attention | Paid sessions, engaged sessions, proof/content interaction đã định nghĩa; CTA intent tách riêng | Cùng source, route, period, denominator; cost/engaged session cùng scope | Role qualification, proof comprehension, accepted form/booking |
| H4 — retargeting chỉ chạy khi khả thi | Source audience audit được, eligibility, frequency và attention/progression tăng thêm | Eligible audience size + native/route metric cùng scope | Rằng phải chạy vì có reserve |

**Hợp đồng đo tối thiểu:** inventory page/GTM/GA4/Google Ads/LinkedIn trước khi reuse; micro-event chỉ reporting và không thành primary Google Ads conversion; không cộng reach xuyên platform; CTA intent, successful form và booking là ba state khác nhau; source hiện chưa xác minh form-success event name nên không tự gọi `accepted_form`; luôn báo timezone, currency, attribution window, latency, missing/hidden data. Mẫu số bằng 0 là *không tính được*, không phải cost bằng 0.

## 4. Data floor và nhịp review

Review đầu sau khoảng **7 ngày delivery hợp lệ**. Thời gian trôi qua không tự làm kết quả đủ mẫu; chưa đạt floor thì giữ observation.

| Lớp | Floor tạm thời cho so sánh đầu | Ý nghĩa |
|---|---|---|
| Tracking/destination | Route QA pass; **0 lỗi critical chưa đóng** về duplicate, privacy, URL, claim hoặc form receiver | Điều kiện để đọc số, không phải kết quả marketing. |
| Search relevance | **20 observed query clicks** được phân loại bằng cùng rubric | Dưới mức này, relevance rate quá mong manh để đổi allocation. |
| Landing attention | **100 paid landing sessions/route/variant** đang so sánh, cùng source/period | Không đồng nghĩa 100 người là qualified audience. |
| LinkedIn | Hai weekly snapshot của cùng audience configuration và distribution/coverage view platform có | Data bị ẩn là limitation, không tự là fail. |
| Retargeting | Source/eligibility được ghi rõ và **>=300 reachable members** | Eligibility guardrail, chưa phải incremental value. |

Các mức `20`, `100`, `70%`, `+20%`, `-15%` và `-10%` dưới đây là **provisional operating proposals**, không phải benchmark ngành. Sau review sạch đầu, Bảo có thể calibrate theo volume thật, nhưng phải lưu giá trị cũ, lý do, ngày hiệu lực; không đổi ngược để làm đẹp kết quả.

## 5. Giai đoạn test → validate → scale

Giai đoạn tính theo **ngày delivery hợp lệ**, không phải ngày lịch. Kênh/route chưa ready hay thiếu source không được tính là đã qua phase.

| Giai đoạn | Mục tiêu và output | Ước tính media |
|---|---|---:|
| G0 — readiness | Business, route, tracking, audience/query, operation checks pass cho phần launch; chỉ go/no-go, chưa có performance conclusion | **0 VNĐ** |
| P1 — test | ~7 ngày đầu để tạo delivery evidence và baseline sạch cho route OSAT-led + tactic đã ready; ra minimum, observation hoặc test question | Tối đa **5.950.000 VNĐ active** (`850.000 × 7`) + **1.050.000 VNĐ reserve giữ**; total ceiling **7.000.000 VNĐ** |
| P2 — validate | ~14 ngày tiếp để lặp cùng-scope comparison, đạt floor và test một diagnosis/lần; ra observation/minimum hoặc Scale 1 | Tối đa **11.900.000 VNĐ active** (`850.000 × 14`) + **2.100.000 VNĐ reserve capacity**; total ceiling **14.000.000 VNĐ** |
| P3 — Scale 1 | Có winner đạt toàn bộ quality gate; reallocation control 7 ngày trong envelope hiện hữu | Tối đa **7.000.000 VNĐ** tại **1.000.000 VNĐ/ngày** |
| P4 — Scale 2 | Scale-1 result lặp lại hai review window và được duyệt envelope lớn hơn; mở rộng có rollback check 7 ngày | Tối đa **8.750.000 VNĐ** tại **1.250.000 VNĐ/ngày** |

Nếu một tactic không eligible, phần tiền đó được giữ lại, không âm thầm chuyển đi. P2 còn inconclusive thì quay về observation với một test giới hạn, không bị gắn fail/close.

## 6. Bốn trạng thái quyết định

### A. Minimum acceptable — tiếp tục học, chưa scale

**Threshold:** route/tactic đúng kỹ thuật, không có integrity issue critical, delivery chạm cấu hình mục tiêu trong dữ liệu thực sự quan sát được, và review đầu không lộ evidence material về audience/traffic sai scope. Attention có thể trung tính, chưa có winner.

**Phản ứng:** giữ base allocation thêm một review window; chỉ đổi một diagnosis/lần (creative/message, query/negative, hoặc ad-to-route match); không mở audience/query để làm đẹp volume. Reserve giữ nếu chưa có test viết rõ.

**Budget:** nếu LinkedIn và Search đều eligible: tối đa **850.000 VNĐ/ngày active** (`600.000 + 250.000`), giữ **150.000 VNĐ/ngày**. Trong 7 ngày: **5.950.000 VNĐ active**, **1.050.000 VNĐ reserve capacity**, trần **7.000.000 VNĐ**. Bucket không eligible thì actual thấp hơn.

### B. Observation / controlled test — thiếu mẫu, mâu thuẫn hoặc có diagnosis

**Threshold:** chưa đạt data floor; signal kênh mâu thuẫn; attention yếu dù delivery relevant; Search quá ít/nhiều observed query out-of-scope; frequency tăng nhưng attention giảm; hoặc account/role view bị ẩn/thiếu.

**Phản ứng:** ghi một test question, chỉ đổi một causal variable, có next review date. Ví dụ: test OSAT mechanism framing với control; siết exact/phrase và negative set; sửa ad promise–landing match; hoặc chờ retargeting đủ eligibility thay vì mở audience. Giữ các biến còn lại, denominator và attribution scope.

**Budget:** giữ tối đa **850.000 VNĐ/ngày** cho base tactic eligible. Reserve tối đa **150.000 VNĐ/ngày** chỉ cho *một* test có hypothesis; maximum 7 ngày vẫn **7.000.000 VNĐ**. Test chưa ready/không rõ hypothesis thì không chi reserve.

### C. Success level 1 — reallocation có kiểm soát trong 1.000.000 VNĐ/ngày

**Threshold:** phải đồng thời có data floor và measurement contract đạt, không critical issue; **Search >=70% relevant clicks** trong observed sample đã rubric; LinkedIn không có material delivery mismatch trong báo cáo khả dụng; landing giữ **>=80%** clean attention baseline khi delivery/spend tăng. Đồng thời primary diagnostic ghi trước tăng **>=20% tương đối** so với clean baseline/control (ví dụ relevance share, engaged sessions cùng scope, hoặc native interaction/reach cùng scope), **hoặc** giữ diagnostic đó và giảm matching cost/outcome **>=15%**. Quality không được xấu đi cùng lúc.

**Phản ứng:** reallocate control 7 ngày từ reserve, giữ `50.000 VNĐ/ngày` buffer; không cùng lúc thêm toàn bộ segment, format và retargeting. Báo control/winner riêng.

| Winner đã validate | LinkedIn | Google Search | Retargeting | Buffer | Tổng/ngày |
|---|---:|---:|---:|---:|---:|
| LinkedIn | 700.000 VNĐ | 250.000 VNĐ | 0 VNĐ | 50.000 VNĐ | 1.000.000 VNĐ |
| Search | 600.000 VNĐ | 350.000 VNĐ | 0 VNĐ | 50.000 VNĐ | 1.000.000 VNĐ |
| Retargeting, chỉ khi eligible | 600.000 VNĐ | 250.000 VNĐ | 100.000 VNĐ | 50.000 VNĐ | 1.000.000 VNĐ |

Scale-1 maximum 7 ngày là **7.000.000 VNĐ**. Bucket chưa ready/không hấp thụ được allocation không chi; không đổi targeting/bid chỉ để chạm spend.

### D. Success level 2 — expansion có phê duyệt lên 1.250.000 VNĐ/ngày

**Threshold:** Scale 1 hợp lệ qua **hai review window liên tiếp, mỗi window 7 ngày delivery hợp lệ**; mỗi window vẫn đạt floor/gate; primary diagnostic winner không giảm quá **10%** so với Scale-1 reference; delivery có capacity tăng budget mà không sai intent hoặc làm frequency/attention xấu đi.

**Phản ứng:** gửi management decision pack gồm spend/pacing vs plan; hai clean windows; scope/denominator; evidence quality/capacity; allocation đề nghị; risk nếu không tăng; rollback rule 7 ngày. Chỉ sau khi duyệt envelope mới Bảo tăng dần. Base route không thắng vẫn quan sát, không tuyên bố close vĩnh viễn.

| Winner đã validate | LinkedIn | Google Search | Retargeting | Reserve | Tổng/ngày |
|---|---:|---:|---:|---:|---:|
| LinkedIn-led | 800.000 VNĐ | 300.000 VNĐ | 0 VNĐ | 150.000 VNĐ | 1.250.000 VNĐ |
| Search-led | 600.000 VNĐ | 500.000 VNĐ | 0 VNĐ | 150.000 VNĐ | 1.250.000 VNĐ |
| Retargeting-led, chỉ khi eligible và không fatigue | 600.000 VNĐ | 250.000 VNĐ | 250.000 VNĐ | 150.000 VNĐ | 1.250.000 VNĐ |

Scale-2 review đầu 7 ngày có maximum media estimate **8.750.000 VNĐ**. Nếu Scale-1 quality guardrail gãy, quay về allocation 1.000.000 VNĐ/ngày trước đó hoặc observation; không giữ spend cao chỉ vì đã được duyệt.

## 7. Response map theo evidence

| Quan sát | Phản ứng | Budget posture |
|---|---|---|
| Claim/privacy/duplicate/route-URL/form-receiver defect critical | Pause **chỉ** phần bị ảnh hưởng trong mandate; sửa và re-QA trước resume. Scope/permission material đưa Bảo quyết định. | Affected spend = 0; không tự redirect. |
| Config eligible nhưng chưa đủ data floor | Observation tới review kế tiếp; báo sample size và missing-data limit. | Base active; reserve giữ. |
| Search relevance <70% | Đọc term theo rubric; siết exact/phrase/negative, không mở broad/sai intent lấy volume. | Giữ hoặc giảm Search; không redirect nếu chưa có test. |
| LinkedIn mismatch hoặc frequency tăng/attention giảm | Giữ audience scope; xoay một proof-safe message/format hoặc refine documented target setting; so với control. | Không scale; ở/nhỏ hơn base 600.000 VNĐ/ngày. |
| Traffic relevant nhưng landing attention <80% baseline | Audit promise match, speed/layout, source attribution; QA xong chỉ test một thay đổi. | Không scale; reserve chỉ cho test nêu rõ. |
| Minimum kéo dài | Chạy thêm review window và ghi hypothesis mới; không đóng vì thiếu lead volume. | Tối đa 850.000 VNĐ/ngày active + reserve giữ. |
| Success 1 / Success 2 | Chạy đúng controlled reallocation / xin duyệt envelope mới trước scale. | Theo bảng Scale 1 / Scale 2; rollback khi gãy guardrail. |

## 8. One-page weekly scorecard

1. **Pacing:** envelope duyệt; plan vs actual; budget còn lại; platform/tactic/segment mix; reserve; timezone/currency/tax-fee basis.
2. **Audience/demand:** LinkedIn distribution/coverage quan sát được; reach/frequency theo platform; Search relevance và visible-query coverage, kèm limitation.
3. **Attention:** sessions, engaged sessions, engagement rate, proof interaction theo paid source/route; native LinkedIn engagement tách riêng.
4. **Progression/commercial:** CTA intent; form acceptance chỉ khi source/name/receiver thật đã validate; booking/lead status chỉ từ source of truth; không gộp synthetic total.
5. **Decision log:** current state, hypothesis, change, owner, start/end, budget at risk, next review và rollback condition.

## 9. Gate trước khi thực thi

- Chốt envelope là media-only hay gồm tax/fees; ngày delivery thật; currency/timezone; mandate của Bảo cho budget change, pause và launch.
- Hoàn thành live inventory về platform goals, tag, consent, UTM/click-ID path, event owner, duplicate, form receiver và route compatibility. Workspace evidence hiện chưa chứng minh các fact này.
- Xác minh Search demand và LinkedIn audience/delivery trong môi trường được phép. Planner OSAT không hiển thị metric ở một configuration; không chứng minh có hoặc không có demand.
- Giữ retargeting inactive tới khi source, eligibility và threshold audience được xác minh.

**Terminal status:** proposal hoàn chỉnh để Bảo trình quản lý. Không phải approval để publish, enable, spend, submit form, upload audience hoặc đổi live measurement configuration.
