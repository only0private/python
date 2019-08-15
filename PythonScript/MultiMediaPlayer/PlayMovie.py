# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 01:29:07 2019

@author: hamaguchi
"""
#import MoviePlayer as app

import tkinter as tk
import subprocess as subpro
import random
import glob
import os

class PlayMovie():
    
    def __init__(self):
        pass
    
    #PLAYボダンの動作を追加
    def pushed_play(self, ref):   
#        if ref == True:
            print("aaa")
#        else:
            print("bbb")
#            genres = glob.glob(r'%s/*' %(self.dir))
#            m = random.randint(0,len(genres)-1)
#            files = glob.glob(r'%s/*' %(genres[m]))
#            m = random.randint(0,len(files)-1)
#            selected_file = files[m]
#            play_file = (r'%s' %selected_file)
#        elif self.val1.get() == False and listbox.size() == 0:
#            return
#        else:
#            for i in range(listbox.size()):
#                judge = listbox.selection_includes(i)
#                if judge == 1:
#                    play_file = ('%s\%s\%s' %(self.dir, ref_var.get(), listbox.get(i)))
#        subpro.Popen([r'C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe', play_file])
    
    def pushed_renew(self):
#        last = listbox.size()
#        listbox.delete(0,last)
#        selected_genre = ref_var.get()
#        if selected_genre != 'Non Genres':
            i = 0
            print(i)
#            fnames = os.listdir('%s\%s' %(self.dir, selected_genre))
#            for fname in fnames:
#                listbox.insert(i, fname)
#                i += 1
        
    def pushed_ref(self):
        return True
        
        
