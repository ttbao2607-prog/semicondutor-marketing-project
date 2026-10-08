from prepare_draft import *
import sys
cid=sys.argv[1];finding=sys.argv[2];direction=sys.argv[3]
core=module('scripts/verify_imagegen_preflight.py');guard=module('scripts/verify_imagegen_anchor_preflight.py');plan=load(BASE+'/dispatch-plan.json');job=next(j for j in plan['calls'] if j['card_id']==cid);old=job['folder'];new=BASE+'/corrective-v1/'+cid.lower();assert not (ROOT/new).exists()
c=load(old+'/contract.json');c['revision']=cid.lower()+'-b13-corrective-contract-v1';c['output']['directory']=new+'/native'
brand=next(x for x in c['references'] if x['role']=='brand_asset');style=next(x for x in c['references'] if x['role']=='campaign_visual');target=dict(style,path=job['output_path'],sha256=sha(job['output_path']),revision='b13-original-edit-target')
c['references']=[target,brand];c['style']['campaign']['instructions']+=' TARGETED EDIT: '+direction
if 'closing' in c['style']:del c['style']['closing']
put(new+'/contract.json',c);cr=ref(new+'/contract.json');pr=c['copy'];review=load(old+'/review.json');review.update(revision=cid.lower()+'-b13-corrective-review-v1',subjects=dict(contract=cr,copy=pr,sources=c['sources']));put(new+'/review.json',review)
release=load(old+'/release.json');release.update(revision=cid.lower()+'-b13-corrective-release-v1',contract=cr,review=ref(new+'/review.json'),groups=[[cid]]);put(new+'/release.json',release)
call=copy.deepcopy(next(x for x in load(old+'/spec.json')['calls'] if x['targets']==[cid]));call['call_id']+='_corrective1';call['output_id']+='_corrective1';call['output_path']=new+'/native/'+call['output_id']+'.png';call['references']=c['references'];call['concepts'][0]['description']+=' TARGETED EDIT: '+direction;call['prompt']=core.make_prompt(c,call);call['prompt_sha256']=hashlib.sha256(call['prompt'].encode()).hexdigest()
spec=load(old+'/spec.json');spec.update(revision=cid.lower()+'-b13-corrective-spec-v1',contract=cr,release=ref(new+'/release.json'),review=release['review'],calls=[call]);put(new+'/spec.json',spec)
script=load(old+'/script-review.json');script.update(revision=cid.lower()+'-b13-corrective-script-v1',corrective_review=dict(finding=finding,direction=direction,exact_copy_unchanged=True,actual_root_review='Same persona/meaning/proof scope; remove unapproved graphic and restore approved source hierarchy. Bounded1corrective/card. Original is edit target only, never accepted style/proof baseline.'));put(new+'/script-review.json',script)
anchor=load(old+'/anchor-review.json');anchor.update(revision=cid.lower()+'-b13-corrective-anchor-v1',subjects=dict(contract=cr,copy=pr,spec=ref(new+'/spec.json'),script_review=ref(new+'/script-review.json')))
for u in anchor['units']:
 if u['card_id']==cid:u['observation']+=' Corrective actual review: '+direction+' Same exact copy and primary meaning; no new claim.'
put(new+'/anchor-review.json',anchor);put(new+'/ledger.json',dict(revision='b13-corrective-ledger-v1',card_id=cid,finding=finding,original=ref(job['output_path'],'original-b13-native'),hypothesis='Reference scene/footer transfer; not proven tool/core cause.',direction=direction,acceptance='Exact text, source at least body size; no skyline/icon/divider or unapproved props. Native/render closure required.',cap=1,status='PREPARED_POSTGEN_NOT_RUN'))
checked=guard.check(ROOT,new+'/release.json',sha(new+'/release.json'),new+'/spec.json',new+'/anchor-review.json',sha(new+'/anchor-review.json'),call['call_id'],'FDI',PERSONA,ROUTE);put(new+'/preparation-preflight.json',checked)
p=BASE+'/corrective-dispatch-plan.json';fix=load(p) if (ROOT/p).exists() else dict(revision='b13-correctives-v1',persona=PERSONA,route=ROUTE,calls=[])
cap=2
if (ROOT/BASE/'t4-authorization.json').exists():
 auth=load(BASE+'/t4-authorization.json');assert auth['user_instruction']=='Xử lý card 3 để pass hậu kiểm.' and cid==auth['card_id'];cap=4
elif (ROOT/BASE/'t3-authorization.json').exists():
 auth=load(BASE+'/t3-authorization.json');assert auth['user_instruction']=='Cho phép lượt sửa T3.' and cid==auth['card_id'];cap=3
assert len(fix['calls'])<cap
fix['calls'].append(dict(folder=new,call_id=call['call_id'],card_id=cid,output_path=call['output_path'],release_sha256=sha(new+'/release.json'),review_sha256=sha(new+'/anchor-review.json')));put(p,fix);print('prepared corrective '+str(len(fix['calls'])-1))
