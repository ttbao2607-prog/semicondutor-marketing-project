# Reader tracking bridge — deployed, technical QA verified

**Execution SUCCESS scoped to deployment/transport, root SELF_REVIEW; independent audit NOT_RUN.** Bảo yêu cầu làm next action và chỉ nguồn Blogspot-Digiwin; sau đó yêu cầu commit nhánh. Đã cập nhật đúng trang reader hiện có bằng bounded head insertion, Save/reopen exact và publish cùng URL. Không tạo lại page, đổi creative/copy/ảnh hoặc đụng form/ad/chi tiền.

Public endpoint: https://solutions.digiwin.com.vn/semiconductor-case-reader ; P1/P2 English tiếp tục dùng t=P1/P2&lang=en.

## Reuse kiến trúc hiện có

[BLOGSPOT_REFERENCE.json](BLOGSPOT_REFERENCE.json) pin source repo C:/home/asus/Blogspot-Digiwin, main6802942, sạch tại lần đối chiếu và không có remote. Đọc AGENTS→CLAUDE, anchor/manifest, bridge core/build/implementation,19Oct transport và28Oct same-session QA. Repo nguồn chỉ đọc, không import các quyết định ngân sách/ad/creative của Blogspot.

- Reader dùng **standalone Google tag G-MV5QWN0XVM**, cookie_domain=digiwin.com.vn, cùng stream website contact. Không nạp GTM container lên reader hoặc thay hệ paid-LadiPage GTM-NGT54TM9/G-20TL63SYLQ; không cài Meta/LinkedIn pixel.
- Giữ acquisition UTM ở ad→reader. Link contact mang bridge_origin=semiconductor_reader, timestamp activation, allowlisted bridge_source/medium/campaign/campaign_id/ad_id/adset_id/card/lane/creative_version và actual treatment/locale. Không thêm UTM nội bộ hoặc mặc định direct là LinkedIn/Facebook. Không cookie/storage tùy biến, PII/form values hoặc raw copied text.
- Native Google-tag config sở hữu page_view và engagement. Không manual page_view, event blog_*, custom CTA/lead/conversion event, GTM receiver thứ hai hoặc consent override. Arrival ở contact được quan sát bằng page_view có bridge context trong page_location; **contact chưa có ep.bridge_* fields**. Phân tích cohort neo vào reader entrance rồi join ordered session/path; không coi bridge metadata là chữ ký chứng minh paid click.
- Đây là điều chỉnh có căn cứ từ đề xuất candidate paid-GTM/forward-UTM trước khi Bảo chỉ Blogspot. Chưa có tag/container/property/form/CMP change ở hệ còn lại. Cách hai host dùng cùng tag/stream/cookie scope tham chiếu [Google tag options](https://developers.google.com/analytics/devguides/collection/ga4/tag-options), [cross-domain measurement](https://support.google.com/analytics/answer/10071811); auto page_view do config tham chiếu [Google pageview documentation](https://developers.google.com/analytics/devguides/collection/ga4/views).

## Evidence / kết quả

| Kiểm | Kết quả thực |
|---|---|
| Offline code | node syntax + meaningful unit controls đạt: direct/unsafe input, exact destination, fresh timestamp, idempotent one config/loader, no custom event dispatch, acquisition query sanitized |
| Existing-page lifecycle | PENDING preflight valid; literal meta selection được Copy-check trước paste; entire unsaved source bằng expected insertion. Save/reopen exact, không identity drift trong cycle này. Cả phần body, router, templates/copy/proof/images và CTA labels bằng baseline |
| Publish/public source | Cùng page/public URL; public core trim-equal single JS source. REQUEST/CLOSEOUT/VALIDATION bind baseline/candidate/source/page/public witnesses |
| Reader measured reload | Một page_view trong measured window, đúng G-MV5QWN0XVM, QA source/campaign/card/cold lane, HTTP204. Initial open trước Network đã có thể gửi event; không nói toàn phiên chỉ một view |
| Native engagement | Observed native scroll request HTTP204 có _et=58098ms. Là thời gian QA, không phải proof khách hiểu bài hoặc một engaged-session report đã xử lý |
| CTA→contact | Actual click tới đúng contact-vn với bridge context; không acquisition UTM trên internal link. Contact page_view HTTP204 cùng MID; so cid/sid trong memory cho sameClient=true/sameSession=true; chỉ lưu booleans |
| Capture limitation | Raw network observation cần re-enable trên origin contact. Initial contact window truncated/unavailable; có **2 contact reloads** sau click, chỉ final re-enabled reload được dùng làm measured contact view. Không claim first-arrival uniqueness, zero duplication toàn QA hoặc funnel rate từ các counts này |
| Regression | P2 English→zh-Hant→English giữ một loader và đúng CTA; locale khác không thêm CTA. Direct P1 không có paid bridge fields. Desktop1280×1000/mobile390×1000 không overflow, ảnh tải đủ, đúng label/notice/contact destination |

[BROWSER_EVIDENCE.json](BROWSER_EVIDENCE.json) có sanitized events, procedure, booleans identity, protected hashes và7DOM control states. [P1 desktop](P1-desktop.png), [P1 mobile](P1-mobile.png), [P2 mobile](P2-mobile.png) chứng minh CTA/runtime layout. Raw cid/sid không lưu vào file và đã bỏ khỏi capture map. Loopback step served once/shut down; viewport reset; network instrumented tab sẽ đóng tại cleanup; giữ public reader và builder bàn giao.

Canonical source baseline4059a1ea22158b801cab1ffabb9ac570b27805c2fd79614a48ecd8e95ccc2715 → candidate04429f539c394f0506679725740a2a52dd81af37ff36b70d8e4dc5c1a103f1d8, apply bằng existing_page_revision.apply_semantic_delta. Core duy nhất tracking/semiconductor-reader-bridge.js; inline block phải sinh từ core theo REQUEST, không sửa độc lập. Baseline có thể phục hồi bằng prior CTA receipt từ main568321fb reader1ac14…; current temp baseline location pin trong PREPARED.json. Không dùng raw normalized Builder source làm canonical.

## Readiness và phần còn lại

Transport/shared identity/context **VERIFIED_SCOPED**. Chưa audit processed GA4/native Session campaign/funnel reports, in-app/real-device/cross-device, consent behavior, form-success/CRM hoặc real paid delivery; không gọi paid traffic thành Organic Search. Source/asset rights/native/current-R5 subgroup decisions và ads release giữ prior scope. Optional custom section metrics chưa triển khai; kế hoạch hiện có thể đọc native reader sessions/engagement, không suy custom section_view đang phát từ reader.

Anchor Vy1.0 SHA2566621d53c845939730ebcb1f59bbf85fb8a0d9acb156e5236e7387c0e69867ac5/email c5a6f35533e7a8b3b439ec4d9a260611fcdd2f67ddb0f046a3e33d28c6316d2b giữ nguyên. Tracking delta không có marketing wording/scene/persona mới; A1/A2 fit unknown không đổi, A3 actual locale giữ đúng, A4/A6 copy/proof/product roles nguyên byte, A5 domesticN/A, A7 CTA destination/language warning và useful content giữ nguyên. Không cấp MSG/native/release PASS mới từ transport QA; frozen core/adapter không sửa.

Docs impact reviewed: tracking contract có scope reader riêng; source README/readiness C09/reader mapping/current entrypoints dẫn đến đây. Historical inventory/CTA/deploy receipts giữ đúng capture-time. Bảo yêu cầu checkpoint toàn CTA+tracking sau hoàn tất: containing commit lưu trên approval-corrected, local-only; không push/merge. Next: chuẩn bị exact paused-build pack và đo campaign theo plan đã duyệt; calendar/dailyUSD/dashboard placement/bidding cụ thể vẫn là execution fields cần cấu hình đúng, không mở lại phê duyệt cap/cadence.

Checkpoint byte policy: scoped .gitattributes -text preserves the exact canonical candidate and new receipt bundles across Windows checkout. Original source body/line endings and historical evidence are not normalized merely for whitespace lint. Git blob identity is checked after checkpoint; no global EOL policy change.
