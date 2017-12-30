# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 22:58:06 2017

@author: hamaguchi
"""

import os
import glob
import shutil
#==============================================================================
# No_genle.jpg と名付ける(gifやwebmは残る)
#==============================================================================

#ワークスペースで作業
#------------------------------------------------------------------------------

genres = os.listdir(r'C:\work\datag')

for genre in genres:
    os.chdir(r'C:\work\datag\%s' % genre)
    filenumber = len(glob.glob('./*'))
    workspace = (r'C:\work\ForWorkFolderImg/%s' % genre)
    os.chdir(workspace)    #作業フォルダを指定
    
    #詳細設定が必要な時
    if os.path.isfile(r".\SelectDetail.txt"):    #詳細設定が必要な場合，ディレクトリにテキストあり
        details = []
        a = (workspace + '\\')
        for x in os.listdir(a):
            if os.path.isdir(a + x):  #ディレクトリが存在するかどうかを確認
                details.append(x)
        for detail in details:
            filenumber = len(glob.glob(r'C:\work\datag\%s\%s\*.*' %(genre, detail)))
            workspace2 = workspace + '\%s' %detail
            os.chdir(workspace2)    #detail内に移動
                
            #jpg専用
            filenames = glob.glob('./*.jpg')
            
            for n in range(len(filenames)):
                filenumber += 1
                os.rename(filenames[n], '%s\%04d_%s.jpg' %(workspace2, filenumber, detail))
                
            for m in glob.glob('./*.jpg'):
                shutil.move(m, r'C:\work\datag\%s\%s' %(genre, detail))
            
            #png専用
            filenames2 = glob.glob('./*.png')
            
            for n in range(len(filenames2)):
                filenumber += 1
                os.rename(filenames2[n], '%s\%04d_%s.png' %(workspace2, filenumber, detail))
            
            for m in glob.glob('./*.png'):
                shutil.move(m, r'C:\work\datag\%s\%s' %(genre, detail))
            
            #jpeg専用
            filenames3 = glob.glob('./*.jpeg')
            
            for n in range(len(filenames3)):
                filenumber += 1
                os.rename(filenames3[n], '%s\%04d_%s.jpeg' %(workspace2, filenumber, detail))
            
            for m in glob.glob('./*.jpeg'):
                shutil.move(m, r'C:\work\datag\%s\%s' %(genre, detail))            
            
    #詳細設定が不必要な場合   
    else:
        #jpg専用
        filenames = glob.glob('./*.jpg')
        
        for n in range(len(filenames)):
            filenumber += 1
            os.rename(filenames[n], '%s\%04d_%s.jpg' %(workspace, filenumber, genre))
            
        for m in glob.glob('./*.jpg'):
            shutil.move(m, r'C:\work\datag\%s' % genre)
        
        #png専用
        filenames2 = glob.glob('./*.png')
        
        for n in range(len(filenames2)):
            filenumber += 1
            os.rename(filenames2[n], '%s\%04d_%s.png' %(workspace, filenumber, genre))
        
        for m in glob.glob('./*.png'):
            shutil.move(m, r'C:\work\datag\%s' % genre)    
        
        #jpeg専用
        filenames3 = glob.glob('./*.jpeg')
        
        for n in range(len(filenames3)):
            filenumber += 1
            os.rename(filenames3[n], '%s\%04d_%s.jpeg' %(workspace, filenumber, genre))
        
        for m in glob.glob('./*.jpeg'):
            shutil.move(m, r'C:\work\datag\%s' % genre)
#------------------------------------------------------------------------------


