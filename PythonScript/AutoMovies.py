# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 03:56:09 2017

@author: hamaguchi
"""

import glob
import subprocess as subpro
import random
#==============================================================================
# windows media playerによる自動再生
#==============================================================================
#動画を自動的に検索
Workspace = (r'C:\work')

#のちに削除(フォルダが複数存在しているため)
#------------------------------------------------------------------------------
Data = ['', 'data', 'ForWorkFolder',]
n = random.randint(1,len(Data)-1)
#n = 3   #指定するとき有効にする
#------------------------------------------------------------------------------

Folder = Data[n]
Files = glob.glob(r'%s\%s\*' %(Workspace, Folder))
m = random.randint(1,len(Files))
Auto = Files[m]
print('folder:%s\nname:%s' %(Folder, Auto))
#ファイル選択・再生
Fname = (r'%s' %Auto)
subpro.Popen([r'C:\Program Files (x86)\Windows Media Player\wmplayer.exe', Fname])