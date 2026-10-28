# Kiểm unified reader / một endpoint — 28/10/2026

**Có: agent đã hợp nhất reader vào một HTML có client-side router.** P1 và P2 chọn đúng nội dung qua query, có thể dùng cùng một file/endpoint nếu host thực hỗ trợ. **Chưa có bằng chứng URL public hoặc import/hosting runtime.** Không cần mặc định host hai file riêng như phương án trước; cách đóng gói unified đã tồn tại và được kiểm ở local.

## Git/source thực tế mới

- Root worktree hiện là `main@568321fb8c951928fcb3867df4de75e9f43685e5`, clean. Actual GitHub `refs/heads/main` cùng SHA, kiểm qua `ls-remote` sau fetch.
- Gói từ `slice/executive-approval-launch-2026-10-28@eaf805a1` đã được nhập chọn lọc vào main và đã lên GitHub. Không phải vẫn chỉ ở nhánh launch như snapshot trước consolidation.
- Corrected worktree vẫn `slice/executive-approval-corrected-2026-10-28@c8e9d00c`; commit này đã là ancestor của main hiện hành, nhưng review/readiness working files mới hơn chưa được nhập/commit/push. Không switch, merge hoặc sửa main trong lượt kiểm này.
- Source: `D:/Digiwin_Semiconducter_Workspace/deliverables/unified-case-reader/unified-case-reader.html`. Current working bytes **905439**, SHA256 `1ac14a1bc4e58c69a3e3d7cd4175a2cc8c65e65ae291ef2d24fb8f71a2ae6302`. Git blob **905146** bytes, SHA256 `b83cd70d8008be26b195541593298042698aa163adf7583db2af7d7a2d65f0c4`. Chênh lệch chỉ CRLF/LF; normalized bytes bằng nhau. Không diễn giải hash khác là content khác.

## Router đã kiểm

Một đường dẫn file, các ad destination phân biệt bằng tham số:

```text
unified-case-reader.html?t=P1&lang=en
unified-case-reader.html?t=P2&lang=en
```

Đây là mẫu đường dẫn, không phải URL public đã publish. **Một upload/file ≠ mọi ad dùng URL hoàn toàn giống nhau.** Nếu link/UTM không có tín hiệu để phân biệt P1/P2, router không thể biết khách cần đọc bài nào.

| Check thực | Kết quả local |
|---|---|
| P1/en desktop1280 và mobile390 | Đúng “From lot records to the next operating decision” |
| P2/en desktop1280 và mobile390 | Đúng “Define record ownership before a system handoff” |
| `treatment=p2&locale=en` | Alias chọn P2/en |
| Chỉ `utm_campaign=fdi_p1_en_cold_test` | Suy P1/en đúng |
| Explicit P2/en + UTM P1/zh-Hant xung đột | Explicit P2/en thắng |
| Link trần / t/lang sai | **O1/en fallback**, không P1/P2; cần direct `t`/`lang` rõ ràng trên ad |
| P2 en→zh-Hant→reload→en | Giữ P2, title/locale đổi đúng; UTM và URL state giữ nguyên |
| Return/CTA của P1/P2 | Gói đã **bỏ return `index.html`**; chỉ còn skip link và 2 link nguồn. Chưa có contact CTA; không có link quay về viewer sai |
| Copy retention | Cả 4 locale packs P1/P2 bằng reader nguồn đã review. Script repo so 33 source routes ×4locale = **132 comparisons**, không lỗi |
| Dependencies | Structural verifier không thấy automatic external assets, forms/iframe, fetch/beacon/tracking dispatch. CSS/JS/ảnh nhúng trong file |

[Browser observations](BROWSER_CHECKS.json) ghi 14 state checks; 7 screenshots (P1/P2 desktop/mobile, locale toggle và cuối hai bài), tất cả cùng content file. Không overflow ngang hoặc ảnh chưa tải trong checks. Local preview đã stop đúng ownership/PID27204; viewport reset, tab đóng. Đây là SELF_REVIEW kỹ thuật, không full native/whole-journey/public-host certification.

## Điểm được cập nhật so với review P1/P2 cũ

1. **G02 return-reset của source readers không còn áp dụng cho candidate unified:** bản hợp nhất đã bỏ link return. Không cần thêm logic restore stage/card vào production unified chỉ để chữa hành vi của viewer demo. Source readers cũ vẫn giữ nguyên và finding cũ đúng cho chúng.
2. **G03 packaging đã có cách làm:** có thể một endpoint chọn P1/P2 bằng query. Host public, query/JS runtime, default locale, tracking/tag inventory và final ad URL vẫn cần kiểm đúng nền tảng.
3. **G01 contact CTA chưa được giải quyết:** P1/P2 vẫn chỉ có đoạn mời trao đổi và source links. Cần chốt bước đọc tiếp hay link tư vấn hiện có; không tự thêm form/provider/API.
4. **Phạm vi gói rộng hơn P1/P2:** HTML nhúng 11 treatment/44 display combinations, 33 source entries/132 locale packs và 3 nhóm hình, gồm ảnh OSAT2020 ở nhóm khác. Mở P1 không có nghĩa payload chỉ chứa P1. Duyệt selected P1/P2 không tự duyệt public toàn thư viện hoặc ảnh/case còn lại. Điều này không thu hồi approval case/translation đã có; chỉ cần đối chiếu đúng phạm vi định upload.

## Hosting/URL — đề xuất sau kiểm

- **Ưu tiên:** chuẩn bị candidate **P1/P2-only trên kiến trúc unified hiện có**, giữ copy/ảnh đã review, một file/endpoint, ad P1/P2 có `t` và `lang` rõ ràng. Đây là đề xuất scope packaging, chưa sửa/build mới theo lượt kiểm này. Có thể tránh mang các nguồn/ảnh ngoài selected set vào public payload.
- **Nếu dùng nguyên gói 11 treatment:** cần quyết định phạm vi public của toàn gói và fallback O1; không bỏ qua vì chỉ chạy hai URL P1/P2. Không tự đổi fallback hoặc chặn treatment khác trong review-only.
- Chứng minh host hiện có nhận HTML/JS/query và reload đúng: code router đọc `window.location` của document; nếu nền tảng bọc iframe, query trên URL ngoài **không tự chứng minh** được truyền vào document trong iframe. Đây là điều kiện kiểm, không kết luận LadiPage fail.
- Upload file lên GitHub là backup code, **không đồng nghĩa host website**. Root main đã push không cấp URL landing tự động, GTM inheritance hoặc quyền publish.
- Nếu dùng route hiện có của LadiPage, áp dụng đúng operator contract/receipt tương ứng; chưa mở editor hoặc nghiên cứu route deploy thay thế trong lượt này. Không suy Basic import cho trang khác chứng minh file này chạy trên host.

## Anchor / gate disposition

VY-CONTENT-ANCHOR1.0 SHA256 `6621d53c845939730ebcb1f59bbf85fb8a0d9acb156e5236e7387c0e69867ac5`; email VY-MAIL-USER-20261006 SHA256 `c5a6f35533e7a8b3b439ec4d9a260611fcdd2f67ddb0f046a3e33d28c6316d2b`, bằng binding hiện hành. P1 Operations/P2 factory IT, FDI English hypothesis; English không chứng minh identity. A1/A2 subgroup/decision unit vẫn chưa có evidence mới; A3 locale/treatment retention và A4 business-value/A6 product scope không đổi; A5 domestic N/A; A7 bỏ unavailable return, contact next-step vẫn mở. Không tạo MESSAGE_ANCHOR_PASS hoặc current-R5 release mới chỉ vì router chạy đúng.

Proof/rights/native/content dispositions trong [review P1/P2](../deep-review/REVIEW_VI.md) giữ scope source assets. Retention cho unified P1/P2 được bổ sung ở đây; không gọi việc loại return là copy rewrite hoặc buyer validation. Overall marketing/release **INSUFFICIENT_EVIDENCE / HOLD**, execution **SUCCESS cho router check**. Không generation, account, ad, publish, Git mutation hoặc asset edit.

Docs impact reviewed: corrected readiness C07 và Git/source status, current notices dẫn tới kết quả mới; historical review/index snapshot được giữ đúng ngày. Canonical main không bị sửa. Hồ sơ kiểm mới chỉ working local trên corrected, chưa commit/push.
