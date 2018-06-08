from tkinter import *

from KMap.ShowKMap import showKMap
from KeyWordMap.ShowKeyWordMap import showKeyWordMap
from OtherGraphic.ColorChange import colorChange
from OtherGraphic.CountStatistics import Map2_1
from OtherGraphic.DistrictAmount import Map3
from OtherGraphic.KChange import kChange
from OtherGraphic.TimeZoneDistribution import *
from RadiusMap.ShowRadiusMap import radiusSearch, radiusTimeChange

class  initialize():
    top=Tk()
    button=Button(top,text="店铺分布情况",command=showKMap)
    button1=Button(top,text="时区店铺分布",command=MapTwo)
    button5=Button(top,text="统计",command=Map2_1)
    button2 = Button(top, text="区域店铺数量",command=Map3)
    latidude = Label(text='纬度：')
    enter_latidtude= Entry(top)
    longitude = Label(text='经度：')
    enter_longitude= Entry(top)
    radius=Label(text="搜索半径：")
    radius_value=Entry(top)
    k=Label(text="k:")
    k_value=Entry(top)
    key_word=Label(text="关键词:")
    key_word_enter=Entry(top)
    button3 = Button(top, text="最近k值", command=showKMap)
    button4=Button(top,text="k的变化",command=kChange)
    button6=Button(top,text="店铺时区渐变",command=colorChange)
    button7=Button(top,text="top-k查询",command=showKeyWordMap)
    button8=Button(top,text="半径搜索",command=radiusSearch)
    button9=Button(top,text="半径时延变化",command=radiusTimeChange)