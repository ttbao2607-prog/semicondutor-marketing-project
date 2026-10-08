> **Partner / Supplier — PO clarification 2026-10-07 · docs checkpoint trên main local.** Partner trong paid scope hiện hành là **nhà cung ứng công nghiệp trong chuỗi bán dẫn/điện tử** (PCB, substrate, linh kiện, vật liệu đóng gói, gia công chính xác cho thiết bị), không mặc định là SI/đối tác phần mềm. [LDP Partner Google Ads đã được duyệt là content anchor](../../../operations/linkedin-safe-batches/parallel-partner-2026-10-07/partner-ldp-content-anchor-v1.md); giữ đúng audience, bài toán nhà máy, vai trò ERP/iMES/dữ liệu thiết bị và scope từng claim/case. P1/P2 hiện là nguồn persona SI, P3 là nguồn nội địa: phải adapt và review mới trước FDI generation, không kế thừa PASS. Snapshot cũ giữ nghĩa lịch sử. Scope docs ambiguity từ source checkpoint 8d94be6 được tích hợp chọn lọc; chưa push.

# Partner Route Page Overrides

> **PROJECT:** Digiwin Semiconductor Marketing
> **Generated:** 2026-09-13 11:28:46
> **Page Type:** Landing / Marketing

> ⚠️ **IMPORTANT:** Rules in this file **override** the Master file (`design-system/MASTER.md`).
> Only deviations from the Master are documented here. For all other rules, refer to the Master.

---

## Page-Specific Rules

### Layout Overrides

- **Max Width:** 1200px
- **Layout:** Responsive grid

### Spacing Overrides

- No overrides — use Master spacing

### Typography Overrides

- No overrides — use Master typography

### Color Overrides

- **Route diagram accent:** `#0F766E` (teal). CTA remains the Master orange.

### Component Overrides

- Use a three-layer integration map: `ERP context > MES execution > OT signals`, with ownership and handoff notes alongside it.
- Present the map as an architecture hypothesis for discovery, never as a verified integration or live product screen.
- **Product-owner exception (2026-09-24):** Supplier/Partner has one consultation CTA only. Reuse the fixed top-header control, relabel it exactly `Tư Vấn`, and freeze it as the inert/provider-free button `partner-cta-header`. Remove the added orange hero and architecture controls. The original hero navigation actions remain. Do not attach PopupX/provider behavior in HTML; the bridge marks this one selector for the later authorized operator handoff. Do not emit CTA analytics.
- For the local mobile compact candidate below 701px, keep the ERP → MES → OT ownership summary visible and allow the full architecture simulation to open on demand. Audience cards must reveal the detailed architecture when activated. Keep proof/source links, section IDs, the approved desktop composition and the single header consultation CTA; this rule does not authorize a live publish.

---

## Page-Specific Components

- Layered architecture map, ownership markers, discovery boundary note and source-safe contact strip.

---

## Recommendations

- Keep system layers legible at 375px by stacking them in DOM order; avoid tiny node labels and decorative complexity.
