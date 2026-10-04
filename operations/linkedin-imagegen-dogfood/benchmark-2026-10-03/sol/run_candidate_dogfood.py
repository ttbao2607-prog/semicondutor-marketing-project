import json, hashlib, importlib.util, tempfile, shutil
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path('D:/linkedin-awareness-harness-redesign')
BASE='operations/linkedin-imagegen-dogfood/benchmark-2026-10-03'
OWN=ROOT/BASE/'sol'
REL=BASE+'/operator/sol/release.json'
PIN='99bfc3a6b794b8cca4ff4eaaddacbc64bdbb1f400ef055286646bc27accaf68f'
SPEC=BASE+'/sol/spec.json'; RECEIPT=BASE+'/sol/preflight.json'; DISPATCH=BASE+'/sol/planned-dispatch.json'; VIEWER=BASE+'/sol/viewer.json'
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,v): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
s=importlib.util.spec_from_file_location('gate',ROOT/'scripts/verify_imagegen_preflight.py');gate=importlib.util.module_from_spec(s);s.loader.exec_module(gate)
def main():
 start=datetime.now(timezone.utc).isoformat()
 pins=load(ROOT/BASE/'operator/trusted-pins-sol.json')['sol']
 assert pins['release']['path']==REL and pins['release']['sha256']==PIN
 protected=[p for p in (ROOT/BASE/'common').glob('*') if p.is_file()]+[ROOT/'scripts/verify_imagegen_preflight.py',ROOT/'tests/test_imagegen_preflight.py',ROOT/'operations/Ad_Artifact_Editorial_QA_Gate.md',OWN/'contract.json',OWN/'call-draft.json',OWN/'viewer.json']
 before={p.relative_to(ROOT).as_posix():sha(p) for p in protected}
 spec={'schema_version':1,'revision':'benchmark-sol-f2-a2-spec-v1',**{k:pins[k] for k in ('release','contract','copy','review')},'calls':[load(OWN/'call-draft.json')]}
 assert not (ROOT/SPEC).exists()
 write(ROOT/SPEC,spec)
 receipt,state=gate.validate(ROOT,REL,PIN,SPEC,scope_call_id='F2_A2');write(ROOT/RECEIPT,receipt)
 call=spec['calls'][0]
 proposal={'schema_version':1,'record_kind':'PLANNED_DISPATCH_CHECK','call_id':'F2_A2','preflight_sha256':sha(ROOT/RECEIPT),'prompt':call['prompt'],'prompt_sha256':call['prompt_sha256'],'reference_paths':[r['path'] for r in call['references']],'output_path':call['output_path']}
 write(ROOT/DISPATCH,proposal)
 dispatch,_=gate.dispatch_check(ROOT,REL,PIN,SPEC,RECEIPT,DISPATCH);write(OWN/'dispatch-check.json',dispatch)
 viewer,_=gate.viewer_check(ROOT,REL,PIN,SPEC,VIEWER);write(OWN/'viewer-check.json',viewer)
 input_paths=set(receipt['input_hashes'])|{SPEC,RECEIPT,DISPATCH,VIEWER}
 cases=[]
 def case(name,mode,mutate):
  temp=Path(tempfile.mkdtemp(prefix='isolated-',dir=OWN)).resolve()
  assert temp.is_relative_to(OWN.resolve()) and temp.parent==OWN.resolve()
  try:
   for namepath in input_paths:
    target=temp/namepath;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/namepath).read_bytes())
   mutate(temp)
   try:
    if mode=='preflight':gate.validate(temp,REL,PIN,SPEC,scope_call_id='F2_A2')
    elif mode=='dispatch':gate.dispatch_check(temp,REL,PIN,SPEC,RECEIPT,DISPATCH)
    else:gate.viewer_check(temp,REL,PIN,SPEC,VIEWER)
    outcome='ACCEPTED';error=None
   except (gate.Invalid,OSError,TypeError,KeyError,AttributeError) as exc:outcome='REJECTED';error=str(exc)
   cases.append({'case':name,'mode':mode,'expected':'REJECTED','observed':outcome,'matched_expectation':outcome=='REJECTED','error':error})
  finally:
   assert temp.is_relative_to(OWN.resolve()) and temp.parent==OWN.resolve() and temp.name.startswith('isolated-')
   shutil.rmtree(temp)
 def bytes_change(path):
  def mutate(t):p=t/path;p.write_bytes(p.read_bytes()+b' ')
  return mutate
 def json_change(path,fn):
  def mutate(t):v=load(t/path);fn(v);write(t/path,v)
  return mutate
 contract=load(OWN/'contract.json')
 for name,path in [('changed contract',pins['contract']['path']),('changed copy',pins['copy']['path']),('changed review',pins['review']['path']),('changed source',contract['sources'][0]['path']),('changed reference',contract['references'][0]['path'])]:case(name,'preflight',bytes_change(path))
 case('changed prompt','preflight',json_change(SPEC,lambda v:v['calls'][0].update(prompt=v['calls'][0]['prompt']+' extra')))
 case('stale receipt after spec revision change','dispatch',json_change(SPEC,lambda v:v.update(revision='changed-spec-v2')))
 case('substituted release versus parent pin','preflight',json_change(REL,lambda v:v.update(revision='substituted-release')))
 case('changed dispatch prompt','dispatch',json_change(DISPATCH,lambda v:v.update(prompt=v['prompt']+' extra')))
 case('changed dispatch reference list','dispatch',json_change(DISPATCH,lambda v:v.update(reference_paths=list(reversed(v['reference_paths'])))))
 case('changed dispatch receipt hash','dispatch',json_change(DISPATCH,lambda v:v.update(preflight_sha256='0'*64)))
 def occupied(t):p=t/call['output_path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b'occupied')
 case('occupied selected output at preflight','preflight',occupied)
 case('occupied selected output at dispatch','dispatch',occupied)
 for field,value in [('internal_notes','repo-only'),('metadata',{'review':'internal'}),('hidden_html','<div hidden>internal</div>'),('attachments',['internal-review.json'])]:case('viewer extra '+field,'viewer',json_change(VIEWER,lambda v,f=field,x=value:v.update({f:x})))
 case('viewer changed approved text','viewer',json_change(VIEWER,lambda v:v['ads'][0]['cards'][0].update(headline='Changed wording')))
 after={p.relative_to(ROOT).as_posix():sha(p) for p in protected}
 assert before==after
 result={'schema_version':1,'start_utc':start,'end_utc':datetime.now(timezone.utc).isoformat(),'trusted_release_path':REL,'parent_supplied_release_sha256':PIN,'positive_checks':{'preflight':receipt['mechanical_verdict'],'dispatch_check':dispatch['mechanical_verdict'],'viewer_check':viewer['mechanical_verdict']},'actual_dispatch_observed':False,'negative_cases':cases,'negative_case_count':len(cases),'all_expected_rejections_observed':all(c['matched_expectation'] for c in cases),'protected_hashes_before':before,'protected_hashes_after':after,'temporary_roots_removed':True,'semantic_verdict':'NOT_ASSESSED','creative_verdict':'INSUFFICIENT_EVIDENCE','stage_result':'MECHANICAL_CHECKS_COMPLETE_FOR_PARENT_AUDIT','limits':'No generation, rendered review, content acceptance, or shared test-suite execution.'}
 write(OWN/'dogfood-results.json',result)
 print(json.dumps({'stage_result':result['stage_result'],'positive_checks':result['positive_checks'],'negative_case_count':len(cases),'all_expected_rejections_observed':result['all_expected_rejections_observed'],'errors':[(c['case'],c['error']) for c in cases]},ensure_ascii=True))
if __name__=='__main__':main()
