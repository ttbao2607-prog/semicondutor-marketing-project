"""Record root's actual review of the authored F2 inputs; no semantic inference."""
from prepare_f2_batches import *
import subprocess

rules={
 'A1':'Eligible commercial outsourced chip-design entity, same semiconductor operating activity as v5. F2 demand-change planning is a concrete Operations/SCM issue, not generic ERP content or target-account validation.',
 'A2':'Same Operations/SCM decision unit with planning responsibilities; group ERP autonomy and local buying authority remain unknown. No Finance role switch or claim every design office is a local ERP buyer.',
 'A3':'FDI English/Simplified Chinese, separately authored business wording. English product/planning period/report source/confirmation owners and Hans 产品/计划期间/批次/报告来源/确认责任 convey the same operational scope. ERP, Fabless and MES first mentions explained. No OSAT/WIP jargon. Language does not establish FDI ownership.',
 'A4':'Business value is implicit: shared basis for discussing the next plan and accountable confirmations. No forecast accuracy, faster replanning result, inventory saving, optimization, automatic rescheduling or ROI/metrics promise.',
 'A5':'N/A: FDI lane, no domestic supplier-entry/audit/qualification promise.',
 'A6':'Concrete demand-change scope -> product/planning period/lots -> recorded status time/report source -> missing information/confirmation owner -> shared discussion. Operational questions and conventions, not unverified ERP planning engine or MES replacement. Scenes blank, neutral and illustrative, no forecast/data/technical records.',
 'A7':'Same persona and outsourced-production planning issue throughout. F2 shared planning basis -> prospective Vietnam consultation -> provider role -> explicit China qualitative outsourcing-management/integrated-solution context -> localized reader with F2 planning questions. China proof is contextual, not proof of exact forecast/replanning mechanism or Vietnam team delivery.'
}
unit_observations=[
 'Cold: changed demand is a review trigger, product/planning period/partner reports are preparation objects; category functional, no counter/CTA.',
 'A1: relevant outsourced lots before partner planning discussion;1/6, no actual status or forecast value.',
 'A2: product/planning-period/lot scope;2/6, no automatic selection/approval claim.',
 'A3: report time/source alongside lot status;3/6, no dated clock or data UI.',
 'A4: missing information and accountable confirming person;4/6, no completed replanning workflow.',
 'A5: scope/source/confirmation owners in shared discussion;5/6. Taiwan ERP/MES full normal source paragraph, discussion CTA, separate production-system context.',
 'A6: exact reused local Vietnam service wording and6/6; reporting workflows/update ownership/priorities remain relevant to planning. No headcount/outcome/Fabless Vietnam deployment claim.',
 'Proof1: exact same-locale supplier first-person introduction/source1/4; current caption explains ERP, no testimonial.',
 'Proof2: exact China identity/legal source2/4. English rebuilt for blank paper; Hans corrected blank-paper output reused. Not forecast proof.',
 'Proof3: qualitative outsourcing inefficiency/integrated-solution context, China case04/legal name3/4. No numerical outcome or ERP-only cause.',
 'Proof4: source-reading next step, exact China publisher/domain/legal-name4/4 andCTA; same source as current reader. Not operational lead submission.'
]
transitions=['Demand-change trigger -> identify relevant outsourced lots','Relevant lots -> product and planning period scope','Scope -> report time and source alongside lot status','Status basis -> missing information and confirming owner','Confirmation responsibility -> shared replanning discussion basis','Shared basis -> prospective Vietnam consultation','Vietnam service -> provider introduction, no claim Vietnam team delivered China case','Provider role -> named China chip-design case','China identity -> qualitative outsourcing challenge/integrated solution','Qualitative context -> source-reading CTA -> localized reader with planning questions']
for batch,loc in [('B16','en'),('B17','zh-Hans')]:
 base=LANE+'/'+batch+'-'+loc+'-f2-v1'
 cards=load(base+'/draft-observations.json')['cards']
 review=dict(revision=batch.lower()+'-actual-f2-root-script-review-v1',stage='PREGEN_SCRIPT',verdict='SCRIPT_REVIEW_PASS',anchor_verdict='MESSAGE_ANCHOR_PASS',reviewer='/root',independence='SELF_REVIEW',draft_manifest_sha256=sha(base+'/draft-manifest.json'),review_method='Actual root reread anchor/original email, exact F2 source, all11 fresh fields/scenes/captions/UI/reader and ten transitions. Reopened official China/Taiwan/Vietnam sources. Native source reuse viewed and exact fields/byte provenance compared in this session; no inherited F1/other-locale PASS. This script transcribes judgment already performed, not keyword approval.',**rules,brand_role='Official supplied Digiwin mark once; functional category/counter distinct from attributed source. Supplier, customer and Taiwan/Vietnam provenance remain separate.',advertiser_voice='English We provide/We develop and provide/Work with our team; Hans 我们提供/我们开发并提供/与我们在越南的团队. Neutral planning questions, no third-person supplier praise or invented quote.',reader='Current China qualitative source summary stays same entity/geography/solution scope, with freshly authored F2 product/planning-period/lot/report-time/source/confirming-owner questions. Original Simplified source disclosure and exact legal entity preserved; return to same-locale F2 journey.',unit_review={c['card_id']:unit_observations[i] for i,c in enumerate(cards)},transition_review=transitions,unresolved_findings=[],postgen='POSTGEN_NOT_RUN',unknowns=['new native/rendered typography','full current mobile evidence','native-market reviewer','PO acceptance','actual entity eligibility/local system authority','live rights'])
 put(base+'/semantic-review.json',review)
 reuse=load(base+'/reuse-ledger.json')
 for a in reuse['artwork']:assert sha(a['path'])==a['sha256']
 put(base+'/reuse-review.json',dict(revision=batch.lower()+'-actual-f2-reuse-review-v1',reviewer='/root',independence='SELF_REVIEW',scope='Actual current F2 text/context/native/source-byte review',verdict='PASS_FOR_SOURCE_NATIVE_REUSE_ONLY',semantic_review=ref(base+'/semantic-review.json'),artwork=reuse['artwork'],observations=[unit_observations[i] for i,c in enumerate(cards) if c['reused']],rendered='Fresh F2 caption/reader/current journey render still pending; no full-render PASS inherited.'))
 print(batch+': actual root F2 script and source-native reuse review recorded; fresh releases required.')

head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
assert head=='461a752f1aab7add8f21dfb5652d5e1097aa2247'
assert subprocess.check_output(['git','rev-parse','HEAD^'],cwd=ROOT,text=True).strip()=='e3b65780356cdf5f489ea3a45ac4927af616cd81'
checked=0
for batch,loc,rev in [('B14','zh-Hans','v1'),('B15','zh-Hant','v2')]:
 for a in load(DEL+'/'+batch+'-'+loc+'-f1-'+rev+'/manifest.json')['artwork']:
  assert subprocess.check_output(['git','show',head+':'+a['path']],cwd=ROOT)==(ROOT/a['path']).read_bytes();checked+=1
put(LANE+'/B14-B15-checkpoint-outcome.json',dict(revision='b14-b15-local-checkpoint-outcome-v1',commit=head,parent='e3b65780356cdf5f489ea3a45ac4927af616cd81',branch='slice/linkedin-safe-fabless-parallel',selected_png_committed_bytes_verified=checked,all439_staged_bytes_verified_before_commit=True,technical_verdict='INSUFFICIENT_EVIDENCE unchanged',main_integration=False,push=False,next='B16/B17 working files after checkpoint, not part of this commit.'))
