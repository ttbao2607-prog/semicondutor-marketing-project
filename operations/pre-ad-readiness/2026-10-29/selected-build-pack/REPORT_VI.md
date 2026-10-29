# Gói chốt P1/P2 trước dựng ad — 29/10/2026

**Đã hoàn thành gói chuẩn bị nội bộ; chưa tạo ad.** Hai cold ad cho đợt đầu và bốn carousel cho RMK được tách rõ, exact source copy/ảnh giữ nguyên. Gói đủ để Bảo review quyết định còn thiếu, chưa đủ để gọi paid-ready.

- [Copy, headline và thứ tự ảnh theo từng ad](AD_FIELDS.md); [6 dòng ad](BUILD_ADS.csv), [20 vị trí card / 16 ảnh duy nhất](BUILD_CARDS.csv).
- [Hash nguồn/asset/reader hiện hành](SOURCE_BINDING.json); tên wave01 là đề xuất cụ thể, actual ad/adset IDs để trống vì chưa tồn tại. CSV là bảng review, không phải file import trực tiếp vào platform.
- [Đối soát từng gap và lựa chọn cần quyết định](GAP_DECISIONS.md); [fit evidence tổng hợp không chứa raw audience](FIT_RECONCILIATION.json).
- [Lịch/pacing/placement/bidding, measurement và stop proposal](OPERATING_PROPOSAL.md).
- [Fresh anchor receipt](MESSAGE_ANCHOR_RECEIPT.md), [contract](PLAN.md), [checks](CHECKS.json).

## Điều đã xử lý trong gói này

1. Loại rủi ro dùng nhầm bảng 99 ad cũ còn ghi UNKNOWN/provisional cho selected destinations. Bảng selected có host thật, t=P1/P2, lang=en, acquisition UTM và creative revision. Mỗi carousel card có attribution riêng nhưng cùng reader đúng journey. Cold/direct-entry không cần đi qua viewer nội bộ. Không thay bảng library/generator lịch sử hoặc chuẩn hóa toàn bộ 99 ad ngoài phạm vi.
2. Giữ đủ hai carousel EXPL/PROOF mỗi journey theo D4; không đưa cả sáu ad vào cold. Hai cold có thể dùng một ad set và ngân sách chung; chưa giả định hai ad set hoặc chia đều delivery.
3. Đối chiếu file thật: captions 188/178/161 và 201/194/161 ký tự; native headline dài nhất 41; PNG1254×1254, lớn nhất1,801,998bytes. Theo [Single image specs](https://www.linkedin.com/help/lms/answer/a426534) và [Carousel specs](https://www.linkedin.com/help/linkedin/answer/a427022) kiểm29/10, không phát hiện vượt hard limits đã đối chiếu. Captions >150 có thể bị thu gọn; giữ copy, không tự rút/generate ảnh. Saved native UI vẫn cần kiểm thực tế.
4. G01/G02/G03 đã gỡ ở public unified route; không hỏi lại contact label/vị trí hoặc host. Tracking truyền dữ liệu đã qua QA scoped; processed reporting/paid outcome chưa được chứng minh.
5. Rà lại Git object của R5 để tách mapping khỏi relevance: 52 retained, 40 Page global/9local/3regional; tất cả chưa xác minh purchasing authority. Có IC design và các nhóm khác ngoài equipment-component. G06 vì vậy còn bằng chứng thiếu thực sự; không gọi R5 sai mapping hoặc tự đổi targeting.

## Phương án cụ thể để Bảo review

Đề xuất một cold ad set, hai ad P1/P2, Feed, Expansion/LAN off, impressions/Maximum delivery. Proposed window 02–08/11 theo UTC; USD10/ngày trung bình cho cả ad set, nominal USD70/tuần, review09/11 giờ VN. D6 chi tiết và điều kiện quy đổi/ceiling nằm trong operating proposal; không coi đây là lịch đã duyệt hoặc dùng hết5,6triệu. Trần11,7triệu/cơ cấu/weekly review không mở lại.

Trước production paused build cần giải quyết: **fit subcohort hoặc copy route**, **paid-use disposition đúng asset set**, **human/domain acceptance và native feed preview**, **actual budget/currency/date/UI fields và reporting readback**. Recommendation fit là kiểm equipment/process-component subcohort và eligible reach trước; nếu quá mỏng, chuẩn bị phương án adapt copy rộng hơn để Bảo chọn, giữ nguyên creative hiện tại trong lượt này. Không dùng quyền duyệt lịch để thay bằng chứng fit.

## Trạng thái và Git

Execution **SUCCESS cho internal pack** khi CHECKS đạt; full paid readiness **INSUFFICIENT_EVIDENCE / LAUNCH HOLD**; independent audit NOT_RUN. Không có live/browser/account mutation hoặc sửa PNG/copy/reader trong lượt này. Không phát sinh data/lead hoặc chi tiền.

Tạo trên owned worktree approval-corrected, source checkpoint9d9f061b; main/GitHub đã xác minh568321fb. Gói mới và notice được lưu trong **containing local commit trên nhánh này** theo yêu cầu commit trước đó của Bảo; chưa push/merge. Các commit reader trước vẫn local; public LadiPage là kết quả deploy trước, không phải GitHub đã đồng bộ.

Docs impact reviewed: readiness index C04/C05/C06/C08/C10/C11 và next-action order, current entrypoints, current build pack/pre-ad plan và selected-build notice được đồng bộ; không rewrite lịch sử review/approval. Không đổi frozen core, locale adapter, targeting, budget authority hay runtime.
