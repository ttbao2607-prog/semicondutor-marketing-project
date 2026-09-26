# Plan rút gọn giao diện mobile cho ba landing page Semiconductor

**Trạng thái (2026-09-26):** ba local mobile candidates đã được triển khai và kiểm tra; chờ Bảo duyệt hình ảnh trước mọi handoff triển khai. Chưa import hoặc publish bản candidate.
**Baseline Git:** `c243673b404409bfbae7250d4e79473a6b01d2f0` (`Close Phase 4 tracking validation`, 2026-09-25).
**Worktree/branch:** `C:/Users/ASUS/.codex/worktrees/semiconductor-mobile-compact` / `slice/mobile-landing-compact-plan`.
**Owner quyết định:** Bảo. **Phạm vi đề xuất:** source responsive của OSAT, Fabless, Supplier/Partner; desktop đã được duyệt là visual baseline.

## 1. Fact, quan sát và giới hạn

- Phase 4 ghi nhận ba route public có loader, đúng số CTA 2/2/1 và không tràn ngang trong smoke ở 390×844. Kết quả này không đo chiều dài trang hoặc mức dễ đọc trên mobile.
- Source tại baseline có 7 section cấp trang ở OSAT, 8 ở Fabless, 8 ở Partner. Ở breakpoint hẹp, các grid chuyển thành cột đơn; nhiều khối card/diagram tiếp tục xếp dọc. Đây là **ứng viên gây scroll dài**, chưa phải kết luận về chiều cao render hoặc hành vi người dùng.
- `21st review --json` trên ba source trả 0 errors, 0 warnings, 0 suggestions. Review tự động không đánh giá độ dài nội dung và nhịp đọc thực tế.
- Đã có baseline render local ở 390×844 và 1440×900, screenshot candidate ở 375/390/768/1024/1440, cùng phép đo chiều cao/section. Chưa có heatmap, scroll depth thực tế hoặc số liệu chuyển đổi của bản candidate.

## 2. Mục tiêu và ranh giới

**Mục tiêu:** ở 375–390px, người đọc nắm được pain → cơ chế → proof/source → hành động bằng một đường đọc ngắn, với nội dung chuyên sâu có thể mở theo nhu cầu. Giữ visual PC tại 1024/1440px, danh tính route, thông điệp và nguồn của claim.

**Không đổi trong slice mobile:** số và ID CTA tư vấn (`osat-cta-header`, `osat-cta-terminal`, `fabless-cta-header`, `fabless-cta-terminal`, `partner-cta-header`), label `Tư Vấn` của Partner, bridge anchors, form/PopupX ownership, GTM/GA4 event names, proof scope và destination public. Không thêm CTA nổi hoặc form trong HTML. HTML canonical vẫn provider-free; binding live là trách nhiệm operator theo mandate riêng.

## 3. Hướng rút gọn theo route — đã áp dụng cho local candidates

| Route | Giữ trong đường đọc chính trên mobile | Ứng viên thu gọn/đưa vào mở rộng | Điều kiện bảo vệ |
|---|---|---|---|
| OSAT | Hero ngắn; 2–3 câu hỏi vận hành tiêu biểu; rail lot → test → quality/4M1E → WIP → cost; một proof CAS IC có nguồn; CTA cuối | Giảm chiều cao hero visual/metrics và các card lặp ý; màn hình mô phỏng nhiều tab trong `#lot-map` thành tóm tắt mặc định, chi tiết mở theo nhu cầu; resource cards dạng danh sách gọn | Không xóa tab/giải thích mang thông tin riêng trước khi audit claim; giữ `#lot-map`, `#cas-ic-case`, `#resources`, CTA và section observer. |
| Fabless | Hero; 3 câu hỏi WIP/lot/cost; flow forecast → outsource → lot/datecode/BIN → cost; một proof Bright Power có nguồn; CTA cuối | Hero proof panel, card dài và tầng giải thích trong `#fabless-map`/`#management-layers` chuyển sang tóm tắt ngắn + mở rộng; gom các resource links cuối trang | Modal/chi tiết hiện có phải còn truy cập được bằng bàn phím và không tự bật; giữ `#bright-power-case`, `#resources`, 2 CTA. |
| Supplier/Partner | Hero; ba nhóm audience tóm tắt; map ERP → MES → OT với ranh giới trách nhiệm; proof/source; nút header `Tư Vấn` | Sơ đồ và các slide sâu trong `#ecosystem-architecture` mở theo nhu cầu; lược đoạn văn trùng giữa `#operations-questions`, `#product-evidence`, `#supply-chain`, `#local-delivery`; resource cards thành danh sách gọn | Chỉ có **một** CTA tư vấn ở header; không tạo terminal CTA. Không ẩn toàn bộ proof hoặc nút nguồn; giữ route business `partner`. |

Ưu tiên thay đổi là **giảm lặp và giảm mật độ mặc định**, rồi mới xét ẩn chi tiết bằng native `<details>` hoặc tab hiện có. Mọi nội dung phụ phải có nhãn rõ, hoạt động bằng bàn phím, và vẫn có đường truy cập tới nguồn. Không dùng `display:none` cho section theo ID chỉ để rút chiều dài: section tracking dựa trên phần tử hiện diện và khả năng giao cắt viewport; thay đổi visibility có thể làm đổi dữ liệu `section_view`/`section_engagement_time`.

## 4. Slices và cổng nghiệm thu

| Slice / owner | Input & dependency | Output và quyền ghi | Acceptance / stop condition |
|---|---|---|---|
| M0 — baseline mobile; landing workflow, read-only | Commit `c243673`; source ba route; design system Master + override; Phase 4 ledger | Screenshot toàn trang và ảnh theo section ở 375×812, 390×844, 768×1024, 1024×768, 1440×900; bảng pixel/viewport từ hero đến CTA/proof; chỉ ghi evidence sanitized trong worktree | Ghi rõ chiều cao thực và điểm dài nhất. Dừng nếu local preview khác source/asset render, không suy đoán từ DOM. Một browser session chỉ một controller. |
| M1 — OSAT; một writer | M0 + OSAT source/override và claim ledger | Mobile CSS/content candidate trong riêng file OSAT; desktop screenshot diff | Desktop giữ visual đã duyệt; mobile không tràn, rail hiểu được, 2 CTA/IDs và các anchor/observer còn đúng. Dừng nếu đổi claim, mất proof/source hoặc bridge selector. |
| M2 — Fabless; một writer | M0 + Fabless source/override | Mobile candidate trong riêng file Fabless; desktop screenshot diff | Flow outsource đọc được, chi tiết mở được bằng bàn phím, 2 CTA/IDs; không thay form/analytics. Dừng nếu nội dung ẩn làm mất đường tới proof/source. |
| M3 — Partner; một writer | M0 + Partner source/override | Mobile candidate trong riêng file Partner; desktop screenshot diff | ERP/MES/OT rõ ở 375px, chỉ 1 CTA header `Tư Vấn`; không đổi business route. Dừng khi CTA bị nhân bản hoặc bản đồ mất nhãn ownership. |
| M4 — audit tích hợp; coordinator/auditor read-only sau các writer | M1–M3 + tracking contract + runbook + docs impact map | Bảng trước/sau, screenshot QA, test log, danh sách canonical docs cần đồng bộ, candidate decision | `node --test tests/landing-tracking.test.cjs` và bridge compatibility pass; test keyboard/touch/reduced-motion/anchor/CTA; render ở 375/768/1024/1440; không regression desktop. Nếu có thay đổi section event semantics, dừng và lập decision pack cho Bảo trước khi chấp nhận candidate. |

M1–M3 có thể chạy song song **sau M0** vì ghi ba file HTML khác nhau. M4 là cổng chung, không có shared-file writer đồng thời. Nếu rút gọn đòi bỏ hẳn một section, proof hay case đã có trên PC, hoặc đổi thứ tự kể chuyện/claim material, lập before/after cụ thể cho Bảo quyết định.

## 5. Định nghĩa pass cho candidate mobile

1. Bảng đo baseline và candidate ghi cùng viewport, chiều cao trang, số màn hình đến pain/cơ chế/proof/CTA cuối, và đoạn được thu gọn. Mục tiêu định lượng giảm chiều cao chỉ chốt sau M0; không bịa ngưỡng trước khi đo.
2. 375px không có text bị cắt, scroll ngang, control dưới 44px hoặc section cần thao tác hover; nội dung mặc định có đủ ý chính. Disclosure có focus rõ, tên dễ hiểu, `aria-expanded`/native state chính xác, không tạo scroll trap.
3. Diff screenshot desktop ở 1024/1440 được audit với visual baseline đã duyệt. Nếu khác ngoài responsive breakpoint, sửa lại trước candidate.
4. CTA 2/2/1, ID, nhãn Partner, provider-free canonical source, PopupX bridge selectors và tracking keys giữ đúng contract. Không diễn giải click CTA là lead hoặc form success.
5. `DOCS_IMPACT_MAP.md` được review trước handoff: khi candidate thực sự đổi landing/CTA/tracking, cập nhật canonical docs có statement stale; không chỉnh history để hợp thức hóa state mới. Local candidate không tự trở thành bản live.

## 6. Kết quả local và bước kế tiếp

- M0: đã đo baseline render 390×844 và 1440×900; baseline ở các viewport khác chưa đo. M1–M3: source của từng route đã có bản mobile compact, desktop 1440 giữ nguyên hình học section.
- M4: QA local ở 375/390/768/1024/1440 không thấy tràn ngang; 12/12 tracking tests pass; ba bridge compatibility checks trả `MODAL_OPENFORM_HANDOFF_READY`. Disclosure, deep link và Enter đã được kiểm tra bằng trình duyệt local. Bản 390×844 lần lượt còn khoảng 10.2k/10.0k/9.3k px cho OSAT/Fabless/Partner, giảm khoảng 39%/32%/35% so với baseline.
- Chờ Bảo duyệt trực quan ba candidate. Sau đó nếu Bảo chọn đưa lên LadiPage, cần chạy lại bridge trên đúng source pin và đi theo mandate/operator route; local QA không xác nhận render hay telemetry của bản live.

**Terminal hiện tại:** `MOBILE_CANDIDATES_READY_FOR_BAO_REVIEW`; chưa có quyền import/publish hoặc `MOBILE_CANDIDATE_PASS` cho live route.

**Docs impact:** đã review `DOCS_IMPACT_MAP.md`; cập nhật `CURRENT_STATE.md`, route overrides và OSAT route truth theo trạng thái local candidate. `Pre_Ad_Readiness_Plan.md` và tracking contract không cần sửa vì trạng thái live, CTA và event contract chưa đổi.
