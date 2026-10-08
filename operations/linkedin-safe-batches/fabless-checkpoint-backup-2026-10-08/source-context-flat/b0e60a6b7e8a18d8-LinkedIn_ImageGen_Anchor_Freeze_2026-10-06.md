# Freeze harness và tiền/hậu kiểm anchor · 2026-10-06

**FROZEN_PER_PO — phiên bản và quy trình; chuẩn bị sản xuất offline.**

Bảo chỉ đạo: “ổn r codex, commit local, sau đó freeze harness/anchor tiền, hậu kiểm. Chuẩn bị làm hàng loạt.” Checkpoint candidate2: `67d1cbd176532ad0b6661ffc3d4f3c042875575d`. Quyết định này supersede trạng thái DEVELOPING / NOT_FROZEN của callable anchor guard và quy trình tích hợp trong các snapshot trước. Core closing-standard đang freeze được giữ đúng bytes hiện hành; baseline visual Sol và quy tắc worker 03/10 không đổi.

## Execution contract và phạm vi

Outcome: có checkpoint local, phiên bản harness/anchor/gates xác định bằng SHA256, quy trình bắt buộc và intake hàng loạt có tiêu chí nghiệm thu. Root thực hiện và SELF_REVIEW; không có independent-agent audit. Kiểm bằng focused tests, manifest raw-byte/Git-index consistency, protected benchmark pins và docs synchronization.

Freeze gồm frozen core hiện hành, Single-image trial gate hiện có tại worktree này, callable anchor wrapper, anchor revision1.0 + email nguồn, AD-ED-01 / MSG-ANCHOR-01 PREGEN_SCRIPT và POSTGEN_ARTIFACT, receipt templates và quy trình corrective. [Manifest](message-anchor/freeze-2026-10-06/manifest.json) xác định file/version cụ thể; [status](message-anchor/freeze-2026-10-06/status.json) xác định lifecycle và scope.

Locale adapter/profiles là dependency được pin để tái lập, **vẫn DEVELOPING / NOT_FROZEN**; không được tự mutate/adopt từ freeze này. Không tạo framework, scheduler hay integration mới. Freeze không cấp generation hàng loạt, main merge, push, publish, account activity hoặc spend. Chuẩn bị lô là phạm vi hiện tại.

## Quy trình đã chốt

1. Intake từng bộ: segment/locale/persona/route, relevance evidence, copy đủ surface, storyboard/props, nguồn/proof và whole-journey mapping. VN phải build lại theo ERP hỗ trợ chuẩn bị năng lực vào chuỗi; FDI business value/ROI có thể implicit, không cần nhét ROI literal hoặc số hứa hẹn.
2. Actual semantic review toàn script và context, AD-ED-01 + MSG-ANCHOR-01, anchor/email revision/hash, từng field/card/transition. Thiếu/stale/FAIL giữ PREGEN_BLOCKED. POSTGEN_NOT_RUN trước ảnh không chặn semantic tiền kiểm hợp lệ.
3. Fresh wrapper ngay trước mỗi call/retry, trusted release/message-review hashes và expected persona/segment/route. Chỉ dùng exact returned payload. Tối đa5refs. Draft locale hoặc core-only PASS không thay thế guard. Wrapper không tự hiểu ngữ nghĩa hoặc intercept manual calls bên ngoài đường này.
4. Hậu kiểm native + actual desktop/mobile + reader/destination nếu có; so từng chữ/source/category/numbers/glyphs/scene, card liền kề và toàn journey. Ghi hash input/output/demo và observations thật. Missing evidence => INSUFFICIENT_EVIDENCE; finding chưa khép => CHANGES_REQUIRED.
5. Phân loại script/message/proof sai => pregen review lại; binding sai => sửa trước inference; render sai => corrective riêng card. Mặc định một corrective/card trong mandate hiện có, revision/path/receipt/guard mới; còn lỗi thì dừng retry và review layout. Không overwrite benchmark hoặc tự sửa executable frozen. Chỉ khép artifact khi đủ actual evidence; không cần mở lại lifecycle tool mỗi lô.
6. Giao bộ đủ ảnh + copy + reader + manifest + receipts + finding ledger. PASS các gate chỉ chứng minh scope được kiểm; live/rights/account/release vẫn theo mandate riêng.

## Dogfood và giới hạn giữ lại

Candidate1 English được Bảo nhận checkpoint nhưng actual mobile evidence còn thiếu. Candidate2 Simplified Chinese:10 ảnh +1 corrective,0refrejection; card9 source hierarchy còn CHANGES_REQUIRED sau bounded corrective; paper bands/lines là fidelity observation, không tự suy thành dữ liệu case. Rendered desktop/mobile/reader chưa hoàn tất sau browser disconnect. [PO checkpoint receipt](linkedin-locale-dogfood/2026-10-06/zh-Hans-osat-candidate2-v1/po-checkpoint-acceptance.json) và closeout/postgen receipts giữ đúng verdict cũ.

Freeze là quyết định PO về phương pháp, **không hồi tố PASS ảnh**. Candidate2 failed card9 không được chọn làm accepted layout reference. Các finding này trở thành điểm kiểm bắt buộc trong lô tới: source đủ hierarchy ở native/feed; giấy trung tính không thêm graphic-data; category tách source; không calendar/chart/wafer/category drift. Grey paper marks phải được reviewer disposition, không tự default PASS hoặc universal ban.

Guard chỉ kiểm binding/declared review, không chứng minh chất lượng semantic prose. Input fixture English literal và A5 copied English-only note đã được ghi nhận; future author phải kiểm scene literals và mọi free-text receipt đúng locale/persona. Không sửa receipt lịch sử. Chinese source phải revise embedded locale literals trước adapter; đổi scene/props cần storyboard review riêng.

Coverage dogfood là một OSAT skeleton English/zh-Hans; không buyer validation, chưa whole-set/zh-Hant/Fabless/Partner/VN acceptance. Main snapshot có thể thiếu Single-image trial inputs: phải kiểm đúng checkout, không fallback hoặc recreate gate. Chuẩn bị theo [batch runbook](LinkedIn_Locale_Batch_Preparation_2026-10-06.md).

Docs impact reviewed: current lifecycle/process statements synchronized; strategy, budget, anchor wording, source rights, audience, landing/CTA/tracking và old freeze/history giữ nguyên.
