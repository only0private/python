# -*- coding: utf-8 -*-

import tkinter as tk
import os
from PlayButtonEvent import PlayButtonEvent as EventP
from RenewButtonEvent import RenewButtonEvent as EventR

# master=noneでＡｐｐｌｉｃａｔｉｏｎのインスタンスが親ウィジェット(ウィンドウ)となる
class MoviePlayer(tk.Frame):    #tk.Frameを継承

    def __init__(self, master = None):    
        super().__init__(master)        
        self.__DATA_DIRECTORY = r'D:\warehouse\data'
        
        # ウィジェット1：再生ボタンの作成
        self.__play = tk.Button(self)   # playというボタンの宣言 
        self.__play["text"] = "PLAY"  # ボタンの名前作成
        self.__play["fg"] = "red"

        # ウィジェット2：停止ボタンの作成
        self.__quit = tk.Button(self, text = "QUIT", command = master.destroy)   #masterを削除する        
        
        # ウィジェット3：ランダム再生のチェックボックスの作成
        self.__randomCheckBoxValue = tk.BooleanVar(self)
        self.__randomCheckBox = tk.Checkbutton(self, text = 'Random', variable = self.__randomCheckBoxValue)
        self.__randomCheckBoxValue.set(False)         #setter 初期値としてFalse(チェックなし)         
        
        # ウィジェット4：チェックボックスの作成
        self.__previewCheckBoxValue = tk.BooleanVar(self)
        self.__previewCheckBoxValue.set(False)
        self.__previewCheckBox = tk.Checkbutton(self, text='Preview', variable=self.__previewCheckBoxValue)
        
        # ウィジェット5：参照ボタンの作成
        self.__refValue = tk.StringVar(self)
        self.__refValue.set('Non Genres')
        self.__genres = os.listdir(self.__DATA_DIRECTORY)
        self.__ref = tk.OptionMenu(self, self.__refValue, *self.__genres)
        
        # ウィジェット6：リストボックスの作成
        self.__genreListBox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.__genreListBox['fg']='blue'
        self.__genreListBox['selectbackground']='blue'
        
        # ウィジェット8：更新ボタンの作成
        self.__renew = tk.Button(self)
        self.__renew['text'] = 'Renew'
        self.__renew['fg'] = 'blue'
        
        
        # commandによるイベント付与
        self.__play["command"] = EventP.callBackPlayButtonEvent(
                self.getrandomCheckBoxValue(), 
                self.getListBox(), 
                self.getDataDirectory(), 
                self.getRefValue())
        
        self.__renew['command'] = EventR.callBackRenewButtonEvent(
                self.getListBox(), 
                self.getRefValue(), 
                self.getDataDirectory())
        
        # gridによるウィジェットの配置
        self.__play.grid(row=0, column=0, columnspan=1, padx=5, pady=5)
        self.__quit.grid(row=0, column=1, columnspan=1, padx=5, pady=5)
        self.__randomCheckBox.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        self.__previewCheckBox.grid(row=1, column=1, columnspan=1, padx=5, pady=5)
        self.__ref.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.__genreListBox.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky=tk.W + tk.E)
        self.__renew.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.pack()
        
        
    
    def getListBox(self):
        return self.__genreListBox
    
    def getDataDirectory(self):
        return self.__DATA_DIRECTORY
    
    def getRefValue(self):
        return self.__refValue
    
    def getrandomCheckBoxValue(self):
        return self.__randomCheckBoxValue
  
    def donothing(self):
        subwindow = tk.Toplevel(self)   # rootを親ウィジェットととしてサブウィンドウを表示
        subwindow.geometry("200x300")
        button = tk.Button(subwindow, text="Do nothing button")
        button.pack()
        
    def closeWindow(self):
        self.master.destroy
    
