# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:54:44 2019

@author: hamaguchi
"""

import hashlib
import tkinter as tk
import MultiMediaPlayerMenuBar as mb

class ConfirmHashValue():
    
    def __init__(self):
        self.toolState = tk.BooleanVar()
        self.toolState.set(False)
    
    
    def callBackGetHashValue(self, password):
        def getHashValue():
            createdHashValue = hashlib.sha224(password.get().encode()).hexdigest()
            textFile = open(r"D:\Database\password.txt")
            preparedHashValue = textFile.read()
            textFile.close
            if createdHashValue == preparedHashValue:
                self.toolState.set(True)
                mb.MultiMediaPlayerMenuBar.setToolsRelease(self.toolState.get())
                return
            else:
                self.toolState.set(False)
                return
        return getHashValue

      