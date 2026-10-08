"""Transcribe root's actual B14/B15 review and verify raw-byte bindings.

No generation, image modification, semantic auto-approval or Git mutations.
The observations below are the root review performed in this session.
"""
import hashlib
import json
import subprocess
from pathlib import Path
from collections import Counter
from PIL import Image
from prepare_next_locales import ROOT, LANE, load, put, sha, PERSONA

def ref(path):
    revision = 'actual-byte-artifact-2026-10-07'
    if path.endswith('.json'):
        content = load(path)
        if isinstance(content, dict):
            revision = content.get('revision', content.get('call_id', revision))
    return dict(path=path, sha256=sha(path), revision=revision)

DEL = 'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'
STATUS = 'REVIEW_DRAFT_RENDER_GATE_PENDING'
ROOT_REVIEW = '/root current Fabless session'
ANCHOR = 'operations/Vy_Email_Content_Anchor.md'
EMAIL = 'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'

MEANINGS = [
    'Outsourced chip-production next-decision hook. Lot/stage/report-time body is a preparation question, not owned-factory status or promised system behavior. Cold has two functional labels and no carousel counter or CTA.',
    'Partner-report/lot clarity before next planning step. Exact process-stage question, explanatory category and 1/6. No assertion that a customer has incorrect reports.',
    'Product/lot references and agreed production-period/test classifications. Exact category and 2/6. No invented identifier, test result or record values.',
    'Stage, recorded-time and partner-report source are separate reconciliation objects. Exact category and 3/6. Scene does not assert a completed workflow.',
    'Report format, exchange timing and update-confirmation owner. Exact category and 4/6. No automatic connector or synchronization capability promise.',
    'Shared basis for next decision connects lot/stage/report-time/update responsibility. Exact 5/6 and discussion CTA. Taiwan ERP business-management and separately defined MES production context appear as full source paragraph on white, not ERP-only execution/outcome proof.',
    'Vietnam consulting/implementation team nuance. First-person invitation to discuss report workflows, update ownership and project priorities. Exact 6/6 and Vietnam ERP service attribution. No headcount, teamwide-language promise, delivery guarantee or local Fabless result.',
    'Provider first-person introduction from ERP to smart manufacturing. Exact 1/4, company-introduction provenance. No customer testimonial, deployment count or geographic proof.',
    'Explicit China chip-design case identity. Exact 2/4, publisher and complete source legal name. No customer logo/facility, Vietnam deployment or attribution to Vietnam team.',
    'Qualitative outsourcing-management challenge and integrated digital solution. Exact 3/4, China case04 and complete legal name. No metrics, ERP-only causality or proof of the exact prospect reporting mechanism.',
    'Source-reading next step, China integrated-solution context. Exact 4/4, complete publisher/domain/case04/legal name and reading CTA. Localized reader points to the same official original source; no new product/result scope.'
]
TRANSITIONS = [
    'Next-decision hook -> partner-report stage question for the same Operations/SCM role.',
    'Report clarification -> matching product/lot and partner conventions before comparison.',
    'Identifiers/conventions -> distinguish stage, recorded-time and report source.',
    'Stage/time/source -> confirm responsibility for maintaining shared updates.',
    'Accountable updates -> common basis for the next decision; Taiwan source remains contextual.',
    'Common decision basis -> prospective Vietnam ERP consulting/implementation discussion.',
    'Local Vietnam service -> general supplier introduction; China customer not attributed to Vietnam team.',
    'Supplier role -> explicitly named China chip-design customer case.',
    'China identity -> qualitative outsourcing-management challenge and integrated-solution context.',
    'Qualitative China context -> reading CTA -> same localized China source reader.'
]
VN_MEANINGS = [
    'Mở vấn đề: trước quyết định tiếp theo, đối chiếu lô, công đoạn và thời điểm báo cáo của đối tác.',
    'Làm rõ mỗi báo cáo của đối tác đang nói tới công đoạn nào.',
    'Đối chiếu mã sản phẩm/lô và quy ước về giai đoạn sản xuất, phân loại kiểm thử.',
    'Tách công đoạn, thời điểm ghi nhận trạng thái và nguồn báo cáo.',
    'Thống nhất định dạng, lịch trao đổi và người xác nhận cập nhật sản xuất.',
    'Đưa các điểm trên vào cùng một cuộc thảo luận; nguồn ERP/MES Đài Loan chỉ là bối cảnh giải pháp.',
    'Mời trao đổi với đội ngũ tại Việt Nam về tư vấn/triển khai ERP, bắt đầu từ quy trình báo cáo, trách nhiệm và ưu tiên dự án.',
    'Giới thiệu vai trò nhà cung cấp giải pháp cho sản xuất, từ ERP tới sản xuất thông minh.',
    'Giới thiệu rõ case doanh nghiệp thiết kế chip tại Trung Quốc, giữ đủ tên pháp nhân nguồn.',
    'Nêu thách thức quản lý thuê ngoài và bối cảnh giải pháp số tích hợp; không dùng số liệu kết quả.',
    'Mời đọc case Trung Quốc; reader cùng ngôn ngữ giữ nguồn gốc và dẫn tới bài gốc.'
]

freeze = load('operations/message-anchor/freeze-2026-10-06/manifest.json')
assert len(freeze['files']) == 24
for item in freeze['files']:
    assert sha(item['path']) == item['sha256'], item['path']
assert sha(ANCHOR) == '6621d53c845939730ebcb1f59bbf85fb8a0d9acb156e5236e7387c0e69867ac5'
assert sha(EMAIL) == 'c5a6f35533e7a8b3b439ec4d9a260611fcdd2f67ddb0f046a3e33d28c6316d2b'

docs = load(LANE + '/docs-reviewed.json')['files']
docs_files = [dict(path=d['path'], sha256=sha(d['path'])) for d in docs]
canonical_root = Path('D:/Digiwin_Semiconducter_Workspace')
canonical_commit = subprocess.check_output(['git','rev-parse','HEAD'], cwd=canonical_root, text=True).strip()
canonical_files = ['CURRENT_STATE.md','DOCS_IMPACT_MAP.md','operations/LinkedIn_Current_Progress_2026-10-07.md']
canonical_pins = [dict(path=p, sha256=hashlib.sha256((canonical_root/p).read_bytes()).hexdigest()) for p in canonical_files]
put(LANE + '/B14-B15-docs-reviewed.json', dict(
    revision='b14-b15-current-canonical-review-v1', reviewer=ROOT_REVIEW,
    files=docs_files,
    decision='Offline owned drafts only. No canonical acceptance/live/business/lifecycle change. Latest main progress snapshot is now stale for B14 corrective closure and B15 generation; bounded coordinator refresh proposal in docs-impact.md is required before accepted handoff/package adoption. Shared canonical writes outside lane mandate; discrepancy disclosed, not silently treated as current.',
    latest_main_review=dict(root=str(canonical_root),commit=canonical_commit,files=canonical_pins,observed='Current progress Fabless row says B14 corrective in progress/B15 no PNG at snapshot; new attempt and postgen records independently support B14 closed scoped findings and B15 full11 plus corrected v2. B16 onward still not run. Reader redesign has no Fabless mapping/adoption, so these batches keep their source-bounded localized readers.'),
    reviewed_truth='Anchor persona/FDI value and VN team nuance preserved; no budget/account/eligibility/rights inference; source scope remains narrow; 11-original exception for these two batches only; rendered evidence gaps retained.'))

batch_reviews = []
for batch, locale, version, corr_count in [('B14', 'zh-Hans', 'v1', 2), ('B15', 'zh-Hant', 'v2', 1)]:
    base = LANE + '/' + batch + '-' + locale + '-f1-v1'
    out = DEL + '/' + batch + '-' + locale + '-f1-' + version
    manifest = load(out + '/manifest.json')
    copy = load(out + '/selected-copy.json')['cards']
    prompts = load(out + '/selected-prompts.json')['calls']
    attempts = load(base + '/attempt-ledger.json')['attempts']
    dispatch = load(base + '/dispatch-plan.json')
    jobs = dispatch['calls'] + load(base + '/corrective-dispatch-plan.json')['calls']
    by_id = {j['call_id']: j for j in jobs}
    assert len(by_id) == len(attempts) == 11 + corr_count
    counts = Counter(a['kind'] for a in attempts)
    assert counts == dict(original=11, corrective=corr_count)
    assert max(Counter(a['card_id'] for a in attempts if a['kind'] == 'corrective').values()) == 1
    fresh = []
    for a in attempts:
        job = by_id[a['call_id']]
        assert sha(a['path']) == a['sha256']
        with Image.open(ROOT / a['path']) as im:
            assert im.format == 'PNG' and im.size == (1254, 1254)
        assert sha(job['folder'] + '/release.json') == job['release_sha256']
        assert sha(job['folder'] + '/anchor-review.json') == job['review_sha256']
        gp = job['folder'] + '/dispatch/' + a['call_id'] + '-fresh-preflight.json'
        g = load(gp)
        assert g['status'] == 'PREGEN_INPUTS_VERIFIED' and g['call_id'] == a['call_id']
        assert g['message_review_sha256'] == job['review_sha256']
        for p, h in g['input_hashes'].items():
            assert sha(p) == h, p
        sc = load(job['folder'] + '/spec.json')['calls'][0]
        assert g['tool_args']['prompt'] == sc['prompt']
        assert hashlib.sha256(sc['prompt'].encode()).hexdigest() == sc['prompt_sha256']
        assert g['tool_args']['referenced_image_paths'] == [str(ROOT / r['path']) for r in sc['references']]
        fresh.append(dict(call_id=a['call_id'], guard=ref(gp), release_sha256=job['release_sha256'], message_review_sha256=job['review_sha256'], prompt_sha256=sc['prompt_sha256']))
    assert len(copy) == len(prompts) == len(manifest['artwork']) == 11
    assert [c['card_id'] for c in copy] == [a['card_id'] for a in manifest['artwork']]
    selected = {a['card_id']: a for a in attempts}
    measures = load(base + '/evidence/full-render-measures.json')
    v2_measures = load(base + '/evidence/v2-final-render-measures.json') if batch == 'B15' else []
    units = []
    for n, (c, art, prompt) in enumerate(zip(copy, manifest['artwork'], prompts), 1):
        a = selected[c['card_id']]
        assert art['sha256'] == sha(art['path']) == sha(art['source']) == a['sha256']
        assert art['source'] == a['path'] and not art['transformation']
        assert prompt['call_id'] == a['call_id'] and prompt['card_id'] == c['card_id']
        sc = load(by_id[a['call_id']]['folder'] + '/spec.json')['calls'][0]
        assert prompt['prompt'] == sc['prompt'] and prompt['prompt_sha256'] == sc['prompt_sha256']
        rendered = []
        for mode, width in [('feed', 333), ('desktop', 640)]:
            replacement = batch == 'B15' and n == 9
            m = next(x for x in (v2_measures if replacement else measures) if x['card'] == n and x['mode'] == mode)
            assert m['image']['loaded'] and abs(m['image']['width'] - width) < .01 and not m['overflow']
            assert m['caption'] == c['caption'] and m['native'] == c['native_headline'] and m['counter'] == str(n) + ' / 11'
            assert m['image']['src'].endswith(c['image'])
            shot = base + '/evidence/' + ('v2-' if replacement else '') + mode + '-' + str(n).zfill(2) + '.jpg'
            rendered.append(dict(mode=mode, actual_dom=m, screenshot=ref(shot), observation='Root actual pixels: approved text, complete attribution where supplied, category/counter, source hierarchy, logo and props legible with no mandatory correction in this observed surface.', byte_binding='B15v2 ten unchanged PNGs are exact same bytes as the actually reviewed zh-Hant v1 screenshots; fresh root selected-revision comparison performed. No inherited cross-locale PASS.' if batch == 'B15' and not replacement else 'Actual selected artifact captured.'))
        mobile = 'INSUFFICIENT_EVIDENCE: full current mobile artwork plus caption/native context not visually certified.'
        if batch == 'B15' and n in (1, 2, 3):
            mobile += ' Original mobile-context pixels observed; associated390CSS DOM/raster mapping unverified.'
        if batch == 'B15' and n == 7:
            mobile += ' v2 mobile team context actually readable; DOM390x844/image315.56 loaded, raw414x937 mapping unverified.'
        if batch == 'B14' and n == 7:
            mobile += ' Settled DOM390x844/image332.44 loaded, screenshot timed out; DOM is not visual PASS.'
        units.append(dict(card_id=c['card_id'], position=n, exact_approved_fields={k:c[k] for k in ['headline','body','source_text','cta','artwork_labels','caption','native_headline','alt']}, native=art, actual_native_observation=a['observations'], message_observation=MEANINGS[n-1], artwork_text='Exact approved glyphs/punctuation/category/sequence reviewed in actual native and feed/main pixels. Empty source/CTA fields have no printed substitute; caption/native/alt remain contextual surfaces.', surfaces=rendered, mobile=mobile, scoped_review='PASS_SELF_REVIEW_NATIVE_FEED_MAIN', full_render_verdict='INSUFFICIENT_EVIDENCE'))

    findings = []
    for r in load(base + '/corrective-native-review.json')['cards']:
        a = selected[r['card_id']]
        findings.append(dict(card_id=r['card_id'], original_sha256=r['original_sha256'], original_finding=r['finding'], original_verdict='CHANGES_REQUIRED', disposition='CLOSED_IN_SELECTED_NATIVE_FEED_MAIN_SELF_REVIEW', corrective_call=a['call_id'], corrected_sha256=a['sha256'], original_retained=True, scope='Blank paper only' if batch == 'B14' else 'Category 设计 -> 設計 only; legal source name remains exact'))
    put(base + '/postgen-original-findings.json', dict(revision=batch.lower()+'-original-output-findings-v1', reviewer=ROOT_REVIEW, independence='SELF_REVIEW', findings=findings, historical_verdict='CHANGES_REQUIRED_FOR_LISTED_ORIGINAL_OUTPUTS', note='Actual original artifacts remain unchanged; current selected revision closes only the described finding. No retroactive original PASS.'))
    evidence = []
    for p in sorted((ROOT / base / 'evidence').glob('*')):
        if p.is_file():
            item = ref(p.relative_to(ROOT).as_posix())
            if p.suffix.lower() in ['.jpg', '.png']:
                with Image.open(p) as im:
                    item.update(format=im.format, width=im.width, height=im.height)
            evidence.append(item)
    semantic = load(base + '/semantic-review.json')
    rules = [dict(rule=k, actual_observation=semantic[k], actual_binding='Per-card exact-field/native/feed/main observations and reader below; localized artwork reconciled against these semantic criteria.', scope='PASS_SELF_REVIEW_ACTUAL_NATIVE_FEED_MAIN_READER_DESKTOP; FULL_MOBILE_INSUFFICIENT_EVIDENCE') for k in ['A1','A2','A3','A4','A5','A6','A7']]
    transitions = [dict(from_card=copy[i]['card_id'], to_card=copy[i+1]['card_id'], actual_observation=TRANSITIONS[i], exact_headline_pair=[copy[i]['headline'],copy[i+1]['headline']], disposition='MATCH_IN_OBSERVED_NATIVE_FEED_MAIN_AND_DESKTOP_READER_SCOPE') for i in range(10)]
    review = dict(
        revision=batch.lower()+'-'+locale.lower()+'-postgen-'+version+'-actual-root-v1',
        stage='POSTGEN_ARTIFACT', date='2026-10-07', reviewer=ROOT_REVIEW, independence='SELF_REVIEW',
        review_method='Transcription of actual root native/pixel/text comparison performed in this session; mechanical assertions bind evidence but do not evaluate semantics or grant authority. Fresh localized and selected-revision review, no inherited B13/B14 PASS or independent native-market certification.',
        status=STATUS, execution='PARTIAL', audit_verdict='INSUFFICIENT_EVIDENCE',
        authorization=ref(base+'/generation-mandate.json'),
        anchor={**ref(ANCHOR), 'id':'VY-CONTENT-ANCHOR', 'revision':'1.0', 'original_email':ref(EMAIL)},
        scope=dict(segment='FDI', locale=locale, persona=PERSONA, route=dispatch['route'], branch='slice/linkedin-safe-fabless-parallel', ordered_units=[c['card_id'] for c in copy]),
        audience='Business hypothesis: commercial outsourced-production Fabless FDI entity with Operations/SCM influencing business-system decisions. No live audience configuration, account eligibility, local buying authority or group ERP autonomy established.',
        binding=dict(manifest=ref(out+'/manifest.json'), copy=ref(out+'/selected-copy.json'), prompts=ref(out+'/selected-prompts.json'), reader=ref(out+'/case-reader.html'), viewer=ref(out+'/index.html'), attempts=ref(base+'/attempt-ledger.json'), semantic_review=ref(base+'/semantic-review.json'), proof_map=ref(base+'/proof-source-mapping.json'), vietnam_team_source=ref(base+'/vietnam-team-source.json'), evidence=evidence, fresh_dispatches=fresh),
        anchor_rules=rules, unit_reviews=units, transition_reviews=transitions,
        reader=dict(actual_desktop='Actual localized reader content and source disclosure observed in pixels; full substantive sections, official original link and return route verified. China company, qualitative outsourcing challenge and integrated-solution scope agree with selected proof cards.', desktop_measure=ref(base+'/evidence/'+('v2-' if batch=='B15' else '')+'reader-measure.json'), desktop_pixels=ref(base+'/evidence/'+('v2-' if batch=='B15' else '')+'reader-desktop-top.jpg'), return_route='CLICKED_AND_OBSERVED_OWN_INDEX_URL', mobile='B15v2 top/substantive context observed at DOM390x844/raw414x937, below-fold source disclosure/link not visually captured; exact mapping unverified. Full mobile reader INSUFFICIENT_EVIDENCE.' if batch=='B15' else 'Full mobile reader pixels missing; INSUFFICIENT_EVIDENCE.'),
        proof_scope='Official China case04 qualitative challenge/integrated-solution background, exact legal name. Vietnam team consulting/implementation is separately sourced prospective service discussion. No metrics, headcount, teamwide languages, customer testimonial/logo/facility, ERP-only causal result, exact F1 functionality proof or Vietnam Fabless deployment.',
        locale_review='Hans business terms directly authored; no inherited English wording. Exact legal name/source and advertiser first-person voice reviewed.' if batch=='B14' else 'Taiwan business terms directly authored: 回報/製程/權責/顧問/導入/數位, ERP企業資源規劃 and MES製造執行系統; IC積體電路 explained in caption. Exact Simplified legal source name deliberately retained and disclosed in reader. Only legal-name exception; mistaken category glyphs corrected. No mechanical national-personality inference.',
        visual_review='Bright neutral B13v5 campaign family, official mark once, grounded material depth. Approved source paragraphs full-width/high-contrast on white, at least body-sized where required. Selected paper blank; new outputs do not inherit B13 generic-rule-line preservation exception. No fabricated record values/charts/technical UI/customer geography decoration.',
        findings=findings, unresolved_creative_findings=[],
        verdicts=dict(MSG_ANCHOR_01='INSUFFICIENT_EVIDENCE_FULL_MOBILE_JOURNEY', AD_ED_01='INSUFFICIENT_EVIDENCE_FULL_MOBILE_SET', observed_semantic_alignment='PASS_SELF_REVIEW_NATIVE_FEED_MAIN_DESKTOP_READER', whole_journey='NOT_READY_NOT_ACCEPTED', independent_native_market='NOT_RUN'),
        technical=dict(feed='All11 actual selected PNGs observed at333CSSpx with caption/native wording.', main='All11 actual selected PNGs observed at640CSSpx with complete artwork; B15v2 new corrected card freshly captured, ten byte-identical source-localized PNGs rebound to prior actual v1 pixels.', mobile='Partial context/DOM only. Full eleven-card plus reader mobile scope and CSS-to-raster precision remain insufficient. No generated artwork correction required solely for capture gap.', capture_limits=['B14 cold fullPage screenshot timed out; bounded viewport/#art auto-scroll gave main evidence.', 'B14 mobile team capture timed out after settled DOM.', 'B15 viewport reset left old tab at390CSS; three initial captures classified mobile-context, then fresh default tab supplied actual333/640 evidence.', 'B15v2 mobile raw capture414x937 differs from DOM390x844; mapping unverified. No exact390 pixel certification.'], browser='Own atomic browser-lock intervals only; Partner-owned lock respected; own tabs closed, viewport override reset, owned preview servers stopped and lock released.'),
        counts=dict(original=11, corrective=corr_count, actual_calls=11+corr_count, selected=11, cross_locale_png_reuse=0, selected_native_dimensions=[1254,1254], transformations=0, original_cap=11, corrective_cap=2, per_card_corrective_cap=1),
        freeze='24/24 pinned bytes unchanged. Harness/guard/process FROZEN_PER_PO; locale adapter DEVELOPING/NOT_FROZEN.',
        docs_review=ref(LANE+'/B14-B15-docs-reviewed.json'),
        git='B14/B15 working files only, uncommitted and unstaged in owned worktree. Previous B13 local checkpoint e3b6578 unchanged. No main integration/push/live.',
        stop='B16-B21 NOT_RUN; end the authorized two-batch generation. Historical B13/canary/original findings retained.'
    )
    put(base+'/postgen-review.json', review)
    verification = dict(revision=batch.lower()+'-raw-byte-closeout-'+version+'-v1', verdict='MECHANICAL_BINDINGS_PASS', review=ref(base+'/postgen-review.json'), selected_manifest=ref(out+'/manifest.json'), count_verification=review['counts'], actual_calls_with_fresh_guard=len(fresh), input_pins_verified=True, selected_prompt_call_identity_verified=True, original_pngs_and_selected_bytes_verified=True, freeze_files=24, frozen_bytes_unchanged=True, semantic_review='Actual root judgment in bound postgen receipt; this verifier does not approve message or artwork.', technical_terminal=STATUS, full_audit_verdict='INSUFFICIENT_EVIDENCE', Git_mutation=False)
    for fname in ['index.html', 'case-reader.html']:
        html=(ROOT/out/fname).read_text(encoding='utf-8')
        assert not any(s in html.lower() for s in ['<form', '<input', 'gtm-', 'gtag(', 'fbq(', 'accepted_form', 'fetch(', 'xmlhttprequest'])
    verification['offline_no_form_or_analytics_dispatch'] = True
    if batch == 'B15':
        previous=load(DEL+'/B15-zh-Hant-f1-v1/manifest.json')
        unchanged=[a['card_id'] for a,b in zip(previous['artwork'],manifest['artwork']) if a['sha256']==b['sha256']]
        assert len(unchanged)==10 and 'RMK-BRIGHT-2' not in unchanged
        assert previous['reader_sha256']==manifest['reader_sha256']
        verification['v1_to_v2_unchanged_pngs']=unchanged
        verification['v1_reader_bytes_unchanged']=True
    put(base+'/verification.json',verification)
    lines=[f'# {batch} — diễn giải và hậu kiểm cho Bảo', '', f'Đã có đủ 11 card {locale}, gồm 1 cold + 6 explanation + 4 case. Giữ anchor v5 và card đội ngũ tư vấn/triển khai ERP tại Việt Nam. {11+corr_count} lượt ImageGen = 11 tạo gốc + {corr_count} sửa; ảnh native1254×1254 giữ nguyên byte.', '', f'[Mở bộ hiện tại](../../../../{out}/index.html) · [Hậu kiểm](postgen-review.json) · [Đối chiếu byte](verification.json)', '', '| Card | Headline hiện tại | Ý nghĩa cho Bảo |', '|---|---|---|']
    for n,c in enumerate(copy):
        lines.append('| '+str(n+1)+' | '+c['headline']+' | '+VN_MEANINGS[n]+' |')
    lines += ['', 'Các lỗi phải sửa đã đóng trong native/feed333/main640: '+('A5 và case2 bỏ toàn bộ nét trên giấy.' if batch=='B14' else 'Case2 sửa nhãn 设计 thành 設計; v1 có lỗi vẫn được giữ riêng, v2 là bộ hiện tại.'), '', 'Đã quan sát đủ 11 card ở feed và main, kiểm caption/native headline/nguồn, reader desktop và đường quay lại. Không còn finding content/artwork bắt buộc sửa trong phạm vi đã quan sát. Đây là tự kiểm của root; chưa có reviewer bản địa độc lập.', '', 'Full mobile của cả bộ/reader chưa đủ, và ánh xạ kích thước CSS390 sang raster chưa chứng minh được. Giữ **REVIEW_DRAFT_RENDER_GATE_PENDING / INSUFFICIENT_EVIDENCE**; không ghi PASS/ready/accepted toàn bộ. Không dùng lượt ImageGen để sửa một khoảng trống bằng chứng browser.', '', 'Case Trung Quốc và đội ngũ tại Việt Nam là hai nguồn, hai phạm vi riêng. Không đưa số liệu kết quả, hứa hiệu quả, tuyên bố ERP gây ra toàn bộ kết quả hoặc suy case này đã triển khai Fabless tại Việt Nam.', '', 'Hiện chỉ là file đang làm trong worktree Fabless, chưa commit/stage/main/push. Dừng trước B16. Freeze24pins nguyên; adapter locale vẫn DEVELOPING / NOT_FROZEN.', '']
    put(base+'/Bao_Review_Vietnamese.md','\n'.join(lines))
    batch_reviews.append(dict(batch=batch, locale=locale, selected_revision=version, review=ref(base+'/postgen-review.json'), verification=ref(base+'/verification.json'), counts=review['counts']))

old=load(LANE+'/ledger.json')
if old['revision']=='fabless-lane-ledger-b14-b15-v1':
    old=old['historical_b13_checkpoint']['prior_ledger']
assert old['revision']=='fabless-lane-ledger-v5-local-checkpoint-authorized'
put(LANE+'/ledger.json',dict(revision='fabless-lane-ledger-b14-b15-v1',owner=ROOT_REVIEW,active_batches=['B14-zh-Hans-f1-v1','B15-zh-Hant-f1-v2'],status=STATUS,execution='PARTIAL',batches=batch_reviews,counts=dict(two_batches_original=22,two_batches_corrective=3,two_batches_actual_calls=25,selected_current_pngs=22,prior_b13_calls=20,lane_cumulative_calls=45),remaining_queue='B16-B21 NOT_RUN',historical_b13_checkpoint=dict(commit='e3b65780356cdf5f489ea3a45ac4927af616cd81',local_only=True,prior_ledger=old),current_git=dict(working_files=True,staged=False,new_commit=False,main_integration=False,push=False,live=False),acceptance='NOT_READY_NOT_ACCEPTED; native/feed/main content reviewed SELF_REVIEW, full mobile evidence pending',stop='Authorized B14 and B15 complete in generation; stop before B16.'))
print('B14/B15: 22 selected native PNGs; 25 actual calls with exact fresh-guard/input/prompt bindings; frozen24 intact; full mobile audit remains INSUFFICIENT_EVIDENCE.')
