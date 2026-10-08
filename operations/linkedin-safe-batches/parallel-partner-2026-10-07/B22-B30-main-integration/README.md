# Partner — selected main integration · 08/10/2026

Theo yêu cầu Bảo: checkpoint nguồn `f17530577bd8f63654900ed72ad2b3ebb3d1eca9`, chọn **8 bộ / 80 PNG final và 8 reader**, tích hợp main local. Source branch giữ toàn bộ lịch sử sản xuất; không merge nguyên nhánh vì chứa bản lỗi/raw/pending và docs cũ.

| Bộ | Viewer | Reader | PNG |
|---|---|---|---|
| B22-en-p1-v1 | [Viewer](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B22-en-p1-v1/supplier-v7/index.html) | [Reader](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B22-en-p1-v1/supplier-v7/case-reader.html) | 10 |
| B23-zh-Hans-p1-v1 | [Viewer](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B23-zh-Hans-p1-v1/index.html) | [Reader](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B23-zh-Hans-p1-v1/case-reader.html) | 10 |
| B25-en-p2-v1 | [Viewer](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B25-en-p2-v1/index.html) | [Reader](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B25-en-p2-v1/case-reader.html) | 10 |
| B26-zh-Hans-p2-v1 | [Viewer](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B26-zh-Hans-p2-v1/index.html) | [Reader](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B26-zh-Hans-p2-v1/case-reader.html) | 10 |
| B27-zh-Hant-p2-v1 | [Viewer](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B27-zh-Hant-p2-v1/index.html) | [Reader](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B27-zh-Hant-p2-v1/case-reader.html) | 10 |
| B28-en-p3-v1 | [Viewer](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B28-en-p3-v1/index.html) | [Reader](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B28-en-p3-v1/case-reader.html) | 10 |
| B29-zh-Hans-p3-v1 | [Viewer](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B29-zh-Hans-p3-v1/index.html) | [Reader](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B29-zh-Hans-p3-v1/case-reader.html) | 10 |
| B30-zh-Hant-p3-v1 | [Viewer](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B30-zh-Hant-p3-v1/index.html) | [Reader](../../../../deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/B30-zh-Hant-p3-v1/case-reader.html) | 10 |

**B24 chưa nhập main:** proof P3 thiếu category/sequence, được xác nhận khi rà B27. Receipt PASS cũ mâu thuẫn với ảnh thực; sửa P3 chỉ được chọn và đóng ở B27. Không đổi receipt lịch sử hoặc nhận PASS hồi tố cho B24.

Các bộ trên giữ kết quả root SELF_REVIEW: native + desktop + actual434px + feed333 theo chấp thuận từng batch; **390px chưa xác minh**. Không chứng nhận independent/native-market/live. Wafer Works / 合晶科技 là một case silicon-materials Taiwan/Shanghai; vai trò tư vấn/triển khai Digiwin Việt Nam được quy nguồn riêng.

[Manifest chọn lọc, source hash, anchor và phạm vi](approved-selected-evidence.json). Archive `source-reviews/` giữ nguyên byte các final/native/render receipts và finding. Các đường dẫn source-only trong receipt/README/manifest phải đọc ở checkpoint nguồn nêu trên, không phải dependency chạy viewer trên main. Status pending lịch sử trong manifest không thay final postgen verdict; B24 exclusion áp dụng trên old PASS.

Docs impact reviewed: đồng bộ trạng thái Partner ở các entrypoint current/build/readiness/index/plan; source brief, proof framing và frozen anchor/guard/process không đổi. Adapter DEVELOPING / NOT_FROZEN. Không push hoặc live action.
