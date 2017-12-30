# -*- coding: utf-8 -*-

import os
import xlrd
import math
import itertools
#==============================================================================
# スケジュール管理
#==============================================================================
os.chdir(r'C:\work\ForScheduler')

#--------------------------------excel操作-------------------------------------
#excel読み込み
file = "Scheduler.xlsx"
book = xlrd.open_workbook(file)
ns1 = book.sheet_by_index(0)

#値を取得する
num_task = ns1.ncols - 1
times, consumptions = [], []  #起床，朝食，昼食，夕食，就寝
for i in range(5):
    times.append(ns1.cell(5+i,1).value)
    consumptions.append(ns1.cell(5+i,2).value)
tasks, weights = [], []
for i in range(num_task):
    tasks.append(ns1.cell(1,i+1).value)
    weights.append(ns1.cell(2,i+1).value)
#------------------------------------------------------------------------------
weight_total = 0
for i in range(num_task):    
    weight_total += weights[i]


#時間の計算
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
margin = 3 #時間の余裕を作る(パラメータ) ←大きくなるほど余裕ができる
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

time = times[4] - times[0]
tasktime = []
for i in range(num_task):
    tasktime.append(str(math.floor(weights[i] / weight_total * (time-margin))))
tasktime = list(map(float, tasktime))

t1 = times[2] - (times[1] + consumptions[1])
t2 = times[3] - (times[2] + consumptions[2])
t3 = times[4] - (times[3] + consumptions[3])
#--------------------------------適合度計算-------------------------------------
#評価開始
value, j, number = 100, -1, -100
all_p = list(itertools.permutations(tasktime))  #全順列作成(時間)
all_p_task = list(itertools.permutations(tasks))  #全順列作成(単語)
for p in all_p:
    s1, s2, s3, i = 0, 0, 0, 0
    while t1 >= s1:
        s1 += p[i]
        i += 1
    i += -1
    s1 = s1 - p[i]
    k1 = i+1
    while t2 >= s2:
        s2 += p[i]
        i += 1
    i += -1
    s2 = s2 - p[i]
    k2 = i+2
    while i - num_task <0:
        s3 += p[i]
        i += 1
    j += 1
    #すべて振り分けられた場合jを更新
    if t1-s1>0 and t2-s2>0 and t3-s3>0:
        new_value = max(t1-s1,t2-s2,t3-s3)
        if new_value < value:
            value = new_value
            number = j
            answer_task = list(all_p_task[j])
            answer_time = list(all_p[j]) 
            answer_task.insert(0,"[朝食]")
            answer_task.insert(k1,"[昼食]")
            answer_task.insert(k2,"[夕食]")
            answer_time.insert(0,consumptions[1])
            answer_time.insert(k1,consumptions[2])
            answer_time.insert(k2,consumptions[3])

#スケジュールを記述
if number > -10:
    print ("THE BEST IS AS FOLLOWING:")
    for i in range(len(answer_task)):
        if answer_task[i] == "[朝食]":
            print("-----%d:00-----" %(int(times[1])))
        if answer_task[i] == "[昼食]":
            print("-----%d:00-----" %(int(times[2])))
        if answer_task[i] == "[夕食]":
            print("-----%d:00-----" %(int(times[3])))
        print("%s : %sh" %(answer_task[i], answer_time[i]))
        while not answer_task[i] == answer_task[-1]:
            print("⇓")
            i = -1
    print("\n==========\nvalue: %d\n==========" %value)
#スケジュールが組めなかったら
else:
    print("THIS SCHEDULE IS IMPOSSIBLE ...")
    print("COULD YOU CHANGE THE MAGIN ?")
