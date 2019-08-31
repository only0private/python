# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 22:34:35 2019

@author: hamaguchi
"""

import tkinter as tk
import MoviePlayer as mp

class MultiMediaPlayerMenuBar():
    
    def __init__(self, root):
        
        menubar = tk.Menu()
    
        __filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label = "File", menu = __filemenu)

        __filemenu.add_command(label = "New", command = self.donothing)
        __filemenu.add_command(label = "Open", command = self.donothing)
        __filemenu.add_command(label = "Save", command = self.donothing)
        __filemenu.add_command(label = "Save as...", command = self.donothing)
        __filemenu.add_command(label = "Close", command = root.destroy)
    
    
        editmenu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Edit", menu = editmenu)

        editmenu.add_command(label = "Undo", command = self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label = "Cut", command = self.donothing)
        editmenu.add_command(label = "Copy", command = self.donothing)
        editmenu.add_command(label = "Paste", command = self.donothing)
        editmenu.add_command(label = "Delete", command = self.donothing)
        editmenu.add_command(label = "Select All", command = self.donothing)
        
        
        toolmenu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Tool", menu = toolmenu)

        toolmenu.add_command(label = "MoviePlayer", command = self.showMP)
        toolmenu.add_separator()
        toolmenu.add_command(label = "Cut", command = self.donothing)
        toolmenu.add_command(label = "Copy", command = self.donothing)
        toolmenu.add_command(label = "Paste", command = self.donothing)
        toolmenu.add_command(label = "Delete", command = self.donothing)
        toolmenu.add_command(label = "Select All", command = self.donothing)


        helpmenu = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Help", menu = helpmenu)

        helpmenu.add_command(label = "Help Index", command = self.donothing)
        helpmenu.add_command(label = "About...", command = self.donothing)        
        
        root.config(menu=menubar)
      
    toolsRelease = False
    
    def donothing(self):
        subwindow = tk.Toplevel()
        subwindow.geometry("200x300")
        button = tk.Button(subwindow, text="Do nothing button")
        button.pack()
        
        
    def setToolsRelease(confirmHashValue):
        MultiMediaPlayerMenuBar.toolsRelease = confirmHashValue
        
        
    def showMP(self):
        if True == MultiMediaPlayerMenuBar.toolsRelease:
            subWindow = tk.Tk()    
            subWindow.geometry("300x400")
            subWindow.title("Movie Player")
            moviePlayer = mp.MoviePlayer(subWindow)
            moviePlayer.mainloop
        else:
            return

        
        
    
    
        