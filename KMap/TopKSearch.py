import pandas as pd
import time
from math import *
from plotly import *
import plotly.graph_objs as go
import plotly.offline as off
from pandas import Series,DataFrame
def topKSearch(latitude,longitude,k):
    file=pd.read_csv("directory.csv")
    lon=file["Longitude"]#经度
    lat=file["Latitude"]#纬度
    StoreNumber=file['Store Number'].fillna('unknown')
    StoreName=file['Store Name'].fillna('unknown')
    address=file['Street Address'].fillna('unknown')
    postcode=file['Postcode'].fillna('unknown')
    PhoneNumber=file['Phone Number'].fillna('unknown')
    #初始半径
    x_r=5
    y_r=5
    listx=[10]*len(lon)
    listy=[5]*len(lat)
    result_list=[[a,b,c,d,e,f,g,h,i] for a,b,c,d,e,f,g,h,i in zip(lon,lat,StoreNumber,StoreName,address,postcode,PhoneNumber,listx,listy)]

    #输入数据
    test_x=latitude
    test_y=longitude
    test_k=k


    def haversine2(x):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # 将十进制度数转化为弧度
        lon1, lat1, lon2, lat2 = map(radians, [x[0], x[1], test_x, test_y])

        # haversine公式
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # 地球平均半径，单位为公里
        return c * r * 1000
    #处理求距离特殊情况
    def solve(x):
        if x[0]*test_x<0 and x[1]*test_y>0 and abs(test_x-x[0])>(360-abs(x[0])-abs(test_x)):
            return (360-abs(x[0])-abs(test_x))*(360-abs(x[0])-abs(test_x))+(x[1]-test_y)*(x[1]-test_y)
        '''   
        elif x[1]*test_y<0 and x[0]*test_x>0:
            return (x[1]-test_y)*(x[1]-test_y)+(x[0]-test_x)*(x[0]-test_x)
        elif x[0]*test_x<0 and x[1]*test_y<0:
            return (x[1]-test_y)*(x[1]-test_y)+(360-abs(x[0])-abs(test_x))*(360-abs(x[0])-abs(test_x))
         '''
        return (x[0]-test_x)*(x[0]-test_x)+(x[1]-test_y)*(x[1]-test_y)
    #处理筛选特殊情况
    def sovle_filter(x):
        if test_x+x[-2]>180:
            return x[1]>=test_y-x[-1] and x[1]<=test_y+x[-1] and (test_x-x[-2])<x[0]<180 or -180<x[0]<-(180-(test_x+x[-2]-180))
        elif test_x-x[-2]<-180:
            return x[1] >= test_y - x[-1] and x[1] <= test_y + x[-1] and (-180<x[0]<(x[-2]+test_x) or (180-abs((test_x-x[-2]+180))<x[0]<-180))
        return x[1]>=test_y-x[-1] and x[1]<=test_y+x[-1] and x[0]>=test_x-x[-2] and x[0]<=test_x+x[-2]
    #按照距离筛选数据
    temp_list = result_list
    def shaixuan(x1,y1):
        for x in temp_list:
            x[-2]=x1
            x[-1]=y1
        data=list(filter(sovle_filter, temp_list))
        return data
    result=[]

    #根据搜索到的数量逐步扩大半径
    start=time.clock()
    while result.__len__()<test_k:
        result = shaixuan(x_r, y_r)
        #增大半径
        x_r+=5
        y_r+=5

    final_result=sorted(result,key=haversine2)[:test_k]#取最近的前k项为最终结果
    lat_result=[]
    lon_result=[]
    datas=[]

    for x in final_result:
        lon_result.append(x[0])
        lat_result.append(x[1])
        data = 'StoreNumber:' + x[2] + '</br>' + 'StoreName:' + x[3] + '</br>' + 'Postcode:' + x[4] + '</br>' + 'PhoneNumber:' + x[5] + '</br>' + 'Address:' + x[6]
        datas.append(data)

    end=time.clock()
    return lon_result,lat_result,final_result,end-start

