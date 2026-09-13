# Osat Route Page Overrides

> **PROJECT:** Digiwin Semiconductor Marketing
> **Generated:** 2026-09-13 11:28:37
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

- **Route diagram accent:** `#0891B2` (cyan). CTA remains the Master orange.

### Component Overrides

- Use a static, responsive lot-trace rail instead of a generic feature grid: `LOT > TEST > QUALITY/4M1E > WIP > COST REVIEW`.
- The diagram is explanatory, not a product screenshot or performance claim. It must be understandable without animation and must stack vertically on mobile.
- Use two consultation CTAs, one in the hero and one after the mechanism/proof-safe section. Both call `OpenformWF2`; OSAT preserves `osat_cta_click` with `cta_location=hero|terminal`.

---

## Page-Specific Components

- Lot identity chip, trace rail, exception-review card and a source-safe contact strip.

---

## Recommendations

- Keep the primary story centered on traceability questions and review handoffs, not a dense dashboard.
- Never add loading skeletons, spinners or drag interactions to this static landing page.
