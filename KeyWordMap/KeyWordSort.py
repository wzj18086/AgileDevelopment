import plotly
import pandas as pd
from plotly.graph_objs import *
import difflib
from math import *
from pandas import *

from Configuration.ReadCsv import ReadCsv


def keywordSort(lat, lon, k, key):
    def new_sort(x):
        return (-x[-2], haverSine(x))

    def readFile():
        file = ReadCsv("directory.csv")
        lat, lon, StoreNumber, StoreName, address, postcode, PhoneNumber = file.getCsvData()
        list_semblance = [0] * len(lat)
        list_datas = [" "] * len(lat)
        result_list = [[a, b, c, d, e, f, g, h, i] for a, b, c, d, e, f, g, h, i in
                       zip(lon, lat, StoreNumber, StoreName, address, postcode, PhoneNumber, list_semblance,
                           list_datas)]
        return result_list

    def solveData():
        temp_list = readFile()
        for x in temp_list:
            x[-1] = str(x[0]) + str(x[1]) + str(x[2]) + str(x[3]) + str(x[4]) + str(x[5]) + str(x[6])
        return temp_list

    def getSemblance(result_list, key):
        for line in result_list:
            line[-2] = difflib.SequenceMatcher(None, line[-1], key).quick_ratio()
        return result_list

    def link_data():
        lat, lon, datas = solveData()
        temp = getSemblance(datas, key)
        series = Series(datas, index=temp)
        return series

    def haverSine(x):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
        # 将十进制度数转化为弧度
        lon1, lat1, lon2, lat2 = map(radians, [x[0], x[1], lat, lon])

        # haversine公式
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # 地球平均半径，单位为公里
        return c * r * 1000

    result_list = getSemblance(solveData(), key)
    result_list = sorted(result_list, key=new_sort)
    return result_list[0:k]
