# S03 — LinkedIn audience research

**Status:** authorized external validation completed on 2026-09-14; this public-repository record is sanitized. No audience was uploaded, no ad was added, no campaign delivered, and no spend occurred.
**Owner:** Executor in this batch  
**Objective:** define a public-source account-universe methodology and role hypotheses while separating candidate identity, externally observed configuration evidence, and verified Campaign Manager delivery evidence.

## Source boundary

- Local: kickoff §§4, 7, 8; source brief “Thực tế VN”, “Thông điệp theo nhóm đối tượng” and “Digital Ads — Bảo”.
- Public official: LinkedIn Matched Audiences overview, https://www.linkedin.com/help/linkedin/answer/a420552/matched-audiences (accessed 2026-09-11); LinkedIn match-rate guidance, https://www.linkedin.com/help/linkedin/answer/a420595/matched-audiences-match-rates (accessed 2026-09-11); company/contact targeting overview, https://www.linkedin.com/help/linkedin/answer/a424397/linkedin-account-and-contact-targeting-overview (accessed 2026-09-11).
- Public official guidance indicates company/contact targeting and member-provided profile layers exist, and audience size/match rate are account/UI outputs. An authorized external read-only validation was completed on 2026-09-14. Raw account, audience, list and screenshot evidence is intentionally retained outside this public repository.

## Fact / proposal / unknown

**Facts:** LinkedIn awareness is planned; OSAT/factory is priority; role/account targeting must be evidenced rather than inferred from aggregate reach. The external validation observed that Company Names, geography and role facets can be configured; it did not establish delivery or commercial outcomes.

**Proposal:** retain a quality-first company universe and use the observed configuration as a production hypothesis only after human review of unresolved entity mappings. Keep Company Names and Job Functions in separate AND groups; do not treat aggregate estimates as account-role delivery proof.

**Unknown:** approval of unresolved parent-level entity mappings, final production audience definition, consent/eligibility, account-reporting granularity, and actual delivery.

**Current UI note:** external validation was limited to non-delivering draft/off configuration. The public record does not retain raw account or audience data. No upload, creative attachment, launch or spend is claimed.

Production handoff: `../ads/linkedin/LinkedIn_Build_Pack.md`.

## Candidate account-universe methodology

| Tier | Provenance | Candidate examples | Status / rule |
|---|---|---|---|
| A — named local lead | Source brief names OSAT/factory, fabless and supplier/SI categories | No account list asserted | Category only; needs Vietnam company universe |
| B — local-brief lead | The local brief names semiconductor cases/companies; no verified account list is present | Not populated in this draft | Names are research leads only, not confirmed target accounts, customers or current legal identities |
| C — public Vietnamese ecosystem | Government/industry sources may identify companies and associations | Not populated in this draft | Add only with URL, date, entity identity and relevance rationale |

No personal names, emails, scraped contacts or PII are included.

## Role / function / seniority hypotheses

| Segment | Function hypotheses | Seniority hypotheses | Exclusions / caution |
|---|---|---|---|
| OSAT / factory | Operations, manufacturing, quality, process engineering, supply chain, finance/controlling, IT/MES | Manager, head/director, VP/executive where available | Do not equate job title with decision authority; validate language and local taxonomy |
| Fabless commercialization | Operations, planning, supply chain, R&D/program, finance, product/operations leadership | Manager/director/VP | Avoid broad chip-design audiences unrelated to commercial operations |
| Supplier/SI/automation | Solution engineering, industrial automation, ERP/MES/OT, partner/channel, quality | Manager/director/partner leadership | Separate partner objective from end-user awareness |

## Objective / format hypotheses

- Primary hypothesis: LinkedIn awareness using pain → mechanism → safe proof direction, subject to account and format availability.
- Candidate formats: single-image or document/carousel-style professional explanation if the authorized account supports it; format is not a required deliverable.
- Retargeting is conditional on an eligible, consent-compatible audience source; do not assume website visitors or engagement audiences exist.

## UI validation plan

1. Obtain human sign-off for the remaining parent-level or otherwise unresolved entity mappings before any production audience decision.
2. Keep Company Names and Job Functions in separate AND groups. Do not use an OR grouping to infer account-role targeting.
3. Keep the audience uncreated and exclude any company-list upload unless a separate mandate and the applicable platform eligibility conditions are met.
4. Re-check audience estimate, delivery eligibility and expansion settings at the moment a production draft is explicitly authorized; external validation is not delivery evidence.
5. Record objective, format, placement, consent/eligibility and reporting constraints as observed or unknown. Do not infer account × role intersection from marginal reports.

## Acceptance, dependencies and stop

**Acceptance:** provenance-bearing public candidate methodology; no PII; role hypotheses and exclusions; sanitized external-validation boundary; explicit production gate.
**Dependencies:** S01 message map; human sign-off on unresolved entity mappings; S04 measurement and a separate operational mandate.
**Stop:** no upload, no audience creation, no campaign build, no message/invitation, no public commit of raw account/audience data, and no claim of match rate/size/reach/delivery beyond the retained evidence scope.
