# Fabless Route Page Overrides

> **PROJECT:** Digiwin Semiconductor Marketing
> **Generated:** 2026-09-13 11:28:45
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

- **Route diagram accent:** `#4F46E5` (indigo). CTA remains the Master orange.

### Component Overrides

- Use a responsive outsourced-WIP handoff flow: `FORECAST > OUTSOURCE > LOT/DATECODE/BIN > COST REVIEW`.
- Make ownership boundaries visually explicit with labels and connecting lines; do not imitate a live dashboard.
- Use two consultation CTAs, one in the hero and one after the final route explanation. Both call `OpenformWF2`; neither emits a new CTA analytics event before GTM inventory.

---

## Page-Specific Components

- Forecast signal card, partner handoff rail, lot/datecode context card and source-safe contact strip.

---

## Recommendations

- Preserve whitespace and a short scan path; do not turn the page into a feature catalogue.
