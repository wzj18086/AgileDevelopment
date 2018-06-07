from math import *
import time
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd


# 按照距离筛选数据
def shaixuan(la, lo, r, result_list):
    temp_list = []
    for x in result_list:
        if haversine(lo, la, float(x[1]), float(x[0])) <= 1000 * r:
            temp_list.append(x)
    return temp_list


# 计算两经纬度点之间的距离
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
la = float(input("请输入纬度:"))
lo = float(input("请输入经度:"))


#读取表格数据
file=pd.read_csv(r"C:\Users\Eleven\Desktop\MJ\directory.csv")
#处理缺省值
file = file.fillna("0")

lat=file["Latitude"]#纬度
lon=file["Longitude"]#经度
StoreNumber=file['Store Number'].fillna('unknown')
StoreName=file['Store Name'].fillna('unknown')
address=file['Street Address'].fillna('unknown')
postcode=file['Postcode'].fillna('unknown')
PhoneNumber=file['Phone Number'].fillna('unknown')

result_list=[[a,b,c,d,e,f,g] for a,b,c,d,e,f,g in zip(lat,lon,StoreNumber,StoreName,address,postcode,PhoneNumber)]


rlist = [1,20,100,500,2000,10000,40076]
runTime = []
for i in rlist:
    start = time.clock()
    shaixuan(la, lo, i,result_list)
    end = time.clock()
    runTime.append(end - start)

trace = go.Scatter(
    x = rlist,
    y = runTime,
    name = 'RunTime Trace',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot')
)
data = [trace]

# Edit the layout
layout = dict(title = '随着r的增长查询时延的变化',
              xaxis = dict(title = 'r'),
              yaxis = dict(title = '查询时延'),
              )

fig = dict(data=data, layout=layout)
py.plot(fig, filename='styled-line')