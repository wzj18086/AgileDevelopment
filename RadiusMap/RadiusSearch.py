import time
from math import *

import pandas as pd
import plotly.plotly as py

from Configuration.ReadCsv import ReadCsv
from Configuration.SetMapData import *
from Configuration.DataFilter import filter


def radiusSearch(la, lo, r):
    # 读取表格数据
    file = ReadCsv("directory.csv")
    lat, lon, store_number, store_name, store_address, postcode, phone_number = file.getCsvData()

    result_list = [[a, b, c, d, e, f, g] for a, b, c, d, e, f, g in
                   zip(lat, lon, store_number, store_name, store_address, postcode, phone_number)]

    start = time.clock()
    final_list = filter(la, lo, r, result_list)
    end = time.clock()

    lat_result = []
    lon_result = []
    myTexts = []
    for x in final_list:
        lat_result.append(x[0])
        lon_result.append(x[1])
        text = ('store_number:' + x[2] + '</br>' +
                'store_name:' + x[3] + '</br>' +
                'Postcode:' + x[4] + '</br>' +
                'phone_number:' + x[5] + '</br>' +
                'Address:' + x[6])
        myTexts.append(text)

    print(repr(final_list))
    print("运行时间：", end - start)
    data, layout = setMapData(lat_result, lon_result, la, lo, myTexts)

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='Multiple Mapbox')
