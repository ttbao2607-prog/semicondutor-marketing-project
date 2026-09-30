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

- Operations-map tabs must update the selected tab, its associated diagram and inspector together. Each pain card selects its matching progress/lot/cost view and scrolls to `fabless-map`; expand the mobile detail before scrolling. Preserve arrow/Home/End tab navigation and Enter/Space card activation. Dynamic map text follows the selected locale. The 2026-09-30 local repair is a candidate only; production still needs a separately authorized existing-page revision.

- Use a responsive outsourced-WIP handoff flow: `FORECAST > OUTSOURCE > LOT/DATECODE/BIN > COST REVIEW`.
- Make ownership boundaries visually explicit with labels and connecting lines; do not imitate a live dashboard.
- Use two consultation CTAs, one in the hero and one after the final route explanation. The frozen HTML CTAs are inert/provider-free and use stable IDs. Any future PopupX behavior belongs to an authorized operator handoff. Do not emit a CTA analytics event until live GTM inventory authorizes reuse.
- For the local mobile compact candidate below 701px, show the four-step outsourced flow in the main reading path and allow the detailed operations map to open on demand. A pain card must reveal the map before selecting its matching view. Keep proof/source links, section IDs, both CTA IDs and the approved desktop composition; this rule does not authorize a live publish.

---

## Page-Specific Components

- Forecast signal card, partner handoff rail, lot/datecode context card and source-safe contact strip.

---

## Recommendations

- Preserve whitespace and a short scan path; do not turn the page into a feature catalogue.
