import importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];BASE=Path(__file__).resolve().parent.relative_to(ROOT).as_posix()
plan=json.loads((ROOT/BASE/('corrective-dispatch-plan.json' if '--corrective' in sys.argv else 'dispatch-plan.json')).read_text(encoding='utf-8'));job=plan['calls'][int(sys.argv[1])]
s=importlib.util.spec_from_file_location('guard',ROOT/'scripts/verify_imagegen_anchor_preflight.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
f=job['folder'];result=m.check(ROOT,f+'/release.json',job['release_sha256'],f+'/spec.json',f+'/anchor-review.json',job['review_sha256'],job['call_id'],'FDI',plan['persona'],plan['route'])
p=ROOT/f/'dispatch'/(job['call_id']+'-fresh-preflight.json');p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'job':job,'tool_args':result['tool_args']},ensure_ascii=True))
