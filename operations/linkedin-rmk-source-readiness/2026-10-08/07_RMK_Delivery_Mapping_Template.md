# 07 · RMK delivery mapping — template

Status: TEMPLATE / NOT FILLED. The CSV next to this file is **header only**: no RMK audience or RMK ad exists yet, so there are no IDs or counts. Rows with real IDs stay private and are not committed.

Purpose: record the RMK side separately from the cold source registry ([02](02_RMK_Source_Registry_Template.md)), so that every ID and UTM value on one row belongs to the same set of ads. One row per RMK ad.

| Field | What to enter | Rule |
|---|---|---|
| `rmk_ad_id`, `rmk_creative_id` | IDs of the RMK ad | Exact platform IDs |
| `rmk_campaign_id`, `rmk_ad_set_id` | IDs of the RMK campaign and ad set | RMK delivery only |
| `rmk_audience_id` | The RMK audience this ad targets | Created from one cold source |
| `source_id` | The `source_id` of the **cold** registry row the audience came from | Foreign key to [02](02_RMK_Source_Registry_Template.md); no copying of cold IDs into this row |
| `treatment`, `locale` | Treatment (O1…P3) and locale of the creative | Matches [04](04_Reader_Entry_Mapping_Draft.md) |
| `utm_campaign_value`, `utm_content_value` | The exact UTM values on this RMK ad's reader link (`..._rmk_<wave>` pattern, creative-level content) | Same pattern rules as [04](04_Reader_Entry_Mapping_Draft.md); no cohort or company detail in URLs |
| `objective` | RMK objective chosen at release (Engagement or click to the reader) | From decision R4 in [01](01_RMK_Source_Rule_Decision_Pack.md) |
| `released_at`, `timezone`, `approved_by` | When it was released and by whom | Only after the release gate in [03](03_RMK_Fallback_Decision_Tree.md) passes |
| `notes` | Anything that changes interpretation | e.g. paused, audience re-processed |

Readback rows in [05](05_Week1_Readback_Template.md) use `source_cohort_id` = the registry `source_id`, and `ad_id`/`creative_id` = the delivery IDs of the ad in that row (a cold ad from [02](02_RMK_Source_Registry_Template.md) or an RMK ad from this table), with `stage` saying which.
