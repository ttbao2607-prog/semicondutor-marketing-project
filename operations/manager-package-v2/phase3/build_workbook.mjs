import fs from 'node:fs/promises';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';
const root='D:/LinkedIn_Package_V2_2026-10-07';
const rec=`${root}/operations/manager-package-v2/phase3`;
const out=`${root}/deliverables/manager-package-v2/2026-10-07/04_Theo_doi/Theo_doi_paid_ads.xlsx`;
const wb=Workbook.create();
const s=wb.worksheets.add('Review tuan');
const j=wb.worksheets.add('Nhat ky');
const reports=[];
for (const sh of [s,j]) {
  sh.showGridLines=false;
  sh.getRange(sh===s?'A1:J29':'A1:W38').format.font={name:'Arial',size:11,color:'#1E293B'};
  sh.getRange(sh===s?'A1:J29':'A1:W38').format.rowHeight=25;
  sh.getRange(sh===s?'A1:J29':'A1:W38').format.verticalAlignment='center';
  sh.getRange(sh===s?'A1:J29':'A1:W38').format.columnWidth=16;
}
s.tabColor='#174DB3';
s.getRange('A2').values=[['Review paid ads']];
s.getRange('A2').format.font={name:'Arial',size:16,bold:true,color:'#1E293B'};
s.getRange('A3').values=[['VND, chưa thuế. Bảo quản lý chi trên dashboard; kế toán xử lý thuế và thanh toán.']];
s.getRange('A3').format.font.italic=true;
s.getRange('A5:B5').values=[['Ngân sách đề xuất','VND, chưa thuế']];
s.getRange('A6:B11').values=[
 ['Trần toàn phương án',11700000],['Đợt LinkedIn đầu',5600000],['Giữ lại trong cùng trần',null],
 ['LinkedIn tiếp theo tối đa',5600000],['Search tùy chọn tối đa',500000],['Tổng theo cơ cấu',null]
];
s.getRange('B8').formulas=[['=B6-B7']];
s.getRange('B11').formulas=[['=SUM(B7,B9:B10)']];
s.getRange('D5:E5').values=[['Chi đã ghi nhận','VND, chưa thuế']];
s.getRange('D6').values=[['Chi đã nhập']];
s.getRange('E6').formulas=[['=IF(COUNT(\'Nhat ky\'!H8:H37)=0,"",SUM(\'Nhat ky\'!H8:H37))']];
s.getRange('D7').values=[['Còn lại so với trần']];
s.getRange('E7').formulas=[['=IF(ISNUMBER(E6),B6-E6,"")']];
s.getRange('D9').values=[['Tuần 1 chạy đúng plan. Review cuối tuần để chọn hướng tuần 2.']];
s.getRange('D10').values=[['Bảo đổi đúng đoạn yếu, giữ phần hiệu quả, trong trần được duyệt.']];
s.getRange('D11').values=[['Lead đã xác minh là tín hiệu bổ sung khi đánh giá đầu tư.']];
s.getRange('B6:B7').format.font.color='#2563EB';
s.getRange('B9:B10').format.font.color='#2563EB';
for(const r of ['B6:B7','B9:B10'])s.getRange(r).format.fill='#FFF4D6';
s.getRange('B6:B11').setNumberFormat('#,##0;(#,##0);0');
s.getRange('E6:E7').setNumberFormat('#,##0;(#,##0);0');
s.getRange('E7').conditionalFormats.add('cellIs',{operator:'lessThan',formula:0,format:{fill:'#FEE2E2',font:{color:'#B91C1C',bold:true}}});
s.getRange('A13').values=[['Kết quả theo tuần và kênh']];
s.getRange('A13').format.font.bold=true;
s.getRange('A14:J14').values=[['Tuần','Kênh','Chi dashboard','Hiển thị','Lượt click','CTR','Phiên tương tác','Lead thô','Lead xác minh','Lead hợp lệ / thô']];
s.getRange('A15:B18').values=[[1,'LinkedIn'],[1,'Search'],[2,'LinkedIn'],[2,'Search']];
// Only aggregate when every populated campaign row in that week/channel has a numeric measure.
// Blank source observations stay unavailable. Zero inputs remain valid observations.
const sourceColumns={C:'H',D:'I',E:'K',G:'M',H:'N',I:'O'};
for(let row=15;row<=18;row++){
 const population=`COUNTIFS('Nhat ky'!$C$8:$C$37,$A${row},'Nhat ky'!$D$8:$D$37,$B${row},'Nhat ky'!$E$8:$E$37,"<>")`;
 for(const [target,source] of Object.entries(sourceColumns)){
   const observed=`COUNTIFS('Nhat ky'!$C$8:$C$37,$A${row},'Nhat ky'!$D$8:$D$37,$B${row},'Nhat ky'!$E$8:$E$37,"<>",'Nhat ky'!$${source}$8:$${source}$37,">=0",'Nhat ky'!$${source}$8:$${source}$37,"<>")`;
   s.getRange(`${target}${row}`).formulas=[[`=IF(AND(${population}>0,${observed}=${population}),SUMIFS('Nhat ky'!$${source}$8:$${source}$37,'Nhat ky'!$C$8:$C$37,$A${row},'Nhat ky'!$D$8:$D$37,$B${row},'Nhat ky'!$E$8:$E$37,"<>"),"")`]];
 }
 s.getRange(`F${row}`).formulas=[[`=IF(COUNT(D${row},E${row})=2,IF(D${row}>0,E${row}/D${row},""),"")`]];
 s.getRange(`J${row}`).formulas=[[`=IF(COUNT(H${row},I${row})=2,IF(H${row}>0,I${row}/H${row},""),"")`]];
}
s.getRange('C15:E18').setNumberFormat('#,##0');
s.getRange('G15:I18').setNumberFormat('#,##0');
s.getRange('F15:F18').setNumberFormat('0.0%');
s.getRange('J15:J18').setNumberFormat('0.0%');
s.getRange('A21:G21').values=[['Tuần','Đúng tệp: nhận định','Phân phối / quan tâm','Hành vi đi tiếp','Chi phí / mức chi','Hướng tuần tiếp','Lý do từ dữ liệu']];
s.getRange('A22:A23').values=[[1],[2]];
s.getRange('B22:G23').format.fill='#FFF4D6';
s.getRange('B22:G23').format.wrapText=true;
s.getRange('A22:G23').format.rowHeight=70;
s.getRange('A25').values=[['Ô vàng: số đề xuất hoặc nhận định Bảo cập nhật. Số thực chạy nhập ở Nhat ky.']];
s.getRange('A26').values=[['Nguồn ngân sách: phương án Bảo gửi Vy ngày 07/10/2026, mục Ngân sách chưa thuế.']];
s.getRange('A27').values=[['Bảng tuần tổng hợp các campaign cùng kỳ; reach và frequency đọc theo từng campaign.']];
s.getRange('A28').values=[['Giữ cùng định nghĩa click, kỳ đo và nguồn trang đọc khi so sánh. Ô trống là dữ liệu cần bổ sung.']];
s.getRange('A25:A28').format.font={name:'Arial',size:11,color:'#475569',italic:true};
s.getRange('A6:A11').format.wrapText=true;
s.getRange('A6:B11').format.rowHeight=35;
s.getRange('A1:A29').format.columnWidth=25;
s.getRange('B1:B29').format.columnWidth=23;
s.getRange('G1:J29').format.columnWidth=20;
s.getRange('A14:J14').format.wrapText=true;
s.getRange('A14:J14').format.rowHeight=46;
s.getRange('A21:G21').format.wrapText=true;
s.getRange('A21:G21').format.rowHeight=45;

j.getRange('A2').values=[['Nhật ký dữ liệu theo kỳ']];
j.getRange('A2').format.font={name:'Arial',size:16,bold:true,color:'#1E293B'};
j.getRange('A3').values=[['Nguồn: chi và phân phối từ dashboard quảng cáo; phiên từ báo cáo trang đọc; lead xác minh từ pipeline công ty.']];
j.getRange('A4').values=[['Một dòng / campaign / tuần / kỳ đo. Cập nhật số lũy kế cùng kỳ vào dòng đó; giữ các kỳ tách nhau.']];
j.getRange('A5').values=[['CTR = click / hiển thị; engagement rate = tương tác / hiển thị LinkedIn; frequency = hiển thị / reach cùng campaign.']];
j.getRange('A6').values=[['CPM = chi / hiển thị × 1.000; CPC = chi / click. Lead hợp lệ / thô = lead xác minh / lead thô.']];
j.getRange('A3:A6').format.font={name:'Arial',size:11,color:'#475569',italic:true};
j.getRange('A7:W7').values=[['Từ ngày','Đến ngày','Tuần','Kênh','Campaign','Nhóm','Ngôn ngữ','Chi dashboard (VND)','Hiển thị','Reach','Click','Tương tác LinkedIn','Phiên có tương tác','Lead thô','Lead xác minh','Đúng tệp / search term','Nhận định','Điều chỉnh','CTR','Engagement rate','CPM (VND)','CPC (VND)','Frequency']];
j.getRange('A8:R37').format.fill='#FFF8E8';
j.getRange('A8:B37').setNumberFormat('dd/mm/yyyy');
j.getRange('C8:C37').dataValidation={rule:{type:'whole',operator:'between',formula1:1,formula2:2}};
j.getRange('D8:D37').dataValidation={rule:{type:'list',values:['LinkedIn','Search']}};
j.getRange('F8:F37').dataValidation={rule:{type:'list',values:['VN','FDI']}};
j.getRange('G8:G37').dataValidation={rule:{type:'list',values:['Tiếng Việt','English','中文 giản thể','中文 phồn thể']}};
for(const [col,name] of [['H','Chi'],['I','Hiển thị'],['J','Reach'],['K','Click'],['L','Tương tác'],['M','Phiên'],['N','Lead thô'],['O','Lead xác minh']]){
 j.getRange(`${col}8:${col}37`).setNumberFormat('#,##0');
 j.getRange(`${col}8:${col}37`).dataValidation={rule:{type:'decimal',operator:'greaterThanOrEqual',formula1:0}};
}
for(let r=8;r<=37;r++){
 j.getRange(`S${r}`).formulas=[[`=IF(COUNT(I${r},K${r})=2,IF(I${r}>0,K${r}/I${r},""),"")`]];
 j.getRange(`T${r}`).formulas=[[`=IF(D${r}="LinkedIn",IF(COUNT(I${r},L${r})=2,IF(I${r}>0,L${r}/I${r},""),""),"")`]];
 j.getRange(`U${r}`).formulas=[[`=IF(COUNT(H${r},I${r})=2,IF(I${r}>0,H${r}/I${r}*1000,""),"")`]];
 j.getRange(`V${r}`).formulas=[[`=IF(COUNT(H${r},K${r})=2,IF(K${r}>0,H${r}/K${r},""),"")`]];
 j.getRange(`W${r}`).formulas=[[`=IF(D${r}="LinkedIn",IF(COUNT(I${r},J${r})=2,IF(J${r}>0,I${r}/J${r},""),""),"")`]];
}
j.getRange('S8:T37').setNumberFormat('0.0%');
j.getRange('U8:V37').setNumberFormat('#,##0');
j.getRange('W8:W37').setNumberFormat('0.00');
j.getRange('A1:B38').format.columnWidth=15;
j.getRange('C1:D38').format.columnWidth=12;
j.getRange('E1:E38').format.columnWidth=24;
j.getRange('F1:G38').format.columnWidth=20;
j.getRange('H1:O38').format.columnWidth=18;
j.getRange('P1:R38').format.columnWidth=30;
j.getRange('S1:W38').format.columnWidth=18;
j.getRange('A7:W7').format.wrapText=true;
j.getRange('A7:W7').format.rowHeight=45;
j.getRange('E8:G37').format.wrapText=true;
j.getRange('P8:R37').format.wrapText=true;
j.getRange('A8:W37').format.rowHeight=38;
j.freezePanes.freezeRows(7); j.freezePanes.freezeColumns(5);
for(const [sh,ranges] of [[s,['A5:B5','D5:E5','A14:J14','A21:G21']],[j,['A7:W7']]]){
 for(const address of ranges){sh.getRange(address).format.fill='#174DB3';sh.getRange(address).format.font.color='#FFFFFF';sh.getRange(address).format.font.bold=true;sh.getRange(address).format.horizontalAlignment='center';}
}
// Meaningful disposable input tests, restored before any deliverable export.
function assertEq(actual,expected,label){if(actual!==expected)throw Error(`${label}: ${JSON.stringify(actual)} != ${JSON.stringify(expected)}`);reports.push({label,expected,actual});}
wb.recalculate();
assertEq(s.getRange('B8').values[0][0],6100000,'held inside cap');
assertEq(s.getRange('B11').values[0][0],11700000,'allocation total');
assertEq(s.getRange('E6').values[0][0],'','missing spend is blank');
j.getRange('C8:O8').values=[[1,'LinkedIn','Sample QA only','FDI','English',200000,10000,2000,100,200,30,4,1]];
wb.recalculate();
assertEq(s.getRange('E6').values[0][0],200000,'recorded spend updates');
assertEq(s.getRange('F15').values[0][0],0.01,'weighted CTR');
assertEq(s.getRange('J15').values[0][0],0.25,'verified lead ratio');
assertEq(j.getRange('U8').values[0][0],20000,'CPM');
assertEq(j.getRange('V8').values[0][0],2000,'CPC');
assertEq(j.getRange('W8').values[0][0],5,'campaign frequency');
j.getRange('K8').values=[[0]];wb.recalculate();assertEq(s.getRange('F15').values[0][0],0,'observed zero click yields zero CTR');assertEq(j.getRange('V8').values[0][0],'','zero-click CPC unavailable');
j.getRange('K8').values=[[null]];wb.recalculate();assertEq(s.getRange('F15').values[0][0],'','missing click keeps CTR unavailable');
j.getRange('C9:E9').values=[[1,'LinkedIn','Second sample QA only']];wb.recalculate();assertEq(s.getRange('C15').values[0][0],'','incomplete campaign measure keeps week total unavailable');
j.getRange('C8:O9').clear({applyTo:'contents'});wb.recalculate();
assertEq(s.getRange('E6').values[0][0],'','sample spend restored');assertEq(s.getRange('C15').values[0][0],'','weekly actuals restored');
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:50},maxChars:2000});
await fs.writeFile(`${rec}/workbook-verification.json`,JSON.stringify({engine:'artifact-tool',nativeExcelTest:false,tests:reports,errorScan:errors.ndjson,finalActuals:'blank; all sample inputs removed'},null,2));
for(const [sheetName,range,file] of [['Review tuan','A1:J28','workbook-review.png'],['Nhat ky','A1:J11','workbook-journal-left.png'],['Nhat ky','K7:W11','workbook-journal-right.png']]){
 const preview=await wb.render({sheetName,range,scale:1.4,format:'png'});await fs.writeFile(`${rec}/${file}`,new Uint8Array(await preview.arrayBuffer()));
}
const xlsx=await SpreadsheetFile.exportXlsx(wb);await xlsx.save(out);
// Export diagnostic is an internal authoring by-product, outside the recipient folder.
try { await fs.rename(out+'.inspect.ndjson',`${rec}/workbook-export-inspect.ndjson`); } catch(e) { if(e.code!=='ENOENT')throw e; }
console.log(JSON.stringify({output:out,tests:reports.length,errorScan:errors.ndjson}));
