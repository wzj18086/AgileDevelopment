from Mj import Map4_2 as Map1
from Mj import what
from PyQt5.QtWidgets import *
from math import *
import sys
import pandas as pd
import os
import json

def getItem(save_log,txt,num,n,grade):

    #for i in gradeList:
        for k in save_log:
            if num == save_log[k]['Store Number']:
                if (save_log[k]['Grade']==''and txt!=""):
                    temp = txt
                    save_log[k]['Grade'] = round(float(temp), 2)
                    save_log[k]['N']=save_log[k]['N']+1


                elif (save_log[k]['Grade']!=''and txt!=""):
                    temp =avg(float(txt),float(grade),float(n))
                    save_log[k]['Grade'] = round(float(temp), 2)
                    save_log[k]['N']=save_log[k]['N']+1


                if(save_log[k]['Grade']!=''):
                    a = str(save_log[k]['Grade'])
                    if float(a) >= 8:
                        save_log[k]['Special'] = True
                    else:
                        save_log[k]['Special'] = False

        return save_log

def avg(grade,old,n):
    ave = (old* n+ grade)/(n+1)
    return ave

def grade_save(save_log):
    """将评分记录写入文件中保存下来"""
    try:
        jsobj = json.dumps(save_log)
        fileobj = open("starbucks.json", "w")
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
            save_log[index]["Store Number"] = file["Store Number"]
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


def search(resultList,save_log):
    gradeList = []
    for i in resultList:
        for j in save_log:
            if(i[2] == save_log[j]['Store Number']):
                gradeList.append(save_log[j])

    return gradeList

if __name__ == '__main__':
    #读取文件
    file = pd.read_csv("directory.csv",encoding='utf-8')

    #展示地图、获取得到的结果List
    resultList = Map1.show()

    app = QApplication(sys.argv)

    #读取所有信息并存储到json中
    save_log = grade_read(file)

    #获取到显示在表格上的List
    gradeList = search(resultList,save_log)
    print(gradeList)

    mytable = what.MyTable(gradeList,save_log)
    mytable.show()
    #p_log = getItem(save_log, mytable, gradeList)
    app.exit(app.exec_())
    #获取表格中的数据用以修改save_log中的数据


    #把save_log的数据放入json中保存
    #grade_save(save_log)
    #gradeList = search(resultList,save_log)
    #print(gradeList)


