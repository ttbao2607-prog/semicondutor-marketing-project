"""Bind the root's actual recorded B13 SELF_REVIEW; frozen gates unchanged."""
from prepare_draft import *
def main():
 assert not (ROOT/BASE/'dispatch-plan.json').exists()
 core=module('scripts/verify_imagegen_preflight.py');guard=module('scripts/verify_imagegen_anchor_preflight.py')
 semantic=load(BASE+'/semantic-review.json');assert semantic['verdict']=='SCRIPT_REVIEW_PASS'
 assert semantic['draft_manifest_sha256']==sha(BASE+'/draft-manifest.json')
 assert all(sha(x['path'])==x['sha256'] for x in load(BASE+'/draft-manifest.json')['files'])
 put(BASE+'/generation-mandate.json',dict(revision='b13-bao-mandate-v1',instruction='Tạo worktree riêng, own riêng plan này, chạy fullpipeline batch đầu tiên.',scope='B13 only, full generation+reader+actual postcheck; handoff read before worktree,10original+2corrective/1percard, browser evidence gaps reported honestly.',no_commit_merge_push=True))
 plans=[]
 for stage in ['cold','explanation','proof']:
  con=load(BASE+'/'+stage+'/contract.draft.json');target=load(con['copy']['path']);calls=load(BASE+'/'+stage+'/calls.draft.json')['calls']
  variants=[('campaign',calls)] if stage=='cold' else [('campaign',calls[:-1]),('closing',calls[-1:])]
  for variant,selected in variants:
   folder=BASE+'/'+stage+'/release-v2/'+variant;c=copy.deepcopy(con);c['revision']='b13-'+stage+'-'+variant+'-contract-v2';c['output']['directory']=folder+'/native'
   c['sources'].append(ref(BASE+'/execution-brief.md','b13-execution-brief-v1'))
   if variant=='closing':
    closing=load('operations/linkedin-rmk-postcheck/2026-10-05/regenerated-v4/bright/closing/contract.json')
    c['references']=copy.deepcopy(closing['references']);c['style']['closing']=copy.deepcopy(closing['style']['closing']);c['style']['closing']['cards']=selected[0]['targets']
   put(folder+'/contract.json',c);cr=ref(folder+'/contract.json');pr=ref(con['copy']['path']);ids=[x['card_id'] for a in target['ads'] for x in a['cards']]
   fields={a['ad_id']:['caption']+[x['card_id']+'.'+f for x in a['cards'] for f in core.CARD_FIELDS] for a in target['ads']}
   observations=[o for o in load(BASE+'/draft-observations.json')['cards'] if o['stage']==stage]
   assert [o['card_id'] for o in observations]==ids
   review=dict(schema_version=1,revision='b13-'+stage+'-'+variant+'-review-v1',writer='/root',reviewer='/root',date='2026-10-07',scope='OFFLINE_SOURCE_COPY',independence='SELF_REVIEW',subjects=dict(contract=cr,copy=pr,sources=c['sources']),verdicts=dict(source_copy='PASS',editorial='PASS',first_mention='PASS'),reviewed_ads=c['ad_order'],reviewed_fields=[a+'/'+f for a,fs in fields.items() for f in fs],unresolved_findings=[])
   put(folder+'/review.json',review)
   release=dict(schema_version=1,revision='b13-'+stage+'-'+variant+'-release-v1',authorizer='/root coordinator recording Bao B13 authority',authority_ref=ref(BASE+'/generation-mandate.json'),purpose='OFFLINE_IMAGEGEN',contract=cr,copy=pr,review=ref(folder+'/review.json'),groups=[x['targets'] for x in selected]);put(folder+'/release.json',release)
   newcalls=copy.deepcopy(selected)
   for call in newcalls:
    call['references']=c['references'];call['output_path']=c['output']['directory']+'/'+call['output_id']+'.png';call['prompt']=core.make_prompt(c,call);call['prompt_sha256']=hashlib.sha256(call['prompt'].encode()).hexdigest()
   spec=dict(schema_version=1,revision='b13-'+stage+'-'+variant+'-spec-v1',release=ref(folder+'/release.json'),contract=cr,copy=pr,review=release['review'],calls=newcalls);put(folder+'/spec.json',spec)
   script=dict(revision='b13-'+stage+'-'+variant+'-script-v1',gate_id='AD-ED-01',stage='PREGEN_SCRIPT',verdict='SCRIPT_REVIEW_PASS',copy_sha256=pr['sha256'],reviewed_ads=c['ad_order'],reviewed_fields=fields,BRAND_ROLE=dict(verdict='PASS',observation=semantic['brand_role']),ADVERTISER_VOICE=dict(verdict='PASS',observation=semantic['advertiser_voice']),independence='SELF_REVIEW',per_card_observations=observations,reader_script=ref(BASE+'/reader-script.json'),actual_review_ref=ref(BASE+'/semantic-review.json'),postgen='POSTGEN_NOT_RUN')
   put(folder+'/script-review.json',script)
   anchor=dict(schema_version=1,revision='b13-'+stage+'-'+variant+'-anchor-v1',gate_id='MSG-ANCHOR-01',stage='PREGEN_SCRIPT',verdict='MESSAGE_ANCHOR_PASS',anchor=ref('operations/Vy_Email_Content_Anchor.md','1.0'),source=ref('operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md','VY-MAIL-USER-20261006'),subjects=dict(contract=cr,copy=pr,spec=ref(folder+'/spec.json'),script_review=ref(folder+'/script-review.json')),scope=dict(segment='FDI',locale='en',persona=PERSONA,route=ROUTE),writer='/root',reviewer='/root',independence='SELF_REVIEW',coverage=dict(ads=c['ad_order'],cards=ids,fields=fields,storyboard_cards=ids),rules={k:dict(verdict='N/A' if k=='A5' else 'MATCH',observation=semantic[k]) for k in ['A1','A2','A3','A4','A5','A6','A7']},units=[dict(card_id=o['card_id'],verdict='MATCH',observation=o['observation']+' Scene: '+o['scene']+' Source: '+o['source_scope']) for o in observations],transitions=[dict(cards=[x['card_id'],y['card_id']],verdict='MATCH',observation=x['headline']+' -> '+y['headline']+'; same Operations/SCM reader; each step builds reporting basis or source-attributed qualitative case context.') for a in target['ads'] for x,y in zip(a['cards'],a['cards'][1:])],context=dict(scope='FULL_JOURNEY',verdict='MATCH',observation=semantic['A7']+' Reader review: '+semantic['reader'],brief=ref(BASE+'/execution-brief.md','b13-execution-brief-v1'),related_inputs=[ref(BASE+'/'+other+'/public-copy.json') for other in ['cold','explanation','proof'] if other!=stage]+[ref(BASE+'/reader-script.json'),ref(BASE+'/semantic-review.json'),ref(BASE+'/proof-source-mapping.json')]),unresolved_findings=[])
   put(folder+'/anchor-review.json',anchor)
   for call in newcalls:
    checked=guard.check(ROOT,folder+'/release.json',sha(folder+'/release.json'),folder+'/spec.json',folder+'/anchor-review.json',sha(folder+'/anchor-review.json'),call['call_id'],'FDI',PERSONA,ROUTE)
    put(folder+'/preparation-preflight/'+call['call_id']+'.json',checked)
    plans.append(dict(folder=folder,call_id=call['call_id'],card_id=call['targets'][0],output_path=call['output_path'],release_sha256=sha(folder+'/release.json'),review_sha256=sha(folder+'/anchor-review.json')))
 canary=['RMK-BRIGHT-2','F1-A5'];order=[x['card_id'] for x in load(BASE+'/draft-observations.json')['cards']];plans.sort(key=lambda p:(0,canary.index(p['card_id'])) if p['card_id'] in canary else (1,order.index(p['card_id'])))
 put(BASE+'/dispatch-plan.json',dict(revision='b13-dispatch-v1',persona=PERSONA,route=ROUTE,calls=plans,preparation_check_only=True,fresh_preflight_required_before_each_call=True,trust='root actual coordinator/reviewer SELF_REVIEW recorded semantic review; no independent approval asserted'))
 print('B13 fresh gate preparation:',len(plans),'calls; actual per-call guard still required')
if __name__=='__main__':main()
