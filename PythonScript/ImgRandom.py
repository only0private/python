# -*- coding: utf-8 -*-


import os
import random
import subprocess as subpro
from time import  sleep
import xlrd
import pyautogui
#==============================================================================
# ランダムで画像を表示
#==============================================================================

os.chdir(r'C:\work\PythonProgram')
file = 'IRpassword.xlsx' 
book = xlrd.open_workbook(file)    #xlrdを使わないと読み込み不可
ns1 = book.sheet_by_index(0)
KEY = ns1.cell(0,1).value

def password(key):
    print("CHECKING PASSWORD....")
    if  key == KEY:
        print("OK!! AVAILABLE THIS PROGRAM.\n")
        print("USEABLE GENRE IS AS FOLLOWS:")
        genres = os.listdir(r"C:\work\datag")
        print(genres)
        
        genre = input("WHAT KINDS OF DRAWING ? \n>>> ")
        
        if genre == "cancel":
            print ("OK. CANCELED.")
        else:
            place = r"C:\work\datag\%s" %genre
            os.chdir(place)
            files = os.listdir(place)
            
            if os.path.isfile(r".\SelectDetail.txt"):    #詳細設定が必要な場合，ディレクトリにテキストあり            
                select = []
                a = (place + '\\')
                print (a)
                for x in os.listdir(a):
                    if os.path.isdir(a + x):  #ディレクトリが存在するかどうかを確認
                        select.append(x)
                print("USEABLE DETAIL IS AS FOLLOWS:")
                print(select)
                
                detail = input("WHAT KINDS OF DETAIL ? \n>>> ")
    
                
                #詳細ジャンルの決定
                place = place + '\%s' %detail
                os.chdir(place)
                files = os.listdir(place)
                genre = detail
            
            print("OK. PLEASE WAIT FOR JUST A MOMENT.")
            #画像表示
            fnames = random.sample(files, len(files))
            for i in range(len(fnames)):
                fname = fnames[i]
                subpro.Popen([r'C:\Program Files\Vieas\Vieas.exe', "%s//%s" %(place, fname)])
                t = 2
                sleep(t)
                pyautogui.keyDown("escape")
                
            
            print("\n******FINISHED COMPLETELY******")
    
    else:
        print("NO. UNAVAILABLE THIS PROGRAM.")
    