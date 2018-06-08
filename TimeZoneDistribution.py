#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-08 09:03:48
# @Author  : mohailang (1198534595@qq.com)

import plotly as py
import pandas as pd
from plotly.graph_objs import *
import random


# 随机颜色
def randomColor():
    r = str(random.choice(range(0, 256)))
    g = str(random.choice(range(0, 256)))
    b = str(random.choice(range(0, 256)))
    rgb = 'rgb(' + r + ',' + g + ',' + b + ')'
    return rgb


def MapTwo():
    # 读取文件
    myFile = pd.read_csv('F:\pythonFiles\directory.csv')
    # 数据清洗-处理缺省值
    myFile = myFile.fillna("None")

    # 读取文件各项数据
    storeNum = myFile["Store Number"]
    storeName = myFile["Store Name"]
    Type = myFile["Ownership Type"]
    streetAddress = myFile["Street Address"]
    city = myFile["City"]
    state = myFile["State/Province"]
    country = myFile["Country"]
    postCode = myFile["Postcode"]
    phoneNumber = myFile["Phone Number"]
    timeZone = myFile["Timezone"]

    # 显示文本
    myText = (
        "StoreNum: " + storeNum + '</br>' +
        "StoreName: " + storeName + '</br>' +
        "OwnershipType: " + Type + '</br>' +
        "StreetAddress: " + streetAddress + '</br>' +
        "City: " + city + '</br>' +
        "State: " + state + '</br>' +
        "Country: " + country + '</br>' +
        "Postcode: " + postCode + '</br>' +
        "phoneNumber: " + phoneNumber + '</br>' +
        "TimeZone: " + timeZone
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
    py.offline.plot(fig, validate=False, filename='map2.html')

