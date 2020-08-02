import xlwt
import xlrd
from datetime import datetime

patt0=xlwt.easyxf("font: name Times New Roman, color-index red, bold on",num_format_str='#,##0.00')
patt1=xlwt.easyxf(num_format_str='DD-MM-YY')
patt2=xlwt.easyxf("font: name Comic Sans MS, color-index green, italic on",num_format_str='#,##0.0000')

wb=xlwt.Workbook()
ws=wb.add_sheet
ws=wb.add_sheet('sheet2',cell_overwrite_ok=False)

ws.write(0,0,78.98,patt0)
ws.write(2,0,datetime.now(),patt1)
ws.write(0,1,5)
ws.write(1,1,5)
ws.write(2,1,5)
ws.write(3,1,5)
ws.write(4,1,1)
ws.write(5,1,6)
ws.write(7,1,xlwt.Formula("B4+B5+B6"),patt2)

wb.save('one.xls')

