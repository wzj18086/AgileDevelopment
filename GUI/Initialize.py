from tkinter import *

from Configuration.Singleton import Singleton
from KMap.KChange import kChange
from KMap.ShowKMap import showKMap
from KeyWordMap.ShowKeyWordMap import showKeyWordMap
from OtherGraphic.CountStatistics import countStatistics
from OtherGraphic.DistrictAmount import districtAmount
from OtherGraphic.TimeZoneDistribution import *
from OtherGraphic.TimeZoneMap import timeZoneMap
from RadiusMap.ShowRadiusMap import radiusSearch, radiusTimeChange, radiusSearchShow, radiusTimeChangeShow


class initialize(Singleton):

    top = Tk()
    button = Button(top, text="店铺分布情况", command=showKMap)
    button1 = Button(top, text="时区店铺分布", command=timeZoneDistribution)
    button5 = Button(top, text="统计", command=countStatistics)
    button2 = Button(top, text="区域店铺数量", command=districtAmount)
    button3 = Button(top, text="最近k值", command=showKMap)
    button4 = Button(top, text="k的变化", command=kChange)
    button6 = Button(top, text="店铺时区渐变", command=timeZoneMap)
    button7 = Button(top, text="top-k查询", command=showKeyWordMap)
    button8 = Button(top, text="半径搜索", command=radiusSearchShow)
    button9 = Button(top, text="半径时延变化", command=radiusTimeChangeShow)

    latitude = Label(text='纬度：')
    enter_latitude = Entry(top)
    longitude = Label(text='经度：')
    enter_longitude = Entry(top)
    radius = Label(text="搜索半径：")
    radius_value = Entry(top)
    k = Label(text="k:")
    k_value = Entry(top)
    key_word = Label(text="关键词:")
    key_word_enter = Entry(top)

