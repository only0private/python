# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:35:34 2017

@author: Hamaguchi
"""

import xlrd
import xlwt
import os
#==============================================================================
#Excelに書き込む 
#==============================================================================
os.chdir(r'C:\work')

#xlsファイル作成
#------------------------------------------------------------------------------
file = 'sample.xls'    #ファイル名****
book = xlwt.Workbook()   #bookを編集していく()
ns1 = book.add_sheet('NewSheet1')    #sheet追加　()はsheet名記入
ns2 = book.add_sheet('NewSheet2')    #sheet追加
book.save(file)    #ファイル保存
print('====%s has generated====\nThe detail is as follows:\n' %file)
#------------------------------------------------------------------------------

#作成したxlsファイルの編集
#------------------------------------------------------------------------------
ns1.write(0, 0, 'A1')    #1行1列目

ns1r1 = ns1.row(0)    #1行目選択
ns1r1.write(1, 'B1')    #1行目の1つ目

ns1r2 = ns1.row(1)    #2行目選択
ns1r2.write(0, 'A2')    #2行目の1つ目


#自動作成(cell位置を記入)
alp=['A','B','C','D','E','F','G','H','I','J','K']    #column情報(A→0, H→7)
n = 7    #列数(アルファベット)選択****
select_alp = alp[n]

for i in range(9):    #行数指定****
    ns1n = ns1.row(i)    #
    ns1n.write(n, '%s%s' %(select_alp, i+1))    #cellにsell位置を記入


book.save(file)#book.saveをすると反映される
#------------------------------------------------------------------------------


#==============================================================================
#Excelを読み込む
#==============================================================================
book = xlrd.open_workbook(file)    #xlrdを使わないと読み込み不可
ns1 = book.sheet_by_index(0)

print('Number of sheet:%d' %book.nsheets)    #sheet数
print('------sheetname------')
for name in book.sheet_names():
    print(name)
print('---------------------\n')
print('Imformation of cell')
print('---------------------')
print('maximum row:%d' %ns1.nrows)
print('maximum column:%d' %ns1.ncols)
print('---------------------\n')

