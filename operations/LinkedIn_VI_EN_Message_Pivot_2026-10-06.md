# LinkedIn — pivot thông điệp VI / English · 2026-10-06

## Quyết định của Bảo

Bảo xác nhận sau lượt rà artifact: bộ tiếng Việt đang sai hướng cho tệp nội địa, cần build lại. Skeleton đã có được giữ; chuỗi asset sẽ đổi hướng sang English ở task sau. Mandate hiện tại là chuẩn hóa tài liệu và commit local, không thực hiện chuyển ngữ, adaptation, sửa copy khách hàng hoặc tạo ảnh.

**VI nội địa: VI_DOMESTIC_CHANGES_REQUIRED / REBUILD_PENDING.** ERP bán dẫn được đặt như một cầu nối về năng lực quản trị để doanh nghiệp nội địa chuẩn bị tham gia chuỗi cung ứng bán dẫn. Câu chuyện cần đi từ nhu cầu tham gia chuỗi, yêu cầu vận hành của khách hàng, khoảng trống quy trình/dữ liệu đến vai trò phù hợp của ERP. Đây không phải lời hứa mua ERP sẽ đạt chuẩn, vượt audit, được chọn làm vendor hay có đơn hàng.

**English: EN_ADAPTATION_DEFERRED.** Giữ cấu trúc và nội dung vận hành hiện có làm đầu vào cho nhánh English/FDI ở task sau. Chưa có bộ English mới, mapping cuối, script acceptance hoặc artwork acceptance. Không đổi nhãn VI thành EN và không coi dịch nguyên văn là hoàn tất adaptation. Ngôn ngữ không tự chứng minh quyền sở hữu FDI hoặc khả năng tiếp cận audience.

## Evidence và phạm vi kết luận

Lượt kiểm đã rà caption/native headline của 11 carousel trong package 05/10, đọc sâu source copy O3/F1/P2/P3 và case copy, xem 6 ảnh native: ba cold Single image trong journey 06/10, O3 card1, P3 card1/card5. Đây là audit hướng audience/message, không phải kiểm lại mọi chữ của toàn bộ 55 ảnh hoặc nghiệm thu asset English.

| Nhóm hiện có | Finding đối với VI nội địa | Handoff |
|---|---|---|
| O1/O2/O3/O4-O/O4-Q | Mở bằng kiểm thử, trạng thái lô, kết sổ của nhà máy đã vận hành trong ngành | Giữ skeleton cho adaptation nhánh English; VI cần câu chuyện mới |
| F1/F2/F3 | Mở bằng WIP, forecast và gia công của doanh nghiệp thiết kế chip | Giữ làm nguồn nhánh English; không tự coi phù hợp mọi FDI |
| P1/P2 | Nói với nhóm tích hợp/SI, khác doanh nghiệp nội địa muốn thành nhà cung ứng | Task sau phải phân biệt đối tác triển khai với nhà cung ứng công nghiệp |
| P3 | Gần nhu cầu nội địa nhất nhưng dừng ở tìm/đối chiếu hồ sơ; chưa nối vai trò ERP với chuẩn bị vào chuỗi | Có thể reuse nguyên liệu giải thích; không giữ nguyên làm luồng VI đã đạt |
| Ba journey 06/10 | Cold mở bằng kết sổ OSAT, gia công Fabless, chuẩn bị quy trình Partner | Giữ demo cấu trúc; chưa đại diện cho hướng VI nội địa mới |
| Bốn bộ case / 16 card | Chứng cứ theo scope từng case; Pressway/Phẩm Thuyên không chứng minh gia nhập chuỗi bán dẫn nhờ ERP | Rà relevance và scope riêng khi mapping hai nhánh; không mở rộng claim |

Nguồn đối chiếu: [message map nội địa](../drafts/S01_Proof_and_Message.md), [build pack](../ads/linkedin/LinkedIn_Build_Pack.md), [journey matrix](linkedin-journey-demo/2026-10-06/README.md), [RMK generation record](linkedin-rmk-postcheck/2026-10-05/README.md). Bản đối soát email Vy là nguồn nội bộ gián tiếp; email gốc chưa được đọc qua Gmail kết nối. Quyết định pivot hiện hành dựa trên chỉ đạo trực tiếp của Bảo trong phiên này.

## Task sau và acceptance

1. English: map từng nhóm tới người mua và bài toán phù hợp, adapt toàn chuỗi cold → explanation → case, gồm caption, headline, body, CTA, alt, storyboard và destination locale. Review thuật ngữ, proof scope và script trước generation; kiểm native/mobile sau generation. Chưa release task sản xuất này trong checkpoint tài liệu.
2. VI nội địa: build lại hook và hành trình từ trigger chuẩn bị tham gia chuỗi; cho thấy vai trò ERP và cơ chế có nguồn. Không chỉ thêm câu “tham gia chuỗi cung ứng” vào artwork vận hành cũ. CTA hướng tới đánh giá hiện trạng/mức sẵn sàng phù hợp; không cam kết kết quả audit hoặc thương mại.
3. Mọi acceptance trước đây giữ đúng revision và phạm vi đã ghi. Pivot này không xóa kết quả kỹ thuật hoặc sửa lịch sử; acceptance cũ không thay acceptance về audience/message mới.

Format Single image cold → ads-derived member audience → Carousel RMK và trần media 11.700.000 VND không đổi. Không suy pivot thành hai campaign được bật, ngân sách chia sẵn, audience đủ điều kiện hoặc permission live. Landing, tracking, proof rights, harness và asset bytes giữ nguyên.

## Execution contract / docs impact

Outcome: các entry point canonical thống nhất VI cần build lại và English chỉ là handoff task sau; lịch sử/asset được bảo toàn. Owner: root thực hiện bounded documentation mutation theo mandate trực tiếp của Bảo; không spawn/delegate. Kiểm chứng bằng diff chỉ gồm Markdown, banner/link hiện hành, toàn bộ suffix tài liệu cũ giữ nguyên, không đổi ảnh/demo/receipt và staged path scope trước commit.

Docs impact reviewed: CURRENT_STATE, README, kickoff/source brief, S01/S03, LinkedIn_Build_Pack, Pre_Ad_Readiness, demo/human-audit runbook, continuity map, Cold_To_RMK_Data_Plan, Report_Artifact_Index, journey README và direction/budget checkpoint được đồng bộ. S02/S04, proof register, tracking/design-system và HISTORY/LOG không cần sửa: query evidence, measurement/budget, quyền dùng claim và implementation không thay đổi.

Execution: **SUCCESS** cho đồng bộ tài liệu sau kiểm tra 14 banner, link tới quyết định pivot, nội dung tài liệu cũ được bảo toàn (đối chiếu Git với chuẩn hóa LF/CRLF) và diff chỉ có Markdown. Git diff --check đạt; containing local commit là bằng chứng lưu checkpoint. Creative status vẫn VI_DOMESTIC_CHANGES_REQUIRED / EN_ADAPTATION_DEFERRED; không có creative PASS hoặc independent-agent audit mới. Checkpoint chỉ local trên slice/linkedin-audience-ready-research, không merge main hoặc push GitHub.


## Selective integration into local main

Bảo subsequently authorized integrating documentation and pivot only into local main. Source commit: 3ac216490c64712e9fd7ac195d2822f6805449bb. Existing main document content is retained below the new current-status banners; two documentation paths absent from main (direction/budget checkpoint and journey README) are included as documentation references only. No artwork, demo HTML/ZIP, generation receipts, package or other preceding branch commits are imported. Journey/asset links in the retained records refer to the source worktree D:/optimize-awareness-LinkedIn-adcopy and may be absent from main. These records do not assert those assets were merged. Prior source-only/no-main-merge statements describe the original checkpoint. Main Fabless working changes are preserved separately and remain uncommitted.

Docs impact reviewed for integration: current format/budget supersede main previous cold Carousel/35m statements only where explicitly replaced by the new decision; S04 receives a bounded budget reconciliation. No asset or operational release is granted.
