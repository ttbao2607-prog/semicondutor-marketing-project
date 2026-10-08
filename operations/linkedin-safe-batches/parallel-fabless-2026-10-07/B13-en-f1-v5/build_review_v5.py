"""Versioned v5 viewer: six edited/new explanation PNGs and five exact v4 reuses."""
from prepare_draft import *
import re, shutil, html
from PIL import Image
OUT='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v5'
V4='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v4'
OLD=Path(BASE).with_name('B13-en-f1-v1').as_posix()
out=ROOT/OUT;out.mkdir(exist_ok=True,parents=True);(out/'assets').mkdir(exist_ok=True)
oldcopy=load(V4+'/selected-copy.json')['cards'];oldpins={x['card_id']:x for x in load(V4+'/manifest.json')['artwork']}
oldprompts={x['card_id']:x for x in load(V4+'/selected-prompts.json')['calls']}
ad=load(BASE+'/explanation-copy.json')['ads'][0]
jobs={x['card_id']:x for x in load(BASE+'/dispatch-plan.json')['calls']}
units=[oldcopy[0]]+[dict(x,caption=ad['caption'],stage='explanation') for x in ad['cards']]+[x for x in oldcopy if x['stage']=='proof']
cards=[];pins=[];prompts=[]
for i,x in enumerate(units,1):
 cid=x['card_id'];reused=cid not in jobs
 src=oldpins[cid]['path'] if reused else jobs[cid]['output_path']
 dest=OUT+'/assets/'+str(i).zfill(2)+'-'+cid.lower()+'.png';shutil.copyfile(ROOT/src,ROOT/dest)
 assert sha(src)==sha(dest)
 with Image.open(ROOT/dest) as im:assert im.size==(1254,1254) and im.format=='PNG'
 pins.append(dict(card_id=cid,path=dest,sha256=sha(dest),source=src,reused=reused,transformation=False))
 cards.append(dict(x,image=Path(dest).relative_to(OUT).as_posix(),status='NATIVE_REVIEWED_RENDER_PENDING'))
 if reused:
  p=dict(oldprompts[cid],reused=True,generated=False,prior_selected_manifest=dict(path=V4+'/manifest.json',sha256=sha(V4+'/manifest.json')))
 else:
  j=jobs[cid];c=load(j['folder']+'/spec.json')['calls'][0]
  p=dict(card_id=cid,call_id=j['call_id'],prompt=c['prompt'],prompt_sha256=c['prompt_sha256'],referenced_image_paths=[r['path'] for r in c['references']],generated=True,reused=False)
 prompts.append(p)
put(OUT+'/selected-copy.json',dict(revision='b13-review-copy-v5-six-explanation',cards=cards))
put(OUT+'/selected-prompts.json',dict(revision='b13-review-prompts-v5',tool='built-in image_gen',calls=prompts))
viewer=(ROOT/V4/'index.html').read_text(encoding='utf-8')
notice='11 of 11 artwork units present · v5: six explanation cards, including Vietnam consulting and implementation. Offline draft; rendered review and whole-journey acceptance pending.'
viewer=re.sub(r'<div class="notice">.*?</div>','<div class="notice">'+notice+'</div>',viewer,count=1,flags=re.S)
data=json.dumps(cards,ensure_ascii=False).replace('</','<\\/')
viewer=re.sub(r'const data=.*?;let pos=0;',lambda _: 'const data='+data+';let pos=0;',viewer,count=1,flags=re.S)
viewer=viewer.replace('B13 · Outsourced-production journey','B13 v5 · Outsourced-production journey')
(out/'index.html').write_text(viewer,encoding='utf-8')
shutil.copyfile(ROOT/V4/'case-reader.html',out/'case-reader.html')
style=re.search(r'<style>.*?</style>',viewer,re.S).group(0)
head='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
e=html.escape
compact=head+'<title>B13 v5 actual eleven artwork</title>'+style+'<main><h1>B13 v5 · Actual 11 artwork</h1><p>Offline · Feed333px · reviewed copy and actual selected PNGs.</p>'+''.join('<article id="'+e(c['card_id'])+'"><h2>'+e(c['card_id'])+'</h2><p>'+e(c['caption'])+'</p><img style="display:block;width:333px;max-width:100%;height:auto" src="'+e(c['image'])+'" alt="'+e(c['alt'])+'"><p>'+e(c['native_headline'])+'</p></article>' for c in cards)+'</main></html>'
(out/'compact-review.html').write_text(compact,encoding='utf-8')
# Explicit desktop640/feed333/mobile surfaces permit independent rendered inspection.
for size in [333,640]:
 page=head+'<title>B13 v5 actual '+str(size)+'px audit</title>'+style+'<main><h1>B13 v5 · '+str(size)+'px audit</h1>'+''.join('<article><h2>'+e(c['card_id'])+'</h2><p>'+e(c['caption'])+'</p><img style="display:block;width:'+str(size)+'px;max-width:100%;height:auto" src="'+e(c['image'])+'" alt="'+e(c['alt'])+'"><p>'+e(c['native_headline'])+'</p></article>' for c in cards)+'</main></html>'
 (out/('audit-'+str(size)+'.html')).write_text(page,encoding='utf-8')
c=next(x for x in cards if x['card_id']=='F1-A6')
team=head+'<title>B13 v5 · Vietnam team card</title>'+style+'<main><h1>B13 v5 · Vietnam team</h1><article><p>'+e(c['caption'])+'</p><img style="display:block;width:333px;max-width:100%;height:auto" src="'+e(c['image'])+'" alt="'+e(c['alt'])+'"><p>'+e(c['native_headline'])+'</p></article><a href="index.html">Review full journey</a></main></html>'
(out/'vietnam-team-audit.html').write_text(team,encoding='utf-8')
put(OUT+'/manifest.json',dict(revision='b13-review-manifest-v5-six-explanation',status='REVIEW_DRAFT_RENDER_GATE_PENDING',imagegen_original=6,imagegen_corrective=0,new_explanation_card=1,sequence_edits=5,reused_pngs=5,generated_selected=6,total_selected=11,planned_units=11,not_generated=[],prior_actual_calls=14,cumulative_actual_calls=20,tool='built-in image_gen',artwork=pins,viewer_sha256=sha(OUT+'/index.html'),reader_sha256=sha(OUT+'/case-reader.html'),raster_transformation=False,zip=False))
(out/'README.md').write_text('''# B13 Fabless F1 English · v5

11 selected native1254-square PNGs: cold1 + explanation6 + China proof4. New explanation card6: Consulting and implementation in Vietnam; local service presence backed by official Digiwin Vietnam publication. Existing explanation1–5 revised only sequence denominator5→6 through built-in ImageGen; cold and4proof PNGs reused byte-identical from PO visually accepted v4. V5=6calls,0corrective,5reuse; historical14calls retained separately, cumulative20. Reader byte-identical. No Vietnam Fabless deployment/result/team headcount or all-team language claim.

Offline REVIEW_DRAFT_RENDER_GATE_PENDING until current rendered evidence is reconciled in the postgen receipt. Native text/source/journey review is SELF_REVIEW, not independent/native-market certification. Open index.html, compact-review.html and vietnam-team-audit.html. Prompt set: selected-prompts.json. No raster transform/ZIP/frozen-core/adapter/shared-canonical/Git/live change. Stop before B14. Prior v1-v4 findings/receipts unchanged.
''',encoding='utf-8')
print('v5 saved:11 units,6 explanation,6calls+5reuse; reader unchanged.')
