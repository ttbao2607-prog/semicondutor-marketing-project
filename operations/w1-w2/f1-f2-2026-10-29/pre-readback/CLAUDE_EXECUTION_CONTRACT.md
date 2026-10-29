# Execution contract — Claude tiếp quản bốn việc trước readback W1

29/10/2026 · revision1 · READY_FOR_EXECUTOR / NOT_STARTED. Bảo yêu cầu Codex commit contract cho mục1–4 và sẽ giao Claude thực hiện. Đây là handoff, không phải Codex đã thực thi hoặc đã spawn Claude. Planner Codex; executor Claude khi Bảo giao; auditor đối chiếu độc lập theo mục audit, chưa được thực hiện. Không mặc định có audit độc lập.

## Goal

Bảo có một readback có evidence kiểm lại được cho các gap hiện hành, một cấu hình RMK dựa trên lựa chọn UI thật để quyết định, và QA desktop/mobile còn thiếu. Thành công không đo bằng số file hoặc việc mở trang: phải biết trường nào đã xác minh, trường nào chưa đọc được và vì sao, có evidence tương ứng. Không sửa ad/lịch để đạt kết quả.

## Start / source / scope

Worktree `D:/Digiwin_F1F2_W1W2_2026-10-29`; branch `slice/f1-f2-w1-w2-decision-pack-2026-10-29`; checkpoint trước contract `2821c7ad`. Trước bắt đầu dùng git-state-recovery, đọc AGENTS, CURRENT_STATE, DOCS_IMPACT_MAP và [audit corrections](AUDIT_FIX_CLOSEOUT.md). Nếu HEAD mới hơn, đọc diff và giữ công việc mới; không reset về checkpoint, không làm trên main. Một browser session chỉ một controller; không delegate/spawn theo contract này. Bảo trực tiếp giao Claude không là mandate tạo thêm executor.

Đọc [P1](PRELAUNCH_READBACK.md), [P2](REPORT_ACCESS_MAP.md), [P3](BASELINE.md), [P5](CAROUSEL_QA.md), [P6](RMK_DECISION_PACK.md), [metric rules](../METRICS.md), [source registry](../SOURCE_REGISTRY.csv). Freshly reread message anchor/email và paid-scope boundary trước review artifact; không kế thừa PASS cũ cho scope mới.

Latest recorded state29Oct: parent Active, ad set On/Scheduled, F1/F2 On/Active, một shared budget USD10/day; lịch01Nov07:00→08Nov06:45 VN. Đây là snapshot, không bằng current observed state. Cold ads chỉ là LI-wave01-F1-en-COLD-v1 và LI-wave01-F2-en-COLD-v1 trong DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH; numeric IDs resolve private. Tên draft không chứng minh còn draft. Hai probe cũ phải giữ nguyên.

Được thực hiện khi Bảo giao: đọc/điều hướng LinkedIn và GA4, xem cấu hình/report/preview không lưu, xem source assets và loopback preview, QA public reader có đánh dấu; ghi internal sanitized evidence/docs và commit local trên branch này. Không login lại hoặc thu credential/PII không cần thiết; theo skill/browser rules của môi trường đang dùng. Không tạo/save audience, ad/draft/report/setting, không Save/Launch/publish, pause/enable, đổi budget/date/targeting/creative/analytics, generate/crop/edit ảnh, submit form/lead, gửi tin nhắn hoặc tạo scheduler. Không mở rộng sang campaign Test/RSCH khác; chỉ giữ observation ngoài scope nếu vô tình thấy. Không push/merge. Nếu bước đọc thực tế có side effect phải dừng bước đó, ghi điều kiện, tiếp tục phần độc lập.

## Plan / expected evidence

### Q1 — Recheck đúng F1/F2 trước launch

Đọc nhãn review/hold/rejection của từng ad (Active không đồng nghĩa approval), parent/ad set status, selected English, đầy đủ tên company list R5 (`TEST-AUD-CONTINGENCY-TRUE-ONLY-R5-52` theo receipt28Oct), dates/timezone hiển thị, USD10 chung, placement/Expansion và hai probeOff. Tên list đã có authority: agent đối chiếu evidence, không hỏi Bảo duyệt lại audience. Phân biệt giá trị selected/checked thật với danh sách options, DOM text hoặc forecast.

Output `FOLLOWUP_Q1_READBACK.md`: observed_at có giờ/timezone, expected/actual theo từng trường, sanitized screenshot/DOM reference. Nếu screenshot fail, giữ raw DOM snapshot private + hash/ref và ghi mức evidence; không giả visual PASS. Không chỉnh editor; rời không lưu. Acceptance: identity và từng field có observed evidence hoặc exact UNVERIFIED với blocker; chỉ MATCH phần thực đọc. Lịch dự kiến và actual first delivery luôn tách.

### Q2 — Đóng đường đọc metric

LinkedIn: xác minh Reach/frequency có thật ở report/available columns, clicks loại nào, timezone nguồn và currency; không chỉ ghi “có nút Customize”. Không lưu preset hoặc thay account setting. GA4: xác minh đúng property/stream theo bridge, đường lọc Session campaign và Session manual ad content/utm_content nếu thực có, reader path và các metric processed engagement. Không cần dimension t nếu campaign/content đủ; không tự tạo custom dimension/tag.

Output `FOLLOWUP_Q2_REPORT_MAP.md`: metric→report/filter→join key→definition→timezone/window/lag→availability, có một observation chứng minh mỗi đường đã thử. Trước delivery, EXPECTED_NO_PAID_DATA là hợp lệ nhưng không chứng minh attribution đã có. Khóa đúng click definition cho readback; missing report/processing không là tracking lỗi thật. Không đòi LinkedIn clicks=GA4 sessions. Ghi source snapshot/extraction time để auditor kiểm được; không chỉ lời kể.

### Q3 — Kiểm feasibility RMK và cấu hình để Bảo chọn

Chỉ mở các lựa chọn UI theo khả năng đọc an toàn: exact source ads có chọn được không, rule, lookback, format/objective hỗ trợ, cách gom cohort. Nếu phải vào create flow để xem, chỉ xem không lưu/tạo; nếu vào flow tự tạo object thì không làm và ghi capability UNVERIFIED. Không coi đề xuất30days/Any interactions là native-supported trước khi thấy.

Output `FOLLOWUP_Q3_RMK_OPTIONS.md`: default đề xuất + alternative có trade-offs, identity/source và value thực thấy, unavailable gì, input cụ thể cần Bảo quyết. Giữ source NOT_VERIFIED_CREATED/reachable UNKNOWN tới khi có evidence khác; chỉ gán Ready/S2 sau actual native readback. Không suy pool từ470+ hoặc forecast; không hứa backfill; không mượn Page/organic/othercampaign. Contract gate300 cần current UI xác minh. Chọn source/timing không đồng nghĩa enable RMK; objective/release và nguồn tiền là quyết định sau. Nếu pool chung, review continuity F1/F2 và không hứa delivery tuần tự.

### Q4 — QA bổ sung carousel desktop và reader mobile

Giữ đúng bốn carousel F1/F2 explanation6 + proof4:20slots/16unique originals. Reuse per-card review đã có, bổ sung desktop và exact source captions/headlines/alt/order/URL với original pixels; không làm lại toànlibrary hoặc generation. Reader F1/F2 mobile kiểm layout/overflow, nội dung/ảnh, transition tới contact-vn có notice tiếng Việt và return đúng treatment. Desktop carousel không thay native preview; chưa có native draft thì native NOT_RUN, không tạo ad để có PASS.

Output `FOLLOWUP_Q4_VISUAL_QA.md` + sanitized captures/observations, exact viewport/route/source revision, per-unit findings và transition dispositions. Dùng local preview cho artwork khi phù hợp. Public reader test ghi QA run ID/window/source/treatment/thiết bị trong log riêng; chỉ dùng cách đánh dấu đã được nguồn đo hỗ trợ, không tự sửa tag hoặc thêm UTM campaign mới. QA có thể vào GA4: không hứa loại trừ nếu chưa kiểm filter. Nếu không tách được test thì ghi contamination trong readback, không tính làm paid outcome. Không submit form hoặc phát sinh lead để test. Quyền dùng exact paid assets đã được Bảo chấp nhận, không xin lại; finding mới chỉ đề xuất bounded correction, không tự sửa.

## Measurement / protected invariants

Q1–Q4 mỗi việc có output, timestamp và evidence reference; task thực sự chưa xác minh ghi PARTIAL/UNVERIFIED, không đổi tên “complete” để che gap. Phân biệt hoàn tất investigation với xác nhận target field. No-data trước chạy không phải số0 đo cho W1. Không suy sufficient sample từ ngày3/7 hoặc số clicks; không declare winner hay ROI. W2 không tự dùng reserve: đọc remaining first envelope trước, Bảo chọn funding trong cap đã duyệt. Không thêm CRM/rep tin nhắn/qualified-lead gate.

State invariant: F1/F2 và probes không bị thay settings/status/date/creative; reader/tracking source và public runtime không đổi; main không được ghi. Nếu phát hiện reject/target drift/link lỗi/budget risk: báo Bảo ngay với evidence và đề xuất bounded action, không tự pause/enable/extend. Ưu tiên Q1/Q2/Q3; Q4 có thể tiếp tục khi một report không truy cập được. Không chờ đủ4task mới báo rủi ro thật.

## Evidence / audit / closeout

Private screenshot/DOM/raw reports giữ ngoài public repo; public receipt có sanitized observations + SHA256/private relative reference, không chứa numeric account/member/lead identities, credentials, billing data hoặc private session URL. Nếu browser change xảy ra ngoài ý muốn, ghi đúng side effect; không nói “read-only” như một bảo đảm không có evidence.

Output cuối `FOLLOWUP_CLOSEOUT.md`: bảng Q1–Q4, actual evidence, gaps/impact, verified vs proposed, exact input Bảo cần chọn, protected invariants readback và next action. Mỗi task chọn một execution status SUCCESS/PARTIAL/FAILURE/BLOCKED theo execution-contract; overall cũng chọn đúng một status. Audit độc lập nếu có: AUDIT_PASS/AUDIT_FAIL/INSUFFICIENT_EVIDENCE, tách khỏi executor status; khi không có reviewer thì NOT_RUN, không tự gọi independent PASS. Audit target: inspect evidence thật từng selected field/report/UI option/image/transition; đối chiếu source/current user scope, main/protected diff và no account mutation. Hash/link checks không thay visual/semantic hoặc live proof.

Trước commit đọc docs impact map: update canonical current pointers nếu observed truth thay đổi; không rewrite history/old capture như đã được PASS lại. Fresh MSG-ANCHOR receipt cho affected internal surfaces, update artifact manifest/pins đúng scope khi sửa. Commit local và báo SHA/worktree status; không push/merge hoặc đổi nhánh người khác. Lưu output mới thay vì sửa số baseline cũ khi không có evidence đính chính.

## Binding và review của chính contract

Contract text-only nội bộ, branch FDI/English, F1 Operations outsourced production và F2 Planning demand/lot replan; không tạo customer-facing copy. A1/A2 giữ R5 là hypothesis, không coi English là FDI/qualified buyer; A3 không đổi segment/locale; A4 không ROI/budget inference; A5 VN message N/A; A6 Bright Power China source/challenges và Taiwan scope giữ; A7 giữ cold→explanation/proof→respective reader→contact-vn notice/return. Codex SELF_REVIEW; MESSAGE_ANCHOR_PASS chỉ cho contract nội bộ này, không native/live/release. Không có independent audit. Existing P1–P7 evidence limits giữ nguyên.

VY-CONTENT-ANCHOR v1.0: `operations/Vy_Email_Content_Anchor.md`, SHA256 read `6621d53c845939730ebcb1f59bbf85fb8a0d9acb156e5236e7387c0e69867ac5`. Original VY-MAIL-USER-20261006: `operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md`, SHA256 read `c5a6f35533e7a8b3b439ec4d9a260611fcdd2f67ddb0f046a3e33d28c6316d2b`.

Docs impact reviewed: CURRENT_STATE có handoff pointer; scope/schedule/actual performance không đổi. README/readiness/build/S04 hiện đã có current P1–P7 pointers và được review; không cần đổi nội dung vận hành chỉ vì thêm contract pending này. Không sửa previous receipts để cấp acceptance hồi tố.
