# -*- coding: utf-8 -*-
import csv, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
CAMP="SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261102]_50.000d-ngay_PAUSED_REVIEW"
BASE="https://solutions.digiwin.com.vn"
def wl(s): return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)
# (prefix, route, seg, anchor) -> locale -> (text,d1,d2)
D={
 ("OSAT_LOT_TEST","/semiconductor-osat","osat","cas-ic-case"):{
  "vi":("Case Jiangsu CAS IC","ERP và iMES trong vận hành","đóng gói tiên tiến"),
  "en":("Jiangsu CAS IC case","ERP and iMES in advanced","packaging operations."),
  "zh-Hans":("Jiangsu CAS IC 案例","ERP 与 iMES","在先进封装运营中。"),
  "zh-Hant":("Jiangsu CAS IC 案例","ERP 與 iMES","在先進封裝營運中。")},
 ("FABLESS_OUTSOURCE_WIP","/fabless","fabless","bright-power-case"):{
  "vi":("Case Bright Power","Rút ngắn chu kỳ phản hồi","Case study tiêu biểu"),
  "en":("Bright Power case","Shorter response cycle","Featured case study"),
  "zh-Hans":("Bright Power 案例","缩短响应周期","典型案例"),
  "zh-Hant":("Bright Power 案例","縮短回應週期","代表案例")},
 ("ERP_MES_OT_PARTNER","/supplierecosystem","supplier","supply-chain"):{
  "vi":("Case Wafer Works","Kết nối dữ liệu từ tăng","trưởng tinh thể đến epitaxy."),
  "en":("Wafer Works case","Connect data from crystal","growth through epitaxy."),
  "zh-Hans":("Wafer Works 案例","连接从晶体生长","到外延的数据。"),
  "zh-Hant":("Wafer Works 案例","串接從晶體生長","到磊晶的資料。")},
}
cols=["Asset action","Level","Campaign","Ad group","Sitelink text","Description line 1","Description line 2","Final URL","Final URL suffix","Status"]
rows=[];bad=[]
for (pre,route,seg,anchor),loc in D.items():
  for l,(t,d1,d2) in loc.items():
    if wl(t)>25 or wl(d1)>35 or wl(d2)>35: bad.append((pre,l,t,wl(t),wl(d1),wl(d2)))
    rows.append({"Asset action":"Create new","Level":"Ad Group","Campaign":CAMP,"Ad group":f"{pre}_{l}",
      "Sitelink text":t,"Description line 1":d1,"Description line 2":d2,
      "Final URL":f"{BASE}{route}?lang={l}#{anchor}",
      "Final URL suffix":f"utm_source=google&utm_medium=cpc&utm_campaign=vn_semiconductor_search_p1&utm_content={seg}_{l}_sitelink&utm_term={{keyword}}","Status":"Enabled"})
with open("semi_case_sitelinks.csv","w",encoding="utf-8-sig",newline="") as f:
  w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
print(len(rows),"rows; over-limit:",bad)
