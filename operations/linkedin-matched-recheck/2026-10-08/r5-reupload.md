# R5 re-upload recovery — 08/10/2026

## Current instruction and target

Bảo directs **try re-upload first; contact LinkedIn Support only if recovery still fails**. Discovery mapping recovery concerns the original company-provided424-row list, not R5. This mandate changes only the R5 recovery sequence; it does not authorize a Discovery upload, campaign delivery, new targeting save or changes to the52-company source.

Target: existing **TEST-AUD-CONTINGENCY-TRUE-ONLY-R5-52**, using its Edit list audience form. No duplicate audience or deletion planned. Same source CSV from the contingency checkpoint,52 rows/10 template columns,5302bytes; SHA256 **fe730e1bff87c0295d820ebbf8763f5e42e64c48d0d1dc72c07409083c4bbb34** reverified before selection. File contents/name and audience name/type unchanged.

## Prepared UI state and completed submission

Existing R5 retained the prior filename. Removed the selected file only inside the unsaved Edit form, then selected the identical approved CSV through the file chooser. LinkedIn reports **Processing complete. Company list ready for upload.** This is file validation, not a completed server audience update or mapping recovery.

The final button **Agree & Update** explicitly accepts Ads Agreement. Bảo gave action-time confirmation: **“Xác nhận Ads Agreement, cập nhật R5”**. Root clicked it **exactly once**. At approximately **14:25 Asia/Saigon on08/10**, LinkedIn displayed **“Your audience has been successfully updated.”** Success toast is retained privately. **SUBMITTED_ONCE / UPDATE_SUCCESS / SAVED_FILENAME_VERIFIED** supersedes the earlier pending form state.

After reload, the same existing R5 row remained **Ready />90% /444,274 members**, last modified **08/10/2026**, active ad sets `-`. Read-only reopening of Edit confirmed **TEST-AUD-CONTINGENCY-TRUE-ONLY-R5-52.csv** persisted; **Cancel** exited without another submission. Details/Matched immediately after retry still showed **0 Companies /Matched0 /Unmatched0**. No intermediate Updating state was observed. This proves update acceptance and the immediate mapping gap, not successful mapping recovery or backend reprocessing cause. The pre-retry count444,392 and post-retry count444,274 are separate observations; no causal explanation asserted.

UI now says upload between10000–300000companies while accepting this52-row file for validation. This is a recorded UI/acceptance discrepancy, not a universal row-count exception. No padding or source changes made.

## Completion criteria and follow-up

Submission criteria are complete: one update, success toast, reload, changed modification date, saved filename readback and immediate Details check. Mapping recovery remains **INSUFFICIENT_EVIDENCE**. Keep the uploader's up-to48-hours/rarely-longer warning separate from its current Ready state; no guaranteed mapping timing is inferred. Record a proposed read-only checkpoint **09/10/2026 at or after14:25 Asia/Saigon** (24h after retry), consistent with the previous24h recheck cadence. If platform processing is then ongoing, retain pending state rather than declare retry failure. No repeated automatic upload.

If a settled recheck still has no mapping, proceed to LinkedIn Support under Bảo's conditional instruction, with sanitized summary/Details contradiction. Support communication has not been sent. No automatic follow-up is scheduled; the timestamp is a recorded checkpoint, not an active reminder. Discovery mapping findings and pre-retry R5 observations remain in the [historical recheck receipt](README.md).

Private UI evidence: `D:/LinkedIn_Closeout_Private_2026-10-05/r5-reupload-2026-10-08`; public Git excludes screenshots/account identifiers/company tables. [Sanitized retry manifest](r5-reupload.json) pins its private evidence. Existing browser tab returned to the Matched table; all4 previous audiences retained. No duplicate created, deletion, campaign attachment, targeting save, enable or spend.

Execution **PARTIAL** for mapping recovery: the authorized re-upload itself is complete; fresh mapping unresolved. Mapping audit **INSUFFICIENT_EVIDENCE**. Root self-review only. DOCS_IMPACT_MAP reviewed; current audience notices synchronized, dated recheck evidence preserved. Working files on `slice/linkedin-matched-recheck-2026-10-08`, not staged/committed/main-merged/pushed.
