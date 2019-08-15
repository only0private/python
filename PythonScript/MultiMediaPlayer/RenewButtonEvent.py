# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 03:10:30 2019

@author: hamaguchi
"""

import os

class RenewButtonEvent():
    
    def callBackRenewButtonEvent(listBox, refValue, DATA_DIRECTORY):
        def renewButtonEvent():
            listBox.delete(0, 'end')
            selectedGenre = refValue.get()
            if selectedGenre != 'Non Genres':
                i = 0
                fnames = os.listdir('%s\%s' %(DATA_DIRECTORY, selectedGenre))
                for fname in fnames:
                    listBox.insert(i, fname)
                    i += 1
        return renewButtonEvent