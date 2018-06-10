from Mj import Map4_2 as Map1
from Mj import what
from PyQt5.QtWidgets import *
from math import *
import sys
import pandas as pd
import os
import json

def getItem(save_log,mytable):
    k = 0
    for i in save_log:
        k = k + 1

        if(mytable.item(k, 4) != None):
            if(mytable.item(k,1)!= None):
                save_log[i]['Grade'] = mytable.item(k,4).text()
            else:
                grade = mytable.item(k, 4).text()
                old = mytable.item(k,1).text()
                n = mytable .item(k,2).text()
                save_log[i]['Grade'] = avg(grade,old,n)

            save_log[i]['N'] = save_log[i]['N']+1

        if(save_log[i]['Grade']!='' and float(save_log[i]['Grade']) >= 8):
            save_log[i]['Special'] = True
    return save_log

def avg(grade,old,n):
    ave = ((int(old))* int(n)+ int(grade))/(int(n)+1)
    return ave


def grade_save(save_log):
    """将评分记录写入文件中保存下来"""
    try:
        jsobj = json.dumps(save_log)
        fileobj = open("starbucks.json","w")
        fileobj.write(jsobj)
        print("Change Success!")
        fileobj.close()
    except:
        print("Change Error!")

def grade_read(file):
    """读取评分记录的文件，如果没有则生成"""
    if not os.path.exists("starbucks.json"):
        save_log = {}
        for index, file in file.iterrows():
            index = str(index)
            save_log[index] = {}
            save_log[index]["Store Name"] = file["Store Name"]
            # save_log[index]["Latitude"] = starbuck["Latitude"]
            # save_log[index]["Longitude"] = starbuck["Longitude"]
            save_log[index]["Grade"] = ""
            save_log[index]["N"] = 0
            save_log[index]["Special"] = False
        try:
            jsobj = json.dumps(save_log)
            fileobj = open("starbucks.json", "w")
            fileobj.write(jsobj)
            print("Save Success!")
            fileobj.close()
        except:
            print("Save Error!")
    else:
        with open("starbucks.json", "r") as fileobj:
            save_log = json.loads(fileobj.read())
            print("Read Success!")
    print(save_log)
    return save_log

#def
#按照距离筛选数据
def shaixuan(la,lo,r,result_list):
    temp_list = []
    for x in result_list:
        if haversine(lo,la,float(x[1]),float(x[0]))<=1000*r:
            temp_list.append(x)
    return temp_list

#计算两经纬度点之间的距离
def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000

def search(resultList,save_log):
    gradeList = []
    for i in resultList:
        for j in save_log:
            if(i[3] == save_log[j]['Store Name']):
                gradeList.append(save_log[j])

    return gradeList

file = pd.read_csv("directory.csv",encoding='utf-8')
resultList = Map1.show()

app = QApplication(sys.argv)

save_log = grade_read(file)

gradeList = search(resultList,save_log)
print(gradeList)

mytable = what.MyTable(gradeList)
mytable.show()



app.exit(app.exec_())
save_log = getItem(save_log,mytable)
grade_save(save_log)


