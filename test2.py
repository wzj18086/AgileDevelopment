import plotly.plotly as py
import plotly
import pandas as pd
from pandas import Series,DataFrame
from plotly.graph_objs import *
from tkinter import *
from text1 import *
from plotlyMap2 import *
from plotlyMap3 import *
from plotlyMap2_1 import *
from Requirement2 import *
import plotly.graph_objs
import plotly.offline
from tkinter import messagebox
import matplotlib.pyplot as plt
from requirment1 import *
from mate import *
from Map4_2 import *
from Run import *
import threading
from c import *

def readFile():
    df = pd.read_csv("directory.csv")
    lat = df['Latitude']
    lon = df['Longitude']
    StoreNumber=df['Store Number'].fillna('unknown')
    StoreName=df['Store Name'].fillna('unknown')
    address=df['Street Address'].fillna('unknown')
    postcode=df['Postcode'].fillna('unknown')
    PhoneNumber=df['Phone Number'].fillna('unknown')
    return lat,lon,StoreNumber,StoreName,address,postcode,PhoneNumber


#top_k
def SolveData():
    lat,lon,StoreNumber,StoreName,address,postcode,PhoneNumber=readFile()
    datas=[]
    i=0
    while i<=lat.__len__()-1:
        c=StoreNumber[i]
        d=StoreName[i]
        f=address[i]
        g=postcode[i]
        h=PhoneNumber[i]
        data='StoreNumber:'+c+'</br>'+'StoreName:'+d+'</br>'+'Postcode:'+g+'</br>'+'PhoneNumber:'+h+'</br>'+'Address:'+f
        datas.append(data)
        i=i+1
    return lat,lon,datas

def SetMap2(lat_result,lon_result):
    mapbox_access_token = 'pk.eyJ1Ijoid3pqMTgwODYiLCJhIjoiY2pmMHM2dmRoMDFsZjJ4dDdiaHZwMmpqayJ9.yBaHqF4D6JKBVe_kvTWAhw'
    lats = (int)(enter_latidtude.get())
    lons = (int)(enter_longitude.get())
    lat, lon, datas = SolveData()
    print(datas)
    data = Data([
        Scattermapbox(
            lat=lat_result,
            lon=lon_result,
            mode='markers',
            marker=Marker(
                size=9
            ),
            text=datas,
        )
    ])
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=lats,
                lon=lons
            ),
            pitch=0,
            zoom=1
        ),
    )
    return data, layout

#key_word top-k
def SetMap():
    mapbox_access_token = 'pk.eyJ1Ijoid3pqMTgwODYiLCJhIjoiY2pmMHM2dmRoMDFsZjJ4dDdiaHZwMmpqayJ9.yBaHqF4D6JKBVe_kvTWAhw'
    lats, lons, lat, lon, datas=keyWordSelect()

    data = Data([
        Scattermapbox(
            lat=lat,
            lon=lon,
            mode='markers',
            marker=Marker(
                size=9
            ),
            text=datas,
        )
    ])
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=lats,
                lon=lons
            ),
            pitch=0,
            zoom=1
        ),
    )
    return data,layout

def showkMap():
    lats=(int)(enter_latidtude.get())
    lons=(int)(enter_longitude.get())
    ks=(int)(k_value.get())
    if(lats>180 or lats<-180 or lons<-180 or lons>180):
        messagebox.askyesno("error","经纬度不合法")
        return
    if ks>=2000:
        ProgressBarShow()
    lon_result, lat_result, final_result, time=requirement_sec(lats,lons,ks)
    #plotly.tools.set_credentials_file('wzj18086', 'FFnoowbWTQmSfuvQQ8r9')
    data, layout = SetMap2(lat_result,lon_result)
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='result.html')

def k_change():
    lats = (int)(enter_latidtude.get())
    lons = (int)(enter_longitude.get())
    times=[]
    k=[1,2,3,5,10,50,100,300,500,1000,3000,5000,10000,15000,20000,25000]
    if (lats > 180 or lats < -180 or lons < -180 or lons > 180):
        messagebox.askyesno("error", "经纬度不合法")
        return
    for x in k:
        lon_result, lat_result, final_result, time = requirement_sec(lats, lons, x)
        times.append(time)
    plt.plot(k, times, label='k_change', linewidth=1, color='r', marker='o',
             markerfacecolor='black', markersize=4)
    plt.xlabel('k')
    plt.ylabel('time (s)')
    plt.legend()
    plt.show()

def color_change():
    df = pd.read_csv("directory.csv")
    draw_timezone_map(df, "draw")

def keyWordSelect():
    lats = (int)(enter_latidtude.get())
    lons = (int)(enter_longitude.get())
    ks = (int)(k_value.get())
    keyword=key_word_enter.get()
    result=keywordSort(lats,lons,ks,keyword)
    final_lat=[]
    final_lon=[]
    final_data=[]
    for x in result:
        Lat=x[0]
        Lon=x[1]
        s='StoreNumber:'+x[2]+'</br>'+'StoreName:'+x[3]+'</br>'+'Postcode:'+x[4]+'</br>'+'PhoneNumber:'+x[5]+'</br>'+'Address:'+x[6]
        final_data.append(s)
        final_lat.append(Lat)
        final_lon.append(Lon)
    return lats,lons,final_lat,final_lon,final_data

def showKeyWordMap():
    data, layout = SetMap()
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='result1.html')

def RadiusSearch():
    lats = (float)(enter_latidtude.get())
    lons = (float)(enter_longitude.get())
    radius=(float)(radius_value.get())
    RadiusSearch_1(lats,lons,radius)

def RadiusTimeChange():
    lats = (float)(enter_latidtude.get())
    lons = (float)(enter_longitude.get())
    RadiusTimeChange_1(lats,lons)

if __name__=='__main__':

    top=Tk()
    top.geometry('300x550')
    top.title("星巴克店铺分布及统计")
    button=Button(top,text="店铺分布情况",command=showkMap)
    button.place(x=50,y=50)
    button1=Button(top,text="时区店铺分布",command=MapTwo)
    button1.place(x=150,y=50)

    button5=Button(top,text="统计",command=Map2_1)
    button5.place(x=250,y=50)

    button2 = Button(top, text="区域店铺数量",command=Map3)
    button2.place(x=50, y=100)

    button2 = Button(top, text="国家店铺数量",command=showChart)
    button2.place(x=150, y=100)

    latidude = Label(text='纬度：')
    latidude.place(x=50,y=150)
    enter_latidtude= Entry(top)
    enter_latidtude.place(x=100,y=150)
    longitude = Label(text='经度：')
    longitude.place(x=50, y=180)
    enter_longitude= Entry(top)
    enter_longitude.place(x=100, y=180)

    radius=Label(text="搜索半径：")
    radius.place(x=50,y=210)
    radius_value=Entry(top)
    radius_value.place(x=100,y=210)

    k=Label(text="k:")
    k.place(x=50,y=240)
    k_value=Entry(top)
    k_value.place(x=100,y=240)

    key_word=Label(text="关键词:")
    key_word.place(x=50,y=270)
    key_word_enter=Entry(top)
    key_word_enter.place(x=100,y=270)

    button3 = Button(top, text="最近k值", command=showkMap)
    button3.place(x=100, y=300)

    button4=Button(top,text="k的变化",command=k_change)
    button4.place(x=100,y=340)

    button6=Button(top,text="店铺时区渐变",command=color_change)
    button6.place(x=100,y=380)

    button7=Button(top,text="top-k查询",command=showKeyWordMap)
    button7.place(x=100,y=430)

    button8=Button(top,text="半径搜索",command=RadiusSearch)
    button8.place(x=100,y=480)

    button9=Button(top,text="半径时延变化",command=RadiusTimeChange)
    button9.place(x=200,y=480)
    top.mainloop()

