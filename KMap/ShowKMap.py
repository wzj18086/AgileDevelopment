from tkinter import messagebox

import plotly.graph_objs
import plotly.offline

from Configuration.ReadCsv import ReadCsv
from Configuration.SetMapData import setMapData
from GUI import Initialize

from KMap.TopKSearch import *


def solveKMapData():
    file = ReadCsv("directory.csv")
    lat, lon, store_number, store_name, store_address, postcode, phone_number = file.getCsvData()
    datas = []
    i = 0
    while i <= lat.__len__() - 1:
        c = store_number[i]
        d = store_name[i]
        f = store_address[i]
        g = postcode[i]
        h = phone_number[i]
        data = 'store_number:' + c + '</br>' + 'store_name:' + d + '</br>' + 'Postcode:' + g + '</br>' + 'phone_number:' + h + '</br>' + 'store_address:' + f
        datas.append(data)
        i = i + 1
    return lat, lon, datas


def setKMap(lat_result, lon_result):
    x = Initialize.initialize()
    lats = int(x.enter_latitude.get())
    lons = int(x.enter_longitude.get())
    lat, lon, datas = solveKMapData()
    data, layout = setMapData(lat_result, lon_result, lats, lons, datas)
    return data, layout


def showKMap():
    x = Initialize.initialize()
    lats = int(x.enter_latitude.get())
    lons = int(x.enter_longitude.get())
    ks = int(x.k_value.get())
    if (lats > 180) or (lats < -180) or (lons < -180) or lons > 180:
        messagebox.askyesno("error", "经纬度不合法")
        return

    lon_result, lat_result, final_result, time = topKSearch(lats, lons, ks)

    data, layout = setKMap(lat_result, lon_result)
    fig = dict(data=data, layout=layout)

    import plotly.offline
    plotly.offline.plot(fig, filename='result.html')
