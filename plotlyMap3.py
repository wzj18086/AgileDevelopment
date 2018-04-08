#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-07 22:24:43
# @Author  : mohailang (1198534595@qq.com)

import pickle
import plotly as py
import pandas as pd


def Map3():
    # 把两位国家代码转换成三位代码
    with open("countryTwoLettersToThree.pickle", "rb") as file:
        threeCountryCode = pickle.load(file)
    myFile = pd.read_csv('F:\pythonFiles\directory.csv')
    # 计算相同国家的次数
    country_count = dict(myFile["Country"].value_counts())
    # 存放每个国家的星巴克数量
    countryNum = [country_count[key] for key in country_count]
    # 转换国家代码
    countryOfThreeLettersList = [threeCountryCode[key] for key in country_count]

    data = [dict(
        type='choropleth',
        Colorscale=[[0, "rgb (255, 255，255)"],
                    [0.3, "rgb(255，80，80)"],
                    [0.35, "rgb(255, 160，160) "],
                    [1, "rgb(255, 0，0) "]],
        z=countryNum,
        reversescale=False,
        autocolorscale=False,
        locations=countryOfThreeLettersList,
        locationmode="ISO-3",
        colorbar=dict(
            autotick=False,
            title='星巴克<br>商店数量'
        ),
    )]

    layout = dict(
        title="National Distribution Map",
        autosize=True,
        hovemode='closest',
        mapbox=dict(
            accesstoken="pk.eyJ1IjoibW9oYWlsYW5nIiwiYSI6ImNqZm93cGs5bDF3OXMyeG1zdGhuejBoNTIifQ.fouiU5hKtls0ohPA7LHJEA",
            bearing=0,
            pitch=0,
            zoom=1,
        )
    )

    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, validate=False, filename='map3.html')


if __name__ == '__main__':
    Map3()
