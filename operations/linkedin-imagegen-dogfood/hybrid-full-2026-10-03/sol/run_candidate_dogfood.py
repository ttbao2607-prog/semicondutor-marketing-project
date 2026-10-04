"""Isolated fixture-only mutations of copied parent-bound candidate inputs; no image calls."""
from pathlib import Path
import json, hashlib, importlib.util, tempfile, shutil, datetime
ROOT=Path('D:/linkedin-awareness-harness-redesign')
BASE='operations/linkedin-imagegen-dogfood/hybrid-full-2026-10-03'
OWN=ROOT/BASE/'sol'
REL=BASE+'/operator/sol/release.json'; SPEC=BASE+'/operator/sol/spec.json'
PIN='bb47aa533d694fd6c1caf2cc345a761c7d54a4e7a9479fed782f013453da129a'
CALL='F2_A1'
RECEIPT='fixture-only/preflight.json'; DISPATCH='fixture-only/planned-dispatch.json'; VIEWER='fixture-only/viewer.json'
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
s=importlib.util.spec_from_file_location('gate',ROOT/'scripts/verify_imagegen_preflight.py');gate=importlib.util.module_from_spec(s);s.loader.exec_module(gate)
def main():
 started=datetime.datetime.now(datetime.timezone.utc).isoformat()
 assert sha(ROOT/REL)==PIN
 release=load(ROOT/REL);contract=load(ROOT/release['contract']['path']);spec=load(ROOT/SPEC)
 paths={REL,SPEC,release['authority_ref']['path'],release['contract']['path'],release['copy']['path'],release['review']['path']}
 paths.update(s['path'] for s in contract['sources']);paths.update(s['path'] for s in contract['references'])
 before={p:sha(ROOT/p) for p in paths}; before['scripts/verify_imagegen_preflight.py']=sha(ROOT/'scripts/verify_imagegen_preflight.py')
 cases=[];positives=[]
 def setup():
  t=Path(tempfile.mkdtemp(prefix='fixture-only-candidate-',dir=OWN)).resolve()
  assert t.parent==OWN.resolve() and t.is_relative_to(OWN.resolve())
  for path in paths:
   target=t/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/path).read_bytes())
  # Deliberately never copy real native outputs. The selected output is pending in each isolated fixture.
  receipt,_=gate.validate(t,REL,PIN,SPEC,scope_call_id=CALL);write(t/RECEIPT,receipt)
  call=next(c for c in spec['calls'] if c['call_id']==CALL)
  proposal={'schema_version':1,'record_kind':'PLANNED_DISPATCH_CHECK','call_id':CALL,'preflight_sha256':sha(t/RECEIPT),'prompt':call['prompt'],'prompt_sha256':call['prompt_sha256'],'reference_paths':[ref['path'] for ref in call['references']],'output_path':call['output_path']}
  write(t/DISPATCH,proposal);(t/VIEWER).write_bytes((ROOT/release['copy']['path']).read_bytes())
  return t
 def cleanup(t):
  assert t.parent==OWN.resolve() and t.is_relative_to(OWN.resolve()) and t.name.startswith('fixture-only-candidate-')
  shutil.rmtree(t)
 def check(t,mode):
  if mode=='preflight':return gate.validate(t,REL,PIN,SPEC,scope_call_id=CALL)[0]
  if mode=='dispatch':return gate.dispatch_check(t,REL,PIN,SPEC,RECEIPT,DISPATCH)[0]
  return gate.viewer_check(t,REL,PIN,SPEC,VIEWER)[0]
 t=setup()
 try:
  for mode in ['preflight','dispatch','viewer']:
   result=check(t,mode);positives.append({'mode':mode,'expected':'PASS','observed':result['mechanical_verdict'],'scope':'ISOLATED_COPIED_REAL_INPUTS_ONLY','actual_dispatch_observed':False})
 finally:cleanup(t)
 def mutate_json(path,fn):
  def mutation(t):v=load(t/path);fn(v);write(t/path,v)
  return mutation
 def bytes_change(path):
  def mutation(t):p=t/path;p.write_bytes(p.read_bytes()+b' ')
  return mutation
 def case(name,mode,mutation):
  t=setup()
  try:
   mutation(t)
   try:check(t,mode);observed='ACCEPTED';error=None
   except (gate.Invalid,OSError,TypeError,KeyError,AttributeError) as exc:observed='REJECTED';error=str(exc)
   cases.append({'case':name,'mode':mode,'expected':'REJECTED','observed':observed,'matched_expectation':observed=='REJECTED','error':error,'scope':'ISOLATED_FIXTURE_ONLY'})
  finally:cleanup(t)
 case('changed contract groups','preflight',mutate_json(release['contract']['path'],lambda v:v['groups'].pop()))
 case('changed campaign style','preflight',mutate_json(release['contract']['path'],lambda v:v['style']['campaign'].update(instructions='altered visual grammar')))
 for name,path in [('changed copy',release['copy']['path']),('changed review',release['review']['path']),('substituted release against parent pin',REL),('changed source',contract['sources'][0]['path']),('changed campaign reference',contract['references'][0]['path'])]:case(name,'preflight',bytes_change(path))
 case('changed assembled prompt','preflight',mutate_json(SPEC,lambda v:v['calls'][0].update(prompt=v['calls'][0]['prompt']+' extra')))
 case('stale receipt after changed spec','dispatch',mutate_json(SPEC,lambda v:v.update(revision='changed-spec-v2')))
 case('changed dispatch prompt','dispatch',mutate_json(DISPATCH,lambda v:v.update(prompt=v['prompt']+' extra')))
 case('changed dispatch reference order','dispatch',mutate_json(DISPATCH,lambda v:v.update(reference_paths=list(reversed(v['reference_paths'])))))
 case('changed dispatch receipt hash','dispatch',mutate_json(DISPATCH,lambda v:v.update(preflight_sha256='0'*64)))
 call=next(c for c in spec['calls'] if c['call_id']==CALL)
 def occupied(t):p=t/call['output_path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b'fixture occupied selected output')
 case('occupied selected output at preflight','preflight',occupied)
 case('occupied selected output at dispatch','dispatch',occupied)
 for key,value in [('internal_notes','fixture internal finding'),('metadata',{'review':'fixture hidden'}),('hidden_html','<div hidden>fixture note</div>'),('attachments',['fixture-review.json'])]:case('viewer extra '+key,'viewer',mutate_json(VIEWER,lambda v,k=key,x=value:v.update({k:x})))
 case('viewer changed approved headline','viewer',mutate_json(VIEWER,lambda v:v['ads'][0]['cards'][0].update(headline='Changed wording')))
 after={p:sha(ROOT/p) for p in paths};after['scripts/verify_imagegen_preflight.py']=sha(ROOT/'scripts/verify_imagegen_preflight.py')
 assert before==after
 assert len(cases)==19 and all(c['matched_expectation'] for c in cases)
 report={'schema_version':1,'record_kind':'ISOLATED_CANDIDATE_DOGFOOD','stage_result':'MECHANICAL_DOGFOOD_COMPLETE_FOR_PARENT_AUDIT','start_utc':started,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parent_supplied_release_path':REL,'parent_supplied_release_sha256':PIN,'selected_fixture_call':CALL,'authentic_review_release_copied_without_edit_for_baseline':'No new real review/release or authority was authored; mutations are fixture-only and cannot authorize generation','positive_checks':positives,'negative_cases':cases,'negative_case_count':len(cases),'all_expected_rejections_observed':True,'real_input_hashes_before':before,'real_input_hashes_after':after,'real_native_outputs_read_or_copied':False,'temporary_roots_removed':True,'generation_calls':0,'actual_dispatch_observed':False,'semantic_verdict':'NOT_ASSESSED_BY_THIS_MECHANICAL_DOGFOOD','creative_verdict':'INSUFFICIENT_EVIDENCE','runtime_identity':'Parent previously accepted reused Sol low; parent verifies current turn after completion'}
 write(OWN/'dogfood-results.json',report)
 print(json.dumps({'stage_result':report['stage_result'],'positive_checks':len(positives),'negative_cases':len(cases),'expected_rejections':True,'real_inputs_unchanged':before==after,'errors':[(c['case'],c['error']) for c in cases]}))
if __name__=='__main__':main()
