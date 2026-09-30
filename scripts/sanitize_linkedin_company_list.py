"""
Script làm sạch dữ liệu CRM phục vụ LinkedIn Matched Audience Discovery.
Chỉ trích xuất: companyname, country, city.
Tuyệt đối loại bỏ: PII, phone, email, các trường CRM (SDR, MDR, stage, săn đón, notes).
Loại trừ 4 tập đoàn theo giả thuyết D1: Intel, Samsung, Hana Micron, Amkor.
"""

import os
import csv

def sanitize_crm_lists():
    file_vn = r'C:\Users\ASUS\OneDrive\Desktop\Temporary\VN_Contact_Linh kiện điện tử.csv'
    file_cn = r'C:\Users\ASUS\OneDrive\Desktop\Temporary\CN-Contact-Điện tử Bán dẫn.csv'
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'private')
    output_file = os.path.join(output_dir, 'linkedin_company_list_sanitized.csv')

    os.makedirs(output_dir, exist_ok=True)

    excluded_keywords = ['INTEL', 'SAMSUNG', 'AMKOR', 'HANA MICRON']
    companies = {}

    # 1. Đọc và lọc tệp VN
    if os.path.exists(file_vn):
        with open(file_vn, 'r', encoding='utf-8-sig') as f:
            for r in csv.DictReader(f):
                cname = (r.get('Tên công ty') or r.get('Company') or '').strip()
                tax = (r.get('Tax code') or '').strip()
                city = (r.get('Province') or '').strip()
                if cname:
                    c_clean = cname.upper()
                    if any(kw in c_clean for kw in excluded_keywords):
                        continue
                    key = tax if tax else c_clean
                    if key not in companies:
                        companies[key] = {
                            'companyname': cname,
                            'country': 'Vietnam',
                            'city': city
                        }

    # 2. Đọc và lọc tệp CN
    if os.path.exists(file_cn):
        with open(file_cn, 'r', encoding='utf-8-sig') as f:
            for r in csv.DictReader(f):
                cname = (r.get('公司全名') or r.get('企業') or '').strip()
                tax = (r.get('稅號') or '').strip()
                city = (r.get('地區') or '').strip()
                if cname:
                    c_clean = cname.upper()
                    if any(kw in c_clean for kw in excluded_keywords):
                        continue
                    key = tax if tax else c_clean
                    if key not in companies:
                        companies[key] = {
                            'companyname': cname,
                            'country': 'Vietnam',
                            'city': city
                        }

    # 3. Xuất file CSV chuẩn định dạng LinkedIn Company List
    fieldnames = ['companyname', 'country', 'city']
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in companies.values():
            writer.writerow(item)

    print(f"Exported {len(companies)} valid companies to: {output_file}")
    return output_file

if __name__ == '__main__':
    sanitize_crm_lists()
