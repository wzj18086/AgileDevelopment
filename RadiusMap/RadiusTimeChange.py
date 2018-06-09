from math import *
import time
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from Configuration.DataFilter import filter
from Configuration.ReadCsv import ReadCsv


def radiusTimeChange(la,lo):
# 按照距离筛选数据


    #读取表格数据
    file = ReadCsv("directory.csv")
    lat, lon, store_number, store_name, store_address, postcode, phone_number = file.getCsvData()

    result_list=[[a,b,c,d,e,f,g] for a,b,c,d,e,f,g in zip(lat,lon,store_number,store_name,store_address,postcode,phone_number)]


    rlist = [1,20,100,500,2000,10000,40076]
    runTime = []
    for i in rlist:
        start = time.clock()
        filter(la, lo, i,result_list)
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