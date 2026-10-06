> **Candidate2 v2 main integration · 2026-10-06:** Bảo authorized offline main adoption of10finalPNG + viewer/reader and review evidence. Card9 source hierarchy closed in native/desktop/feed; whole-journey remains INSUFFICIENT_EVIDENCE (mobile2–10 and reader visual pending). This adoption does not infer gate PASS or production readiness. Adapter developing; callable guard/freeze dependencies not imported. [Selection](<../linkedin-locale-dogfood/2026-10-06/candidate2-main-integration/selection.json>). Earlier candidate2-excluded/pre-merge notes remain dated snapshots. No push.

> **FDI locale artifacts · 2026-10-06 — approved offline integration.** Candidate1 English-v4 và candidate3 phồn thể final đã được Bảo duyệt đưa vào main local:20 PNG gốc +2 viewer/reader, giao bằng thư mục, không ZIP. Candidate1 không còn lỗi ảnh mở nhưng vẫn thiếu actual mobile render; không nâng gate thành technical ready. Candidate3 scoped root SELF_REVIEW native/desktop/feed/mobile/reader,0 finding material mở. Candidate2 giản thể card9 còn cần sửa source hierarchy và render chưa đủ: giữ riêng trên nhánh nguồn. Adapter vẫn DEVELOPING / NOT_FROZEN. [Phạm vi và provenance](../linkedin-locale-dogfood/2026-10-06/approved-main-selection/README.md). Source checkpoint `bfb710a`; không nhập lịch sử nghiên cứu, guard/freeze executable chưa có trên main hoặc cấp quyền generation/live. VN v3/Aplus hiện hành giữ nguyên; không push.

> **Main integration · 2026-10-06 — adapter DEVELOPING / NOT_FROZEN.** Bảo chỉ cho tích hợp checkpoint `ffb4fba` (anchor/gate và adapter draft) vào main local; adapter còn developing, chưa freeze/adopt/release. Core ImageGen frozen giữ nguyên scope riêng. [Phạm vi tích hợp và dependency](Main_Integration_2026-10-06.md): không đưa ảnh/viewer/input journey VI cũ lên main; full-journey dogfood, native EN/Chinese QA và creative acceptance còn pending. Các receipt/source-only status bên dưới giữ phạm vi checkpoint cũ, không chứng minh input/asset hiện có trên main. Không push/live.

> **Message anchor · 2026-10-06 — MSG-ANCHOR-01 bắt buộc.** Email gốc đã được Bảo cung cấp trực tiếp trong phiên; [anchor nội dung VN / FDI EN–Chinese](../Vy_Email_Content_Anchor.md) tách định hướng audience/persona/message khỏi đề xuất vận hành và phần đã superseded. FDI tập trung business value/ROI có căn cứ; VN là ERP hỗ trợ chuẩn bị năng lực vào chuỗi. Phải đối chiếu anchor revision/SHA256 trước generation và hậu kiểm từng artifact/surface + toàn journey. FAIL → CHANGES_REQUIRED; thiếu review/binding/evidence → INSUFFICIENT_EVIDENCE; đều chặn SCRIPT_REVIEW_PASS và ready/accepted handoff. Core harness, artwork và receipt cũ giữ nguyên; không PASS hồi tố. Những ghi nhận email gốc chưa có và budget/schedule/proposal cũ bên dưới giữ nghĩa lịch sử, không thay trạng thái hiện hành. Bảo đã yêu cầu commit checkpoint local trên nhánh hiện tại; containing commit lưu anchor/gate và adapter draft. Không merge main/push/live; các ghi nhận chưa commit bên dưới là snapshot chuẩn bị.

# English / Chinese localization adapter v1 · 06-10-2026

**Execution scope: offline adapter and authored draft examples. Creative status: LOCALIZATION_DRAFT_REVIEW_REQUIRED.** Bảo requested a lightweight separate adapter retaining the storyboard while localizing language and cultural nuance. Root owns this bounded implementation; no worker/delegation, image generation, account action or Git mutation. The frozen core is unchanged; this adapter is not adopted as a replacement release gate.

## Outcome and verification contract

Deliver a standard-library preparation script, separate locale profiles and reproducible examples. Acceptance: card/ad order, scene descriptions, props, proof/source pins, reference roles, limits and surfaces survive; all customer-visible text is supplied by the locale author; assembled prompts explicitly carry the locale; old approvals/releases are absent; source inputs remain unchanged. Verify with focused positive/negative tests, example-file inspection and the existing 65 core tests. Audit target: resulting candidate objects and prompts, not a claimed language/creative PASS. Human terminology and rendered typography acceptance remains a separate step.

## Small adapter, separate profiles

[Script](../../scripts/prepare_linkedin_locale.py) + [profiles](profiles.json), with no SDK, API, translation service, scheduler or new harness framework. `en` is international English; `zh-Hans` is the mainland draft; `zh-Hant` is the separately authored Taiwan draft. Future US/UK/Hong Kong or buyer-role specificity needs a new explicit profile. Language alone is not audience eligibility or FDI ownership evidence.

The author supplies localized copy and a rationale for every card. The adapter **does not translate automatically**: culture/domain decisions stay visible and reviewable. It preserves the exact scene description, props, concept IDs, narrative order and source map. Reader questions, headline/body, category/role labels, caption, source attribution, CTA, native headline and alt may be rewritten. A culturally unsuitable visual metaphor is an unresolved editorial finding requiring a new reviewed scene revision; v1 does not silently change it.

| Profile | Editorial choice in this draft | Layout care |
|---|---|---|
| English | Concrete operational question, responsible team and next step; no idiom or inflated benefit. International English baseline, not an invented universal English-speaker personality. | Longer words; authored breaks, no font shrinking to force the old VI line count. |
| Mainland Chinese | Explicit object being reconciled; draft vocabulary 制造业、在制品、核对; independently authored sentence flow. | Simplified glyphs, Chinese punctuation/line boundaries, mixed Latin acronym spacing. |
| Taiwan Chinese | Draft vocabulary 諮詢、在製品、紀錄、月底結帳; authored for Taiwan separately. | Traditional glyphs and Taiwan punctuation placement; no mechanical simplified→traditional conversion. |

All vocabulary remains provisional for native semiconductor/domain review. Preserve customer legal names, case geography, product/version names, units and the meaning of attributed results. `protected_literals` locks exact selected names; numeric/URL tokens are checked conservatively across all copy fields. The adapter cannot prove semantic equivalence, catch numbers written as words, certify correct script usage or discover an omitted protected name. Those remain explicit review obligations. It may reject valid numerical formatting changes; submit a separately reviewed revision instead of bypassing the check.

## Example: retain the financial-close storyboard

Source: [existing OSAT cold input](../linkedin-journey-demo/2026-10-06/osat/v1/public-copy.json), linked to O3. Calendar + factory records + chip-package tray remain unchanged. No customer outcome or product integration is asserted. This demonstrates localization mechanics on one real card, not mapping the whole campaign.

| VI source | English draft | Mainland draft | Taiwan draft |
|---|---|---|---|
| Đến ngày kết sổ. Số liệu xưởng đã chốt? | Month-end is here. Do the factory records reconcile? | 月末结账前，工厂记录核对了吗？ | 月底結帳前，工廠紀錄核對了嗎？ |

English makes “chốt” an explicit reconciliation question rather than ambiguous “finalized numbers”. Both Chinese drafts name the records and the pre-close timing. The open reconciliation point is preserved; no automation, cost reduction or guaranteed audit readiness is added. See authored inputs [en](examples/en.json), [zh-Hans](examples/zh-Hans.json), [zh-Hant](examples/zh-Hant.json), and resulting manifests/calls under [drafts](drafts/).

## Use and handoff

For a new draft, start from an example localization JSON. Keep the same copy schema and every card ID/order; author every field and one rationale per card. Specify a **new** output directory and unique revision. Example command from repository root, using the provided English input:

```powershell
python -B scripts/prepare_linkedin_locale.py --contract operations/linkedin-journey-demo/2026-10-06/osat/v1/contract.json --copy operations/linkedin-journey-demo/2026-10-06/osat/v1/public-copy.json --spec operations/linkedin-journey-demo/2026-10-06/osat/v1/spec.json --localization operations/linkedin-locale-adapter/examples/en.json --out operations/linkedin-locale-adapter/drafts/en-next
```

`prepare_examples.py` reproduces the three initial directories **only when absent**. The CLI refuses an existing output directory, leaving prior drafts and native art alone. It checks the current frozen core SHA and source copy/contract pins before assembly. Profiles and input hashes, rationale, and pending reviews are recorded in each manifest. These hashes are evidence, not independent authorization.

Output: `public-copy.draft.json`, `contract.draft.json`, `calls.draft.json` with assembled preview prompts, and `manifest.json`. **No review/release is created or inherited.** `calls.draft.json` deliberately lacks the required release/contract/copy/review envelope of a dispatch spec and cannot pass the frozen gate as a ready call spec. The frozen assembly uses the words “approved artwork”; in these preview prompts that heading is a template heading, not an approval. Do not dispatch preview prompts.

Before ImageGen: native market/domain review all fields, intent and glossary; review brand role/advertiser voice and proof; check first mentions separately on every declared surface; author fresh editorial detail/review and independently authorized release; pin the candidate inputs; create the normal full call spec from the reviewed calls and regenerate prompt hashes. Run the **existing** gate matching the channel: core for carousel, existing bounded Single-image trial adapter for the cold example. Neither is replaced here. Native PNG bytes, logo/reference roles and closing-source hierarchy retain existing requirements.

Definitions use ASCII `(...)` even in Chinese to satisfy the frozen first-mention matcher. This is an explicit harness compatibility choice; fullwidth `（...）` is not silently normalized. Profile definitions are draft terminology, not blanket first-mention PASS. Locale is inserted into `style.campaign.instructions`, which the existing assembler actually serializes; merely changing contract.locale was insufficient.

After authorized generation, inspect exact glyphs, language mixing, punctuation, source/CTA and line breaks at native and ordinary ~333px artwork width. Native CRC/dimension/hash checks cannot certify Chinese typography. Landing/PDF/destination locale, viewer `lang`/controls and cold→explanation→case continuity must match before creative acceptance; this task does not modify them.

## Research applied

- [Microsoft: localization overview](https://learn.microsoft.com/en-us/globalization/localization/localization-overview): localization includes visual/context adaptation, terminology and in-context validation. Applied here as author rationale plus separate native/domain and rendered reviews.
- [Microsoft: global English writing tips](https://learn.microsoft.com/en-us/style-guide/global-communications/writing-tips): clear international wording, consistent terms and avoidance of idioms/culture-specific references. Applied as an international B2B English baseline; finer regional messaging is a project choice needing evidence.
- [W3C: Chinese layout requirements](https://www.w3.org/International/clreq/): script and regional typography are separate concerns, including punctuation placement and line-breaking behavior. Applied as two Chinese profiles and mandatory glyph/line-boundary review. This working document is typography guidance, not evidence of buyer behavior or ImageGen capability.

Project choices such as tone, terms and the OSAT hook are draft editorial proposals informed by these sources; none proves that a national audience prefers a specific persuasion style.

## Verification result

**SUCCESS** for the bounded adapter/draft scope: 65 unchanged core tests and 9 adapter tests passed, including three-locale multi-card synthetic interoperability and rejection of changed order, numeric claims, protected entities, unknown locale and overflowing copy. All three real OSAT example prompts carry their locale; source/core bytes and scene/props remain intact. [Verification and output hashes](verification.json) record root inspection, not an independent-agent or native-language acceptance. No ImageGen calls. Source examples and new files remain uncommitted on the owned slice; main/GitHub have not received this adapter.

## Documentation impact

CURRENT_STATE, README, build pack, readiness, human-audit runbook, schema and visual instructions receive a dated draft-only pointer. The pivot record gets a scoped preparation addendum. Whole-set English asset production remains deferred; VI domestic rebuild remains pending. Strategy/source brief/S01/S03, budget, proof rights, tracking, landing design and historical receipts need no change: this preparation does not decide campaign mapping, certify new proof or change implementation/live state.
