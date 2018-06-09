import pandas as pd
import time
from math import *
from plotly import *
import plotly.graph_objs as go
import plotly.offline as off
from pandas import Series, DataFrame

from Configuration.ReadCsv import ReadCsv


def topKSearch(latitude, longitude, k):
    file = ReadCsv("directory.csv")
    lat, lon, store_number, store_name, address, postcode, phone_number = file.getCsvData()
    # 初始半径
    initial_x = 5
    initial_y = 5
    list_x = [10] * len(lon)
    list_y = [5] * len(lat)
    result_list = [[a, b, c, d, e, f, g, h, i] for a, b, c, d, e, f, g, h, i in
                   zip(lon, lat, store_number, store_name, address, postcode, phone_number, list_x, list_y)]

    # 输入数据
    input_x = latitude
    input_y = longitude
    input_k = k

    def haveRSine(x):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
        # 将十进制度数转化为弧度
        lon1, lat1, lon2, lat2 = map(radians, [x[0], x[1], input_x, input_y])

        # haversine公式
        d_lon = lon2 - lon1
        d_lat = lat2 - lat1
        a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # 地球平均半径，单位为公里
        return c * r * 1000

    # 处理筛选特殊情况
    def sovleFilter(x):
        if input_x + x[-2] > 180:
            return input_y - x[-1] <= x[1] <= input_y + x[-1] and (input_x - x[-2]) < x[0] < 180 or \
                   -180 < x[0] < -(180 - (input_x + x[-2] - 180))
        elif input_x - x[-2] < -180:
            return input_y - x[-1] <= x[1] <= input_y + x[-1] and (-180 < x[0] < (x[-2] + input_x) or
                                                                   (180 - abs((input_x - x[-2] + 180)) < x[0] < -180))
        return input_y - x[-1] <= x[1] <= input_y + x[-1] and input_x - x[-2] <= x[0] <= input_x + x[-2]

    # 按照距离筛选数据
    temp_list = result_list

    def filter(x1, y1):
        for x in temp_list:
            x[-2] = x1
            x[-1] = y1
        data = list(filter(sovleFilter, temp_list))
        return data

    result = []

    # 根据搜索到的数量逐步扩大半径
    start = time.clock()
    while result.__len__() < input_k:
        result = filter(initial_x, initial_y)
        # 增大半径
        initial_x += 5
        initial_y += 5

    final_result = sorted(result, key=haveRSine)[:input_k]  # 取最近的前k项为最终结果
    lat_result = []
    lon_result = []
    datas = []

    for x in final_result:
        lon_result.append(x[0])
        lat_result.append(x[1])
        data = 'store_number:' + x[2] + '</br>' + 'store_name:' + x[3] + '</br>' + 'Postcode:' + x[
            4] + '</br>' + 'phone_number:' + x[5] + '</br>' + 'Address:' + x[6]
        datas.append(data)

    end = time.clock()
    return lon_result, lat_result, final_result, end - start
