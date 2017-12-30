# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:20:06 2017

@author: hamaguchi
"""

import os
import random
import time
#==============================================================================
# 単語勉強
#==============================================================================
os.chdir(r'C:\work\PythonProgram\English_data')
word1 = ("word1_datas.txt")
word2 = ("word2_datas.txt")
num = input("SELECT NUMBER 1 OR 2 >> ")
if num == "1":
    word = word1
elif num == "2":
    word = word2

f = open(word,"r")
raw_file1 = f.read()
list_file1 = raw_file1.split('\n')

count = 42
words = random.sample(list_file1, count)    #list_file1の要素をランダムでcountの数だけlistに入力
j = 0
k = 0
l = 0
mistake = []
for i in range(count):
    t1 = time.time()
    answer = input("\n\n  %d. %s [y/n] >> " %(i+1,words[i]))
    if answer == "y":
        t2 = time.time()
        if t2-t1 > 3:   #遅い判定
            k += 1
            mistake.append(words[i])    #覚えてない単語入力
        else:           #正解判定
            l += 1
    elif answer == "n": #不正解判定
        j += 1
        mistake.append(words[i])
    else:               #不正解判定
        j += 1
        mistake.append(words[i])
    
    if j+k > count/10: #失敗
        print("\n\n############################################")
        print("              YOU WERE FAILED...")
        print("############################################")
        print("YOUR SCORE IS AS FOLLOWING:")
        print("----------------------------")
        print("SUCCESS: %d" %l)
        print("MISTAKE: %d" %j)
        print("DELAY: %d" %k)
        print("----------------------------\n")
        print("YOU HAVE TO REMEMBER AS FOLLOWING:")
        print(mistake)
        break
if j+k <= count/10:           #成功
    perfect = ''
    print("\n\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    print("                    CONGRATULATION!!")
    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    print("\nYOUR SCORE IS AS FOLLOWING:")
    print("----------------------------")
    if len(mistake) == 0:
        perfect = ("⇐ PERFECT!!")
    print("　SUCCESS: %d %s" %(l, perfect))
    print("　MISTAKE: %d" %j)
    print("　DELAY: %d" %k)
    print("----------------------------\n")
    
    if len(mistake) > 0:
        print("YOU HAVE TO REMEMBER AS FOLLOWING:")
        print(mistake)
