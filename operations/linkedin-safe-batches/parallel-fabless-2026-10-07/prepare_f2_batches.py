"""Bounded F2 drafting/release assembly; root review is supplied separately."""
import copy, inspect, sys, shutil
import prepare_next_locales as old
from prepare_next_locales import ROOT, LANE, V1, V5, LOGO, CLOSING, PERSONA, load, put, ref, sha, module
DEL='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'
SOURCE='operations/linkedin-imagegen-dogfood/continuous-rollout-2026-10-04/F2/common/f2-copy.json'

def author(batch):
    locale='en' if batch=='B16' else 'zh-Hans'
    base=LANE+'/'+batch+'-'+locale+'-f2-v1'
    assert not (ROOT/base/'dispatch-plan.json').exists()
    assert not (ROOT/base/'attempt-ledger.json').exists() or not load(base+'/attempt-ledger.json')['attempts']
    baseline=DEL+('/B13-en-f1-v5' if locale=='en' else '/B14-zh-Hans-f1-v1')
    authored=load(LANE+'/f2-authored-input.json')[locale]
    baseline_cards=load(baseline+'/selected-copy.json')['cards']
    profiles=load('operations/linkedin-locale-adapter/profiles.json')['locales'][locale]
    freeze=load('operations/message-anchor/freeze-2026-10-06/manifest.json')['files']
    assert len(freeze)==24 and all(sha(x['path'])==x['sha256'] for x in freeze)
    route='offline '+locale+' demand-change cold -> F2 planning reconciliation -> Vietnam consulting/implementation -> qualitative China outsourcing case -> localized planning-question reader'
    mandate=dict(revision=batch.lower()+'-f2-mandate-v1',instruction='commit đi codex, r chạy 2 batch kế.',scope='B16 F2 English and B17 F2 Simplified Chinese; same anchor/persona/Vietnam nuance.11selected positions with reviewed same-locale reuse, not11new calls.',original_cap=10,corrective_cap=2,per_card_corrective_cap=1,stop='Stop before B18; new Git mutation after B14/B15 checkpoint not included.',trust='SELF_REVIEW; no inherited PASS or native-market certification')
    put(base+'/generation-mandate.json',mandate)
    (ROOT/base/'execution-brief.md').write_text('# '+batch+' F2 '+locale+'\n\nGoal: full offline planning journey, native bytes, reader and actual review.\nOwner: /root; two owned Fabless roots only, no shared mutation/subagent/live.\nPersona: '+PERSONA+'. F2 is a planning lens within the same Operations/SCM decision unit; no Finance role switch. Eligible commercial outsourced-production entity and local system authority remain unverified.\nRoute: '+route+'.\nBusiness value: a shared basis for replanning and accountable partner confirmations; no guaranteed agility, forecast accuracy, automatic rescheduling or ROI numbers. Existing processes/systems remain alternatives to ERP purchase.\nMeasurement: exact current fields/scenes/persona/proof/reader reviewed before inference; fresh callable guard each call; two hard canaries F2-A5/F2-A3;10original+2corrective/onepercard. Inspect native/feed333/main640/mobile390/journey/reader; gaps PARTIAL/INSUFFICIENT_EVIDENCE, not PASS.\nReuse: local Vietnam card and proof retained only after fresh F2 exact-byte/source/semantic review. English proof2 rebuilt because its original paper lines are not literally blank; no inherited B13 preservation exception for this new output.\nAuditor target: final selected bytes, guard pins, per-unit actual text/scene observations,10transitions and reader/return. Root SELF_REVIEW, no independent-market/PO acceptance. Frozen24/core/adapter/shared canon read-only. Stop before B18.\n',encoding='utf-8')
    proof=copy.deepcopy(load(LANE+'/B14-zh-Hans-f1-v1/proof-source-mapping.json'))
    proof.update(revision=batch.lower()+'-f2-proof-map-v1',locale=locale,retrieval='Fresh official case04 read2026-10-07: qualitative outsourcing inefficiency and integrated digital solution. No outcomes/metrics imported.',f2_bridge='Partner coordination/information responsibility is relevant contextual background for planning discussion, not proof of forecast accuracy, F2 mechanism or replanning outcomes.')
    put(base+'/proof-source-mapping.json',proof)
    vn=copy.deepcopy(load(V5+'/vietnam-team-source.json'));vn['revision']=batch.lower()+'-f2-vietnam-service-v1'
    put(base+'/vietnam-team-source.json',vn)
    reader=copy.deepcopy(load((V5 if locale=='en' else LANE+'/B14-zh-Hans-f1-v1')+'/reader-script.json'))
    reader['revision']=batch.lower()+'-f2-reader-v1';reader['sections'][2]['text']=authored['reader_question']
    reader['return_label']='Return to the planning journey' if locale=='en' else '返回委外计划主题'
    put(base+'/reader-script.json',reader)
    put(base+'/ui.json',dict(revision=batch.lower()+'-f2-ui-v1',**authored['ui']))
    core=module('scripts/verify_imagegen_preflight.py')
    observations=[];reused=[]
    source_prompts={x['card_id']:x for x in load(baseline+'/selected-prompts.json')['calls']}
    manifest={x['card_id']:x for x in load(baseline+'/manifest.json')['artwork']}
    source_specs={}
    for p in (ROOT/LANE).rglob('spec.json'):
        for c in load(p.relative_to(ROOT).as_posix()).get('calls',[]):source_specs[c['call_id']]=p.relative_to(ROOT).as_posix()
    scenes=[
      'Bright neutral desk, blank partner report sheets beside a wafer protective carrier; separate sheets represent reports to reconcile, not actual statuses or forecast charts.',
      'A neutral packaged chip and small lot trays beside blank report sheets; product and lot scope are illustrative, no printed identifiers or technical layouts.',
      'Separate blank partner reports and neutral wafer protective carrier; differing report sources are abstract, no dates, status values, clock faces or technical UI.',
      'Blank open folder, neutral chip tray and simple unlabelled responsibility nodes with open connectors; no check marks, completed workflow, screens or record values.',
      'Grouped blank partner reports, neutral chip carrier and responsibility nodes on white; a shared discussion basis, no automatic planning engine or results.'
    ]
    for stage in ['cold','explanation','proof']:
        rows=[];concepts={}
        baseline_stage=[x for x in baseline_cards if x['stage']==stage]
        inputs=[dict(authored['cold'])] if stage=='cold' else authored['cards']+[dict(baseline_stage[5])] if stage=='explanation' else [dict(x) for x in baseline_stage]
        caption=authored['cold_caption'] if stage=='cold' else authored['caption'] if stage=='explanation' else authored.get('proof_caption',baseline_stage[0]['caption'])
        for i,a in enumerate(inputs):
            cid='COLD-FABLESS-'+batch if stage=='cold' else 'F2-A'+str(i+1) if stage=='explanation' else a['card_id']
            labels=authored['cold_labels'][:] if stage=='cold' else authored['labels']+[str(i+1)+'/6'] if stage=='explanation' and i<5 else a['artwork_labels'][:]
            row=dict(card_id=cid,headline=a['headline'],body=a['body'],source_text=a.get('source_text',''),cta=a.get('cta',''),native_headline=a.get('native_headline',a['headline']),alt=authored['alt_prefix']+a['headline'],artwork_labels=labels)
            rows.append(row)
            original=baseline_stage[0] if stage=='cold' else baseline_stage[i]
            origin_id=original['card_id'];is_reused=(stage=='explanation' and i==5) or (stage=='proof' and not (batch=='B16' and i==1))
            origin_art=manifest[origin_id]
            reference_art=origin_art['path']
            if (stage=='explanation' and i==4) or (batch=='B16' and stage=='proof' and i==1):
                reference_art=DEL+'/B14-zh-Hans-f1-v1/assets/'+('06-f1-a5.png' if stage=='explanation' else '09-rmk-bright-2.png')
            oldspec=load(source_specs[source_prompts[origin_id]['call_id']])['calls'][0]
            concept=copy.deepcopy(oldspec['concepts'][0]);concept.update(card_id=cid,concept_id=batch.lower()+'-'+cid.lower()+'-f2-scene-v1',reader_question=row['headline'],artwork_labels=labels)
            if stage=='cold':concept['description']=scenes[0]+' Demand-change planning hook; blank paper only.'
            elif stage=='explanation' and i<5:concept['description']=scenes[i]
            concept['description']+=' Exact approved words only. Blank paper everywhere; no chart, tick, date, status, forecast curve, metric, technical chip UI, customer facility/marks or geography decoration. Keep full-width source paragraphs on white at least body-sized; shrink scene before type. Official logo once, exact category/sequence, no extra header label.'
            concepts[cid]=concept
            observations.append(dict(stage=stage,card_id=cid,reviewed_fields=['caption']+list(core.CARD_FIELDS),exact_fields=row,caption=caption,scene=concept['description'],observation='Actual root authored/reviewed F2 scope: '+row['headline']+'; operating question/shared planning basis or separately attributed service/qualitative China case, not product capability or customer result.',source_scope=proof['f2_bridge'] if stage=='proof' else 'Planning questions or separate local Vietnam consultation',reference_artwork=reference_art,reused=is_reused))
            if is_reused:
                reused.append(dict(card_id=cid,original_card_id=origin_id,path=origin_art['path'],sha256=origin_art['sha256'],kind='reuse',width=1254,height=1254,source_prompt=source_prompts[origin_id],source_spec=source_specs[source_prompts[origin_id]['call_id']],transformation=False,copy_native_bytes=True))
        ad=batch+'-COLD' if stage=='cold' else 'F2-A' if stage=='explanation' else 'RMK-BRIGHT'
        cp=base+'/'+stage+'/public-copy.json';put(cp,dict(schema_version=1,revision=batch.lower()+'-f2-'+stage+'-copy-v1',ads=[dict(ad_id=ad,caption=caption,cards=rows)]))
        template=V1+'/cold/release-v2/campaign/contract.json' if stage=='cold' else V5+'/release/f1-a6/contract.json' if stage=='explanation' else V1+'/proof/release-v2/closing/contract.json'
        c=copy.deepcopy(load(template));c.update(revision=batch.lower()+'-f2-'+stage+'-contract-draft-v1',locale=locale,copy=ref(cp),ad_order=[ad],card_order={ad:[x['card_id'] for x in rows]},groups=[[x['card_id']] for x in rows],definitions=profiles['definitions'])
        c['limits']['caption']=255
        c['surfaces']={ad:[dict(surface_id='full-feed',reading_order=['caption']+[x['card_id']+'.'+f for x in rows for f in core.CARD_FIELDS])]}
        c['sources']=[ref(base+'/execution-brief.md',batch.lower()+'-f2-brief-v1'),ref(SOURCE,'f2-source-read-v1'),ref(LANE+'/f2-authored-input.json'),ref(base+'/proof-source-mapping.json'),ref(base+'/vietnam-team-source.json'),ref(baseline+'/selected-copy.json'),ref('operations/linkedin-locale-adapter/profiles.json')]
        c['card_sources']={x['card_id']:[s['path'] for s in c['sources']] for x in rows}
        c['style']['campaign']['instructions']=profiles['prompt_guidance']+' '+profiles['typography']+' B13v5 bright white/blue photographic campaign family. Reference wording is not approved copy. Official supplied logo once; no extra DIGIWIN header. Exact category/sequence near logo. Body comfortably readable at333CSSpx. Source normal full-width main paragraph on white, at least body-sized. All paper blank; no bars/rules/charts/ticks/data glyphs/UI/customer geography/seal/badge. Only approved artwork words. Demand-change questions are not forecast accuracy or automatic replanning claims. Reduce scene before type.'
        if stage!='proof':c['style'].pop('closing',None)
        else:c['style']['closing']['cards']=['RMK-BRIGHT-4']
        c['output']['directory']=base+'/'+stage+'/native'
        put(base+'/'+stage+'/contract.draft.json',c);put(base+'/'+stage+'/concepts.draft.json',dict(revision=batch.lower()+'-'+stage+'-f2-concepts-v1',concepts=concepts))
    put(base+'/reuse-ledger.json',dict(revision=batch.lower()+'-f2-proposed-reuse-v1',scope='PROPOSED_PENDING_ACTUAL_F2_REVIEW',artwork=reused))
    put(base+'/draft-observations.json',dict(revision=batch.lower()+'-f2-author-observations-v1',cards=observations))
    pins=[ref(base+'/'+p) for p in ['generation-mandate.json','reader-script.json','proof-source-mapping.json','vietnam-team-source.json','ui.json','reuse-ledger.json','draft-observations.json']]+[ref(base+'/'+s+'/'+p) for s in ['cold','explanation','proof'] for p in ['public-copy.json','contract.draft.json','concepts.draft.json']]
    put(base+'/draft-manifest.json',dict(revision=batch.lower()+'-f2-draft-v1',locale=locale,persona=PERSONA,route=route,files=pins,frozen_files_verified=24,selected_intent=11,postgen='POSTGEN_NOT_RUN'))
    for helper in ['fresh_preflight.py','record_attempt.py','prepare_draft.py']:shutil.copyfile(ROOT/V5/helper,ROOT/base/helper)
    put(base+'/attempt-ledger.json',dict(revision=batch.lower()+'-f2-attempts-v1',attempts=[]))
    print(batch+': authored11positions; '+str(len(reused))+' proposed exact-byte reuse; no semantic release automatically granted.')

def release(batch):
    code=inspect.getsource(old.release).replace("locale = 'zh-Hans' if batch == 'B14' else 'zh-Hant'","locale = 'en' if batch == 'B16' else 'zh-Hans'").replace("'-f1-v1'","'-f2-v1'")
    code=code.replace("for o in observations:\n        stage", "for o in observations:\n        if o['reused']: continue\n        stage")
    code=code.replace('explicit PO B14/B15 mandate','explicit PO B16/B17 mandate').replace("canary = ['F1-A6', 'RMK-BRIGHT-3']","canary = ['F2-A5', 'F2-A3']").replace('original_cap=11','original_cap=10').replace("print(batch + ': 11 prepared releases; fresh wrapper still mandatory before every actual call.')","print(batch + ': '+str(len(plans))+' fresh releases prepared; wrapper required for each actual inference.')")
    env=dict(old.__dict__);exec(code,env);env['release'](batch)

if __name__=='__main__':
    assert sys.argv[1] in ['author','release'] and sys.argv[2] in ['B16','B17']
    (author if sys.argv[1]=='author' else release)(sys.argv[2])
