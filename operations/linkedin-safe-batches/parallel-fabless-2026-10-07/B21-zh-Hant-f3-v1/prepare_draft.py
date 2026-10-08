"""Own B13 authoring only; no automatic semantic approval or ImageGen."""
import copy, hashlib, importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
BASE=Path(__file__).resolve().parent.relative_to(ROOT).as_posix()
PERSONA='Operations / SCM Manager influencing business-system decisions at an eligible commercial Fabless FDI entity with outsourced production'
ROUTE='offline English cold -> F1 outsourced-lot reporting -> qualitative China Bright Power integrated-solution case -> English case reader'
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def put(p,v):
 q=ROOT/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ref(p,revision=None): return dict(path=p,sha256=sha(p),revision=revision or load(p).get('revision','source-v1'))
def module(p):
 s=importlib.util.spec_from_file_location(Path(p).stem,ROOT/p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def card(cid,h,b,s='',cta='',labels=None): return dict(card_id=cid,headline=h,body=b,source_text=s,cta=cta,native_headline=h,alt='Illustration: '+h,artwork_labels=labels or [])
F1='operations/linkedin-imagegen-dogfood/continuous-rollout-2026-10-04/F1'
BR='operations/linkedin-rmk-postcheck/2026-10-05/regenerated-v4/bright'
ENTITY='上海晶丰明源半导体股份有限公司'
def main():
 assert not (ROOT/BASE/'draft-manifest.json').exists(), 'fresh revision required'
 fm=load('operations/message-anchor/freeze-2026-10-06/manifest.json');assert all(sha(x['path'])==x['sha256'] for x in fm['files'])
 core=module('scripts/verify_imagegen_preflight.py')
 rows={
 'cold':[card('COLD-FABLESS-B13','Outsourced production. Your next decision.','Align the lot, stage and report time before the next handoff.',labels=['OUTSOURCED CHIP OPERATIONS','ERP for manufacturing'])],
 'explanation':[
 card('F1-A1','Partner reports. A clear view of each lot?','Before planning the next step, check which process stage each partner report describes.'),
 card('F1-A2','Start with the product and lot.','Check the product and lot references. Agree how each partner identifies production periods and test classifications.'),
 card('F1-A3','Which stage does this report describe?','Identify the process stage, when the status was recorded and which partner report supports it.'),
 card('F1-A4','Who keeps the shared view current?','Agree the report format, exchange schedule and owner who confirms each production update.'),
 card('F1-A5','Give the next decision a shared basis.','Bring lot, stage, report time and update ownership into the same discussion.','Digiwin Taiwan semiconductor solution material:\nERP and MES for management and production.','Explore outsourced-production questions')],
 'proof':[
 card('RMK-BRIGHT-1','Digital solutions for manufacturing','We develop and provide digital solutions for manufacturing, from ERP to smart manufacturing.','Digiwin Vietnam · Company introduction'),
 card('RMK-BRIGHT-2','A chip-design case from China','Bright Power is a chip-design business in China. Explore its digital-solution implementation context.','Digiwin Vietnam · Semiconductor case collection\n'+ENTITY),
 card('RMK-BRIGHT-3','Outsourcing management in focus','The case identifies inefficient outsourcing management among its challenges and describes an integrated digital solution.','Digiwin Vietnam · China case04\n'+ENTITY),
 card('RMK-BRIGHT-4','Read the chip-design case','Explore the business challenges and integrated digital-solution context in the named China case.','Digiwin Vietnam · digiwin.com.vn\nSemiconductor case04\n'+ENTITY,'Read the China case')]
 }
 caps={
 'cold':'We provide manufacturing ERP solutions. Chip-design operations teams using outsourced production: align partner reports before the next decision.',
 'explanation':'We provide manufacturing ERP solutions. Fabless means chip design without an owned fabrication plant. Operations teams: align lot reports and responsibilities across production partners.',
 'proof':'We provide digital solutions for manufacturing. Explore outsourcing-management challenges in a named chip-design case from China.'}
 for stage in ['explanation','proof']:
  for i,x in enumerate(rows[stage],1):x['artwork_labels']=['ERP · CHIP OPERATIONS' if stage=='explanation' else 'CHIP-DESIGN CASE',str(i)+'/'+str(len(rows[stage]))]
 scenes={
 'COLD-FABLESS-B13':('An illustrative bright architectural tabletop: a central operations review plinth receives two blank paper reports from separate abstract subcontractor work surfaces. Small neutral chip packages ground outsourced production. Thin blue physical paths imply communication, not automated synchronization. No actual customer buildings, fabrication plant, screen or dashboard.',['central review plinth','two abstract partner surfaces','blank reports','neutral chip packages']),
 'F1-A1':('Separate blank partner reports beside a wafer protective carrier, with open neutral paths expressing the unanswered stage question. Illustrative outsourced-production context, no owned fabrication facility.',['blank partner reports','wafer protective carrier']),
 'F1-A2':('Close physical comparison of a neutral chip product sample and two blank partner record surfaces. Restrained physical linking paths show correspondence to be checked; no technical IDs, dates or test values.',['neutral chip sample','blank correspondence records']),
 'F1-A3':('Oblique tabletop with wafer protective carrier, neutral unlabelled stage nodes and a detached blank report surface. Open paths express stage, report time and source questions, not a confirmed production state.',['wafer protective carrier','neutral stage nodes','blank report']),
 'F1-A4':('Two distinct coordination surfaces connected through a shared blank record surface; an unlabelled neutral owner token suggests responsibility to agree. No completed approval, automatic update or product connector.',['two coordination surfaces','shared blank record','neutral owner token']),
 'F1-A5':('Compact low physical platform with blank partner report and neutral chip sample; open relationship path supports a shared discussion. Leave a large dedicated full-width source paragraph beneath scene.',['blank partner report','neutral chip sample','open physical path']),
 'RMK-BRIGHT-1':('Illustrative bright manufacturing-management desk with a neutral chip sample and blank paper dossier. No customer facility, software UI, actual product or equipment evidence.',['neutral chip sample','blank paper dossier']),
 'RMK-BRIGHT-2':('An open case dossier next to a neutral chip sample in a bright tabletop scene. Introduces a chip-design company case, not documentary customer premises or a customer mark.',['open blank dossier','neutral chip sample']),
 'RMK-BRIGHT-3':('Two blank subcontractor record surfaces and a central blank coordination folio linked by open physical paths. Illustrative management context only; no completed workflow or actual customer implementation diagram.',['blank subcontractor records','central coordination folio']),
 'RMK-BRIGHT-4':('A small open blank case booklet with a neutral chip sample on a low platform; compact scene above a large full-width source block and separate CTA. No skyline or customer facility.',['blank case booklet','neutral chip sample'])}
 pins=[];observations=[]
 for stage in ['cold','explanation','proof']:
  old=load(F1+'/worker/campaign/contract.json') if stage=='explanation' else load('operations/linkedin-safe-batches/2026-10-07/B4-en-o2-v1/cold/adapter-draft/contract.draft.json') if stage=='cold' else load(BR+'/campaign/contract.json')
  c=copy.deepcopy(old);ad='B13-COLD' if stage=='cold' else 'F1-A' if stage=='explanation' else 'RMK-BRIGHT'
  p=BASE+'/'+stage+'/public-copy.json';out=dict(schema_version=1,revision='b13-'+stage+'-en-copy-v1',ads=[dict(ad_id=ad,caption=caps[stage],cards=rows[stage])]);put(p,out)
  c.update(revision='b13-'+stage+'-contract-draft-v1',locale='en',copy=ref(p),ad_order=[ad],card_order={ad:[x['card_id'] for x in rows[stage]]},groups=[[x['card_id']] for x in rows[stage]],definitions={'OSAT':'outsourced semiconductor packaging and testing','Fabless':'chip design without an owned fabrication plant','WIP':'work in process'})
  c['limits']['caption']=255
  sources=[F1+'/common/f1-copy.json',F1+'/common/source-attachments/evidence-register.md',F1+'/common/source-attachments/local-terminology-evidence.json'] if stage!='proof' else [BR+'/source.json',BR+'/copy.json',BASE+'/proof-source-mapping.json']
  c['sources']=[ref(q,'b13-exact-source-v1') for q in sources];c['card_sources']={x['card_id']:sources for x in rows[stage]}
  c['surfaces']={ad:[dict(surface_id='full-feed',reading_order=['caption']+[x['card_id']+'.'+f for x in rows[stage] for f in core.CARD_FIELDS])]}
  c['references']=copy.deepcopy(load(F1+'/worker/campaign/contract.json')['references'])
  c['style']=copy.deepcopy(load(F1+'/worker/campaign/contract.json')['style'])
  c['style']['campaign']['instructions']='International English. Bright white and pale blue R2 photographic material depth, grounded daylight shadows, navy/blue large type, authentic official supplied Digiwin mark once. Cohort-appropriate illustrative chip-design/outsourcing management; no owned fab, customer facility, faces, screens, technical chip data, charts, ticks or fabricated records. Print only the exact approved artwork text. Caption/native headline/alt stay outside raster. Category and sequence distinct from source. Headline dominant; body comfortably readable at333px. Source must be a full-width WHITE main paragraph, at least body-sized (about56native pixels on1080), high-contrast navy, generous space for the full legal name. Reduce scene before source typography. No tiny footer, source icon column, divider or unapproved punctuation. English international business voice; no inherited Vietnamese wording. '+('Single cold image: no sequence, no swipe; category and ERP role line clearly readable.' if stage=='cold' else 'Exact reviewed category and sequence near logo; no extra DIGIWIN label.')
  calls=[]
  for i,x in enumerate(rows[stage]):
   desc,props=scenes[x['card_id']];desc+=' All record surfaces are blank: no microglyphs, IDs, dates, statuses, results or extra labels. Official mark once; exact approved text only.'
   call=dict(call_id='B13_'+x['card_id'].replace('-','_'),targets=[x['card_id']],references=c['references'],concepts=[dict(card_id=x['card_id'],concept_id='b13-'+x['card_id'].lower()+'-scene-v1',reader_question=x['headline'],description=desc,props=props,artwork_labels=x['artwork_labels'])],artwork_text={x['card_id']:{f:x[f] for f in ['headline','body','source_text','cta','artwork_labels']}},output_id=x['card_id'].lower()+'-b13-en-v1',output_path=BASE+'/'+stage+'/native/'+x['card_id'].lower()+'-b13-en-v1.png')
   calls.append(call);observations.append(dict(stage=stage,card_id=x['card_id'],native_headline=x['native_headline'],reviewed_fields=['caption']+list(core.CARD_FIELDS),scene=desc,source_scope='Attributed China integrated digital-solution context; qualitative outsourcing pain, not proof of a specific F1 lot-report mechanism.' if stage=='proof' else 'Source-bound management questions; Taiwan ERP/MES publication context on closing; not Vietnam ERP-only capability.',observation=' | '.join([caps[stage],x['headline'],x['body'],x['source_text'],x['cta'],x['alt'],str(x['artwork_labels'])])))
  c['output']['directory']=BASE+'/'+stage+'/native';put(BASE+'/'+stage+'/contract.draft.json',c);put(BASE+'/'+stage+'/calls.draft.json',dict(revision='b13-'+stage+'-calls-draft-v1',calls=calls));pins.extend([ref(p),ref(BASE+'/'+stage+'/contract.draft.json'),ref(BASE+'/'+stage+'/calls.draft.json')])
 put(BASE+'/intake.json',dict(revision='b13-intake-v1',owner='/root Fabless session',branch='slice/linkedin-safe-fabless-parallel',source_checkpoint='f2883d1c9db7c4abb72afa8998d2bde0cc192b74',persona=PERSONA,route=ROUTE,locale='en',segment='FDI',customer_fit='Content audience hypothesis only: commercial chip-design entity using outsourced production, Operations/SCM influences local business-system evaluation. Actual company fit, ownership and system authority unknown; no target account/live claim.',business_trigger='Report-format and ownership standardization when disconnected partner reports obstruct accountable next-step decisions. Existing systems/process fixes remain alternatives to ERP purchase.',proof_disposition='Fresh qualitative bridge: F1 reporting/coordination questions -> named China case with stated outsourcing-management inefficiency and integrated digital solution. No claim this case proves the exact F1 mechanism or Vietnam ERP-only delivery. Numeric outcome divergence retained HOLD.',new_original_cap=10,corrective_cap=2,per_card_corrective_cap=1,canary=['RMK-BRIGHT-2','F1-A5'],stop='After B13 generated/reviewed or material/native/cap blocker; never begin B14 without Bao review.',postgen='POSTGEN_NOT_RUN'))
 put(BASE+'/reader-script.json',dict(revision='b13-reader-en-v1',entity=ENTITY,source_url='https://www.digiwin.com.vn/resources/digiwin-semiconductor-8-case-studies-cn/',title='Outsourcing management in a China chip-design case',intro='The Digiwin Vietnam case collection presents Bright Power, '+ENTITY+', as a chip-design company in China.',sections=[dict(title='The business challenge',text='The source identifies inefficient outsourcing management alongside slow engineering and order responses.'),dict(title='The solution context',text='It describes an integrated digital solution. The case offers context for examining outsourcing coordination and information responsibilities.'),dict(title='Questions for your own operation',text='Which lot and process stage does each partner report describe? When was it recorded? Who confirms a production update? Which shared reporting conventions support the next decision?')],source_language='The original source is Simplified Chinese. This page is an English summary.',source_cta='Read the original China case',return_label='Return to the outsourced-production journey'))
 pins.extend([ref(BASE+'/intake.json'),ref(BASE+'/reader-script.json'),ref(BASE+'/proof-source-mapping.json')]);put(BASE+'/draft-observations.json',dict(revision='b13-observations-draft-v1',cards=observations));pins.append(ref(BASE+'/draft-observations.json'));put(BASE+'/draft-manifest.json',dict(revision='b13-draft-manifest-v1',files=pins,frozen_files_verified=24))
 print('B13 draft authored:10 units + reader; no review PASS or release generated.')
if __name__=='__main__':main()
