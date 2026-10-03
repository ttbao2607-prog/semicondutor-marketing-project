# Dogfood ImageGen F2-A2 ngày 2026-10-03

Hai thử nghiệm local đã tạo ảnh và preview đầy đủ, nhưng cả hai cần thay đổi vì ảnh native 1254×1254 không khớp contract đã pin 1024×1024. Kết quả chạy là `PARTIAL`; đo benchmark `COMPLETE`; candidate contract audit `FAIL`; Luna và Sol đều `CHANGES_REQUIRED`. Lifecycle harness vẫn `testing_dogfood`; Bảo chưa cấp content acceptance (`NOT_GRANTED`). Không chỉnh ảnh hoặc đổi contract cũ để hợp thức hóa kết quả.

Cấu hình thực tế được admission/acceptance skill gates xác minh, không dựa vào lời tự nhận của child. Parent `/root` giữ operator và final auditor; review candidate độc lập với writer, audit dispatch của chính operator là SELF.

| Chỉ số / quan sát | Luna `gpt-6-luna/max` | Sol `gpt-6.1-sol/low` |
|---|---:|---:|
| Active child time, chỉ 4 turns (giây) | 1603.850 | 280.999 |
| Candidate preparation (giây) | 803.346 | 104.299 |
| Output tokens | 79,027 | 6,970 |
| Uncached input tokens | 163,972 | 55,017 |
| Base / correction calls | 1 / 0 | 1 / 0 |
| Image tool elapsed, operator time riêng (giây) | 28 | 31 |
| Child negative cases rejected | 17/17 | 18/18 |
| Fixed parent negative cases rejected | 18/18 | 18/18 |
| Native kích thước / contract | 1254×1254 / 1024×1024 FAIL | 1254×1254 / 1024×1024 FAIL |
| Story fit, scoped operator review | OPEN: central upward curve ambiguity | PASS scoped |

Thời gian/token lấy từ primary exact-child rollout task_started/task_complete/token_count, chỉ bốn lượt bootstrap/preparation/mechanical dogfood/viewer. Thời gian chờ operator giữa lượt, image tool và documentation closeout sau benchmark không tính vào active child time. Output token bao gồm reasoning output được record, không cộng trùng. Một trial mỗi cấu hình, khác effort và concept tự do, cùng nguồn/copy/style/gate và stochastic image tool không có fixed seed exposed: không suy ra general model ranking, giá tiền hay buyer performance. Image-generator model identity không exposed trong invocation; provenance chỉ ghi software agent `gpt-image`, không xác minh một model version riêng.

## Kết quả và giới hạn quan sát

Parent freshly rerun shared 35 tests đều pass; implementation `SUCCESS` và corrected-implementation `AUDIT_PASS` ở checkpoint vẫn có giá trị riêng. Fresh parent preflight/dispatch checks và normalized 18 negative cases mỗi candidate đều đạt expected result. Candidate dimensional FAIL không phủ định các kiểm tra này. Trước mỗi call parent independently reviewed source/copy/contract, pin review/release và kiểm tra exact prompt/references/output. Tổng hai base calls, zero corrections, zero child correction rounds.

Parent đối chiếu native headline/body/ba labels nguyên văn; mark visually consistent với reference, không phải pixel certification. Không thấy thêm readable wording, internal caveats hoặc repo receipt trong native/complete HTML/two-file export. Metadata caBX/C2PA được đọc riêng, CBOR payload bytes accounted for; provider creation/conversion/watermark/hash/signature metadata giữ nguyên, không thấy harness prompt/review/contract. Opaque binaries được tóm tắt; không claim cryptographic signature certification. Native bytes và source inputs được bảo toàn.

Desktop 1280×900 và mobile 390×844 fixtures đã được parent CUA xem: image loaded, không horizontal overflow, chữ/labels không clipped. Desktop content width khác nhau 608px Luna và 640px Sol theo cùng prose template; mobile cả hai 358.4px. Body/labels nhỏ ở feed scale; operator có thể đọc fixture đã xem nhưng PO/buyer understanding chưa tested. Backend native screenshot clipping của Sol được giải quyết bằng full-page capture và DOM, không quy thành lỗi HTML.

Luna có central rising curve và dashed baseline nổi bật, có thể bị đọc thành growth/improvement và kéo chú ý khỏi ba chiều đối chiếu. Đây là operator visual ambiguity finding, không chứng cứ fabricated numerical result hoặc buyer verdict. Sol có scoped story-fit pass; không biến thành content acceptance.

Size mismatch chung được quy cho operator/tool control gap: operator đã pin 1024 khi chưa có evidence built-in interface có thể honor kích thước đó. Không quy lỗi này cho child configuration. Không resize/composite/retry hoặc correction; trial cũ vẫn FAIL. Pilot không kiểm tra full-carousel transitions, set diversity, Taiwan closing-source readability, buyer hay live readiness.

## Evidence và byte identities

Các đường dẫn bên dưới là repo-relative, SHA-256 tính trên saved bytes.

| Evidence | SHA-256 |
|---|---|
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/final-audit.json` | `f61fed5b34ee0a244500b9b359bb91171400a26a689e19797a9a30a164ff8747` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/runtime-benchmark-metrics.json` | `68c8026d83040a97fc5f1cab106757831ce4e9c8237a79716a601e2562c5e6b5` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/luna/release.json` | `edfe7b7bb5dae896d81678d366deda5753a89536d50842e60158296d921ac60a` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/luna/actual-dispatch.json` | `8ce706229c70429bb5086670538dbd103d32b7bd70256c701086b232863f34d4` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/luna/postgen-review.json` | `3382f97e4a87ca9f87cb5affcad5b37a7cdbf73dadfc977c50329b25d90fb261` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/luna/provenance-inspection.json` | `3b3c312ad034fe1667599eb0c011035a83679a2428c86329ef353c12929ef88f` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/luna/independent-dogfood.json` | `a9e88a102350b3c3814aa3faa5528826f52faa5cd5603040da1d666bae775d00` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/luna/output/f2-a2.png` | `4594d10a6a67050d9b779ad52776aebdfccc2578632039bdd3ee7da5ff48a100` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/luna/index.html` | `3709c8383f008415301ac9723669e14e64cef8bf5fc441b81d820284beb0cfff` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/sol/release.json` | `99bfc3a6b794b8cca4ff4eaaddacbc64bdbb1f400ef055286646bc27accaf68f` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/sol/actual-dispatch.json` | `45545866635c92f060d7b6f714d45722818b6ce90f44bd58c8dff8608070be45` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/sol/postgen-review.json` | `098e6d719fa9ae1c5f7e1962f0a3a7a7ffaa81a10f3de9f2ae5ab8522506fa6c` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/sol/provenance-inspection.json` | `3581a2de935150fd15a7d0e1e7c5793366eaea108569e2b35b4c20863354fb9c` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/operator/sol/independent-dogfood.json` | `adc37aebeb9351d45052b33dc18c2e2aeaa2bec9cd583fecfd0044b05c01073f` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/sol/output/f2-a2.png` | `ad1877eed58f1bf351d4dfa9386aca154e393bfe2f3a66ed9697ff777f2755da` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/sol/index.html` | `157ea2f1fa8da6a1a28b09ad1a3fbdc02f4f83e48f6c13ea7f985069000dd03a` |
| `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/common/copy.json` | `2e551ab0de465046e198ad0822417a72c585f3b35796c46dccca1876f859d2ea` |
| `scripts/verify_imagegen_preflight.py` | `2b4c7666887fe2d8c3973fb79ac6a3379b0cbba375c9c82fd92fac0553c690f7` |
| `tests/test_imagegen_preflight.py` | `86c0110b04ce84746c84d0e03fb1344ed0937e2c72a3e87cf5b1a32062e02b15` |
| `operations/Ad_Artifact_Editorial_QA_Gate.md` | `a045be594186b09c1e60fa41b276ac4ccdd4a9a20873d89f2ae738d4088c61e0` |

Actual image sizes: Luna 1,356,588 bytes; Sol 1,233,004 bytes. Child evidence `luna/dogfood-results.json` và `sol/dogfood-results.json` nằm dưới cùng benchmark root; parent fixed-case evidence được pin ở bảng trên. Authority/scope: `operations/linkedin-imagegen-dogfood/benchmark-2026-10-03/authority.md` và `allocation-and-contract.md`; trusted releases ở bảng evidence, mỗi release chỉ một base call.

## Bước tiếp theo và documentation impact

Review một sizing policy tương lai tương thích với native output đã quan sát, hoặc chứng minh một route có exact-size control. Trước call tương lai cần contract/review/release mới được pin độc lập và kiểm tra native dimensions sau call. Không sửa các contract/review/release cũ, không đổi failed trial thành PASS; không có generation/correction/live/Git release mới từ report này. Nếu Luna được tiếp tục bằng mandate riêng, đơn giản hóa forecast-change cue rồi review actual raster. Bảo quyết định content acceptance; hiện `NOT_GRANTED`.

Docs impact reviewed: updated current entry/status/build/readiness/execution/harness/schema/visual/runbook records và DOCS_INDEX; report này là HISTORY / LOG, status JSON vẫn CANONICAL. Source/proof/strategy/rights/budget/targeting/tracking và viewer artifacts không đổi. Historical statements giữ nguyên dưới newest superseding addendum. Documentation closeout do cùng Sol leaf làm ngoài benchmark timing/usage; parent independently reconciles before handoff.

Git recovery không Fetch xác nhận branch `slice/linkedin-harness-redesign-plan`, HEAD/baseline `7e95a44dc5a3e5c25c07cda7c0f905822b8ba864` unchanged, dirty working tree, no upstream. Đây là thay đổi file trên máy, chưa staged hoặc commit; baseline commit local-only theo cached remote refs, không kiểm tra live GitHub. Không staging/push/merge/history mutation. Cached `origin/main` chỉ là remote-reference candidate, không live remote state.
