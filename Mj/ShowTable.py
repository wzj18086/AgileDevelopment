from Mj import Map4_2 as Map1
from Mj import what
from PyQt5.QtWidgets import *
from math import *
import sys
import csv


resultList = Map1.show()
app = QApplication(sys.argv)
mytable = what.MyTable(resultList)
mytable.show()
app.exit(app.exec_())

if mytable.item(1,6)!= None:
    score = mytable.item(1,6).text()
    storeNumber = mytable.item(1,2).text()
    # 读取表格数据
    with open('directory.csv', 'r') as csvinput:
        with open('directory.csv', 'w') as csvoutput:
            reader = csv.DictReader(csvinput)
            writer = csv.DictWriter(csvoutput)
            all = []
            for row in reader:
                if row['Store Number'] == storeNumber:
                    row.append(score)
                    all.append(row)



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

