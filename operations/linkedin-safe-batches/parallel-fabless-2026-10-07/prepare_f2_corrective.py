"""Assemble a bounded edit from root's recorded actual finding; no ImageGen."""
import copy,sys,hashlib
from prepare_next_locales import ROOT,LANE,load,put,ref,sha,module,PERSONA
batch,cid=sys.argv[1:3];assert batch in ['B16','B17']
loc='en' if batch=='B16' else 'zh-Hans';base=LANE+'/'+batch+'-'+loc+'-f2-v1'
extra='--extra-po' in sys.argv
assert not extra or (batch=='B16' and cid=='F2-A5')
n=2 if extra else 1
record=base+'/actual-corrective-'+cid.lower()+('-extra-po' if extra else '')+'-review.json';actual=load(record)
assert not extra or actual['po_authorization']=='Cho thêm 1 lượt sửa F2-A5'
assert actual['verdict']=='SCRIPT_REVIEW_PASS' and actual['anchor_verdict']=='MESSAGE_ANCHOR_PASS' and actual['independence']=='SELF_REVIEW'
attempts=load(base+'/attempt-ledger.json')['attempts'];assert sum(a['kind']=='corrective' for a in attempts)<2
assert sum(a['kind']=='corrective' and a['card_id']==cid for a in attempts)==n-1
a=[a for a in attempts if a['card_id']==cid][-1];assert a['sha256']==actual['original_sha256']==sha(a['path'])
plan=load(base+'/dispatch-plan.json');job=next(j for j in plan['calls'] if j['card_id']==cid);old=job['folder'];folder=base+'/corrective-v'+str(n)+'/'+cid.lower()
assert not (ROOT/folder/'native').exists()
c=copy.deepcopy(load(old+'/contract.json'));c['revision']=batch.lower()+'-'+cid.lower()+'-corrective-contract-v1';c['output']['directory']=folder+'/native'
c['references'][0]=dict(**ref(a['path'],a['call_id']+'-actual-edit-target'),role='campaign_visual',attributes=['colors','lighting','shadows','material_depth','typography_hierarchy','campaign_identity','scene_diagram_integration'])
c['sources'].append(ref(record));c['style']['campaign']['instructions']+=' '+actual['edit_instructions']
for k in c['card_sources']:c['card_sources'][k].append(record)
put(folder+'/contract.json',c);cr=ref(folder+'/contract.json')
review=copy.deepcopy(load(old+'/review.json'));review['revision']=batch.lower()+'-'+cid.lower()+'-corrective-source-review-v1';review['subjects']=dict(contract=cr,copy=c['copy'],sources=c['sources']);put(folder+'/review.json',review)
release=copy.deepcopy(load(old+'/release.json'));release.update(revision=batch.lower()+'-'+cid.lower()+'-corrective-release-v1',contract=cr,review=ref(folder+'/review.json'));put(folder+'/release.json',release)
sc=copy.deepcopy(load(old+'/spec.json'));call=sc['calls'][0];call.update(call_id=batch+'_'+cid.replace('-','_')+'_C'+str(n),references=c['references'],output_id=cid.lower()+'-'+loc+'-c'+str(n),output_path=c['output']['directory']+'/'+cid.lower()+'-'+loc+'-c'+str(n)+'.png');call['prompt']=module('scripts/verify_imagegen_preflight.py').make_prompt(c,call);call['prompt_sha256']=hashlib.sha256(call['prompt'].encode()).hexdigest()
sc.update(revision=batch.lower()+'-'+cid.lower()+'-corrective-spec-v1',contract=cr,release=ref(folder+'/release.json'),review=release['review']);put(folder+'/spec.json',sc)
s=copy.deepcopy(load(old+'/script-review.json'));s['revision']=batch.lower()+'-'+cid.lower()+'-actual-corrective-script-v1';s['corrective_review']=ref(record);s['corrective_observation']=actual['observation'];put(folder+'/script-review.json',s)
ar=copy.deepcopy(load(old+'/anchor-review.json'));ar['revision']=batch.lower()+'-'+cid.lower()+'-actual-corrective-anchor-v1';ar['subjects']=dict(contract=cr,copy=c['copy'],spec=ref(folder+'/spec.json'),script_review=ref(folder+'/script-review.json'));ar['context']['related_inputs'].append(ref(record));ar['context']['observation']+=' Actual root corrective: '+actual['observation'];put(folder+'/anchor-review.json',ar)
g=module('scripts/verify_imagegen_anchor_preflight.py').check(ROOT,folder+'/release.json',sha(folder+'/release.json'),folder+'/spec.json',folder+'/anchor-review.json',sha(folder+'/anchor-review.json'),call['call_id'],'FDI',PERSONA,plan['route']);put(folder+'/preparation-preflight.json',g)
cp=base+'/corrective-dispatch-plan.json';new=load(cp) if (ROOT/cp).exists() else dict(revision=batch.lower()+'-f2-corrective-plan-v1',persona=PERSONA,route=plan['route'],locale=loc,calls=[],corrective_cap=2,per_card_corrective_cap=1)
assert len(new['calls'])<2 and sum(j['card_id']==cid for j in new['calls'])==n-1
if extra:new['po_card_exception']=dict(card_id=cid,authorized_corrective_cap=2,authorization=ref(record))
new['calls'].append(dict(folder=folder,card_id=cid,call_id=call['call_id'],output_path=call['output_path'],release_sha256=sha(folder+'/release.json'),review_sha256=sha(folder+'/anchor-review.json')));put(cp,new)
print(batch+' '+cid+': actual-reviewed corrective prepared; fresh wrapper required.')
