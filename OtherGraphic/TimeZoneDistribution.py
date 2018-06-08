#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-08 09:03:48
# @Author  : mohailang (1198534595@qq.com)

import plotly as py
import pandas as pd
from plotly.graph_objs import *
import random


# 随机颜色
from Configuration.ReadCsv import ReadCsv


def randomColor():
    r = str(random.choice(range(0, 256)))
    g = str(random.choice(range(0, 256)))
    b = str(random.choice(range(0, 256)))
    rgb = 'rgb(' + r + ',' + g + ',' + b + ')'
    return rgb


def timeZoneDistribution():
    # 读取文件

    file = ReadCsv("directory.csv")
    myFile=file.readCsv()
    lat, lon, StoreNumber, StoreName, address, postcode, PhoneNumber = file.getCsvData()
    timeZone=myFile["Timezone"]
    # 显示文本
    myText = (
        "StoreNum: " + StoreNumber + '</br>' +
        "StoreName: " + StoreName + '</br>' +
        "StreetAddress: " + address + '</br>' +
        "Postcode: " + postcode + '</br>' +
        "phoneNumber: " + PhoneNumber + '</br>'
    )
    # 添加数据到源文件
    myFile['Text'] = myText
    # 处理重复数据
    timeZoneSet = set(timeZone)
    # 根据 TimeZone 重新排列文件
    groupByTimeZone = myFile.groupby(timeZone)

    # 存放Scattermapbox
    messages = []
    for subTimeZone in timeZoneSet:
        newTimeZoneGroup = groupByTimeZone.get_group(subTimeZone)
        messages.append(Scattermapbox(
            lat=newTimeZoneGroup["Latitude"],
            lon=newTimeZoneGroup["Longitude"],
            mode='markers',
            marker=Marker(
                size=10,
                color=randomColor()
            ),
            name=subTimeZone,
            text=newTimeZoneGroup['Text'],
        )
        )
    data = Data(messages)

    layout = Layout(
        autosize=True,
        hovermode='closest',
        title="Timezone Distribution Map",
        mapbox=dict(
            accesstoken="pk.eyJ1IjoibW9oYWlsYW5nIiwiYSI6ImNqZm93cGs5bDF3OXMyeG1zdGhuejBoNTIifQ.fouiU5hKtls0ohPA7LHJEA",
            bearing=0,
            pitch=0,
            zoom=1
        ),
    )

    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, validate=False, filename='timeZoneDistribution.html')

