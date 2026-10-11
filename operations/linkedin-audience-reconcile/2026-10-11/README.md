# Kết quả đối soát LinkedIn audience — 11/10/2026

Đã chuẩn bị một gói đối soát tổng thể trên nhánh `slice/linkedin-audience-reconcile-2026-10-11`. Discovery vẫn **CHANGES_REQUIRED**. R5 đã đọc được mapping, alias còn thiếu đã xác nhận và reach theo cấu hình cũ giữ nguyên. Việc hoàn tất báo cáo không cấp trạng thái sẵn sàng chạy quảng cáo.

## Hai pipeline

| Pipeline | Đầu vào đã thực hiện | Readback 10/10 | Disposition hiện tại |
|---|---|---|---|
| Discovery / tệp công ty Week1 | Master424 giữ nguyên; cách ly15 bản ghi theo PO; upload409 một lần 08/10 16:20 | Ready, >90%, 794.946 members; Matched199, Unmatched93 | 17 cặp có bằng chứng đúng entity, 2 cặp sai đã xác nhận, 180 cặp thiếu bằng chứng; CHANGES_REQUIRED |
| R5 / backup Week2 | Master203 → TRUE_ONLY52; upload lại exact52 một lần 08/10 khoảng14:25 | Ready, >90%, 444.625 members; Matched52, Unmatched0; Details52 | Lỗi Details0 cũ đã hết ở lần đọc này; không còn căn cứ gửi Support cho lỗi đó. Persona/locale và release vẫn HOLD |

Summary được reload lại ngày11/10 và giữ cùng trạng thái/member counts. Mapping **từng dòng** của báo cáo dùng extract ngày10/10; không giả rằng toàn bộ199/93/52 dòng đã được đọc lại ngày11/10. Thời điểm đọc10/10 khoảng12:07–12:14 sớm hơn mốc T+48h của upload Discovery (16:20); không gọi extract đó là chứng minh backend đã xử lý xong ở T+48h. Fresh Details kiểm ngày11/10 được ghi trong receipt riêng. Khi kiểm ảnh, generic screenshot giữ số R5 dưới heading Discovery; ảnh đó bị loại khỏi proof. Direct tab screenshot mới đã được đọc thực tế và xác nhận Discovery794.946/199, tabs199/93. Reach/configuration dựa trên actual DOM snapshots; không ghi các ảnh viewport cũ là proof đầy đủ mọi filter.

Week1/Week2 ở đây là cách gọi hai tuyến công việc. Không suy số tuần creative thành persona, ngôn ngữ hoặc hai campaign đã được duyệt. Member counts là pool của list, không phải reach Việt Nam hoặc số buyer đủ điều kiện.

## Discovery: phạm vi đã đối soát

Toàn bộ199 matched đều nối duy nhất với projection của một bản ghi trong uploaded409. Đã kiểm đủ93 unmatched: 64 entry có một projection khớp, 28 entry cùng tên nhưng khác projection, 1 entry khớp nhiều bản ghi trùng. UI không hiện email-domain; không coi projection so sánh được là toàn bộ10 cột server.

| Disposition của409 source records | Số bản ghi |
|---|---:|
| Chỉ thấy trong Matched | 179 |
| Thấy exact projection ở cả Matched và Unmatched | 20 |
| Chỉ thấy trong Unmatched | 46 |
| Chưa thấy exact projection trong hai extract | 164 |
| Tổng | 409 |

164 là khoảng trống coverage chưa giải thích được, không phải164 công ty bị LinkedIn bỏ. 20 bản ghi xuất hiện cả hai phía và28 entry khác projection ngăn suy denominator/backend version từ UI. Không tính199/409 thành match rate hay diễn giải badge >90% như độ chính xác entity.

17 cặp đúng gồm11 cặp đã có bằng chứng trước, được giữ đúng intended entity/output Page, cộng6 cặp có numeric redirect/About và nguồn entity đối chiếu bổ sung. Cả11 input từng được cải thiện12 ô identifier nay đều xuất hiện trong Matched và có identity bridge phù hợp; không sửa ngược các identifier đã được chứng minh. Identity vẫn không chứng minh ICP, quyền mua ERP hoặc locale.

Hai finding D01/D02 thuộc **hai bản ghi cùng tên còn giữ lại trong409**, khác với hai bản ghi đã cách ly trong15. Do đó không kết luận “quarantine15 thất bại”. D01 vẫn vào đúng Page sai trước; D02 vào Page sai mới được đối chiếu độc lập, không mang verdict của Page cũ sang Page mới.

## Một gói đề xuất và ngoại lệ

Gói riêng tư chứa199 matched dispositions,93 unmatched dispositions,409 source dispositions,15 quarantine được bảo toàn,11 identifier-retention checks và52 R5 readbacks. Mỗi trường hợp thiếu bằng chứng giữ thiếu sót cụ thể từ source ledger hoặc yêu cầu exact numeric Page/website/address bridge; không nâng verdict chỉ từ tên giống nhau.

Đề xuất D01/D02: mở rộng cách ly tạm đúng2 bản ghi còn giữ lại; tập đề xuất khi đó là **407 giữ /17 cách ly trên master424**. Đây là **PROPOSED_NOT_APPROVED**. Chưa tạo CSV mới hoặc upload; bản uploaded409 và quarantine15 giữ nguyên byte/hash. Đề xuất không tự giải quyết180 cặp thiếu bằng chứng hoặc version/coverage. Nếu Bảo chọn scope407, cần duyệt đồng thời phạm vi ngoại lệ chất lượng còn lại; sau đó mới xuất một file cuối có hash và có mandate upload riêng. Không chia thành nhiều upload sửa dần.

Exact replacement Page của D01/D02 còn unresolved. Nguồn parent/subsidiary, địa chỉ tương tự và personal-profile search không đủ để thay employer Page. Các trường hợp khác trong180 và khoảng trống version/coverage được gom chung trong gói, không bị bỏ khỏi báo cáo.

## R5: alias và reach

52/52 input projections nối duy nhất về source52. 51 output link names khớp tên normalized; một alias còn lại được kiểm qua numeric redirect tới Page đã chấp nhận, About/domain/location và tên pháp nhân phù hợp. Giữ lựa chọn R5 trước đó. **Không gọi đây là fresh independent entity audit52/52**; tên khớp không thay bằng chứng pháp nhân/ICP.

Fresh unsaved editor11/10 dùng R5 AND Vietnam (recent or permanent), sau đó thêm các lớp AND độc lập. Trong mỗi lớp, thuộc tính nối OR.

| Cấu hình | English profile language |
|---|---:|
| R5 AND Vietnam | 8.200 |
| Thêm Functions: Engineering / IT / Operations / Quality Assurance | 5.000 |
| Thêm Seniorities: Manager / Director / VP / CXO | 460 |
| Cùng cấu hình đầy đủ, đổi riêng profile language sang Vietnamese | <300 |

Các số bằng snapshot07/10; đây là ước lượng hiện trên UI, không phải delivery. Snapshot đầu ở bước base còn giữ13triệu mặc định trước khi cập nhật; snapshot đó bị loại, đã đọc lại và chụp trực tiếp reach8.200 ổn định. UI giải thích English bao phủ các profile language tại location đã chọn, trừ Sponsored Messaging. Vì vậy460 không chứng minh audience FDI/English; <300 không chứng minh không có buyer nội địa. Chinese không có trong dropdown quan sát được. Không tự mở rộng targeting, thêm predictive, sửa function/seniority hay dùng nationality làm proxy.

Đã chọn **Do not save** ở dialog thoát. Saved inventory giữ5 mục với các giá trị readback như trước; Matched giữ4 mục, không có mục mới. Source CSV, campaign, ngân sách và creative không thay đổi.

## Kết thúc và việc còn lại

Execution **SUCCESS** cho preparation có giới hạn theo [PLAN](PLAN.md), với root self-review ghi riêng. Audience Discovery **CHANGES_REQUIRED**; R5 release **HOLD**. Còn thiếu quyết định/bằng chứng về180 Page identities, version/coverage, exact replacement Pages, ICP/customer decision unit và phân tuyến VN/FDI/locale. Không ghi PO acceptance hoặc independent audit.

Docs impact reviewed: cập nhật notice audience ở CURRENT_STATE, README, DOCS_IMPACT_MAP, LinkedIn_Build_Pack, S03, Pre_Ad_Readiness_Plan và LinkedIn_Current_Progress. Giữ thân tài liệu trước đó và dated receipts như snapshot lịch sử; sent package08/10 giữ nguyên. Ngân sách11,7triệu, cold Single image → member từ ads mới → Carousel RMK, frozen core và adapter DEVELOPING/NOT_FROZEN không đổi.

Git: baseline `f266e11d68d9818232674f4473dc23d687efeca9`; thay đổi mới là working files trên nhánh local, chưa staged/commit/push/merge. Main checkout và actual remote main vẫn baseline tại lần kiểm. Các nhánh local mới hơn thuộc scope khác được ghi trong [Git state](GIT_STATE.md); không lấy opened checkout làm toàn bộ tiến độ dự án.

[Aggregate summary](SUMMARY.json) · [Evidence/hash receipt](EVIDENCE_RECEIPT.json) · [Anchor review](MESSAGE_ANCHOR_REVIEW.md) · [Final self-review](SELF_REVIEW.json). Private row/account artifacts chỉ lưu ngoài repository; không đưa lên public Git.
