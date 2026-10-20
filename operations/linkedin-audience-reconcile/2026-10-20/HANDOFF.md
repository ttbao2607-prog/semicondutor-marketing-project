# HANDOFF — LinkedIn Discovery audience, P7 readback + v4 upload — 20/10/2026

Executor: Claude solo, AUDIT_MODE=SELF. Account Campaign Manager của Digiwin (Active). Chi tiết bằng chứng: [README.md](README.md). Cycle trước: [repair-cycle-2](../2026-10-12/repair-cycle-2/README.md).

## Trạng thái một dòng

**Execution PARTIAL · v4 đã upload lên audience mới · P7 cho v4 NOT_DONE (Details đang 0/0) · Audit INSUFFICIENT_EVIDENCE · Discovery cũ CHANGES_REQUIRED · R5 mapping OK.**

## Fact (đã đọc trực tiếp trên LinkedIn, 20/10)

| Audience | Matched / Unmatched | Ghi chú |
|---|---|---|
| TEST-AUD-CONTINGENCY-TRUE-ONLY-R5-52 | 52 / 0 | Mapping khôi phục (8/10 từng 0/0/0). |
| TEST-AUD-COMPANY-LIST-DISCOVERY-202610 | 135 / 93 | ≈47/135 (~35%) khớp sai đơn vị (self-audit theo tên). 85/93 unmatched là tồn dư các lần upload cũ (9/30, 10/6, 10/8); chỉ 7 thuộc upload 12/10. Các dòng dấu 12/10 chỉ 142 so với 310 dòng v3 (chưa giải thích). |
| TEST-AUD-CONTINGENCY-MASTER-203-20261006 | 178 / 13 | Chưa đánh giá chất lượng khớp. |
| VN_ERP_Partners_List_01 | không đọc Details | Không thuộc scope; 1 ad set đang gắn. |
| **TEST-AUD-COMPANY-LIST-DISCOVERY-202610-V4** (mới) | **0 / 0 (chưa xử lý)** | Ready, 782,059 members, tạo 20/10. |

## Hành động ghi đã thực hiện (live account)

- Một lần tạo audience mới V4 (Company list) từ `linkedin_discovery_v4_20261020_PROPOSED_NOT_UPLOADED.csv`: 263 dòng = v3 (310) trừ 47 dòng khớp sai; sha256 `5c0c5d9ce9580d0c60c0787403395f544a73087cf3e6bfb6a0ccee31cf65cccc`. Mandate: Bảo chọn "Tạo audience mới" trong chat; Agree and upload bấm đúng một lần.
- Không sửa audience nào khác; không gắn ad set, không enable, không spend, không đổi campaign/creative/tracking. Không push.
- CSV v4, changelog, danh sách tên và mọi tên công ty ở kho private `D:/LinkedIn_Closeout_Private_2026-10-05/discovery-repair-cycle-2026-10-12/`; không vào Git.

## Unknown

- Matched/unmatched và chất lượng khớp thực của V4 (chờ LinkedIn xử lý, có thể tới 48h).
- Vì sao v3 310 dòng chỉ còn 142 dòng dấu 12/10 trên audience cũ; dialog nhận 263 dòng dù ghi "10,000–300,000".
- Tỷ lệ khớp sai chính xác (47 là phân loại thủ công; cần đối chiếu CSV private).
- Chất lượng MASTER-203; tab Saved.

## Next action (chỉ đọc, không upload lặp)

1. **Từ 21/10** (sau giờ upload; tối đa ~22/10): đọc Details V4 → Matched/Unmatched, so với 263 dòng, rà 3 trang matched tìm khớp sai (đối chiếu cột input với Page).
2. Ghi receipt P7 cho v4, chạy documentation sync gate, kết luận PASS / CHANGES_REQUIRED / INSUFFICIENT_EVIDENCE.
3. Nếu V4 vẫn 0/0 sau khi settled: báo Bảo; theo chỉ đạo 8/10, LinkedIn Support cần Bảo xác nhận riêng (gửi message ra ngoài).

## Quyết định chờ Bảo (L2)

Dùng audience nào cho ads (V4, R5, MASTER-203 hay Discovery cũ): **để sau khi P7 của V4 có kết quả**, theo chỉ đạo của Bảo ngày 20/10.

## Docs impact

Canonical notices về audience (CURRENT_STATE.md, README.md và các entrypoint đã sync ở cycle 12/10) **chưa cập nhật**: chúng còn ghi Discovery "Updating"/P7 chưa làm. Cập nhật sau khi P7 của V4 có kết luận, để tránh sync hai lần với trạng thái chưa ổn định. Docs impact reviewed: receipt này là lịch sử/evidence, không thay canonical; cần sync canonical ở bước P7.
