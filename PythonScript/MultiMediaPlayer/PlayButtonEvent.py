# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 02:31:06 2019

@author: hamaguchi
"""

import subprocess as subpro
import random
import glob

class PlayButtonEvent():
        
    def callBackPlayButtonEvent(randomCheckBoxValue, genreListBox, DATA_DIRECTORY, refValue):
        def playButtonEvent():
            if randomCheckBoxValue.get() == True:
                genres = glob.glob(r'%s/*' %(DATA_DIRECTORY))
                m = random.randint(0,len(genres)-1)
                files = glob.glob(r'%s/*' %(genres[m]))
                m = random.randint(0,len(files)-1)
                selected_file = files[m]
                randomPlayFile = (r'%s' %selected_file)
                PlayButtonEvent.playMovie(randomPlayFile)
                return
            elif refValue.get() == False and genreListBox.size() == 0:
                return
            else:
                for i in range(genreListBox.size()):
                    judge = genreListBox.selection_includes(i)
                    if judge == 1:    
                        selectedPlayFile = ('%s\%s\%s' %(DATA_DIRECTORY, refValue.get(), genreListBox.get(i)))
                        PlayButtonEvent.playMovie(selectedPlayFile)
                return
        return playButtonEvent
    
    def playMovie(playFile):
        POTPLAYER = r'C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe'
        subpro.Popen([POTPLAYER, playFile])
        return
    