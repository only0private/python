# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:54:24 2019

@author: hamaguchi
"""

import tkinter as tk
import MultiMediaPlayerMenuBar as mb
import ConfirmHashValue as chv
from PIL import Image, ImageTk

class MultiMediaPLayer(tk.Frame):
    
    def __inti__(self, master=None):
        super().__init__(master)
        
if __name__=="__main__":    
    # 親ウィジェットの作成
    root = tk.Tk() 
    root.geometry("1500x844")
    root.title("Multi Media Player")
    
    # 背景の追加
    img = Image.open(r'.\image\main.jpg')
    mainImg = ImageTk.PhotoImage(img, root)
    
    canvas = tk.Canvas(root, bg = "black", width=1500-1, height=844-1)
    canvas.place(x=0, y=0) 
    canvas.create_image(0, 0, image=mainImg, anchor=tk.NW)
    
    def callBackPrintMessage(message):
        def printMessage():
            print(message)
            return
        return printMessage
    
    # メニューバーの作成
    mb.MultiMediaPlayerMenuBar(root)
    
    # ラベルの作成
    root.__passwordLabel = tk.Label(root, text = "password")
    root.__passwordLabel.grid(row=0, column=0, columnspan=1, padx=15, pady=15)
    
    # パスワードの入力テキストボックスの作成
    root.__enteredPassword = tk.StringVar(root)
    root.__passwordTextBox = tk.Entry(root, textvariable = root.__enteredPassword)
    root.__passwordTextBox.grid(row=0, column=1, columnspan=1, padx=10, pady=15)
    
    # 照合による制限解除用変数
    toolRelease = chv.ConfirmHashValue()
    
    # 認証ボタンの作成
    root.__collationButton = tk.Button(root, text = "COLLATION", fg = "red")
    root.__collationButton.grid(row=0, column=2, columnspan=1, padx=10, pady=15)
    root.__collationButton["command"] = toolRelease.callBackGetHashValue(root.__enteredPassword)
    
    # 確認ボタンの作成(後に消去)
    root.__button = tk.Button(root, text = "CONFIRN", fg = "blue")
    root.__button.grid(row=1, column=0, columnspan=1, padx=10, pady=15)
#    root.__button["command"] = callBackPrintMessage(toolRelease.getToolState())
    
    
    # 親ウィジェットに他のウィジェットを乗せる
    mmp = MultiMediaPLayer(master=root)  # rootを親ウィジェットとしてインスタンス化
    mmp.mainloop()

