#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-08 14:55:38
# @Author  : mohailang (1198534595@qq.com)


import plotly as py
import pandas as pd
import numpy as np
from plotly.graph_objs import *
from plotly import figure_factory as FF
import csv


def Map2_1():
    # 读取数据文件
    myFile = pd.read_csv('F:\pythonFiles\directory.csv')
    # 清洗数据-处理缺省值
    myFile = myFile.fillna("None")
    timeZone = myFile["Timezone"]
    # 处理重复数据并排序
    timeZoneSort = sorted(set(timeZone))
    # 根据 TImeZone 重新排列
    groupByTimeZone = myFile.groupby(timeZone)
    # 计算相同时区出现的次数
    timeZone_count = dict(groupByTimeZone["Timezone"].value_counts())
    # 计算星巴克的总数
    storeSum = sum(timeZone_count.values())
    # 每个时区的星巴克的比例
    rateText = [(value / storeSum) for value in timeZone_count.values()]

    length = len(timeZoneSort)
    valuesList = list(timeZone_count.values())
    # 把时区的相关信息写入文件
    with open("timeZone.csv", "w") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["Timezone", "Amount", "Rate"])
        for x in range(length):
            writer.writerow([timeZoneSort[x], valuesList[x], rateText[x]])
    file = pd.read_csv("timeZone.csv")
    table = FF.create_table(file)
    py.offline.plot(table, filename='map2-1.html')

