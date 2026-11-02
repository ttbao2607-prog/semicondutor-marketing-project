# -*- coding: utf-8 -*-
import csv, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
CAMP="SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261102]_50.000d-ngay_PAUSED_REVIEW"
BASE="https://solutions.digiwin.com.vn"
SUF=lambda seg,l,kind:f"utm_source=google&utm_medium=cpc&utm_campaign=vn_semiconductor_search_p1&utm_content={seg}_{l}_{kind}&utm_term={{keyword}}"
def wl(s): return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)
KW={"vi":"Digiwin Việt Nam bán dẫn","en":"Digiwin semiconductor Vietnam","zh-Hans":"鼎捷 越南 半导体","zh-Hant":"鼎捷 越南 半導體"}
# brand RSA: headlines/descriptions composed ONLY from approved build-sheet copy (+ brand name)
H={
"vi":["Digiwin Việt Nam","Digiwin cho ngành bán dẫn","Traceability cho OSAT","Quản trị WIP theo lot","Quản trị outsourced WIP","Nối ERP MES và OT","Kiến trúc dữ liệu nhà máy","Trao đổi bài toán Fabless"],
"en":["Digiwin Vietnam","Digiwin for Semiconductor","OSAT Lot Traceability","Fabless Outsourced WIP","Semiconductor ERP MES OT","Factory IT & OT Integration","Shopfloor Data Architecture","Bridge Quality & Shopfloor"],
"zh-Hans":["鼎捷 越南 半导体","半导体封测批次追溯","无晶圆厂外包在制品","半导体 ERP MES OT 集成","工厂 IT 与 OT 深度互联","OSAT 批次与品质追踪","封测制造数据底座","打通设备机台与企业系统"],
"zh-Hant":["鼎捷 越南 半導體","半導體封測批次追溯","無晶圓廠委外在製品","半導體 ERP MES OT 整合","工廠 IT 與 OT 深度互聯","OSAT 批號與品質追蹤","封測製造數據底座","打通設備機台與企業系統"]}
D={
"vi":["Khung cơ chế nối lot, 4M1E, test data, quality, WIP và cost close.","Khung cơ chế nối forecast, outsourced WIP, Datecode/BIN/lot và cost.","Xác định nguồn dữ liệu, ownership và handoff giữa ERP, MES và OT.","Trao đổi một pain point OSAT cụ thể, không gửi dữ liệu sản xuất qua trang."],
"en":["Connect lot genealogy, 4M1E, test data, WIP and cost closing in one unified model.","Bridge design forecast, outsourced foundry WIP, packaging test and final inventory.","Define clear data ownership and interface boundaries across ERP, MES and shopfloor OT.","Discuss specific OSAT operational challenges without sending sensitive production data."],
"zh-Hans":["连接销售预测、代工厂晶圆流转、外包封测进度与在制品成本，消除外包黑盒。","明确 ERP、MES 与车间底层 OT 之间的数据归属权与握手协议，杜绝信息孤岛。","深入探讨具体封测运营难点，无需在网页上传敏感生产数据，保障核心资产。","交流芯片委外加工管理方案，无需在网页提供敏感电路设计或客户私密信息。"],
"zh-Hant":["串聯銷售預測、晶圓代工進度、外包封測在製品與結算成本，打破外包黑盒子。","明確 ERP、MES 與現場底層 OT 之間的數據權責與介面協定，杜絕資訊斷層。","深入交流封測運營痛點，無需在網頁上傳機密生產數據，守護企業核心資產。","共同探討晶片委外管理架構，無需在網頁提交敏感電路圖紙或商業核心機密。"]}
# sitelinks -> the 3 LDPs (labels derived from package labels; descriptions = first section headings already used)
SLK={
"vi":[("OSAT đóng gói kiểm thử","/semiconductor-osat","Khi cần đối chiếu một lô hàng,","thông tin nằm ở đâu?"),("Fabless gia công ngoài","/fabless","Hàng chưa về kho.","Quyết định vẫn cần được đưa ra."),("Nhà cung ứng công nghiệp","/supplierecosystem","Một chuỗi ngành,","không chỉ một bài toán vận hành.")],
"en":[("OSAT packaging & test","/semiconductor-osat","When a lot needs review,","where is the information?"),("Fabless outsourcing","/fabless","Goods are not yet in stock.","Decisions still need to be made."),("Industrial suppliers","/supplierecosystem","One industry chain,","not just one operating problem.")],
"zh-Hans":[("封测 OSAT","/semiconductor-osat","当需要核查某个批次时，","信息在哪里？"),("无晶圆厂 Fabless","/fabless","货物尚未入库。","决策仍需推进。"),("工业供应商","/supplierecosystem","一条产业链，","而不只是单一运营问题。")],
"zh-Hant":[("封測 OSAT","/semiconductor-osat","當需要核查某個批次時，","資訊在哪裡？"),("無晶圓廠 Fabless","/fabless","貨物尚未入庫。","決策仍需推進。"),("工業供應商","/supplierecosystem","一條產業鏈，","而不只是單一營運問題。")]}
NEG={
"vi":["tuyển dụng","việc làm","thực tập","khóa học","luận văn","cổ phiếu","chứng khoán"],
"en":["semiconductor jobs","semiconductor internship","semiconductor course","semiconductor thesis","semiconductor stock price"],
"zh-Hans":["招聘","求职","实习","培训课程","毕业论文","股票","股价"],
"zh-Hant":["徵才","職缺","實習","培訓課程","畢業論文","股票","股價"]}
cols1=["Campaign","Ad Group","Ad Group Status","Keyword","Criterion Type","Ad type"]+[f"Headline {i}" for i in range(1,16)]+[f"Description {i}" for i in range(1,5)]+["Final URL","Final URL suffix","Status"]
rows=[];bad=[]
def r(**k):
    d={c:"" for c in cols1};d.update(k);rows.append(d)
for l in ["vi","en","zh-Hans","zh-Hant"]:
    ag=f"BRAND_DIGIWIN_{l}"
    r(**{"Campaign":CAMP,"Ad Group":ag,"Ad Group Status":"Enabled"})
    r(**{"Campaign":CAMP,"Ad Group":ag,"Keyword":KW[l],"Criterion Type":"Exact","Status":"Enabled"})
    for h in H[l]:
        if wl(h)>30: bad.append(("H",l,h,wl(h)))
    for x in D[l]:
        if wl(x)>90: bad.append(("D",l,x,wl(x)))
    d={"Campaign":CAMP,"Ad Group":ag,"Ad type":"Responsive search ad","Final URL":f"{BASE}/semiconductor-osat?lang={l}","Final URL suffix":SUF("brand",l,"rsa_v1"),"Status":"Enabled"}
    for i,h in enumerate(H[l],1): d[f"Headline {i}"]=h
    for i,x in enumerate(D[l],1): d[f"Description {i}"]=x
    r(**d)
    for t in NEG[l]:
        r(**{"Campaign":CAMP,"Keyword":t,"Criterion Type":"Negative Phrase","Status":"Enabled"})
with open("semi_brand_neg.csv","w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=cols1);w.writeheader();w.writerows(rows)
cols2=["Asset action","Level","Campaign","Ad group","Sitelink text","Description line 1","Description line 2","Final URL","Final URL suffix","Status"]
s=[]
for l,items in SLK.items():
    for t,route,d1,d2 in items:
        if wl(t)>25 or wl(d1)>35 or wl(d2)>35: bad.append(("SL",l,t,wl(t),wl(d1),wl(d2)))
        s.append({"Asset action":"Create new","Level":"Ad Group","Campaign":CAMP,"Ad group":f"BRAND_DIGIWIN_{l}","Sitelink text":t,"Description line 1":d1,"Description line 2":d2,"Final URL":f"{BASE}{route}?lang={l}","Final URL suffix":SUF("brand",l,"sitelink"),"Status":"Enabled"})
with open("semi_brand_sitelinks.csv","w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=cols2);w.writeheader();w.writerows(s)
print(len(rows),"rows (adgroups+kw+rsa+negatives);",len(s),"sitelinks; over-limit:",bad)
