# -*- coding: utf-8 -*-

import tkinter as tk
import os
from PlayButtonEvent import PlayButtonEvent as EventP
from RenewButtonEvent import RenewButtonEvent as EventR

# master=noneでＡｐｐｌｉｃａｔｉｏｎのインスタンスが親ウィジェット(ウィンドウ)となる
class Application(tk.Frame):    #tk.Frameを継承

    def __init__(self, master=None):    
        super().__init__(master)        
        self.__DATA_DIRECTORY = r'D:\warehouse\data'
        
        # ウィジェット1：再生ボタンの作成
        self.__play = tk.Button(self)   # playというボタンの宣言 
        self.__play["text"] = "PLAY"  # ボタンの名前作成
        self.__play["fg"] = "red"

        # ウィジェット2：停止ボタンの作成
        self.__quit = tk.Button(self, text = "QUIT", command = master.destroy)   #masterを削除する        
        
        # ウィジェット3：ランダム再生のチェックボックスの作成
        self.__randomCheckBoxValue = tk.BooleanVar()
        self.__randomCheckBoxValue.set(False)         #setter 初期値としてFalse(チェックなし)
        self.__randomCheckBox = tk.Checkbutton(text = 'Random', variable = self.__randomCheckBoxValue)         

        # ウィジェット4：チェックボックスの作成
#        self.__checkBoxValue2 = tk.BooleanVar()
#        self.__checkBoxValue2.set(False)
#        self.__checkbox2 = tk.Checkbutton(text = 'Continue', variable = self.__checkBoxValue2)
        
        # ウィジェット5：チェックボックスの作成
        self.__previewCheckBoxValue = tk.BooleanVar()
        self.__previewCheckBoxValue.set(False)
        self.__previewCheckBox = tk.Checkbutton(text='preview', variable=self.__previewCheckBoxValue)
        
        # ウィジェット6：参照ボタンの作成
        self.__refValue = tk.StringVar()
        self.__refValue.set('Non Genres')
        self.__genres = os.listdir(self.__DATA_DIRECTORY)
        self.__ref = tk.OptionMenu(root, self.__refValue, *self.__genres)
        
        # ウィジェット7：リストボックスの作成
        self.__listBox = tk.Listbox(selectmode=tk.SINGLE)
        self.__listBox['fg']='blue'
        self.__listBox['selectbackground']='blue'
        
        # ウィジェット8：更新ボタンの作成
        self.__renew = tk.Button()
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
        
        # packによるウィジェットの設置
        self.pack()
        self.__play.pack(fill = 'both')
        self.__quit.pack(fill = 'both')
        self.__randomCheckBox.pack()   #packのみしか起動しない？
#        self.__checkbox2.pack()
        self.__previewCheckBox.pack()
        self.__ref.pack()
        self.__listBox.pack(fill = "both")  
        self.__renew.pack()
        
    
    def getListBox(self):
        return self.__listBox
    
    def getDataDirectory(self):
        return self.__DATA_DIRECTORY
    
    def getRefValue(self):
        return self.__refValue
    
    def getrandomCheckBoxValue(self):
        return self.__randomCheckBoxValue
  
    def donothing(self):
        subwindow = tk.Toplevel(root)   # rootを親ウィジェットととしてサブウィンドウを表示
        subwindow.geometry("200x300")
        button = tk.Button(subwindow, text="Do nothing button")
        button.pack()
        
    def closeWindow(self):
        self.master.destroy
    
                        
#メインウィンドウ作成(上記したクラスでオブジェクトを作成し、使用する)        
root = tk.Tk()      # ウィジェットrootの作成      
root.geometry("300x400")
root.title("Movie Player")   #ステータスバーの名前決定

# 親ウィジェットに他のウィジェットを乗せる
app = Application(master=root)  # rootを親ウィジェットとしてインスタンス化


#メニューバーの作成################################################################
menubar = tk.Menu(root)

#"File"というメニューバーを追加------------------------------------------------------
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=app.donothing)
filemenu.add_command(label="Open", command=app.donothing)
filemenu.add_command(label="Save", command=app.donothing)
filemenu.add_command(label="Save as...", command=app.donothing)
filemenu.add_command(label="Close", command = app.master.destroy)
#------------------------------------------------------------------------------

#"Edit"というメニューバーを追加------------------------------------------------------
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=app.donothing)
#区切り作成
editmenu.add_separator()
#区切り後の選択肢を作成
editmenu.add_command(label="Cut", command=app.donothing)
editmenu.add_command(label="Copy", command=app.donothing)
editmenu.add_command(label="Paste", command=app.donothing)
editmenu.add_command(label="Delete", command=app.donothing)
editmenu.add_command(label="Select All", command=app.donothing)
#------------------------------------------------------------------------------

#"Help"というメニューバーを追加------------------------------------------------------
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help Index", command=app.donothing)
helpmenu.add_command(label="About...", command=app.donothing)
#------------------------------------------------------------------------------

root.config(menu=menubar)
###############################################################################

#上記したボタンなどをつける(クラス"Application"を起動する)
app.mainloop()
