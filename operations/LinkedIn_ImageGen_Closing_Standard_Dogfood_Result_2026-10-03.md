# Closing standard dogfood — kết quả 03-10-2026

Chuẩn card kết đã qua dogfood F2 Fabless và O1 chất lượng OSAT; freeze phạm vi `FROZEN_HARNESS_CLOSING_STANDARD_TESTED_F2_O1` theo mandate Bảo: “oki chốt làm chuẩn harness, làm harness xong commit checkpoint r sau đó dogfood tiếp nhé để freeze harness.” Phạm vi là mechanism/closing reference/layout đã kiểm chứng trên hai tình huống và P3 anchor được PO chấp nhận; không tự chấp nhận toàn bộ exact production sets, không quyền live/publish/push.

Checkpoint implementation `3587fe740988a8ef50fe5df96b7231daea574add` đã lưu local TRƯỚC các image calls;119 raw pins được xác minh trước finalization guide/plan; sau hai authorized current-guide/dogfood-plan updates,117/119 còn byte-identical. Historical raw images/copy/receipts không đổi. Kết quả dogfood/docs sau checkpoint ở working tree local UNCOMMITTED/UNSTAGED; không có mandate commit thứ hai, không push/merge/live.

## Ba lớp kết quả

| Lớp | Kết quả và giới hạn |
|---|---|
| Implementation/mechanical |65 unit checks đã PASS trước checkpoint:49regression+16closing. Independent audit implementation `cfb12531e0d204ad87685d5db3d7969a7b5e747be5d70b691bb19cb211772da8`. Root kiểm tra5review/release/specchains, preflight/dispatch/native bindings và2viewer projections. Không dùng mechanical PASS thay creative verdict. |
| Native/render/story | PASS selected10cards,2full5carousels;20actual positions desktop1280×900/mobile390×844, image606.6667/332.6667px; không overflow, source fullwidth/source once/cùng hierarchy hoặc lớn hơn body, đọc nozoom; exactcopy/labels/logo/CTA, source không skyline/iconcolumn. |
| Adoption/authority | Closing method freeze theo conditional PO mandate đã đủ audit scope. Mechanism+exactF3 freeze cũ giữ nguyên. Whole-campaign exact-production/buyer/live acceptance NOT_GRANTED; không mở remaining rollout tự động. |

10base+1correction =11actualcalls; selected10. F2 có1correction A2, O1zero. Native1254square/original bytes giữ nguyên. F2body62/source92 là context-transfer test, không longer-copy; O1body147/source92 kiểm tra body dài; không bịa source dài hơn.

## Selected cards và lỗi được giữ lại

| Card | Selected native | Audit |
|---|---|---|
| F2_A1 | `3ef8e1af06ac0b7c2e96bb721080da8e9eaf519126e8ebc08ac3f2159b282886` | scopedPASS |
| F2_A3 | `2376281e801ea63e19cd403e6aaad67933d4448b3f97103025861f3be2528d51` | scopedPASS |
| F2_A4 | `0bd61f0755331b09c4267774b9f40982f6a42ac7ed11b330b149ffeb27c3ec1f` | scopedPASS |
| F2_A5 | `b5b359618d4ea610d01aed5df66977063f05f66fb7861a5d492c0893f3bd50f7` | scopedPASS |
| F2_A2_R2 | `844131d6c35668150034ce92e89881f822f9b74d1698f4dc732f24c869d85573` | scopedPASS |
| O1_A1 | `57dffde9abbfcca1ab10c85de1565a8a03d84fe1f0594da2a24039b7e98b5f94` | scopedPASS |
| O1_A2 | `d2b09aece6aefc2d7b2f56b74f91093012127684d66ad9ac9c712b40a9c45c38` | scopedPASS |
| O1_A3 | `0328a21ff75539819e22b20378c38654a7c4aba04e057092cc3d3bc5b34abe3e` | scopedPASS |
| O1_A4 | `2b10ecf95cea30fc48ea1f9988cbc274d6d00a3d907cb4fa2b3a8de61ff70d99` | scopedPASS |
| O1_A5 | `e76d8a41aa02410d9ae4a2463dc5b37f3e8f7f945e0181d2ca1d2656ff682eb5` | scopedPASS |

F2baseA2 SHA `09c9aa7dcabc3987bf504ff5b88a62f4a56940674679f8f72c88ea2cfe580010` thêm final period sau approved headline không có punctuation cuối: exactcopyFAIL. Native gốc và finding được giữ; A2r2 SHA `844131d6c35668150034ce92e89881f822f9b74d1698f4dc732f24c869d85573` chọn cho reader, headline/body exact. Unnumbered calendar bars chỉ minh họa kỳ kế hoạch, không metrics/results. Không sửa copy để hợp thức hóa lỗi.

F2 bốn transitions: forecast đổi/phạm vi lô → sản phẩm/kỳ kế hoạch → trạng thái/thời điểm/nguồn → câu hỏi thiếu/người xác nhận → căn cứ trao đổi/nguồn. Dotted question không trình bày handshake là agreement hoàn tất. O1: kiểm thử bất thường → quan hệ lô tách/gộp → ngữ cảnh trước kết luận → người/bước kiểm tra tiếp → quản trị thông tin bên cạnh technical assessment. Cả hai fullstory scopedPASS.

Cross-family scopedPASS: office/daylight/white-blue-navy, material depth, official header và semiconductor/diagram integrated ổn định, phù hợp acceptedP3 B/F3frozenfamily. Cardmeaning khác nhau, không dùng prop quotas/IDs để chứng minh chất lượng. Background pictograms/placeholderlines unlabelled, không số liệu/identifiers/microtext. App screenshot warmcast không được diễn giải là nativepalette defect.

## Evidence và public boundary

- Parent native/render/story observations: `operations/linkedin-imagegen-dogfood/closing-standard-harness-2026-10-03/operator/dogfood-observations.json`, SHA256 `21b44c74a46bd30e151d94be4bfa5cb02e6e4923117f7b0cdf560d13265949ca`.
- Final closeout audit completed parent receipt: `operations/linkedin-imagegen-dogfood/closing-standard-harness-2026-10-03/operator/parent-final-audit.json`; FINAL_PARENT_AUDIT_PASS after independent final audit and fresh paired acceptance. Receipt exists; no SHA field added because parent final candidate inventory is rebound after these docs, avoiding circular hash.
- Implementation audit: new namespace `operator/implementation-final-audit.json`; guide/schema amendment and reference-approval.json retain exact PO accepted anchor `016b69513d28bee0ab1b371e4ff5c8f4a86acb531a40125d72785622b01a7416`.
- Exact approved copies: common/f2-copy SHA `45b83f7a59323a2c00a0016f6f06472395b7f4a7a079ab5ec15c55c718a2b919`, common/o1-copy SHA `a10f0cdd6f73d3607ac04c23897c644446c242d5232622346407d28794cc1925`.
- Reader HTML F2 SHA `56e76e2128e273f12eb5a0422bfefb9a5c2e6a16e25fca9dfc31d36c28968c89`; O1 SHA `dc1037eef5dd5c52e238f0a03774ef46127c13d449cc4fc89a26dfe6708c0722`. Sevenfiles each: HTML+5rawPNG+officiallogo; manifests/projections stay sol/{f2,o1}/ outside public bundles.
- All20full-card desktop/mobile positions observed; next/previous/dots/ArrowRight and endpoints checked. Parent reset viewport, closed agent tab, stopped owned loopback. No broad keyboard/accessibility claim beyond observed controls.

Docs impact reviewed: schema/visual guide/process/currentstatus updated; strategy/proofrights/landing/tracking/budget unchanged. Oldfailed runs/receipts/native bytes/freeze scopes remain. Next work must use fresh source-copy and bounded per-scenario review/release; successful tested closing method does not authorize blanket all-scenario production or consume remaining correction budget automatically.
