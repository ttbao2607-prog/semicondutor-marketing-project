"""Package frozen bytes/copy into offline review HTML; no image transformation."""
import base64, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
V2 = ROOT / 'operations/linkedin-awareness-execution/production-imagegen-v2'
COPY = V2 / 'revised-copy-vi-v2.json'
mapping = {
 'A1':'a1-pilot/A1-v1-native.png','A2':'remaining-pilot/A2-v3-native.png',
 'A3':'critical-pilot/A3-v1-native.png','A4':'remaining-pilot/A4-v2-native.png',
 'A5':'critical-pilot/A5-v1-native.png','B1':'remaining-pilot/B1-v2-native.png',
 'B2':'remaining-pilot/B2-v2-native.png','B3':'remaining-pilot/B3-v2-native.png',
 'B4':'remaining-pilot/B4-v2-native.png','B5':'critical-pilot/A5-v1-native.png'}
sources=[]
def embed(path, id, mime):
 b=path.read_bytes(); sources.append({'id':id,'original_path':path.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'embedded_without_transform':True})
 return 'data:'+mime+';base64,'+base64.b64encode(b).decode('ascii')
copy=json.loads(COPY.read_text(encoding='utf-8-sig'))
copy_bytes=COPY.read_bytes()
sources.append({'id':'revised-copy-json','original_path':COPY.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(copy_bytes).hexdigest(),'bytes':len(copy_bytes)})
for rec in copy['records']: rec['image']=embed(V2/mapping[rec['id']],rec['id'],'image/png')
logo=embed(ROOT/'operations/linkedin-awareness-execution/production-r3/dependencies/digiwin-logo.webp','official-logo','image/webp')
template=(OUT/'template.html').read_text(encoding='utf8')
html=template.replace('__COPY_JSON__',json.dumps(copy,ensure_ascii=False).replace('</','<\\/')).replace('__LOGO_URI__',logo)
(OUT/'index.html').write_text(html,encoding='utf8')
(OUT/'source-map.json').write_text(json.dumps({'baseline':'42ec8ce32c37022ec0775987ea93630cea8ab207','status':'OFFLINE_SIMULATION_RENDER_PENDING','sources':sources,'historical_differences':['A1/A3 PNG retain illustration label omitted in revised copy.','A1 PNG retains duplicate DIGIWIN header.','A3 PNG retains generic check marks.','A5/B5 PNG retains original em dash; revised copy uses period.'],'source_constraints':{'help':'https://www.linkedin.com/help/linkedin/answer/a423087','tips':'https://business.linkedin.com/advertise/ads/sponsored-content/carousel-ads/tips?product=sales','help_observed':'150 recommended introductory characters,255max,headline2lines','tips_retrieval':'tool unavailable; partial-next-card treatment supplied in parent mandate, not newly verified'}} ,ensure_ascii=False,indent=2),encoding='utf8')
print('Saved index.html bytes='+str((OUT/'index.html').stat().st_size)+'; 10card records embedded; images unchanged.')
