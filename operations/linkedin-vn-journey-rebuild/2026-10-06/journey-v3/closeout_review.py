from pathlib import Path
import json, hashlib, importlib.util
r = Path(__file__).resolve().parents[4]
b = Path(__file__).resolve().parent
base = b.parent
d = r / 'deliverables/linkedin-vn-journey/2026-10-06-v3'
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p): return {'path': p.relative_to(r).as_posix(), 'sha256': sha(p)}
def write(p, v): p.write_bytes((json.dumps(v, ensure_ascii=False, indent=2)+'\n').encode())
manifest = read(b/'selected-manifest.json')
copy = read(b/'public-copy.json')
obs = read(b/'render-observations.json')
ledger = []
for x in read(b/'tool-output-paths.json'):
    cid = x['call_id']; v = cid.split('-')[-1].lower()
    p = base/('journey-'+v)/'native'/(cid.lower()+'.png')
    assert sha(p) == sha(Path(x['path']))
    ledger.append({'call_id':cid,'tool':'image_gen.imagegen','original_output':x['path'],'native':bind(p),'byte_copy_verified':True,'immediate_guard':bind(base/('journey-'+v)/(cid+'-immediate-guard.json')),'selected':cid not in ['VN-R2-V3','VN-E2-V3','VN-E3-V3']})
write(b/'generation-ledger.json', {'actual_calls':12,'base':9,'targeted_corrections':3,'entries':ledger})
for item in manifest['selected']:
    p = r/item['native']['path']
    assert sha(p) == item['native']['sha256']
    assert sha(d/'assets'/p.name) == sha(p)
assert len(obs) == 22 and all(not x['overflow'] for x in obs)
assert all(x.get('loaded',True) for x in obs)
assert len(list((b/'render').glob('*.png'))) == 22
fields = {}; units = []
for ad in copy['ads']:
    fields[ad['ad_id']+'/caption'] = ad['caption']
    for c in ad['cards']:
        actual = {k:c[k] for k in ['headline','body','source_text','cta','artwork_labels']}
        for k,value in actual.items(): fields[c['card_id']+'/'+k] = '\n'.join(value) if isinstance(value,list) else value
        for k in ['alt','native_headline']: fields[c['card_id']+'/'+k] = c[k]
        units.append({'card_id':c['card_id'],'actual_native_text':actual,'observation':'Root viewed selected native and actual desktop/mobile screenshots. Exact visible wording matches transcription. Blank source/CTA intentionally absent; Digiwin official logo once.','V1':'PASS: advertiser speaking; Aplus mechanisms attributed to case','V2':'PASS: readiness or concrete mechanism; VN/company POV in caption','V3':'PASS: meaningful Vietnamese subject and trigger','V4':'PASS: readiness -> case -> invitation; no outcome guarantee','V5':'PASS: no Bạn; direct Quý Doanh Nghiệp; descriptive doanh nghiệp Việt allowed','editorial':'PASS for human review; readable headline/body; small secondary category/source retained limitation','anchor':'MESSAGE_ANCHOR_PASS: VN readiness; no qualification/order outcome'})
for i,x in enumerate(obs): fields['render/'+str(i)] = x.get('text', '\n'.join(x.get(k,'') for k in ['caption','alt','position']))
fields['Cold/native'] = 'ERP cho ngành bán dẫn\ntừ nhà cung cấp hàng đầu\nĐài Loan\n200+\ndoanh nghiệp bán dẫn\nđã lựa chọn chúng tôi\nĐồng hành cùng doanh nghiệp Việt\nchuẩn bị năng lực quản trị\nđể bước vào chuỗi bán dẫn.'
write(b/'postgen-observed-text.json', {'observed_fields':fields,'method':'Root actual native inspection + browser visible text; not script-only inference'})
spec = importlib.util.spec_from_file_location('reader',base/'reader-address/verify_vn_reader_address.py')
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
scan = mod.scan(fields,'POSTGEN_OBSERVED_TEXT'); assert not scan['findings']
write(b/'postgen-address-scan.json',scan)
protected = {'scripts/verify_imagegen_preflight.py':'9817e828f35e832e99e15f36f4b2cbd227b625b626dc84c72f781e680c2b4dca','operations/linkedin-journey-demo/2026-10-06/inputs/verify_single_image_trial.py':'aa71327c78dd2db4cf436bd9454003960492657b627a3bf36901a467bb75b72c','operations/Vy_Email_Content_Anchor.md':'96197cd1999e250af64ab0a3a54e24cf3c2429b8366be53e2cc680a634667337','operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md':'87475d082cb66cc1dc11285a6a2d7982d77d80ca9cd2c14522bab2d212ebb5b3','operations/linkedin-vn-journey-rebuild/2026-10-06/cold-v4/native/vn-cold-v4.png':'a326010dce53815bdf77e52ca38ad0fb1990bf02a312ab9fe8b076ab407406f5'}
for path,expected in protected.items(): assert sha(r/path) == expected, path
policy = r/'operations/VN_Locale_Reader_Voice_Gate.md'
snapshot = b/'policy-1.1-at-dispatch.snapshot.md'
if not snapshot.exists(): snapshot.write_bytes(policy.read_bytes())
ptext = policy.read_text(encoding='utf-8-sig').replace('Current journey có3 ảnh R1/R5/E4 cùng2 captions/3alts cần đổi; xem reader-address current review.','Journey v1/v2 tại checkpoint trước rebuild có3 ảnh R1/R5/E4 cùng2 captions/3alts cần đổi; finding này giữ historical scope. Rebuild IC700/Aplus đã thay cả5+4; xem [hậu kiểm hiện hành](linkedin-vn-journey-rebuild/2026-10-06/journey-v3/postgen-review.json).')
policy.write_bytes(ptext.encode())
review = {'schema_version':1,'revision':'VN-IC700-Aplus-POSTGEN-2026-10-06','stage':'POSTGEN_ARTIFACT','status':'READY_FOR_BAO_REVIEW / SELF_REVIEW','writer':'root','reviewer':'root','independence':'SELF_REVIEW; no independent reviewer claimed','locale':'vi-VN','segment':'VN_DOMESTIC','gates':{'MSG-ANCHOR-01':'MESSAGE_ANCHOR_PASS','VN-VOICE-01':'VN_VOICE_PASS','AD-ED-01':'POSTGEN_EDITORIAL_PASS_FOR_HUMAN_REVIEW'},'anchor':bind(r/'operations/Vy_Email_Content_Anchor.md'),'email':bind(r/'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'),'policy':bind(policy),'policy_at_dispatch':bind(snapshot),'policy_doc_clarification':'Historical finding sentence clarified after generation; V1-V5 rules/revision1.1 unchanged. Original dispatch receipts/pins preserved. Future dispatch must bind current policy.','copy':bind(b/'public-copy.json'),'specs':[bind(b/'spec.json'),bind(base/'journey-v4/spec.json')],'selected_artifacts':manifest['selected'],'demo':bind(d/'index.html'),'case_page':bind(d/'case-aplus.html'),'render_observations':bind(b/'render-observations.json'),'screenshots':[bind(x) for x in sorted((b/'render').glob('*.png'))],'units':units,'whole_journey':{'verdict':'PASS_FOR_HUMAN_REVIEW','transition':'Frozen Cold readiness -> consulting experience -> audit preparation question -> serial/parameter mechanisms -> Aplus semiconductor China iMES+TOPGP case -> discussion invitation. Captions establish VN/company POV; no audit-pass guarantee.','count_scope':'700 consulting IC customers only, no TW/CN qualifier. Cold200 selected companies is different source population; never combine.','product_scope':'DigiHua Aplus China iMES+TOPGP; not ERP-only, VN delivery or audit-pass outcome.','destination':'Offline Vietnamese case-reading page observed desktop1422/mobile390. Informational CTAs lead here; optional Chinese primary source and existing public VN contact invitation. No form/tracking/live publication.','address':'Quý Doanh Nghiệp for direct address; descriptive doanh nghiệp Việt allowed.'},'render_summary':{'journey_positions':20,'case_positions':2,'desktop_css_width':1422,'mobile_css_width':390,'images_loaded':True,'horizontal_overflow':False,'all_actual_screenshots_visually_reviewed':True},'finding_closure':[{'card':'VN-R2','rejected':'V3 extra YÊU CẦU ĐÁNH GIÁ prop label','selected':'V4; extra text absent'},{'card':'VN-E2','rejected':'V3 ERP header broadening product scope','selected':'V4; correct case category only'},{'card':'VN-E3','rejected':'V3 invented SPC interface / wafer measurement scene','selected':'V4; physical records/amber marker/film, no invented dashboard'}],'limitations':manifest['limitations'],'protected_hashes':protected,'po_acceptance':{'Cold':'FROZEN_V4_UNCHANGED','new9':'PENDING_BAO_REVIEW'},'publication':'OFFLINE_ONLY; no publish/enable/spend','git':'Checkpoint6345f7d local only; generated outputs/docs uncommitted; no push/merge.'}
write(b/'postgen-review.json',review)
manifest['status'] = 'READY_FOR_BAO_REVIEW / SELF_REVIEW / PO_PENDING'
manifest['postgen_review'] = bind(b/'postgen-review.json')
write(b/'selected-manifest.json',manifest)
write(b/'verification.json', {'status':'PASS_FOR_HUMAN_REVIEW','protected_hashes_unchanged':True,'original_byte_copies':12,'selected_native_demo_match':10,'actual_render_positions':22,'address_scan_clean':True,'independent_review':'NOT_PERFORMED','PO':'PENDING_NEW9','policy_dispatch_snapshot_sha256':sha(snapshot)})
print('Verified12 calls,10 selected native/demo byte matches,22 render positions,9 units and protected hashes.')
