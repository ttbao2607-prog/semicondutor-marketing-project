# Plan chuẩn bị trước readback W1 — F1/F2

Revision1 · 29/10/2026 · PLAN_READY. Authority ban đầu: Bảo yêu cầu “Dựng plan 7 điều trên, commit lên nhánh.” Plan không là lệnh thực hiện bảy hạng mục live. **Cập nhật 29/10/2026:** Bảo cấp mandate chỉ-đọc cho P1–P3; P1–P3 đã chạy (COMPLETE_WITH_GAPS, xem [PRELAUNCH_READBACK](PRELAUNCH_READBACK.md), [REPORT_ACCESS_MAP](REPORT_ACCESS_MAP.md), [BASELINE](BASELINE.md)). Cùng ngày Bảo giao tiếp P4–P7: đã soạn nội bộ [COLD_OPTIONS](COLD_OPTIONS.md), [CAROUSEL_QA](CAROUSEL_QA.md), [RMK_DECISION_PACK](RMK_DECISION_PACK.md), [W2_ACTION_CARDS](W2_ACTION_CARDS.md), [CRITERIA_DECISIONS](CRITERIA_DECISIONS.md), [INCIDENT_CARDS](INCIDENT_CARDS.md); các quyết định của Bảo vẫn NOT_DECIDED.

## Kết quả cần đạt và phạm vi

Đến kỳ readback gần nhất, Bảo có thể đọc đúng số, nhận diện khâu yếu và chọn một thay đổi cụ thể với asset/cấu hình/budget/recheck đã chuẩn bị. Mỗi hạng mục chỉ COMPLETE khi có đầu ra và evidence đúng acceptance bên dưới; UNAVAILABLE có lý do được ghi riêng, không biến thành dữ liệu0 hoặc giả PASS.

Làm trên worktree D:/Digiwin_F1F2_W1W2_2026-10-29, branch slice/f1-f2-w1-w2-decision-pack-2026-10-29; root thực hiện/tự review, không delegate. Planner/Executor/Auditor là trách nhiệm; independent audit NOT_RUN. Không làm trên main, không merge/push, không dựng scheduler/framework hoặc triển khai downstream.

Current source: [W1 activation](../../../pre-ad-readiness/2026-10-29/f1-f2-cycle/SCHEDULE_ACTIVATED.md), [decision pack](../README.md), [metric rules](../METRICS.md), [asset options](../ASSET_OPTIONS.md), [scope paid/downstream](../../../paid-scope/PO_Paid_Downstream_Boundary_2026-10-29.md). Last observed29Oct: R5/English, một shared cold ad set F1/F2, USD10/day, parent Active, ad set On/Scheduled, hai ads On/Active; không có readback mới ở lượt lập plan. W1 lịch01Nov07:00→08Nov06:45 VN, saved platform dates01–07Nov; actual eligible-delivery days phải đọc lại.

## Thứ tự và mốc tương đối

- Trước first delivery, mục tiêu trước01Nov07:00 VN: P1 preflight; P2 thử report; P3 ghi baseline. P3 có thể song song P1/P2 vì có thể dùng dữ liệu lịch sử sẵn có. Nếu trễ, giữ cutoff lịch sử trước actual delivery và ghi retrieval time, không giả đã quan sát trước chạy.
- Trong thời gian chờ readback: P4 brief/reuse, P5 carousel QA, P6 RMK decision pack. Ưu tiên P6 sớm để Bảo chọn nguồn tích lũy; không đợi W1 hết mới bàn rule.
- Trước kỳ review đầu tiên: P7 đóng các phương án vận hành và đề xuất criteria sau kết quả P1–P6. Không đợi đủ W1 mới báo lỗi integrity/delivery thật.
- Ngày delivery3/7 là checkpoint đề xuất, không là lịch task tự động. Chưa có đủ dữ liệu thì readback vẫn thực hiện và ghi INCONCLUSIVE; không đổi mốc chỉ để đạt kết luận.

## P1 — Kiểm trước ngày chạy

Owner: agent đọc/đối soát, Bảo quyết định khi cần thay trạng thái hoặc lịch. Dependency: exact ad identity trong saved/activation receipts; numeric IDs/screenshots lưu private.

Việc làm khi thực thi: đọc parent/ad set/từng ad, review/rejection/hold, schedule và timezone, USD10 shared, placement/targeting drift; xác nhận hai probe vẫnOff. Có problem thì ghi exact visible evidence và action đề xuất, không bấm enable/relaunch theo suy đoán.

Đầu ra: PRELAUNCH_READBACK.md, sanitized status snapshot có observed_at, expected vs actual và incident list. Acceptance: đúng hai ads/parent; dates/currency/budget đọc từ saved UI; không lấy activation snapshot cũ làm trạng thái mới. Nếu reject/hold: chuẩn bị nguyên nhân và next action cụ thể. Change cần mandate tương ứng, không chờ hếtW1.

## P2 — Thử đường lấy báo cáo

Owner: agent; dependency: source registry và quyền đọc LinkedIn/GA4 đang có. Chỉ đọc/report navigation; không sửa tag, GA4 config/dimensions, campaign hoặc tạo integration.

Việc làm: tìm đúng ad-set/ad reports và demographic breakdown khi nguồn có; ghi click definition, currency/timezone, report window và lag. Với GA4, thử lọc current reader theo treatment/UTM riêng F1/F2 và chọn processed sessions/engagement. Trước delivery chưa có paid rows là EXPECTED_NO_PAID_DATA; cần chứng minh có thể tìm đúng report/filter, không giả nguồn đã attributed.

Đầu ra: REPORT_ACCESS_MAP.md, bảng metric→nguồn/report/filter→identity/join key→definition→availability/lag→cách đọc lại; sample sanitized nếu có. Acceptance: đọc được hoặc ghi cụ thể UNAVAILABLE/PROCESSING/PERMISSION_MISSING; phân biệt link clicks/all-clicks và HTTP204/processed report; lưu report filters mà không phụ thuộc link session riêng trong Git. Không tự tạo property/tag nếu thiếu report.

## P3 — Baseline trước chạy

Owner: agent đọc nguồn sẵn có; dependency: P2 khi lấy từ nguồn đó, có thể thu thập phần độc lập trước. Mốc cutoff phải trước actual first delivery; proposed matched reference window là7ngày trước start, điều chỉnh theo coverage và timezone nguồn, không trộn kỳ.

Việc làm: ghi baseline reader/site engagement và traffic source từ GA4 nếu có; direct/brand search/follower đúng scope khi nguồn sẵn có. Traffic paidF1/F2 trước chạy chưa phát sinh không tự là0 đã đo. Synthetic tests phải tách; nếu không loại được thì ghi contamination. Baseline brand/site rộng chỉ là context, không chứng minh causal lift của hai ads.

Đầu ra: BASELINE.md/CSV với kỳ đo, extraction time, nguồn, definition, raw count có thật hoặc UNKNOWN/UNAVAILABLE, coverage và test contamination. Acceptance: không lấy organic làm paid; không đòi mua công cụ hoặc sửa tracking để điền đủ; ghi rõ source nào không đủ quyền/không có lịch sử. Baseline retrieval muộn nhưng window trước delivery phải gắn nhãn RETROSPECTIVE, không nhận là preflight đã làm.

## P4 — Phương án thay cold F1/F2

Owner: agent chuẩn bị nội bộ; Bảo chọn variant khi có evidence C4. Dependency: current accepted B13/B16 source và anchor. Không cần chờ metric để inventory/brief, chưa chọn winner.

Việc làm: rà exact reuse variant đã tồn tại. Mỗi F1/F2 chuẩn bị một phương án thay ưu tiên; nếu không có asset phù hợp thì dùng một brief, không giả có swap-ready PNG. Chỉ rõ giữ gì/đổi gì (hook hoặc visual), persona/pain/business value, caption/headline/alt/URL liên quan và rollback asset nguồn. Phân biệt visual-only test với đổi tình huốngF3.

Đầu ra: COLD_OPTIONS.md + source path/revision, disposition REUSE_CANDIDATE hoặc BRIEF_ONLY, điểm cần QA. Acceptance: F1 giữ Operations/partner reports trước quyết định; F2 giữ Planning/affected lots trước replan; giữ Digiwin/manufacturing ERP, không bịa ROI/outcome. Candidate phải đủ cụ thể để Bảo so sánh, không chỉ ghi “đổi hình”. Generation/asset adaptation/upload là việc riêng sau quyết định; chưa tạo variant trong lượt lập plan.

## P5 — QA bốn carousel dự phòng

Owner: agent review nội bộ; dependency: exact candidate card lists/accepted assets và reader hiện hành. Không tạo ad. Native platform preview chỉ thực hiện trong mandate dựng draft sau này; chưa native thì ghi rõ limitation.

Việc làm: review riêng F1 explanation6/proof4 và F2 explanation6/proof4: ảnh gốc đủ resolution, readability desktop/mobile, caption/native headline/alt/order/card limits theo nguồn; cold→giải thích→Bright proof→respective reader→contact-vn notice/return. Ghi reuse cùng image nếu có, không giả4bộ là20ảnh unique. Dùng preview loopback khi cần; public reader chỉ đọc, không publish.

Đầu ra: CAROUSEL_QA.md + per-card checklist/evidence, defect list và source pins. Acceptance: từng card/surface/transition có disposition; quyền dùng existing exact set đã được Bảo chấp nhận, không xin lại. Bright Power China/challenges giữ scope, không KPI hay module outcome mới. Có lỗi thì đề xuất bounded fix; không âm thầm sửa/generate. Review nội bộ không được gọi full native/live-ready.

## P6 — Cấu hình RMK để Bảo quyết sớm

Owner: agent đề xuất, Bảo chọn rule/window/objective và việc tạo audience. Dependency: hai exact new-cold source ads; P2 report map; [S0–S4](../../../linkedin-rmk-source-readiness/2026-10-08/03_RMK_Fallback_Decision_Tree.md). Không cần chờ đủpool để soạn cấu hình.

Việc làm: chuẩn bị option mặc định có lý do và alternative: source cohort chung tương thích hay cần tách; Any interactions vs chargeable clicks nếu UI/format hỗ trợ; lookback theo current available options; objective Engagement hoặc reader-click phù hợp. Rule rộng hơn có thể nhiều người nhưng yếu intent hơn; window dài hơn có thể thêm reach nhưng cũ hơn. Không nêu số ngày/rule như native-supported nếu chưa kiểm UI. Đề xuất sớm decision về source creation để tránh bị động; không tự tạo audience và không hứa platform backfill lịch sử.

Đầu ra: RMK_DECISION_PACK.md có exact source keys, rule/window/objective options, trade-offs, expected evidence, input cần Bảo chọn và fallback nếu chưa tạo/processing/too-small. Acceptance: không dùng Page/organic/othercampaign pool; repo gate300reachable là contract cần đối chiếu current native UI, không performance guarantee. Source choice/creation tách khỏi enable RMK; Ready/eligible/readback vẫn bắt buộc. Không đổi format cold để gom warm nếu chưa có mandate.

## P7 — Gói W2, criteria và xử lý sự cố

Owner: agent soạn, Bảo quyết định và giao operator. Dependency: P1–P6 theo mức hoàn thành; thiếu dữ liệu vẫn soạn nhánh HOLD.

Việc làm: chuẩn bị4action cards: (A) giữ hết lịch/giữ tiền; (B) tiếp tục cold với scope giữ nguyên; (C) thay một đoạn; (D) RMK saugate. Mỗi card có trigger liên kết C1–C7, phần giữ/đổi, source/asset, prerequisite, budget/date proposal, owner, rollback, exit và recheck. Candidate date/spend phải được Bảo chốt trước thực thi, không tự nốiW1 hoặc dùng reserve.

Chuẩn bị criteria decision sheet trước khi đọc kết quả để chọn threshold sau dữ liệu không thành hợp thức hóa winner: ghi proposed minimum evidence/coverage, exposure imbalance, CTR/click definition, pacing/frequency warning và disposition khi mẫu nhỏ. Numeric criteria hiện UNSET; mọi giá trị đề xuất phải có source/rationale và Bảo chọn trước phép thử áp dụng, không gọi industry benchmark là KPI đã duyệt. Không bắt phải có numeric threshold mới được báo technical fault hoặc giữ tiền.

Chuẩn bị incident cards cho wrong URL/locale/claim, targeting drift, review/delivery hold, measurement lỗi thật, budget risk: exact evidence→phạm vi ảnh hưởng→đề xuất pause/sửa→kiểm phục hồi→rollback. Không trao quyền autonomous pause/enable qua plan; workflow review-only này không dừng campaign. Không thêm CRM/rep tin nhắn/lead-validation gate.

Đầu ra: W2_ACTION_CARDS.md + CRITERIA_DECISIONS.md + INCIDENT_CARDS.md, nối [decision log](../DECISION_LOG.csv). Acceptance: Bảo có thể chọn một phương án cụ thể; trường thiếu vẫn NOT_DECIDED, không đủ điều kiện thì HOLD. Giữ cap11,7triệu/đợt đầu5,6triệu/reserve6,1triệu; actual accounting basis và remaining spend điền khi có, không bịaFX. W1 hết mà chưa có quyết định thì để lịch kết thúc.

## Evidence, trạng thái và quyền thực thi

[Tracker](TASKS.csv) là sổ kế hoạch; ở lúc lập plan toàn bộ task PLANNED, sau 29/10 cả bảy task đã có output nội bộ (P1–P3 và P5 COMPLETE_WITH_GAPS; P4 COMPLETE_BRIEF_ONLY; P6–P7 COMPLETE_AWAITING_BAO_INPUT). Khi làm, ghi started/observed/completed, artifact path, gap và evidence. Output P1–P7 đã tạo ngày 29/10 (nội bộ, chưa có quyết định của Bảo). Các output nội bộ đã có, nhưng không đồng nghĩa mọi acceptance về live/data/native đã đóng; xem AUDIT_FIX_CLOSEOUT.md cho gaps hiện hành.

Read-only live/browser/report checks theo mandate thực thi được giao; không suy mandate viết plan cấp quyền thay settings. Tạo audience/draft, sửa/generate creative, publish, pause/enable, đổi ngày/budget và giải ngân phải đúng quyết định tương ứng; các điều khoản action-time nếu xuất hiện được xử lý tại bước đó. User acceptance cũ về exact paid assets/budget envelope không hỏi lại.

Audit target: đối chiếu7task với danh sách Bảo duyệt, kiểm source/current schedule, authority boundaries, main unchanged và protected diff; inspect thực tế từng output khi execution đến, không dùng keyword/hash thay semantic review. Root self-review chỉ chứng minh plan nội bộ, independent audit NOT_RUN. Execution status cho lượt này SUCCESS nghĩa plan đã được tạo và checkpoint, không7task đã thực hiện.

Docs impact reviewed: cập nhật current/README/pre-ad readiness plan pointers cho phạm vi plan mới; parent pack README/hash receipts giữ nguyên; audience/message, cap, actual schedule/creative/tracking implementation không đổi. S04/build/index đã review, không cần thay nội dung vận hành ở lượt plan; historical receipts/manifests giữ nguyên. [Review binding](REVIEW.json).
