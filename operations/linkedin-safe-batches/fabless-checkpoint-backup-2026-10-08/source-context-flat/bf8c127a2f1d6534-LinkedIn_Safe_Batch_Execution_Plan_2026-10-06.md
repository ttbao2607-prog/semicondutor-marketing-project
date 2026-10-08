> **B4–B5 đã vào main local · 2026-10-07:** Source checkpoint `2252250`; selected integration `b2694b4` đã cập nhật main sạch tại D:/Digiwin_Semiconducter_Workspace.20PNG final + viewer/reader và evidence đã đối chiếu byte trong commit;49file integration đúng scope, không failed/canary/corrective dirs. Full attempts vẫn ở nhánh nguồn; working edits ngoài scope giữ nguyên. Technical mobile/main-viewer640 INSUFFICIENT_EVIDENCE giữ riêng; không PASS hồi tố.24frozen pins nguyên, adapter DEVELOPING/NOT_FROZEN. Chưa push/GitHub; B6 chưa chạy. [Closeout](operations/linkedin-safe-batches/2026-10-07/B4-B5-main-integration/local-main-closeout.json).

> **B4–B5 PO checkpoint / selected main mandate · 2026-10-07:** Bảo duyệt hai bộ hiện tại và yêu cầu checkpoint + nhập main riêng artifact cuối. B4 English và B5 zh-Hans có20PNG chọn; technical/render vẫn REVIEW_DRAFT_RENDER_GATE_PENDING / INSUFFICIENT_EVIDENCE, không PASS hồi tố. Full attempts lưu nhánh nguồn; main chỉ selected artifacts và evidence.24frozen pins nguyên, adapter DEVELOPING/NOT_FROZEN. Chỉ local, chưa push; B6 chưa được chạy trong lượt Git này.

> **B4 PO accepted / B5 generated · 2026-10-07:** Bảo duyệt B4 offline và cho batch tiếp. B5 O2 zh-Hans Operations + Quality có10PNG chọn =8new +2proof B2 reuse;9ImageGen calls=8original+1corrective. Proof1–2 dựng mới cho nguồn lớn; proof2 sửa bỏ skyline/pagodas ngoài storyboard. Current artifact **REVIEW_DRAFT_RENDER_GATE_PENDING / MSG-ANCHOR INSUFFICIENT_EVIDENCE**, xem scope/finding ở hậu kiểm; mobile/main-viewer640 chưa đủ.24frozen pins nguyên, adapter DEVELOPING/NOT_FROZEN. B4–B5 chỉ local working files chưa checkpoint/main/push; B2–B3 integration cc904e2 vẫn riêng. Dừng chờ Bảo duyệt B5. [B5](<deliverables/linkedin-safe-batches/2026-10-07/B5-zh-Hans-o2-v1/index.html>) · [Hậu kiểm](<operations/linkedin-safe-batches/2026-10-07/B5-zh-Hans-o2-v1/postgen-review.json>).

> **B2 PO accepted / B3 generated · 2026-10-07:** B2 acceptance hiện tại đã ghi nhận riêng, không rewrite historical findings. B3 zh-Hant O1 có10ảnh chọn + reader,12calls=10original+2corrective; **CHANGES_REQUIRED** vì proof1 nguồn còn nhỏ. Proof2–3 source hierarchy CLOSED scoped native/desktop333; đủ10ảnh desktop333 có caption/native headline và reader desktop actual. Full mobile/main-viewer640 còn INSUFFICIENT_EVIDENCE (screenshot timeout); không anchor/wholejourney PASS. Taiwan terminology review riêng, legal-name glyph nguồn giữ nguyên; nguồn reader giản thể được disclosure.24frozen pins nguyên, adapter DEVELOPING/NOT_FROZEN. Checkpoint local trên nhánh hiện tại theo mandate Bảo; chưa merge main/push; main local vẫn26f89d0. Dừng trước W2 cho Bảo kiểm. [Hậu kiểm B3](<linkedin-safe-batches/2026-10-07/B3-zh-Hant-o1-v1/postgen-review.json>) [Diễn giải cho Bảo](<linkedin-safe-batches/2026-10-07/B3-zh-Hant-o1-v1/Bao_Review_Vietnamese.md>).

> **B1 main local / B2 generated · 2026-10-06:** B1-v2 đã được PO duyệt offline và nhập main local `26f89d0`, source checkpoint `88f87ae`; chưa push. B2 zh-Hans O1 cùng persona QA + Operations đã đủ10ảnh chọn + reader,12calls=10original+2corrective; artifact **CHANGES_REQUIRED**. O1-A4 bỏ dấu check, proof3 tăng nguồn đã CLOSED native/feed333/mobile390×844; proof1–2 nguồn còn nhỏ, O1-A1 visual-fidelity observation chờ PO disposition. Actual compact review đủ10ảnh/feed/mobile và reader desktop/mobile; chưa chứng nhận full viewer caption-context, final anchor INSUFFICIENT_EVIDENCE.24frozen pins nguyên; adapter DEVELOPING/NOT_FROZEN. B2 chỉ working files local chưa commit/merge; hết cap2corrective, dừng trước B3 cho Bảo kiểm. [Hậu kiểm B2](<linkedin-safe-batches/2026-10-06/B2-zh-Hans-o1-v1/postgen-review.json>). Các trạng thái trước bên dưới là snapshot riêng, không PASS hồi tố.

# Kế hoạch sản xuất theo batch an toàn · 2026-10-06

**PLAN_PREPARED / GENERATION_NOT_STARTED.** Bảo yêu cầu commit và merge artifact candidate2 vào main, sau đó lập kế hoạch chạy batch. Mandate hiện tại hoàn tất Git integration và lập kế hoạch; chưa bắt đầu ImageGen hàng loạt hoặc cấp quyền spawn/live/push.

Candidate2 v2 đã được nhập main local theo chỉ đạo PO: 10 PNG final + viewer/reader + evidence. Checkpoint nguồn `6704d09`, follow-up receipt `2d6fd22`; main sau tích hợp/khôi phục byte receipt: `89d94be6abb839f8834d1b62d9c715296fcd5d4c`. Đây là offline adoption, không biến missing evidence thành technical PASS. Candidate2 còn mobile2–10 và reader visual; candidate1 còn mobile; candidate3 là benchmark OSAT zh-Hant có scoped final rendered review. Hồ sơ cũ không rewrite.

## Kết quả mong muốn và phạm vi

Từng journey có đúng segment/locale/persona, thông điệp qua anchor trước gent, artifact qua kiểm native và browser thực, output/review được pin theo revision. Khi có lỗi, chỉ sửa card liên quan và dừng đúng giới hạn. Không sản xuất cả thư viện trước khi biết lô nhỏ đạt.

Một batch = **một journey, một locale, một persona/decision unit**. Full journey thường 1 cold + 5 explanation + 4 proof + reader; số unit thực lấy từ intake, không ép nguồn khác vào cấu trúc này. Caption, CTA, alt, header/category, source, scene literals và reader đều thuộc review. Một controller browser, một writer; root có thể thực hiện và phải ghi SELF_REVIEW, không giả independent/native-market acceptance. Không có mandate delegation.

FDI English/zh-Hans/zh-Hant giữ business value/ROI implicit qua vận hành, phối hợp Finance và bằng chứng đúng scope. Nội địa tiếng Việt giữ hướng ERP hỗ trợ chuẩn bị năng lực vào chuỗi, không gắn nguyên skeleton vận hành FDI rồi dịch ngược. Partner triển khai/SI không đồng nghĩa nhà cung ứng công nghiệp. Intel/Amkor/Hana Micron/Samsung không mặc nhiên là buyer ERP địa phương.

## Thứ tự lô đề xuất

| Lô / wave | Phạm vi | Điều kiện chuyển tiếp |
|---|---|---|
| B0 — kiểm lại, 0 ImageGen | Candidate2 v2 mobile2–10 + reader desktop/mobile; candidate1 mobile; smoke preview cả desktop/feed/mobile trước inference mới | Có ảnh browser ổn định, không DOM-only PASS; source hierarchy/copy/case/9 transitions đủ evidence. Browser hỏng thì giữ REVIEW_PENDING và dừng generation mới |
| B1 — một treatment OSAT mới, English | Đề xuất O1 làm intake đầu tiên; chọn hook/persona/proof sau khi review source và ICP. Nếu O1/proof không fit, giữ HOLD, không tự gán case06 | Toàn script + reader + storyboard được duyệt trước call; canary2card qua native/feed/mobile, rồi mới hoàn tất journey |
| B2 — cùng treatment, zh-Hans | Author theo cách người đọc Chinese diễn đạt; giữ mechanism/storyboard/proper names/numbers | Không kế thừa semantic PASS từ English. Fresh receipts/guard, same independent field coverage và rendered review |
| B3 — cùng treatment, zh-Hant | Author thuật ngữ, dấu câu và line breaks riêng | Không coi chuyển giản thể→phồn thể là acceptance; qua review riêng như B2 |
| W2 — OSAT còn lại | O2, O4-O, O4-Q lần lượt; O3 pilot chỉ reuse revision final phù hợp, không gent lại mặc định | Mỗi treatment/locale là batch riêng, không đồng thời mở nhiều bộ. Sau B1–B3, PO xem ledger trước mở wave rộng hơn |
| W3 — Fabless | F1 → F2 → F3; đề xuất F1 + case04/Bright từ matrix cũ làm intake đầu, còn proof fit/decision authority phải recheck | Không suy thiết kế chip = target FDI phù hợp; source integrated mechanism không thành ERP-only causality |
| W4 — Partner | P1/P2/P3 sau mapping rõ SI/triển khai hoặc nhà cung ứng | Pressway là case Workflow ERP/quy trình đúng scope, không proof semiconductor entry hoặc ERP–MES connector. P3 không được nhận VN-ready chỉ bằng localization |
| Lane VN riêng | Tiếp tục từ VN revision hiện hành trên main sau recheck anchor; lập intake nội địa riêng | Không overwrite VN đã duyệt, không dùng backlog VN sai hướng làm nguồn đạt. Scope/nguồn mới cần xác định trước release |

Đây là thứ tự đề xuất, không phải lịch live hoặc blanket acceptance toàn thư viện. Inventory lịch sử: 11 carousel/55card, 4 case/16card, 3 cold skeleton; không nhân mọi thứ cho mọi locale rồi coi đó là quota. Ledger intake mới xác định units còn thiếu, exact reusable assets và số call thực. Tránh generate lại proof/cold đã phù hợp nếu byte revision/copy/locale/persona vẫn đúng; khi reuse vẫn recheck context và whole-journey mới.

## Giới hạn vận hành cho lô đầu

- Tối đa **1 journey đang generation**, gọi tuần tự. Trần đề xuất **10 original calls/lô**; lô có cấu trúc lớn hơn phải phân lại scope trước chạy.
- Canary: chọn trước **2 card khó nhất chưa có asset reusable** — source/case tên dài hoặc closing source, và headline/body dài. Nếu chỉ còn một card mới thì kiểm một; không tạo ảnh chỉ để đủ hai. Tất cả script/caption/reader đã tiền kiểm trước canary.
- Chỉ tiếp tục phần còn lại khi canary qua native + feed khoảng333px + mobile actual khoảng390px. Preview hoạt động trước gent và phải tiếp tục hoạt động; call cap không thay acceptance.
- Giới hạn bổ sung cho wave đầu: **tối đa2 corrective calls/lô, một corrective cho mỗi card** theo frozen method. Card vẫn lỗi sau corrective hoặc cần corrective thứ3 thì HOLD, review layout/source/scene; không retry vòng lặp. Đây là execution budget đề xuất, không sửa frozen process.
- Nếu phát hiện lỗi message/proof sau inference: dừng lô, quay lại script/context review, không sửa ảnh bằng cách nhét disclaimer. Nếu binding sai: sửa input/guard trước call. Nếu browser mất evidence: dừng generation mới, không gent lại ảnh để chữa lỗi preview.

## Tiền kiểm bắt buộc trước từng call

1. Dùng checkout nguồn có đủ dependency: `D:/optimize-awareness-LinkedIn-adcopy`, named branch `slice/linkedin-audience-ready-research`, baseline `2d6fd2281c0367a213789278aad1a28b55233090`. Trước session chạy git-state-recovery và đối chiếu SHA hiện tại; không assume main có executable guard. Main artifact-only merge chưa import guard/freeze/Single-image inputs mới. Nếu chạy từ worktree batch mới, branch từ đúng checkpoint nguồn và không trộn historical research vào main.
2. Reread anchor/email và kiểm 24 file theo `message-anchor/freeze-2026-10-06/manifest.json`. Harness/anchor/process giữ FROZEN_PER_PO; adapter/profiles vẫn DEVELOPING và được pin. Thiếu/mismatch file => HOLD, không fallback/recreate gate.
3. Điền intake từ frozen template vào **path revision mới**, ghi owner, persona/decision unit, route, ICP relevance, proof rights/scope, ordered units, input revisions/hashes, reusable assets, destination và generation mandate cụ thể. PENDING template không release.
4. Author/review toàn fields và reader: brand role, advertiser voice, source hierarchy tối thiểu ngang body, category/source tách vai trò, entity/country/exact numbers/integrated mechanism. Review scene English literals và receipt prose đúng locale; không copy A5 note của locale khác. Chinese typography/terms do actual review, không chỉ check string.
5. Actual PREGEN_SCRIPT review MSG-ANCHOR-01 + AD-ED-01 với current anchor/email SHA, unit và transition coverage; missing/FAIL/stale => blocked. Ghi SELF_REVIEW nếu đúng thực tế; không tạo native-market claim không có người review.
6. Tạo fresh contract/review/release/spec và trusted hashes. Chạy callable wrapper ngay trước **mỗi original/corrective**; dùng đúng returned payload, tối đa5reference, pin ref roles/SHA. Draft adapter/calls không phải release. Không suy effective model/effort khi ImageGen không expose.

## Hậu kiểm và handoff

Native: nguyên byte PNG, decode/dimension/hash; so từng chữ, số, tên, country, punctuation, category/source/CTA, thêm/bớt scene và glyph. Không resize/composite/overlay để che lỗi. Paper bands/lines cần disposition có lý do: formatting trung tính không có values/axes/trends khác graphic data mới; không auto PASS hoặc cấm toàn bộ giấy có line.

Browser: local-web-preview chỉ loopback, smoke thử cả viewport trước ImageGen; desktop, feed khoảng333px và mobile actual390px, ghi viewport/image width thực và screenshot observations đúng card. Không tính frame stale, screenshot timeout hay DOM loaded/nooverflow là visual PASS. Kiểm đủ10card nếu intake10unit, toàn reader/destination offline, control/return navigation và tất cả transition. External public proof link có thể chỉ được kiểm href/source snapshot thì ghi đúng scope; không gọi live destination verified.

Mỗi lô giữ attempt ledger (original/rejection/corrective), input/output/demo/receipt SHA, lỗi/phân loại/closure, reused assets và evidence gaps. Corrective có path/revision/review/guard mới, kiểm affected card + adjacent + whole journey. Không mutate lifecycle harness/adapter theo lỗi asset; lỗi lặp có evidence chung thì đề xuất revision riêng.

Giao **thư mục thường**, assets selected final, copy/manifest/reader/receipts; không ZIP. PASS chỉ khi mọi required evidence đủ, CHANGES_REQUIRED cho lỗi mở, INSUFFICIENT_EVIDENCE cho thiếu kiểm. PO offline adoption và technical/live readiness là trạng thái riêng. Main chỉ nhận selected artifact và evidence/docs theo mandate Git cụ thể; không merge cả research branch. No push/publish/spend từ kế hoạch này.

## Tiêu chí đánh giá kế hoạch/lô

Kế hoạch hoàn tất khi main candidate2 đúng bytes, giới hạn lô/canary/stop condition rõ, queue không lẫn segment và checkout dependency xác định. Batch execution chỉ SUCCESS khi intake/script/guard đúng, ảnh/reader đủ actual evidence, không còn finding material mở và docs impact đã review. Reviewer kiểm manifest/ledger/ảnh/browser evidence so với tiêu chí này; đây chưa phải kết quả một batch đã chạy.

Docs impact: CURRENT_STATE, README, readiness, build pack và adapter README được cập nhật pointer trạng thái integration/kế hoạch. Frozen batch preparation/freeze record và historical verdict giữ nguyên; ghi nhận cũ “zh-Hant chưa dogfood”, “candidate2 card9 còn lỗi” trong snapshot được supersede bằng candidate3/candidate2-v2 receipts hiện hành, không sửa pinned file. Budget/strategy/rights/landing/tracking không đổi. File kế hoạch mới đang local working tree; chưa commit hoặc nhập main bởi task lập plan.
