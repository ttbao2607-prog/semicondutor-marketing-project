"""Build the authorized reader preview once all five approved scenario native files exist. No generation or browser control."""
from pathlib import Path
import json, hashlib, html, datetime, struct
ROOT=Path('D:/linkedin-awareness-harness-redesign')
RUN=ROOT/'operations/linkedin-imagegen-dogfood/corrective-rollout-2026-10-04/O4-Q'
OWN=RUN/'worker'
OUTPUT=Path('D:/linkedin-awareness-harness-redesign/operations/linkedin-imagegen-dogfood/corrective-rollout-2026-10-04/O4-Q/public')
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def escape(v):return html.escape(v,quote=True)
def save_internal(p,obj):p.write_bytes((json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
def main():
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument("--selection",default="selected-origins.json");args=parser.parse_args()
 copy_path=RUN/'common/o4-q-copy.json';copy=load(copy_path);origin=load(OWN/args.selection);brief={'references':[{'role':'brand_asset',**origin['logo']}]};destinations_map={'O4-Q-B':'https://solutions.digiwin.com.vn/semiconductor-osat?lang=vi'}
 sources={cid:ROOT/item['path'] for cid,item in origin['cards'].items()}
 assert all(sha(sources[cid])==item['sha256'] for cid,item in origin['cards'].items())
 assert sha(copy_path)==origin['copy']['sha256']
 missing=[p.name for p in sources.values() if not p.is_file()]
 if missing:
  print(json.dumps({'build_result':'WAITING_FOR_NATIVE_FILES','missing':missing}));return 2
 assert len(sources)==5 and all(len(ad['cards'])==5 for ad in copy['ads'])
 assert OUTPUT.resolve()==Path('D:/linkedin-awareness-harness-redesign/operations/linkedin-imagegen-dogfood/corrective-rollout-2026-10-04/O4-Q/public').resolve()
 logo_ref=next(ref for ref in brief['references'] if ref['role']=='brand_asset');logo=ROOT/logo_ref['path'];assert sha(logo)==logo_ref['sha256']
 source_hashes={p.relative_to(ROOT).as_posix():sha(p) for p in sources.values()};source_hashes[copy_path.relative_to(ROOT).as_posix()]=sha(copy_path);source_hashes[logo.relative_to(ROOT).as_posix()]=sha(logo)
 # Refuse to replace an unrelated pre-existing user bundle.
 assert not OUTPUT.exists() or not any(OUTPUT.iterdir()),'Output bundle already populated; preserve it for review.'
 assets=OUTPUT/'assets';assets.mkdir(parents=True,exist_ok=True)
 for cid,p in sources.items():
  target=assets/(cid.lower()+'.png');target.write_bytes(p.read_bytes());assert sha(target)==sha(p)
 (assets/'digiwin-logo.webp').write_bytes(logo.read_bytes())
 feeds=[]
 for index,ad in enumerate(copy['ads'],1):
  destinations={destinations_map[ad['ad_id']]}
  assert len(destinations)==1
  destination=destinations.pop();assert destination in ['https://solutions.digiwin.com.vn/semiconductor-osat?lang=vi'],destination
  cards=[]
  for i,card in enumerate(ad['cards'],1):
   image='assets/'+card['card_id'].lower()+'.png'
   raw=sources[card['card_id']].read_bytes();assert raw[:8]==b'\x89PNG\r\n\x1a\n';width,height=struct.unpack('>II',raw[16:24]);assert width==height and width>=1080
   cards.append('<article class="card"'+(' hidden' if i!=1 else '')+'><a class="native-link" href="'+image+'" target="_blank" rel="noopener" aria-label="'+escape(card['native_headline'])+'"><img class="artwork" src="'+image+'" alt="'+escape(card['alt'])+'" width="'+str(width)+'" height="'+str(height)+'"></a><p class="native-headline">'+escape(card['native_headline'])+'</p>'+('<a class="reading-link" href="'+escape(destination)+'">'+escape(card['cta'])+'</a>' if card['cta'] else '')+'</article>')
  dots=''.join('<button type="button" class="dot" aria-label="'+str(i)+'/5" aria-pressed="'+('true' if i==1 else 'false')+'"></button>' for i in range(1,6))
  feeds.append('<section class="feed" aria-label="'+escape(ad['cards'][0]['native_headline'])+'"><img class="brand" src="assets/digiwin-logo.webp" alt="Digiwin"><p class="caption">'+escape(ad['caption'])+'</p><div class="cards">'+''.join(cards)+'</div><nav class="navigation" aria-label="'+escape(ad['cards'][0]['native_headline'])+'"><button class="previous" type="button" aria-label="Ảnh trước" disabled>‹</button><div class="dots">'+dots+'</div><span class="position" aria-live="polite" aria-atomic="true">1/5</span><button class="next" type="button" aria-label="Ảnh tiếp">›</button></nav></section>')
 source='''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>'''+escape(copy['ads'][0]['cards'][0]['headline'])+'''</title>
<style>
*{box-sizing:border-box}body{margin:0;padding:16px;background:#fff;color:#0B132B;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:640px;margin:auto;display:grid;grid-template-columns:minmax(0,1fr);gap:24px}.feed{min-width:0;padding:16px;border:1px solid #e3e8f0;border-radius:12px;background:#fff}.brand{display:block;width:126px;max-width:50%;height:auto;margin-bottom:16px}.caption{font-size:16px;line-height:1.5;margin:0 0 16px;overflow-wrap:anywhere}.card[hidden]{display:none}.native-link{display:block}.artwork{display:block;width:100%;height:auto;aspect-ratio:1/1;object-fit:contain}.native-headline{font-size:18px;line-height:1.4;font-weight:600;margin:14px 0;overflow-wrap:anywhere}.reading-link{display:inline-block;color:#0052ff;font-size:16px;line-height:1.5;max-width:100%;overflow-wrap:anywhere}.navigation{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:16px}.navigation>button{width:40px;height:40px;border:1px solid #c8d5e8;background:#fff;color:#0052ff;border-radius:50%;font-size:26px;cursor:pointer}.navigation>button:disabled{opacity:.4;cursor:default}.dots{display:flex;align-items:center;gap:4px}.dot{padding:0;width:28px;height:32px;border:0;background:transparent;cursor:pointer}.dot:after{content:"";display:block;width:8px;height:8px;margin:auto;border-radius:50%;background:#b9c7da}.dot[aria-pressed="true"]:after{background:#0052ff}.position{font-size:14px;min-width:28px}a:focus-visible,button:focus-visible{outline:3px solid #0052ff;outline-offset:3px}@media(max-width:760px){main{grid-template-columns:minmax(0,1fr);gap:24px}.feed{padding:12px}.navigation{gap:6px}.dot{width:26px}.caption{font-size:16px}}
</style>
</head>
<body><main>'''+''.join(feeds)+'''</main>
<script>
for(const feed of document.querySelectorAll('.feed')){
 const cards=[...feed.querySelectorAll('.card')],dots=[...feed.querySelectorAll('.dot')],previous=feed.querySelector('.previous'),next=feed.querySelector('.next'),position=feed.querySelector('.position');let selected=0;
 function show(value){selected=Math.max(0,Math.min(cards.length-1,value));cards.forEach((card,i)=>{card.hidden=i!==selected});dots.forEach((dot,i)=>{dot.setAttribute('aria-pressed',String(i===selected))});previous.disabled=selected===0;next.disabled=selected===cards.length-1;position.textContent=String(selected+1)+'/5'}
 previous.addEventListener('click',()=>show(selected-1));next.addEventListener('click',()=>show(selected+1));dots.forEach((dot,i)=>dot.addEventListener('click',()=>show(i)));
 feed.addEventListener('keydown',event=>{if(event.key==='ArrowLeft'){event.preventDefault();show(selected-1)}if(event.key==='ArrowRight'){event.preventDefault();show(selected+1)}});
}
</script>
</body>
</html>
'''
 (OUTPUT/'index.html').write_bytes(source.encode('utf-8'))
 # Public projection is retained inside the repo for the parent viewer checker; no internal manifest goes in reader export.
 (OWN/'public-copy.json').write_bytes(copy_path.read_bytes())
 files={p.relative_to(OUTPUT).as_posix():sha(p) for p in OUTPUT.rglob('*') if p.is_file()}
 assert len(files)==7 and set(files)=={'index.html','assets/digiwin-logo.webp'}|{'assets/'+cid.lower()+'.png' for cid in sources}
 assert source_hashes=={path:sha(ROOT/path) for path in source_hashes}
 save_internal(OWN/'viewer-build-manifest.json',{'schema_version':1,'built_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'output_directory':str(OUTPUT),'files':files,'input_hashes':source_hashes,'copy_projection':'public-copy.json exact common bytes','cards_per_feed':[5],'native_bytes_unchanged':True,'official_logo_bytes_unchanged':True,'rendered_verdict':'NOT_ASSESSED','navigation_verdict':'SOURCE_ONLY_PARENT_BROWSER_CHECK_REQUIRED','viewer_boundary':'Only HTML, five native PNG and logo in reader export; internal manifest stays repo-only','destinations_from_source_metadata':True})
 print(json.dumps({'build_result':'BUILT_FOR_PARENT_RENDER_AUDIT','files':len(files),'html_sha256':files['index.html'],'rendered_verdict':'NOT_ASSESSED'}));return 0
if __name__=='__main__':raise SystemExit(main())
