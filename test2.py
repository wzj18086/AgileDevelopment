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


def readFile():
    df = pd.read_csv("F:\pythonFiles\directory.csv")
    lat = df['Latitude']
    lon = df['Longitude']
    StoreNumber=df['Store Number'].fillna('unknown')
    StoreName=df['Store Name'].fillna('unknown')
    address=df['Street Address'].fillna('unknown')
    postcode=df['Postcode'].fillna('unknown')
    PhoneNumber=df['Phone Number'].fillna('unknown')
    return lat,lon,StoreNumber,StoreName,address,postcode,PhoneNumber

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

def SetMap():
    mapbox_access_token = 'pk.eyJ1Ijoid3pqMTgwODYiLCJhIjoiY2pmMHM2dmRoMDFsZjJ4dDdiaHZwMmpqayJ9.yBaHqF4D6JKBVe_kvTWAhw'
    lat,lon,datas=SolveData()
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
                lat=38.92,
                lon=-77.07
            ),
            pitch=0,
            zoom=0.1
        ),
    )
    return data,layout

def showMap():
    #plotly.tools.set_credentials_file('wzj18086', 'FFnoowbWTQmSfuvQQ8r9')
    data, layout = SetMap()
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='result.html')

if __name__=='__main__':

    top=Tk()
    top.geometry('300x300')
    top.title("星巴克店铺分布及统计")
    button=Button(top,text="店铺分布情况",command=showMap)
    button.place(x=50,y=50)
    button1=Button(top,text="时区店铺分布",command=MapTwo)
    button1.place(x=150,y=50)

    button5=Button(top,text="统计",command=Map2_1)
    button5.place(x=250,y=50)

    button2 = Button(top, text="区域店铺数量",command=Map3)
    button2.place(x=50, y=100)

    button2 = Button(top, text="国家店铺数量",command=showChart)
    button2.place(x=150, y=100)


    top.mainloop()

