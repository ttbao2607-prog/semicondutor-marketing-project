# Google Search campaign — receipt 2026-11-02 (built Paused, then **ENABLED on 02/11/2026 at Bảo's explicit instruction**)

**Account:** DIGIWIN SOFTWARE VIETNAM. Chrome already signed in; no credential entered. The 18 pre-existing campaigns and other teams' drafts were not touched.

**Mandates (Bảo, 02/11/2026), in order:** (1) set up a draft, stop before publish; include EN/Chinese RSAs per the approved package. (2) Route B (bulk upload), ₫50,000/day, campaign cap ₫500,000, omit SI-framed Supplier headlines, copy verbatim otherwise, `Page views` placeholder goal OK, add 6 `link#section` sitelinks before cloning. (3) Cap = 10 days from the start date (track it); Digiwin may use the customer proofs → add case sitelinks; update repo docs; delete the wizard draft; add brand ad groups and negatives. (4) Review done → **enable**.

## Current state (read back in the UI unless noted)
| Item | Value |
|---|---|
| Campaign | `SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261102]_50.000d-ngay_10d_end20261111` (renamed at go-live; it was `…_PAUSED_REVIEW`). **Enabled · Eligible (Learning)**; ads `Eligible`; Search; Maximize clicks (₫25,000 max CPC set in file, not re-read); ₫50,000/day; Google Search Network only; AI Max and final URL expansion off |
| Dates | **Start 02/11/2026, end 11/11/2026** (10 days inclusive; auto-stops 11/11). The "campaign is ending soon" banner is this end date |
| Location / languages | Vietnam (presence option saved, saved value not re-read) / Vietnamese, English, Chinese (simplified), Chinese (traditional) — both set manually (upload columns were ignored) |
| Ad groups (16) | 12 segment: `OSAT_LOT_TEST`, `FABLESS_OUTSOURCE_WIP`, `ERP_MES_OT_PARTNER` × `vi/en/zh-Hans/zh-Hant`; 4 brand: `BRAND_DIGIWIN_<locale>` |
| Keywords (28) | segment groups: 2 each (1 phrase + 1 exact) from approved package `06_Google/Tu_khoa`; brand groups: the plan's brand keyword, exact |
| Negatives (24) | distinct terms of `06_Google/Loai_tru` (4 locales), **campaign level, phrase match** (plan left match type open) |
| RSAs (16) | verbatim build-sheet copy (segment) / composed from approved copy + brand name (brand); Ad strength read for 10 of 16 (table virtualized): OSAT vi Poor, OSAT zh-Hans Poor, Supplier vi Poor, Supplier en Poor, Fabless vi Average, Fabless en Good, Fabless zh-Hans Good, 3 brand Pending |
| Sitelinks (96) | segment groups: 7 each = 6 section links + 1 customer-case link (OSAT `#cas-ic-case`, Fabless `#bright-power-case`, Supplier `#supply-chain`); brand groups: 3 each → OSAT / Fabless / Supplier pages; wording from live LDP headings |
| URL suffix | `utm_source=google&utm_medium=cpc&utm_campaign=vn_semiconductor_search_p1&utm_content=<seg>_<lang>_{rsa_v1|sitelink}&utm_term={keyword}` |
| Spend since go-live | not yet read |

Files in `upload-files/`: `01_campaign_adgroups_keywords_rsa.csv` (49 valid rows applied; its 72 sitelink rows were rejected and re-sent as 02), `02_sitelinks_applied.csv` (72), `03_case_sitelinks_applied.csv` (12), `04_brand_adgroups_kw_rsa_applied.csv` (12), `05_brand_sitelinks_applied.csv` (12), `build_csv.py`, `case_sitelinks.py`, `brand_neg.py`. (Negatives from `brand_neg.py` were rejected as a file upload — `Negative Phrase` is invalid in Criterion Type — and entered in the UI instead.)

## Tracking (Bảo's 10-day cap)
Google Search has no total-spend cap; the ₫500,000 cap is enforced by dates (₫50,000 × 10 days). Google may spend up to 2× the daily budget on one day. **If the campaign is paused and restarted, set a new start date and end = start + 9 days.** Checks due: **05/11 (day 3), 09/11 (day 7), 11/11 (last day)** — cumulative spend ≤ ₫500,000, search-terms report (negatives, brand overlap), ad/asset disapprovals, whether Chinese-language impressions occur at all.

## Decisions and deviations from the build sheet
- 9 SI/partner-implementer headlines omitted in `ERP_MES_OT_PARTNER` (PO clarification 07/10). Remaining per group: vi 11, en 8, zh-Hans 10, zh-Hant 10. Bảo approved.
- Keywords from the approved package (2 per group), not the longer build-sheet lists.
- Proof sitelinks added after Bảo confirmed proof-use rights (Jiangsu CAS IC, Bright Power, Wafer Works); recorded as a PO statement in `operations/Public_Source_Register.md`, no rights document in the repo. The Bright Power description omits "48h → 02h" (documented source stub has no figures; the live LDP heading does) — restore if Bảo clears the figure.
- **Brand — set by Claude, not specified in the plan** (plan gave only the keywords; "route unresolved"): final URL = OSAT page of the same locale; RSA text = approved build-sheet text + brand name (no 车规级 line); 3 sitelinks to the three LDPs. Brand overlap with other campaigns in this account bidding on "Digiwin" **not checked**.
- Wizard draft (OSAT/vi only) discarded; only that row was selected; 3 other drafts remain.

## Open (go-live is a PO decision, not a readiness PASS)
- MSG-ANCHOR-01 and native review (EN/zh-Hans/zh-Hant): **NOT_RUN / INSUFFICIENT_EVIDENCE**. Bảo's 02/10 first-mention rule: copy not reworded.
- Build-sheet claims kept verbatim, flagged: 车规级/車規級 (automotive-grade), "40年", "实时/Real-time", "verified".
- Conversion goal: the uploaded campaign shows "Account-default: No goals added" (Maximize clicks, so no bidding impact).
- Live-page defect: zh-Hans Fabless `management-layers` heading contains traditional characters; own simplified wording used in the sitelink.

## Incidents (no live/published object affected)
1. In the wizard, a click on the ⋮ menu hit "Remove" and deleted the first ad group draft; rebuilt. 2. A Tab keystroke in the sitelink dialog put a URL string into keyboard-shortcut mode; closed, no change. 3. One click toggled "different final URL for mobile"; reverted. 4. First upload attempt: Location/Languages/sitelink columns not recognised; fixed manually/with a corrected file.

## Docs synchronized for this state
`CURRENT_STATE.md`, `README.md`, `ads/google/Google_Search_Build_Sheet.md` (current-state banner), `operations/Pre_Ad_Readiness_Plan.md`, `operations/Pre_Ad_Readiness_Index_2026-10-28.md` (S01 row), `operations/Public_Source_Register.md` (proof-use statement), `drafts/S04_Measurement_and_Budget.md` (budget). Older "offline draft / no remote campaign / paused" statements elsewhere remain as dated history.
