import pandas as pd
from math import *
from plotly.graph_objs import *
import plotly.plotly as py
import time



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

def show():
    # 用户输入数据
    la = float(input("请输入纬度:"))
    lo = float(input("请输入经度:"))
    r = float(input("请输入搜索半径(单位为公里):"))

    #yo = pd.read_csv("directory.csv")
    #yo.insert(13,'Score',"")
    #yo.to_csv("directory.csv",mode="w")

    #读取表格数据
    file=pd.read_csv("directory.csv")

    lat=file["Latitude"]#纬度
    lon=file["Longitude"]#经度
    StoreNumber=file['Store Number'].fillna('unknown')
    StoreName=file['Store Name'].fillna('unknown')
    address=file['Street Address'].fillna('unknown')
    postcode=file['Postcode'].fillna('unknown')
    Score=file['Score'].fillna("")

    result_list=[[a,b,c,d,e,f,g] for a,b,c,d,e,f,g in zip(lat,lon,StoreNumber,StoreName,address,postcode,Score)]

    start=time.clock()
    final_list = shaixuan(la,lo,r,result_list)
    end=time.clock()

    lat_result = []
    lon_result = []
    myTexts = []
    for x in final_list:
        lat_result.append(x[0])
        lon_result.append(x[1])
        text = ('StoreNumber:' + x[2] + '<br/>' +
                'StoreName:' + x[3] + '<br/>' +
                'Address:' + x[4] + '<br/>' +
                'Postcode:' + x[5] + '<br/>' +
                'Score:' + x[6])
        myTexts.append(text)


    print(repr(final_list))
    print("运行时间：", end - start)

    data = Data([
        Scattermapbox(
            lat=lat_result,
            lon=lon_result,
            mode='markers',
            marker=Marker(
                size=9,
                color='rgb(0,0,255)',
                opacity=0.7
            ),
            text=myTexts
        )
    ])
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken='pk.eyJ1IjoiZWxldmVuZXIiLCJhIjoiY2pmb3VkcDJzMXBybDMzczJmeWN2bGNrZyJ9.-zXlvQCWfxjeyEnPJmPAAA',
            style = 'outdoors',
            bearing=0,
            center=dict(
                lat=la,
                lon=lo
            ),
            pitch=0,
            zoom=10
        ),
    )

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='Multiple Mapbox')
    return final_list


