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

from Configuration.ReadCsv import ReadCsv


def countStatistics():
    # 读取数据文件
    my_file =ReadCsv("directory.csv").readCsv()
    # 清洗数据-处理缺省值
    my_file = my_file.fillna("None")
    timeZone = my_file["Timezone"]
    # 处理重复数据并排序
    timeZoneSort = sorted(set(timeZone))
    # 根据 TImeZone 重新排列
    group_by_time_zone = my_file.groupby(timeZone)
    # 计算相同时区出现的次数
    time_zone_count = dict(group_by_time_zone["Timezone"].value_counts())
    # 计算星巴克的总数
    store_sum = sum(time_zone_count.values())
    # 每个时区的星巴克的比例
    rate_text = [(value / store_sum) for value in time_zone_count.values()]

    length = len(timeZoneSort)
    values_list = list(time_zone_count.values())
    # 把时区的相关信息写入文件
    with open("timeZone.csv", "w") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["Timezone", "Amount", "Rate"])
        for x in range(length):
            writer.writerow([timeZoneSort[x], values_list[x], rate_text[x]])
    file = ReadCsv("timeZone.csv").readCsv()
    table = FF.create_table(file)
    py.offline.plot(table, filename='countStatistics.html')

