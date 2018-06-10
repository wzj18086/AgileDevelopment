

import pickle
import plotly as py
import pandas as pd



def districtAmount():
    # 把两位国家代码转换成三位代码
    with open("CountryTwoLettersToThree.pickle", "rb") as file:
        three_country_code = pickle.load(file)
    from Configuration.ReadCsv import ReadCsv
    my_file = ReadCsv('directory.csv').readCsv()
    # 计算相同国家的次数
    country_count = dict(my_file["Country"].value_counts())
    # 存放每个国家的星巴克数量
    country_num = [country_count[key] for key in country_count]
    # 转换国家代码
    country_of_three_lettters_list = [three_country_code[key] for key in country_count]

    data = [dict(
        type='choropleth',
        Colorscale=[[0, "rgb (255, 255，255)"],
                    [0.3, "rgb(255，80，80)"],
                    [0.35, "rgb(255, 160，160) "],
                    [1, "rgb(255, 0，0) "]],
        z=country_num,
        reversescale=False,
        autocolorscale=False,
        locations=country_of_three_lettters_list,
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
    py.offline.plot(fig, validate=False, filename='distrinctAmount.html')

