# 02 · RMK source registry — template

Status: TEMPLATE / NOT FILLED. The CSV next to this file is **header only**: no campaign exists, so there are no real IDs, delivery rows or member counts. Do not put historical test-campaign numbers in it (they are not baseline for the new campaign). Registry rows that hold real IDs or account data stay private and are not committed to the public repository; this template carries field names only.

Fill one row per **source cohort** at the moment the exact cold release exists, before any RMK audience is created.

| Field | What to enter | Rule |
|---|---|---|
| `source_id` | Short local label for the cohort (e.g. `COLD-W1-A`) | Unique, no PII |
| `campaign_id`, `ad_set_id`, `creative_ids` | IDs of the new cold release copied from the platform | Only exact new cold IDs; never Page, organic or unrelated campaigns |
| `stage` | `cold` for the source cohort; `rmk` for a derived RMK audience, with the originating cold `source_id` in `notes` | Keeps stages apart |
| `utm_campaign_value`, `utm_content_values` | The exact UTM values used on the reader links of these ads (see [04](04_Reader_Entry_Mapping_Draft.md)) | Links ad IDs to reader sessions; no cohort or company detail in URLs |
| `format` | Single image (Brand awareness) | Must match the decided route |
| `content_revision` | Journey/creative revision and treatment (O1…P3, locale) | Pin so slices with different scope are not merged |
| `targeting_revision` | Company list file name/hash revision, location, functions, seniority | Record the version actually used |
| `interaction_rule` | R1 decision (A/B) | From [decision pack](01_RMK_Source_Rule_Decision_Pack.md) |
| `lookback_days` | R2 decision | Same |
| `pool_structure` | R3 decision | Same |
| `owner` | Person responsible | Named |
| `approved_scope` | What this cohort may be used for | Approved by Bảo |
| `observed_at`, `timezone` | Date/time of each readback and account timezone | Fresh status each time |
| `audience_status` | Processing / Ready / not created | As displayed |
| `displayed_members` | Count shown by the platform | List-level number, not unique matched people |
| `filtered_reachable` | Reachable members after filters in the UI | Gate: at least 300 |
| `eligible` | yes / no / UNKNOWN | UNKNOWN until read |
| `notes` | Anything that could change interpretation | e.g. delivery paused, version change |

Rules that apply to every row: do not predict pool size from CTR × reach; do not add unique audiences across creatives; do not fill zero where nothing was observed (write UNKNOWN); no synthetic or test visits in paid results.

Related: [fallback decision tree](03_RMK_Fallback_Decision_Tree.md) · [week 1 readback template](05_Week1_Readback_Template.md).
