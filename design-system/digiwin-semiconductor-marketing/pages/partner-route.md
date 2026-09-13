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
- Use two consultation CTAs, one in the hero and one after the architecture/handoff section. Both call `OpenformWF2`; neither emits a new CTA analytics event before GTM inventory.

---

## Page-Specific Components

- Layered architecture map, ownership markers, discovery boundary note and source-safe contact strip.

---

## Recommendations

- Keep system layers legible at 375px by stacking them in DOM order; avoid tiny node labels and decorative complexity.
