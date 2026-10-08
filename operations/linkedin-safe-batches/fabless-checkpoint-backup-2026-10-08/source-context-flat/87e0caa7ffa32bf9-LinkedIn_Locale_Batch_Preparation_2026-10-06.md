# Chuẩn bị sản xuất hàng loạt · 2026-10-06

**PROCESS_BASELINE_FROZEN / INTAKE_PREPARED / GENERATION_NOT_STARTED.** Scope offline; [freeze hiện hành](LinkedIn_ImageGen_Anchor_Freeze_2026-10-06.md). Adapter locale vẫn developing, dùng đúng dependency pin và review output từng revision.

Inventory nguồn theo [pivot](LinkedIn_VI_EN_Message_Pivot_2026-10-06.md):11 carousel/55 card giải thích,4 case/16 card bằng chứng,3 cold Single-image skeleton. Đây là số lượng nguồn, không phải số lượng asset mới đã accepted hoặc lệnh nhân bản mỗi locale. Candidate1/2 chỉ cover một OSAT journey.

| Nhóm intake | Phạm vi nguồn | Việc phải làm trước release call |
|---|---|---|
| OSAT O1/O2/O3/O4-O/O4-Q |5 carousel nguồn |Map local decision authority và supplier-chain relevance, tránh tự nhắm tập đoàn dùng hệ thống chung; chọn persona/case/reader phù hợp |
| Fabless F1/F2/F3 |3 carousel nguồn |Review ERP trigger và proof fit; không suy toàn bộ fabless là FDI buyer phù hợp |
| Partner P1/P2/P3 |3 carousel nguồn |Tách SI/đối tác triển khai với nhà cung ứng công nghiệp; P3 chưa đạt hướng VN chỉ bằng dịch |
| Case/RMK |4 bộ/16 card nguồn |Recheck proper names, geography, exact numbers, integrated mechanism, rights/scope và source hierarchy |
| Cold entry |3 skeleton nguồn |Hook/CTA/persona phải nối đúng explanation → case → reader; không reuse artwork sai hướng làm bản locale đã đạt |

English và zh-Hans có pilot evidence; mọi bộ còn lại vẫn UNREVIEWED. zh-Hant chưa dogfood; review terminology/culture/glyphs riêng, không coi Simplified→Traditional conversion là acceptance. VN là REBUILD_PENDING, không dịch lại skeleton vận hành cũ rồi nhận PASS nội địa. Queue chưa chọn locale/case cho từng nhóm thay PO khi thiếu relevance evidence.

## Intake bắt buộc cho mỗi lô

Một lô = một journey/locale/persona được mapping rõ, không mixed-language batch. Điền [intake template](message-anchor/freeze-2026-10-06/batch-intake-template.json) vào path revision mới; template PENDING không phải release. Chọn owner writer/reviewer; nếu root làm cả hai ghi SELF_REVIEW. Ghi source revisions/hashes, persona/decision unit, ICP evidence, locales, source rights, exact surfaces/order và dependency paths. FULL_JOURNEY phải include cold/explanation/proof/reader khi thuộc scope.

1. Reread anchor/email và manifest; kiểm code/input current SHA, source literals đúng locale, receipt prose không copy persona/locale cũ. Main thiếu Single-image input thì giữ blocked channel đó.
2. Author English/Chinese culture nuance theo persona, giữ storyboard; scene change quay lại review source. Map proof tới claim, phân biệt Taiwan solution với outcome case Trung Quốc. FDI ROI implicit hợp lệ; VN ERP readiness không hứa qualification/orders.
3. Thực hiện actual anchor/editorial/script review toàn fields/storyboard/transitions; tạo contract/review/release/spec và trusted receipts fresh. Source layout đủ dòng/body hierarchy và category vị trí riêng; case numbers chỉ trong approved copy, props giấy trung tính.
4. Trong mandate generation mới, guard trước từng call, exact payload/max5refs. Ghi attempt ledger original/corrective và hash ảnh, không ghi runtime model/effort nếu tool không expose. Không spawn từ batch prep.
5. Native + browser-visible desktop/mobile/feed readability + reader review; rõ actual viewport/image width, wording nhỏ/source, glyphs, overflow và journey continuity. Tool display/DOM metrics không thay screenshot/actual render inspection. Preview theo local-web-preview; chỉ dừng own helper/session.
6. Một corrective/card rồi recheck affected/adjacent/wholejourney; lỗi tiếp => dừng để review layout. Không cần thêm stage mới hoặc mutate harness/adapter status chỉ vì finding riêng asset.
7. Gate receipts/manifest/ZIP byte checks và docs impact trước handoff. PASS phải có đủ evidence; failed/missing giữ đúng verdict. Không overwrite artifact/receipts cũ. Commit/merge/push chỉ theo scope đã được Bảo cấp.

## Điều kiện bắt đầu lô và closeout

Bắt đầu generation khi đã có mandate cho lô, intake filled, source/proof phù hợp, actual PREGEN_SCRIPT PASS và fresh guard. Lô không phải chờ sửa mọi historical benchmark, nhưng không được dùng failed candidate2 card9 như accepted source-layout reference. Khi preview chưa hoạt động, có thể hoàn tất intake/script; chưa gọi artifact PASS.

Closeout ghi số call/ref rejection/corrective, actual failures/closures, render evidence, remaining findings, whole-journey verdict và input/output hashes. Đồng bộ canonical docs nếu current truth đổi; nếu không: **Docs impact reviewed: no canonical update required.** Routine asset defects ghi ledger và bounded corrective; lỗi chung có evidence qua nhiều bộ cần đề xuất revision frozen process/code, không silent mutate.
