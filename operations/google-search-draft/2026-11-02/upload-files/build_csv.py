# -*- coding: utf-8 -*-
"""Build Google Ads bulk-upload CSV for the semiconductor Search draft (campaign Paused)."""
import csv, re, sys, unicodedata, io

ROOT = r"D:\Digiwin_Semiconducter_Workspace"
SHEET = ROOT + r"\ads\google\Google_Search_Build_Sheet.md"
KW_DIR = ROOT + r"\deliverables\manager-package-v2\2026-10-07\06_Google\Tu_khoa"
OUT = r"C:\Users\ASUS\AppData\Local\Temp\claude\D--Digiwin-Semiconducter-Workspace\efe2d053-b7aa-4f70-bd1b-f519268e6313\scratchpad\semi_search_upload.csv"

CAMPAIGN = "SEMI_[SEARCH]_vn_semiconductor_search_p1_[20261102]_50.000d-ngay_PAUSED_REVIEW"
BASE = "https://solutions.digiwin.com.vn"
LOCALES = ["vi", "en", "zh-Hans", "zh-Hant"]
LOC_NAME = {"vi": "Vietnamese", "en": "English", "zh-Hans": "Simplified", "zh-Hant": "Traditional"}
GROUPS = [  # (sheet group key, ad group prefix, route, utm segment)
    ("OSAT_LOT_TEST", "OSAT_LOT_TEST", "/semiconductor-osat", "osat"),
    ("FABLESS_OUTSOURCE_WIP", "FABLESS_OUTSOURCE_WIP", "/fabless", "fabless"),
    ("ERP_MES_OT_PARTNER", "ERP_MES_OT_PARTNER", "/supplierecosystem", "supplier"),
]
SECTION_TITLES = {  # sheet "### n. ..." -> locale
    "Vietnamese": "vi", "English": "en", "Simplified Chinese": "zh-Hans", "Traditional Chinese": "zh-Hant",
}
# SI / implementer-partner framing conflicts with PO clarification 2026-10-07 (Supplier = industrial supplier)
SI_DROP = {
    "Supplier SI: Nối dữ liệu",
    "Electronics MES Partner", "Industrial Automation Partner", "End-to-End Traceability SI", "Semiconductor SI Partner",
    "电子制造 MES 实施伙伴", "半导体生态 SI 合作方案",
    "電子製造 MES 導入夥伴", "半導體生態 SI 合作方案",
}


def wlen(s):
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)


# ---------- parse RSA copy from build sheet ----------
text = open(SHEET, encoding="utf-8").read()
rsa = {}  # (locale, group) -> (headlines, descriptions)
cur_loc = cur_grp = None
for line in text.splitlines():
    m = re.match(r"### \d\. ([A-Za-z ]+?) \(", line)
    if m:
        cur_loc = SECTION_TITLES.get(m.group(1).strip())
        continue
    m = re.match(r"#### (\w+)", line)
    if m and cur_loc:
        cur_grp = m.group(1)
        continue
    m = re.match(r"(Headlines|Descriptions) \((\d+)\): (.*)", line)
    if m and cur_loc and cur_grp:
        items = re.findall(r"`([^`]+)`", m.group(3))
        d = rsa.setdefault((cur_loc, cur_grp), {"h": [], "d": []})
        d["h" if m.group(1) == "Headlines" else "d"] = items

# ---------- keywords from approved package ----------
def read_kw(loc):
    lines = [l.strip() for l in open(f"{KW_DIR}\\{loc}.txt", encoding="utf-8-sig").read().splitlines()]
    res, sect = {}, None
    for l in lines:
        if l in ("OSAT", "Fabless", "Supplier / industrial factory"):
            sect = {"OSAT": "OSAT_LOT_TEST", "Fabless": "FABLESS_OUTSOURCE_WIP",
                    "Supplier / industrial factory": "ERP_MES_OT_PARTNER"}[l]
            res[sect] = []
        elif l.startswith("Digiwin brand"):
            sect = None
        elif sect and (l.startswith('"') or l.startswith("[")):
            res[sect].append(l)
    return res

# ---------- sitelinks (text<=25, desc<=35 weighted; names/desc taken from live LDP section headings) ----------
SL = {}
def sl(page, loc, rows):
    SL[(page, loc)] = rows
# rows: (anchor, text, d1, d2)
sl("osat", "vi", [
 ("operations-questions", "Câu hỏi vận hành", "Khi cần đối chiếu một lô hàng,", "thông tin nằm ở đâu?"),
 ("lot-map", "Hành trình lot", "Theo một lot, dữ liệu vận hành", "theo từng nhịp sản xuất"),
 ("management-layers", "Hai lớp vận hành", "Từ quản trị đến thực thi:", "một nhu cầu kết nối thông tin"),
 ("industry-delivery", "Hệ sinh thái bán dẫn", "Giải pháp đa mắt xích bán dẫn", "và kiểm thử"),
 ("local-delivery", "Hiện diện tại Việt Nam", "Kinh nghiệm ngành quốc tế.", "Năng lực chuyển giao tại Việt Nam"),
 ("resources", "Nguồn tham khảo", "Đối chiếu cơ chế với", "nguồn tham khảo")])
sl("osat", "en", [
 ("operations-questions", "Operating questions", "When a lot needs review,", "where is the information?"),
 ("lot-map", "Lot journey", "Follow one lot. Operations data", "for every production beat"),
 ("management-layers", "Two operating layers", "From management to execution:", "one need to connect information"),
 ("industry-delivery", "Semiconductor ecosystem", "One solutions ecosystem, across", "semiconductor and testing links"),
 ("local-delivery", "Local presence in Vietnam", "International industry experience.", "Delivery capability in Vietnam."),
 ("resources", "Sources & cross-checks", "Check the mechanism against", "reference sources.")])
sl("osat", "zh-Hans", [
 ("operations-questions", "运营问题", "当需要核查某个批次时，", "信息在哪里？"),
 ("lot-map", "批次历程", "追踪一个批次。", "覆盖每个生产节拍的运营数据。"),
 ("management-layers", "两层运营架构", "从管理到执行：", "同一个信息连接需求。"),
 ("industry-delivery", "半导体产业链", "一个解决方案生态，覆盖", "半导体与测试的多个环节。"),
 ("local-delivery", "越南本地交付", "国际行业经验。", "越南本地交付能力。"),
 ("resources", "参考来源与核对", "将机制与参考来源", "进行核对。")])
sl("osat", "zh-Hant", [
 ("operations-questions", "營運問題", "當需要核查某個批次時，", "資訊在哪裡？"),
 ("lot-map", "批次歷程", "追蹤一個批次。", "涵蓋每個生產節拍的營運資料。"),
 ("management-layers", "兩層營運架構", "從管理到執行：", "同一個資訊串接需求。"),
 ("industry-delivery", "半導體產業鏈", "一個解決方案生態，涵蓋", "半導體與測試的多個環節。"),
 ("local-delivery", "越南在地交付", "國際產業經驗。", "越南在地交付能力。"),
 ("resources", "參考來源與核對", "將機制與參考來源", "進行核對。")])

sl("fabless", "vi", [
 ("operations-questions", "Câu hỏi vượt ranh giới", "Hàng chưa về kho.", "Quyết định vẫn cần được đưa ra."),
 ("fabless-map", "Bản đồ vận hành phân tán", "Một chuỗi đối tác.", "Nhiều lớp thông tin cần nối."),
 ("management-layers", "Ba nhóm thông tin", "Từ WIP ở đối tác đến thông tin", "phục vụ quyết định."),
 ("relationship-proof", "Bằng chứng quan hệ", "Bằng chứng từ hồ sơ", "của doanh nghiệp."),
 ("industry-delivery", "Danh mục IC Design", "Một danh mục ngành,", "nhiều doanh nghiệp IC Design."),
 ("resources", "Nguồn tham khảo", "Từ câu hỏi vận hành đến bằng", "chứng có thể đối chiếu.")])
sl("fabless", "en", [
 ("operations-questions", "Cross-company questions", "Goods are not yet in stock.", "Decisions still need to be made."),
 ("fabless-map", "Operations map", "One partner chain.", "Many data layers to connect."),
 ("management-layers", "Management information", "From partner WIP to information", "for decisions."),
 ("relationship-proof", "System relationship proof", "Evidence from company", "records."),
 ("industry-delivery", "IC design portfolio", "One industry portfolio,", "many IC design companies."),
 ("resources", "References", "From operating questions to", "evidence that can be reviewed.")])
sl("fabless", "zh-Hans", [
 ("operations-questions", "跨企业边界的问题", "货物尚未入库。", "决策仍需推进。"),
 ("fabless-map", "分布式运营示意图", "一条合作链。", "多层信息需要衔接。"),
 ("management-layers", "三类管理信息", "从合作伙伴在制品", "到支持决策的信息。"),
 ("relationship-proof", "系统关系依据", "来自企业", "公开资料的依据。"),
 ("industry-delivery", "本地布局与交付", "一个行业组合，", "涵盖多家 IC 设计企业。"),
 ("resources", "参考资料", "从运营问题到", "可核对的依据。")])
sl("fabless", "zh-Hant", [
 ("operations-questions", "跨企業邊界的問題", "貨物尚未入庫。", "決策仍需推進。"),
 ("fabless-map", "分散式營運示意圖", "一條合作鏈。", "多層資訊需要銜接。"),
 ("management-layers", "三類管理資訊", "從合作夥伴在製品", "到支援決策的資訊。"),
 ("relationship-proof", "系統關係依據", "來自企業", "公開資料的依據。"),
 ("industry-delivery", "在地布局與交付", "一個產業組合，", "涵蓋多家 IC 設計企業。"),
 ("resources", "參考資料", "從營運問題到", "可核對的依據。")])

sl("supplier", "vi", [
 ("audience-context", "Bối cảnh doanh nghiệp", "Một chuỗi ngành,", "không chỉ một bài toán vận hành."),
 ("ecosystem-architecture", "Kiến trúc vận hành", "Nhìn rõ ranh giới từng lớp", "trước khi nói về kết nối chuỗi."),
 ("operations-questions", "Giá trị vận hành", "Kết nối để giải bài toán nhà máy,", "không phải để nối thêm phần mềm."),
 ("product-evidence", "Năng lực giải pháp", "Một dòng dữ liệu xuyên suốt", "nhà máy bán dẫn."),
 ("local-delivery", "Hiện diện tại Việt Nam", "Kinh nghiệm ngành quốc tế.", "Năng lực chuyển giao tại Việt Nam"),
 ("resources", "Giải pháp và case study", "Bắt đầu từ lớp thông tin", "cần kết nối.")])
sl("supplier", "en", [
 ("audience-context", "Business context", "One industry chain,", "not just one operating problem."),
 ("ecosystem-architecture", "Operating architecture", "See each layer's boundary clearly", "before discussing connectivity."),
 ("operations-questions", "Practical operating value", "Connect to solve factory", "challenges, not add software."),
 ("product-evidence", "Solution capabilities", "One continuous data flow", "across the semiconductor factory."),
 ("local-delivery", "Local presence in Vietnam", "International industry experience.", "Delivery capability in Vietnam."),
 ("resources", "Solutions & case studies", "Start with the information", "layer that needs connecting.")])
sl("supplier", "zh-Hans", [
 ("audience-context", "企业场景", "一条产业链，", "而不只是单一运营问题。"),
 ("ecosystem-architecture", "运营架构", "清楚了解各层边界，", "再讨论产业链连接。"),
 ("operations-questions", "实际运营价值", "连接以解决工厂问题，", "而非继续增加软件。"),
 ("product-evidence", "解决方案能力", "一条贯通的数据流，", "覆盖半导体工厂。"),
 ("local-delivery", "越南本地交付", "国际行业经验。", "越南本地交付能力。"),
 ("resources", "解决方案与案例", "从需要连接的", "信息层开始。")])
sl("supplier", "zh-Hant", [
 ("audience-context", "企業情境", "一條產業鏈，", "而不只是單一營運問題。"),
 ("ecosystem-architecture", "營運架構", "清楚了解各層邊界，", "再討論產業鏈串接。"),
 ("operations-questions", "實際營運價值", "串接以解決工廠問題，", "而非繼續增加軟體。"),
 ("product-evidence", "解決方案能力", "一條貫通的資料流，", "涵蓋半導體工廠。"),
 ("local-delivery", "越南在地交付", "國際產業經驗。", "越南在地交付能力。"),
 ("resources", "解決方案與案例", "從需要串接的", "資訊層開始。")])

# ---------- build rows ----------
COLS = ["Campaign", "Ad Group", "Campaign Status", "Campaign Type", "Networks", "Budget", "Budget type",
        "Bid Strategy Type", "Maximum CPC bid limit", "Languages", "EU political ads", "Targeting method", "Exclusion method",
        "Ad Group Status", "Keyword", "Criterion Type", "Ad type"] + \
       [f"Headline {i}" for i in range(1, 16)] + [f"Description {i}" for i in range(1, 5)] + \
       ["Path 1", "Path 2", "Final URL", "Final URL suffix",
        "Link Text", "Description Line 1", "Description Line 2", "Status"]
rows = []
def row(**kw):
    r = {c: "" for c in COLS}
    r.update(kw)
    rows.append(r)

row(**{"Campaign": CAMPAIGN, "Campaign Status": "Paused", "Campaign Type": "Search", "Networks": "Google search",
       "Budget": "50000", "Budget type": "Daily", "Bid Strategy Type": "Maximize clicks",
       "Maximum CPC bid limit": "25000", "Languages": "vi;en;zh_CN;zh_TW", "EU political ads": "No",
       "Targeting method": "Location of presence", "Exclusion method": "Location of presence"})

problems = []
dropped = []
for loc in LOCALES:
    kws = read_kw(loc)
    for key, prefix, route, seg in GROUPS:
        ag = f"{prefix}_{loc}"
        url = f"{BASE}{route}?lang={loc}"
        row(**{"Campaign": CAMPAIGN, "Ad Group": ag, "Ad Group Status": "Enabled"})
        for k in kws[key]:
            if k.startswith('"'):
                row(**{"Campaign": CAMPAIGN, "Ad Group": ag, "Keyword": k.strip('"'), "Criterion Type": "Phrase", "Status": "Enabled"})
            else:
                row(**{"Campaign": CAMPAIGN, "Ad Group": ag, "Keyword": k.strip("[]"), "Criterion Type": "Exact", "Status": "Enabled"})
        d = rsa[(loc, key)]
        hs = [h for h in d["h"] if h not in SI_DROP]
        dropped += [(ag, h) for h in d["h"] if h in SI_DROP]
        ds = d["d"]
        for h in hs:
            if wlen(h) > 30: problems.append(("H>30", ag, h, wlen(h)))
        for x in ds:
            if wlen(x) > 90: problems.append(("D>90", ag, x, wlen(x)))
        r = {"Campaign": CAMPAIGN, "Ad Group": ag, "Ad type": "Responsive search ad", "Final URL": url,
             "Final URL suffix": f"utm_source=google&utm_medium=cpc&utm_campaign=vn_semiconductor_search_p1&utm_content={seg}_{loc}_rsa_v1&utm_term={{keyword}}",
             "Status": "Enabled"}
        for i, h in enumerate(hs, 1): r[f"Headline {i}"] = h
        for i, x in enumerate(ds, 1): r[f"Description {i}"] = x
        row(**r)
        for anchor, t, d1, d2 in SL[(seg, loc)]:
            if wlen(t) > 25: problems.append(("SLtext>25", ag, t, wlen(t)))
            if wlen(d1) > 35: problems.append(("SLd1>35", ag, d1, wlen(d1)))
            if wlen(d2) > 35: problems.append(("SLd2>35", ag, d2, wlen(d2)))
            row(**{"Campaign": CAMPAIGN, "Ad Group": ag, "Link Text": t, "Description Line 1": d1, "Description Line 2": d2,
                   "Final URL": f"{url}#{anchor}",
                   "Final URL suffix": f"utm_source=google&utm_medium=cpc&utm_campaign=vn_semiconductor_search_p1&utm_content={seg}_{loc}_sitelink&utm_term={{keyword}}",
                   "Status": "Enabled"})

with open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS, quoting=csv.QUOTE_MINIMAL)
    w.writeheader(); w.writerows(rows)

sys.stdout.reconfigure(encoding="utf-8")
print("rows:", len(rows), "ad groups:", len(LOCALES) * len(GROUPS))
print("problems:", problems)
print("dropped SI headlines:", dropped)
for (loc, g), d in sorted(rsa.items()):
    print(loc, g, len(d["h"]), "headlines", len(d["d"]), "desc")
