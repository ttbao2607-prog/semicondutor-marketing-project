# Google Search campaign — receipt 2026-11-02 (built Paused, then **ENABLED on 02/11/2026 at Bảo's explicit instruction**)

**Account:** DIGIWIN SOFTWARE VIETNAM. Chrome already signed in; no credential entered. The 18 pre-existing campaigns and other teams' drafts were not touched.

**Mandates (Bảo, 02/11/2026), in order:** (1) set up a draft, stop before publish; include EN/Chinese RSAs per the approved package. (2) Route B (bulk upload), ₫50,000/day, campaign cap ₫500,000, omit SI-framed Supplier headlines, copy verbatim otherwise, `Page views` placeholder goal OK, add 6 `link#section` sitelinks before cloning. (3) Cap = 10 days from the start date (track it); Digiwin may use the customer proofs → add case sitelinks; update repo docs; delete the wizard draft; add brand ad groups and negatives. (4) Review done → **enable**.

## Current state (read back in the UI unless noted)
| Item | Value |
|---|---|
| Campaign | `SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261102]_50.000d-ngay_10d_end20261111` (renamed at go-live; it was `…_PAUSED_REVIEW`). **Enabled · Eligible (Learning)**; ads `Eligible`; Search; Maximize clicks (₫25,000 max CPC set in file, not re-read at capture time — **02/11 follow-up: not saved live, checkbox unchecked**); ₫50,000/day; Google Search Network only; AI Max and final URL expansion off |
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
Google Search has no total-spend cap; the ₫500,000 cap is enforced by dates (₫50,000 × 10 days). *(Capture-time wording, **superseded by the 02/11 follow-up below**: dates alone do not prove a hard cap, and, per the plan's 02/11 source check (not yet re-verified), Google documents campaign total budgets for new Search campaigns only.)* Google may spend up to 2× the daily budget on one day. **If the campaign is paused and restarted, set a new start date and end = start + 9 days.** Checks due: **05/11 (day 3), 09/11 (day 7), 11/11 (last day)** *(labels = elapsed days after 02/11; inclusive-day equivalents are 04/11 and 08/11 — PO schedule unchanged)* — cumulative spend ≤ ₫500,000, search-terms report (negatives, brand overlap), ad/asset disapprovals, whether Chinese-language impressions occur at all.

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

## Follow-up 02/11/2026 — post-audit readback (Claude, Chrome extension, read-only; original record above preserved)
Basis: Codex post-audit plan (commit `077aae9a`) and a fresh readback of the saved campaign. Settings panels were opened and cancelled; nothing was saved; the date-range view was changed to "This month" for reading only.

| Item | Readback |
|---|---|
| Status | Enabled · Eligible (Learning) |
| Budget | average daily ₫50,000 (not a total budget) |
| Dates | 02/11/2026 → 11/11/2026 saved |
| Bidding | Maximize clicks; "Set a maximum cost per click bid limit" **unchecked** (file value ₫25,000 not saved) |
| Budget tooltip / report | "In November, you won't be charged more than ₫1,450,000"; monthly spending limit ₫1.45M, monthly forecast ₫0, cost to date ₫0; ten daily limits of about ₫100K (2× daily) for 02–11/11 |
| Delivery 01–02/11 | 0 impressions, 0 clicks, ₫0 (reporting lag; not performance) |
| Goals / network / AI Max | "Account-default: No goals added"; Google Search Network only; AI Max off, text customization and final URL expansion off; Vietnam (country); English, Chinese (simplified) and 2 more |

Disposition: the ₫500,000 PO cap is not shown to be a hard platform cap (upper bound by the 2× daily limit over ten days is about ₫1.0M — my inference from the chart). **Bảo 02/11:** wants a new campaign with a total budget ₫500,000 (option b), method (copy-and-edit vs rebuild) to be confirmed with him first — nothing created, no pause/enable. CPC ₫25,000 apply/not-apply NOT_CONFIRMED. Not yet done: current Google guidance re-check, full 28 keyword / 24 negative / 16 ad / 96 sitelink inventory, MSG-ANCHOR-01/native review. No raw screenshot archive was saved. Status: CHANGES_REQUIRED; remediation PARTIAL (readback + docs only); independent audit NOT_RUN.

## Follow-up 02/11/2026 (later) — live changes on Bảo's instruction
1. **Max CPC (F2) applied** on the existing campaign: before = checkbox unchecked; after = checked, ₫25,000, Maximize clicks kept; verified after page reload. Recovery route: untick the checkbox and Save.
2. **Copy-paste test (F1 route 1):** the campaign was copied and pasted with "Pause new campaigns after pasting" ticked. Result: new campaign `…_50.000d-ngay_10d_end20261111 #2`, **Paused**, same ad groups, no spend. Its Budget row shows only "average daily budget" — no total-budget option — so copy-paste cannot meet the ₫500,000 total-budget goal. Settings panels were cancelled without saving.
3. The original campaign remains **Enabled** and was NOT paused (Bảo: pause the old campaign only after the new one is ready). `#2` is a paused leftover: remove or reuse is Bảo's decision. Next: fallback (new campaign with total budget, via CSV / wizard + copy of ad groups), pending Bảo's confirmation of start/end dates and naming; assets/negatives/sitelinks must be re-verified on the new campaign. Status: PARTIAL; independent audit NOT_RUN.

## Follow-up 02/11/2026 (final) — new total-budget campaign, old one paused
Mandate: Bảo (new campaign with total budget; start 03/11; pause the old campaign once the new one is enabled; try copy-paste first, CSV as fallback). Claude via Chrome extension. A "Confirm it's you" passkey prompt appeared mid-way; Bảo completed it himself.

| Item | Result |
|---|---|
| Route | Copy-paste of the campaign could not set a total budget → used the Create-campaign wizard (Search, no goal guidance, new campaign, not the other team's draft) |
| New campaign | `SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261103]_500.000d-tong_10d_end20261112`; **Enabled, status Pending (starts 03/11)**; budget **Campaign total ₫500,000**, 03/11→12/11/2026 |
| Settings read back | Maximize clicks, max CPC ₫25,000; Google Search Network only (Partners/Display off); Vietnam (country, presence option); English, Vietnamese, Chinese (simplified), Chinese (traditional); AI Max off, text customization and final URL expansion off; automatically created assets off; campaign URL options empty; goal = campaign-specific `Page views` (deviation: the old campaign had Account-default/no goals) |
| Content | Wizard needed one ad group, so a temporary "Ad group 1" (3 headlines / 2 descriptions, 2 keywords) was created; the 16 ad groups of the paused copy `#2` were pasted in, then the temporary one was removed (permanent removal, confirmed) |
| Counts (UI pagination) | 16 ad groups, 28 keywords, 16 ads, 96 sitelink associations; ads show Pending/under review — not an approval claim |
| Negatives | Not carried by ad-group paste (0 after paste). Added 25 phrase-match negatives at campaign level = full distinct union of `06_Google/Loai_tru` (7 vi + 5 en + 7 zh-Hans + 6 zh-Hant after removing the shared 股票). The old campaign shows 24; one source term is missing there (not identified) |
| Old campaign | `…[20261102]_50.000d-ngay_10d_end20261111` set **Paused** after the new one was published; cost ₫0 (no delivery 01–02/11) |
| Paused copy `#2` | `…_end20261111 #2` — Paused at capture time; **later removed** at Bảo's instruction (see the last follow-up) |

Incidents: the wizard showed "Changes failed to save" after the passkey prompt and the Review step showed reverted settings (all countries, AI Max on, no ad); the draft was reloaded, inspected, the missing keywords/ad re-entered, and settings re-verified before Publish. Publishing opened a "Set up with a Google Tag" page — not used (no tag/conversion change). A saved "Keyword text contains AI" view filter was removed from the keywords view for reading only. Chrome screenshot timeouts occurred several times; text/element reads were used instead.

Not done / unknown: delivery and actual spend (campaign starts 03/11; check cumulative spend against ₫500,000 and the Budget report after the first day); item-by-item diff of ad copy, sitelink URLs and UTM suffix versus the old campaign; re-check of Google's current total-budget guidance (source from the plan's 02/11 check, not re-verified by me); brand-overlap check; MSG-ANCHOR-01 / native review (NOT_RUN, copy copied verbatim). No checkpoints were scheduled (see the last follow-up). Execution: PARTIAL; independent audit NOT_RUN; this does not close the earlier CHANGES_REQUIRED.

## Follow-up 02/11/2026 (last) — decisions by Bảo
1. Copy `#2` **removed** (permanent). Done via that campaign's own settings page (status → Removed → Confirm), after the list-selection route could not be verified visually.
2. No scheduled checks, reminders or automation. Bảo opens Google Ads manually; this repo only keeps a handoff for future agents: `HANDOFF_FUTURE_AGENTS.md` in this folder.
3. Goal `Page views` kept on the new campaign: awareness / Maximize-clicks run, not optimizing for lead conversions. It does not steer bidding under Maximize clicks; treat it as reporting only (not a lead conversion; the form/`accepted_form` success event is not verified).

## Follow-up 03/11/2026 — start-date live readback (Gemini via Chrome CDP, read-only)
Mandate: Bảo (check daily to-do / readback Google Search status on campaign start date 03/11/2026 ~10:30 +07:00).
Inspected live via Chrome CDP on port 9340 (read-only; no UI changes saved or submitted).

| Item | Result |
|---|---|
| Live campaign | `SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261103]_500.000d-tong_10d_end20261112` |
| Platform status | **Enabled** · **Eligible (Limited)** with sub-label *Limited by bid strategy* (Google recommends target ROAS / value bidding; normal and expected under Maximize clicks with CPC cap) |
| Budget & dates | **Campaign total: ₫500,000**; start Nov 3, 2026, end Nov 12, 2026 |
| Bidding settings | **Maximize clicks**; "Set a maximum cost per click bid limit" is **checked**, value = **₫25,000** |
| Ads approval | **16/16 RSAs are Eligible (Approved)** (0 Disapproved, 0 Pending/under review). Ad strengths: 1 Excellent, 1 Good, 8 Average, 6 Poor |
| Keywords (28 total) | Exactly **4 Eligible**: `"PCB manufacturing ERP"`, `"PCB制造ERP"`, `"半导体封装测试 MES"`, `[semiconductor test data management]`; **24 Not eligible / Low search volume** (F3 unchanged; low search volume is not zero demand) |
| Negatives | Exactly **25 phrase-match negatives** active at campaign level (full union of `06_Google/Loai_tru`) |
| Assets / Sitelinks | **115 total asset associations** active; sitelinks are **Eligible** |
| Day-1 morning delivery | **0 impressions, 0 clicks, ₫0 cost** (expected morning reporting lag on start date; not a performance conclusion) |
| Old campaign | `SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261102]_50.000d-ngay_10d_end20261111` confirmed **Paused** (16 ad groups, cost ₫0) |
| Paused copy `#2` | Confirmed **Removed** |

Notes & deviations:
- Playwright MCP directly failed on large DOM responses (>1MB frame size); direct Node.js CDP WebSocket script via port 9340 was used to inspect settings safely and read-only.
- All 16 RSAs have cleared Google editorial review on start date.
- The ₫25,000 max CPC checkbox is confirmed active in live bidding configuration.
- Still open / unobserved: practical delivery pacing and budget cap behavior over the 10-day run; MSG-ANCHOR-01 and native review (NOT_RUN, copy retained from build sheet); independent audit NOT_RUN.

