from plotly.graph_objs import *
import plotly.plotly as py
import plotly.offline as offline
import pandas as pd
import random
import pickle
import os

from Configuration.MapSettingStrategy import MapSettingStrategy
from Configuration.ReadCsv import ReadCsv
from Configuration.SetMapData import *


def timeZoneMap():
    file = ReadCsv("directory.csv")
    df = file.readCsv()
    drawTimezoneMap(df, "draw")

# 生成随机颜色
def randomColor():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    return 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'


# 判断文件是否存在


# 按照时区或国家分组绘制世界地图
def drawGroupBy(df, attr, filename):
    # 缺失值处理
    df = df.fillna('Null')
    df['text'] = "Store Number: " + df['Store Number'] + '</br></br>' + "Store Name: " + df['Store Name'] + '</br>' + \
                 "Address: " + df['Street Address'] + '</br>' + "Postcode: " + \
                 df['Postcode'] + '</br>' + "Phone Number: " + df['Phone Number']
    attr_set = set(df[attr])
    attr_group = df.groupby(attr)
    # 存放Scattermapbox
    data = []
    for attr in attr_set:
        group = attr_group.get_group(attr)
        data_temp=setLoopData(group,attr,randomColor())
        data.append(Scattermapbox(data_temp))
    data = Data(data)
    layout = setLoopDataLayout(title='StarBucks<br>(Hover for details)')
    fig = dict(data=data, layout=layout)
    offline.plot(fig, validate=False, filename=str(filename) + '.html')


# 按照经纬度绘制世界地图


def drawLogLat(df, attr, filename):
    df['text'] = "Store Number: " + df['Store Number'] + '</br>' + "Store Name: " + df[
        'Store Name'] + '</br>' + "Address: " + \
                 df['Street Address'] + '</br>' + "Postcode: " + df['Postcode'] + \
                 '</br>' + "Phone Number: " + df['Phone Number']
    # 设置颜色槽
    scl = [[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"],
           [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]]
    map_set = MapSettingStrategy(setLogLatMapData(attr=attr, df=df, color_scale=scl,title='StarBucks with '
                                                + str(attr) + '<br>(Hover for details)'))
    data, layout = map_set.execute()
    fig = dict(data=data, layout=layout)
    offline.plot(fig, validate=False, filename=str(filename) + '.html')


# 绘制国家密度图

def drawCountryMap(df, filename="CountryMap"):
    # 映射表
    with open('CountryTwoLettersToThree.pickle', 'rb') as f:
        change_country_code = pickle.load(f)
    # 国家数量
    country_count = dict(df['Country'].value_counts())
    values = [country_count[key] for key in country_count]
    country_list = [change_country_code[key] for key in country_count]
    color_scale = [[0, "rgb(5, 10, 172)"],
                   [0.45, "rgb(40, 60, 190)"],
                   [0.85, "rgb(70, 100, 245)"],
                   [0.90, "rgb(90, 120, 245)"],
                   [0.95, "rgb(106, 137, 247)"],
                   [1, "rgb(220, 220, 220)"]]
    map_set = MapSettingStrategy(setCountryMapData(country_list=country_list,
                                                   values=values, color_scale=color_scale,title="CountryMap"))
    data, layout = map_set.execute()
    fig = dict(data=data, layout=layout)
    offline.plot(fig, validate=False, filename=str(filename) + '.html')


def drawTimezoneMap(df, filename="timezone_shadow"):
    # 缺失值处理
    df = df.fillna('Null')
    df['text'] = "Store Number: " + df['Store Number'] + '</br></br>' + "Store Name: " + df[
        'Store Name'] + '</br>' + "Address: " + df['Street Address'] + '</br>' + "Postcode: " + df[
                     'Postcode'] + '</br>' + "Phone Number: " + df['Phone Number']

    tz_count = df['Timezone'].value_counts()
    # 将时区对应的数量转化为字典
    tz_dict = dict(tz_count)
    tz_dict = dict(sorted(tz_dict.items(), key=lambda kv: (-kv[1], kv[0])))
    # 根据时区的数量存放颜色
    tz_color = {}
    r_per = (220 - 5) / 4889
    g_per = (150 - 10) / 4889
    b_per = (220 - 172) / 4889

    for key in tz_dict:
        diff = 4889 - tz_dict[key]
        r = 255 + r_per * diff
        g = 0 + g_per * diff
        b = 0 + b_per * diff
        tz_color[key] = 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'

    tz_group = df.groupby('Timezone')
    # 存放Scattermapbox
    data = []
    for tz in tz_dict:
        group = tz_group.get_group(tz)
        data_temp=setLoopData(group,str(tz_count[tz]) + ',' + tz,tz_color[tz])
        data.append(data_temp)

    data = Data(data)
    layout = setLoopDataLayout(title='StarBucks<br>(Timezone Distribution Map)')
    fig = dict(data=data, layout=layout)

    offline.plot(fig, validate=False, filename=str(filename) + '.html')
