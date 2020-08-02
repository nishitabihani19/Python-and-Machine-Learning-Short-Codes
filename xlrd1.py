import xlrd
import xlwt
import requests
import json
print(dir(xlrd.open_workbook))
book=xlrd.open_workbook('oxford.xls')
print(book.nsheets)
print(book.sheet_names())
n1=int(input('enter'))
first_sheet = book.sheet_by_index(n1)
#n2=int(input('enter2'))

len_row=(len(first_sheet.row_values(0)))
len_col=(len(first_sheet.col_values(0)))
#print(xlrd.__sizeof__(row_values))
print(len_row,len_col)
print(first_sheet.row_values(len_col-1))
print(first_sheet.col_values(len_row-1))

