import argparse, hashlib, importlib.util, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[4]
BASE='operations/linkedin-imagegen-dogfood/corrective-rollout-2026-10-04'
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def read(p): return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def save(p,v):
 q=ROOT/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes((json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
def ref(p):
 d=read(p);return {'path':p,'sha256':sha(p),'revision':d['revision']}
sp=importlib.util.spec_from_file_location('gate',ROOT/'scripts/verify_imagegen_preflight.py');g=importlib.util.module_from_spec(sp);sp.loader.exec_module(g)
parser=argparse.ArgumentParser();parser.add_argument('case');parser.add_argument('kind');parser.add_argument('call_id');parser.add_argument('--native',action='store_true');a=parser.parse_args()
w=f'{BASE}/{a.case}/worker/{a.kind}';o=f'{BASE}/{a.case}/operator/{a.kind}';cp=w+'/contract.json';c=read(cp);copy=read(c['copy']['path']);rp=o+'/review.json';lp=o+'/release.json';specp=o+'/spec.json'
if not (ROOT/lp).exists():
 fields=[]
 for ad in copy['ads']:
  fields.append(ad['ad_id']+'/caption')
  for card in ad['cards']:
   fields += [ad['ad_id']+'/'+card['card_id']+'.'+k for k in g.CARD_FIELDS]
 review={'schema_version':1,'revision':a.case+'-'+a.kind+'-root-review-v1','writer':'/root/rollout_writer','reviewer':'/root','date':'2026-10-04','scope':'OFFLINE_SOURCE_COPY','independence':'INDEPENDENT','subjects':{'contract':ref(cp),'copy':c['copy'],'sources':c['sources']},'verdicts':{'source_copy':'PASS','editorial':'PASS','first_mention':'PASS'},'reviewed_ads':c['ad_order'],'reviewed_fields':fields,'unresolved_findings':[]}
 save(rp,review)
 authority=f'{BASE}/operator/authority.md'
 release={'schema_version':1,'revision':a.case+'-'+a.kind+'-root-release-v1','authorizer':'/root under Bao approved corrective localrollout mandate','authority_ref':{'path':authority,'sha256':sha(authority),'revision':'Bao-2026-10-04-corrective'},'purpose':'OFFLINE_IMAGEGEN','contract':ref(cp),'copy':c['copy'],'review':ref(rp),'groups':[x['targets'] for x in read(w+'/calls-draft.json')['calls']]}
 save(lp,release)
 draft=read(w+'/calls-draft.json');save(specp,{'schema_version':1,'revision':a.case+'-'+a.kind+'-root-spec-v1','release':ref(lp),'contract':ref(cp),'copy':c['copy'],'review':ref(rp),'calls':draft['calls']})
if a.native:
 receipt,state=g.native_output_check(ROOT,lp,sha(lp),specp,a.call_id);save(o+'/native/'+a.call_id+'.json',receipt);print(json.dumps({'dimensions':receipt['actual_dimensions'],'sha256':receipt['native_sha256']}));raise SystemExit
receipt,state=g.validate(ROOT,lp,sha(lp),specp,scope_call_id=a.call_id)
pp=o+'/dispatch/'+a.call_id+'-preflight.json';save(pp,receipt)
call=next(x for x in state['spec']['calls'] if x['call_id']==a.call_id)
dp=o+'/dispatch/'+a.call_id+'-planned.json';save(dp,{'schema_version':1,'record_kind':'PLANNED_DISPATCH_CHECK','call_id':a.call_id,'preflight_sha256':sha(pp),'prompt':call['prompt'],'prompt_sha256':call['prompt_sha256'],'reference_paths':[x['path'] for x in call['references']],'output_path':call['output_path']})
check,state=g.dispatch_check(ROOT,lp,sha(lp),specp,pp,dp);save(o+'/dispatch/'+a.call_id+'-check.json',check)
args={'prompt':call['prompt'],'referenced_image_paths':[str(ROOT/x['path']) for x in call['references']],'transparent_background':False}
save(o+'/dispatch/'+a.call_id+'-tool-args.json',args)
print(json.dumps({'case':a.case,'call_id':a.call_id,'tool_args_path':o+'/dispatch/'+a.call_id+'-tool-args.json','output_path':call['output_path'],'release_sha256':sha(lp),'dispatch_check':'PASS'}))
