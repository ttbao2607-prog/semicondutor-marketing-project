# F1/F2 — schedule activated 29/10/2026

Outcome: SCHEDULE_ACTIVATED / FUTURE_START. Bảo explicitly authorized enabling this campaign and then confirmed the current LinkedIn Ads Agreement/Advertising Guidelines at the final action. Root performed the UI workflow and self-reviewed readback; no delegation or independent audit claimed.

## Observed account state

- Existing parent VALIDATION_ONLY_VN_SEMICONDUCTOR_ABM_2026-09-14: Paused → Active, saved and read back.
- Exact ad set DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH: Draft/Off → On, status “Not delivering — Scheduled”. Historical draft name retained for identity continuity; it no longer describes current authority/state.
- LI-wave01-F1-en-COLD-v1 and LI-wave01-F2-en-COLD-v1: both On / Active in ads table after launch. Success modal separately stated “Your ads are being reviewed”. No final policy approval or actual delivery inferred from these labels.
- Daily budget USD10 shared across two cold ads. Saved platform dates 01–07/11/2026; review displays 01/11 07:00 → 08/11 06:45 Vietnam time. Seven UTC calendar days, nominal USD70; daily budget is average pacing, not a newly configured lifetime hard cap. Existing VND plan ceiling remains unchanged; no FX assumption.
- R5 Vietnam/English, four functions and Manager/Director/VP/CXO; 470+ UI estimate. Feed only, RightRail/LAN/Expansion off. Reach optimization / Maximum delivery retained.
- Both historical validation ad sets remained Draft/Off after parent activation and launch. No RMK, VN, Chinese, Search or unrelated campaign enabled by this workflow.

Schedule is automatic once the future start arrives, subject to LinkedIn review/account eligibility. No need to press launch on Sunday. Not currently delivering because future Scheduled; no performance claim.

## Evidence and boundaries

Private screenshots outside public Git: schedule-launch-success.png (success modal), schedule-on.png (exact On/Scheduled row), schedule-ads-active.png (two On/Active ads). SHA256 manifest below pins those private files without account identifiers, billing data or browser state. Saved dates were reopened before launch; review showed actual local times. Initial table switch did not change parent; Edit campaign → Status Active → Save did, verified before launch.

Docs impact reviewed: CURRENT_STATE, README, readiness plan/index, LinkedIn build pack and S04 updated with current operational status. Old draft-only receipts and proposal dates retained as historical evidence, superseded for this exact pair by this receipt. No creative/reader/tracking changes. Remaining task is monitoring review/delivery and paid metrics using existing plan; downstream response/CRM handled by the designated team. No automatic monitoring job created.

Git checkpoint is local on slice/executive-approval-corrected-2026-10-28; no push or merge. This external LinkedIn change exists independently of local Git publication.
