

import plotly as py
import pandas as pd
from plotly.graph_objs import *
import random


# 随机颜色
from Configuration.ReadCsv import ReadCsv
from Configuration.SetMapData import setLoopData, setLoopDataLayout


def randomColor():
    r = str(random.choice(range(0, 256)))
    g = str(random.choice(range(0, 256)))
    b = str(random.choice(range(0, 256)))
    rgb = 'rgb(' + r + ',' + g + ',' + b + ')'
    return rgb


def timeZoneDistribution():
    # 读取文件

    file = ReadCsv("directory.csv")
    my_file=file.readCsv()
    lat, lon, store_number, store_name, address, postcode, phone_number = file.getCsvData()
    time_zone=my_file["Timezone"]
    # 显示文本
    my_text = (
        "StoreNum: " + store_number + '</br>' +
        "store_name: " + store_name + '</br>' +
        "StreetAddress: " + address + '</br>' +
        "Postcode: " + postcode + '</br>' +
        "phone_number: " + phone_number + '</br>'
    )
    # 添加数据到源文件
    my_file['Text'] = my_text
    # 处理重复数据
    time_zone_set = set(time_zone)
    # 根据 TimeZone 重新排列文件
    group_by_time_zone = my_file.groupby(time_zone)

    # 存放Scattermapbox
    messages = []
    for sub_time_zone in time_zone_set:
        new_time_zone_group = group_by_time_zone.get_group(sub_time_zone)
        data_temp=setLoopData(new_time_zone_group,sub_time_zone,randomColor())
        messages.append(data_temp)
    data = Data(messages)
    layout = setLoopDataLayout(title="Timezone Distribution Map")

    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, validate=False, filename='timeZoneDistribution.html')

