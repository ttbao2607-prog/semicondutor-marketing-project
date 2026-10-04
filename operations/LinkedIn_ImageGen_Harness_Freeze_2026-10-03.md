# Harness freeze và project worker — 03-10-2026

Bảo phê duyệt checkpoint với nguyên văn chỉ đạo:

> Okie đẹp rồi codex. Chốt harness này và dùng sol làm chuẩn cho project - Luna không đạt yêu cầu visual bằng Sol. Commit checkpoint này status như vậy nhé (freeze harness hiện tại và chọn sol làm worker chính nếu spawn child).

Quyết định hiện hành: adopt/freeze hybrid R2 harness hiện tại; chọn họ visual Sol làm baseline của project và gpt-6.1-sol/low làm native leaf worker mặc định khi có mandate spawn child. Luna không được chọn theo đánh giá visual của Bảo trong project này. Đây là lựa chọn vận hành theo PO, không xếp hạng model tổng quát hoặc kết luận chi phí.

Coordinator/root hiện tại không đổi. Trước mutation phải xác minh effective runtime model và reasoning effort qua canonical admission/acceptance checks; không tự khai từ prompt, không silent fallback sang Luna hay model/effort khác. Thay đổi lựa chọn cần override mới của Bảo. Quy tắc chỉ thuộc repository này, không đổi global skills/config và không tự cấp quyền spawn.

## Frozen mechanism và phạm vi

- Gate SHA256: `6cf752ff249553e88222edea647ee0e0efeb215816fc2ab0b6b0201974ab44a8`.
- Tests SHA256: `f0d45c2356bba488dd65d3247b1341fdb8140eb33624f92eacc5032d9fed6dde`.
- 49 tests đã PASS (35 legacy +14 focused); parent19 negative+3 positive/model đã tái lập. Không rerun trong docs freeze.
- Reference core: campaign_visual allowed attributes, independently pinned style.campaign và assembled prompt; active r2-1/r2-2/r2-4/r2-6+official logo. Kit sáu R2 vẫn phục vụ human comparison, không exact composition/wording/data transfer.
- Output forward native_square_min>=1080; legacy exact output/prompt bytes giữ nguyên. Native checker CRC/dimensions/hash không chứng nhận visual/semantic/provenance.
- Lượt bounded hoàn tất20 original native PNG1254square, bốn full five-card carousels F2-A/P2-A,20base/0correction; một rejection7refs trước inference tạo zero ảnh. Original/native/export giữ nguyên.

Lifecycle vẫn `testing_dogfood` theo “status như vậy”. PO hiện chấp nhận adoption/freeze và hướng visual Sol. Historical operator creative audit FAIL, cả hai candidate CHANGES_REQUIRED, bảy definite text violations, SolF2-A3 quarantine, pending-state và mobile source findings giữ nguyên. PO lựa chọn hướng không hồi tố sửa audit/contract hoặc xác nhận rằng mọi thẻ đã đáp ứng từng tiêu chí. Trial cũ exact1024/actual1254 vẫn FAIL. Không buyer validation, blanket whole-set external release, live/readiness, correction call hoặc account authority.

Containing local freeze checkpoint ghi quyết định này; prior baseline `7e95a44dc5a3e5c25c07cda7c0f905822b8ba864`. Không push/merge được cấp. Commit SHA được Git chứa bản ghi xác định, không tự ghi SHA vào nội dung của chính checkpoint. Parent sở hữu stage/commit và final audit.

## Primary evidence

| Path | SHA256 |
|---|---|
| `operations/LinkedIn_ImageGen_Hybrid_Full_Dogfood_Benchmark_2026-10-03.md` | `1c7137095da4b4e38e2b14e58d041856fa2dbcbb882d62cbdd04a06b166344b7` |
| `operations/linkedin-imagegen-dogfood/hybrid-full-2026-10-03/operator/final-audit.json` | `69152fbb1dccc363d347772b09c8ea3ab20a723b235d2d02d533ab9d26facbeb` |
| `operations/linkedin-imagegen-dogfood/hybrid-full-2026-10-03/operator/native-observations.json` | `21ecf0fa7809c4475537a4f2dd19efce7f5a48e8bf2dda9dee1143db0e8fcca3` |
| `operations/linkedin-imagegen-dogfood/hybrid-full-2026-10-03/operator/final-mechanical-audit.json` | `1e9c8c9e59b67662e97fe1f8e36cb581febc1ce6debb9f0aae8d8366c39fc390` |
| `operations/linkedin-imagegen-dogfood/hybrid-full-2026-10-03/operator/native-metadata-audit.json` | `7331044ce54e0e4cdc2a2f0179517c0962a2fcc4b8471fab99e9d2699171f88c` |
| `operations/linkedin-imagegen-dogfood/hybrid-full-2026-10-03/operator/render-audit.json` | `6decc76658bb87f74209723f296a5357e90f497fc847ea0f62f8f497d9e4812f` |

Docs impact reviewed: project operating defaults/current freeze acceptance changed; current entry/build/readiness/process/schema/visual/kit/criteria/status synchronized by dated addendum. No change to strategy, proof/rights/sourcecopy, landing/CTA, budget/targeting, tracking or global configuration. Historical benchmark/preparation/receipts untouched. Parent adds freeze manifest/audits separately.

Repo-only `.gitattributes` dùng `-text` cho các tệp/phạm vi được pin để giữ raw bytes qua checkout, tránh LF/CRLF làm lệch SHA256; không tắt textual diff hoặc đổi Git config.
