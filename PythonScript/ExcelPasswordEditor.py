# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:06:19 2017

@author: hamaguchi
"""

import os
import xlwt
#==============================================================================
# excelpassword作成
#==============================================================================

os.chdir(r'C:\work\PythonProgram')
file = "IRpassword.xlsx"
book = xlwt.Workbook()   #bookを編集していく()
ns1 = book.add_sheet('NewSheet1')    #sheet追加　()はsheet名記入
ns1.write(0,0,'password')
ns1.write(0,1,'ooo')
book.save(file)
