> **PO freeze hiện hành · 2026-10-06:** harness hiện hành + callable anchor guard + quy trình tiền/hậu kiểm **FROZEN_PER_PO**, theo [freeze record](../LinkedIn_ImageGen_Anchor_Freeze_2026-10-06.md). [Chuẩn bị lô](../LinkedIn_Locale_Batch_Preparation_2026-10-06.md) đã có intake/gates; chưa generation hàng loạt. Adapter locale vẫn DEVELOPING / NOT_FROZEN. Candidate2 checkpoint `67d1cbd` đã commit local, card9 CHANGES_REQUIRED/rendered scope INSUFFICIENT_EVIDENCE giữ nguyên; không PASS hồi tố. Chỉ hiện tại ở nhánh local, chưa main/push. Snapshot developing/no-freeze cũ bên dưới được supersede riêng scope harness/guard/process; không supersede artifact findings.

> **Chinese candidate2 observation · 2026-10-06:** [10+1calls](../linkedin-locale-dogfood/2026-10-06/zh-Hans-osat-candidate2-v1/README.md) có fresh guard ngay trước inference. Adapter giữ mô tả scene nên English literals phải được xử lý ở reviewed source revision trước localize; literal đã bắt trước gent. Fixture A5 free-text copied English-only note được reconciled ở postrun, các scope/hash Chinese đúng; wrapper không chứng minh semantics của prose, historical receipts giữ nguyên. Card9 layout còn lỗi/rendered evidence chưa đủ; PARTIAL/CHANGES_REQUIRED, không freeze. Core/adapter/guard bytes và lifecycle unchanged; ghi nhận selection-only bên dưới là snapshot cũ.

> **Candidate1 corrective checkpoint · 2026-10-06:** Hướng corrective ba card ở mục dưới đã được thực hiện trong [candidate1 v4](../linkedin-locale-dogfood/2026-10-06/en-osat-candidate1-corrective-v3/README.md), thêm source layout review và reflow; finding gốc đã khép. [PO receipt](../linkedin-locale-dogfood/2026-10-06/en-osat-candidate1-corrective-v3/po-checkpoint-acceptance.json) ghi acceptance bản hiện tại, nhưng actual mobile-device evidence vẫn pending, không hồi tố PASS benchmark. Các câu “chưa generation/closure” bên dưới giữ phạm vi snapshot v2 trước corrective. Wrapper/core/adapter bytes và lifecycle không đổi; candidate2 zh-Hans chỉ có selection plan, chưa dispatch hoặc freeze.

# Nối script → anchor trước ImageGen · frozen 2026-10-06

Effective procedure: 2026-10-06. **FROZEN_PER_PO**, per current freeze record; no generation, release or live authority created. Owner: root under Bảo's request to prevent paying for images whose script already misses the message anchor. Frozen core and existing Single-image trial code stay unchanged.

## Execution contract

Outcome: a callable pregen wrapper must refuse missing/pending/stale anchor or script review and return a payload only after fresh frozen mechanical validation plus exact review bindings. Scope: a new wrapper, receipt JSON template, synthetic tests and documentation integration. No semantic auto-approval, changes to prior receipts/creative/core, stage/commit/merge or image calls. Evidence: positive FIXTURE_ONLY and negative stale/coverage/persona/script/context tests, current core hash and gate links. Root self-inspection only; no independent-agent or creative acceptance.

## Current gap and new path

The anchor was already mandatory in PREGEN_SCRIPT and postcheck documents. `prepare_linkedin_locale.py` only writes drafts and does not read an accepted anchor receipt; `verify_imagegen_preflight.py` checks frozen mechanics and does not implement MSG-ANCHOR-01. Neither was a script-enforced anchor dispatch gate. The new [wrapper](../../scripts/verify_imagegen_anchor_preflight.py) closes that gap for its execution path.

Required path for every future image call, VI or FDI EN/Chinese:

1. Define the actual persona, route, locale, audience/ICP relevance and full-journey brief. Author all copy fields and scenes; check hook → mechanism → business value/readiness → proof → CTA before generation.
2. Reviewer reads [current anchor](../Vy_Email_Content_Anchor.md) and original email, reviews each field/card/scene and transitions. Record actual semantic findings and closures, not a default PASS. Complete both AD-ED-01 PREGEN_SCRIPT and MSG-ANCHOR-01 receipts. No images are needed to inspect the script; record POSTGEN_NOT_RUN.
3. Build fresh frozen contract/review/release/spec for the reviewed copy. Final spec binds exact reader questions, descriptions, props, artwork text, references and assembled prompts. No copy/prompt tweaks after review. The anchor receipt pins contract/copy/final spec, editorial script receipt and context/other-stage inputs; these are external receipts, avoiding circular core pins.
4. Immediately before each tool call, run the wrapper with coordinator-supplied trusted release and message-review SHAs, selected call ID and expected persona/segment/route. It rechecks current bytes and frozen gate. Use only the exact returned tool payload under existing explicit generation authority. Run again before a retry or changed call.
5. After generation, inspect native and actual desktop/mobile artwork for faithful rendering, added/missing wording, glyphs and visual/story drift. Postcheck remains required, but cannot rescue an unreviewed script after money is spent.

```powershell
python -B scripts/verify_imagegen_anchor_preflight.py --root . --release <repo-relative-release.json> --release-sha256 <trusted-sha256> --spec <final-spec.json> --message-review <completed-anchor-review.json> --message-review-sha256 <trusted-review-sha256> --call-id <released-call-id> --segment FDI --persona "<specific reviewed persona>" --route "<reviewed route>"
```

Use `VN_DOMESTIC` for vi/vi-VN; `FDI` for en/zh-Hans/zh-Hant. [JSON receipt template](../templates/Message_Anchor_Pregen_Receipt_Template.json) is deliberately PENDING and cannot pass. It complements [semantic review template](../templates/Message_Anchor_Review_Receipt_Template.md), not a way to manufacture a review.

## Corrective sau dogfood — Bảo 2026-10-06

Áp dụng cho các session VN / FDI English–Chinese trong scope generation đã được giao. Đây là quy trình phát hiện và sửa bounded artifact, không tự cấp thêm quyền generation, tự động retry, freeze/adopt hoặc đổi lifecycle harness/adapter. [Đối sánh v2](../linkedin-locale-dogfood/2026-10-06/en-osat-journey-v2/README.md) vẫn CHANGES_REQUIRED; không sửa benchmark v1/v2 để biến nó thành PASS.

**Phòng lỗi trước gent:** category/header và source/footer là hai vai trò, vị trí riêng; ghi literal bắt buộc từng vùng, không cho source thay category. Scene cần record/lot reconciliation dùng giấy/folder/tray trung tính; tránh calendar/chart hoặc vùng dữ liệu có thể ngụ ý số liệu case ngoài script. Nếu đổi props/scene đã duyệt, phải review lại storyboard/source contract, không coi đó là localization thuần túy. ROI implicit không phải lỗi và không thêm ROI claim chỉ để qua gate.

**Khi hậu kiểm bắt lỗi:** phân loại script/message/source sai (quay lại PREGEN_SCRIPT), lỗi binding/payload (sửa input/gate trước call), hoặc render thêm/thiếu/sai so với script đúng (targeted corrective). Không rerun cả bộ khi chỉ một card lỗi. Mỗi card có ledger: exact finding, original PNG/hash, nguyên nhân giả thuyết, thay đổi định làm, copy/scene/reference revision và acceptance criteria. Không coi giả thuyết prompt là nguyên nhân đã chứng minh.

**Corrective bounded:** trong scope đã được giao, mặc định một lượt corrective cho card lỗi, kiểm lại sau lượt đó; không phải quyền tự gọi tool cho mọi session. Dùng revision/output path mới và input/release/spec + actual script/anchor review mới, chạy wrapper ngay trước call. Đổi reference pack phải review vai trò/phạm vi và giữ tối đa5refs. Có thể reference ảnh lỗi để chỉnh trực tiếp sau khi xem nó, nhưng ảnh lỗi không trở thành proof/style baseline được chấp nhận. Không overwrite PNG/receipt cũ.

**Khép lỗi:** xem native và rendered desktop/mobile, so đủ text/category/source/CTA/proper names/numbers, tìm graphic data mới và regression; rebuild revision-pinned demo/manifest, recheck card liền trước/sau và whole-journey anchor. Sửa ảnh không mặc nhiên là PASS. Thiếu rendered evidence => INSUFFICIENT_EVIDENCE; còn lỗi => CHANGES_REQUIRED. Sau một corrective vẫn lỗi hoặc thêm regression, dừng vòng retry và đề xuất đổi scene/layout có review; không nới tiêu chí hay nâng lifecycle. Chỉ khi lỗi lặp có evidence chung qua nhiều candidate mới cân nhắc thay adapter/harness dưới mandate riêng.

**Ba finding v2 và hướng corrective:** O3-A5 bỏ bar/pie chart tự sinh trên giấy, dùng blank/neutral records mà vẫn giữ ý shared cost review; RMK-R4-1 khóa `SEMICONDUCTOR CASE` ở header, đặt source đúng vùng riêng; RMK-R4-3 thay calendar tô ô bằng props trung tính sau storyboard review, chỉ giữ kết quả15→5 trong field đã duyệt và attribution case. Đây là kế hoạch, chưa có corrective generation hoặc closure.

## What the guard checks

**Dogfood repair 2026-10-06:** selected calls now reject more than **5 reference images** before returning a tool payload. This is the limit observed from the built-in tool in the failed English pilot, outside the frozen core. Two synthetic boundary tests and a replay of the real six-reference failed release verify blocking without inference. Prompt/source preparation also receives explicit literal-header and cohort/scene review in the repeat pilot; those semantic/render requirements are not automatically proven by this count check. At that repair checkpoint wrapper remained DEVELOPING / NOT_FROZEN; current freeze supersedes that lifecycle only; core, locale adapter and profiles unchanged. [Controlled repeat and benchmark](../linkedin-locale-dogfood/2026-10-06/en-osat-journey-v2/brief.md).

- Trusted receipt hash, canonical current anchor path/revision/hash and original-email source hash.
- Exact contract/copy/spec/script-review bindings; actual script verdict, BRAND_ROLE and ADVERTISER_VOICE PASS plus complete field coverage.
- Caller-expected persona/route/segment and locale; all A1–A7 verdicts/observations; ordered per-card script and storyboard coverage, per-ad transitions and unresolved findings.
- Context brief hash; FULL_JOURNEY requires related stage input pins, all read again. Reviewer must supply all relevant inputs and assess cross-stage transitions; the script cannot discover omitted journey components or judge whether an observation is persuasive.
- Frozen core hash; pinned existing Single-image trial adapter only for that channel. If absent on main, Single-image checking fails until an explicitly approved input/gate route is provided; no fallback or recreated adapter.
- Fresh mechanics/prompt/output checks for the selected call. FIXTURE_ONLY always returns no generation payload. Missing/stale/failed evidence exits nonzero with PREGEN_BLOCKED and `tool_args: null`.

The wrapper validates that a real declared review is bound to current inputs; **it does not understand or certify the message automatically**, authenticate a person's identity, or cryptographically prove a truthful review. External trusted SHAs must come from the coordinator/reviewer, not be self-selected to bless the writer's draft. It cannot intercept manual calls made outside this path; AGENTS/runbook require the path and direct calls that skip it are noncompliant. Core-only PASS and draft prompt files are insufficient dispatch evidence. No image tool is called by this wrapper.

The original locale adapter remains a draft authoring tool. Any old auto-written SCRIPT_REVIEW_PASS detail without anchor and complete field coverage cannot pass this new wrapper; do not retrofit PASS into historical receipts. Make a fresh actual review. Unused postgen fields do not delay pregen: they remain explicitly POSTGEN_NOT_RUN until an authorized image exists.

Docs impact: AGENTS, CURRENT_STATE, editorial gate, canonical runbook and locale-adapter docs point to the callable pregen guard; existing anchor message rules/revision and frozen harness code remain intact. Other strategy/budget/proof/landing/tracking truths are unaffected.
