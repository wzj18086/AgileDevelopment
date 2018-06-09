import time
from math import *

import pandas as pd
import plotly.plotly as py

from Configuration.ReadCsv import ReadCsv
from Configuration.SetMapData import *


def radiusSearch(la,lo,r):
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

    # 用户输入数据


    #读取表格数据

    file = ReadCsv("directory.csv")
    lat, lon, StoreNumber, StoreName, address, postcode, PhoneNumber = file.getCsvData()

    result_list=[[a,b,c,d,e,f,g] for a,b,c,d,e,f,g in zip(lat,lon,StoreNumber,StoreName,address,postcode,PhoneNumber)]

    start=time.clock()
    final_list = shaixuan(la,lo,r,result_list)
    end=time.clock()

    lat_result = []
    lon_result = []
    myTexts = []
    for x in final_list:
        lat_result.append(x[0])
        lon_result.append(x[1])
        text = ('StoreNumber:' + x[2] + '</br>' +
                'StoreName:' + x[3] + '</br>' +
                'Postcode:' + x[4] + '</br>' +
                'PhoneNumber:' + x[5] + '</br>' +
                'Address:' + x[6])
        myTexts.append(text)


    print(repr(final_list))
    print("运行时间：", end - start)
    data,layout=setMapData(lat_result,lon_result,la,lo,myTexts)

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='Multiple Mapbox')


