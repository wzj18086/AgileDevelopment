import pandas as pd
import plotly.graph_objs as go
import plotly.offline as off

from Configuration.ReadCsv import ReadCsv


def init():
    data = ReadCsv("directory.csv").readCsv()
    grouped = data.groupby('Country').size()  # series 类型，国家星巴克数量

    # 创建关于国家名字数组
    country = []
    return country, grouped


# 绘制条形图
def barCharts(name):
    '''
  绘制柱状图
  '''
    country, grouped = init()
    data_set = {'x': country,
               'y1': grouped,
               }
    data_g = []
    tr_y1 = go.Bar(
        x=dataset['x'],
        y=dataset['y1'],

    )
    data_g.append(tr_y1)

    layout = go.Layout(title="country bar", xaxis={'title': 'country'}, yaxis={'title': 'amount'})
    fig = go.Figure(data=data_g, layout=layout)
    off.plot(fig, filename=name)


# 绘制饼图
def pieCharts(name):
    country, grouped = init()
    data_set = {'labels': country,
               'values': grouped}
    data_g = []
    tr_p = go.Pie(
        labels=data_set['labels'],
        values=data_set['values']
    )
    data_g.append(tr_p)
    layout = go.Layout(title="country pie")
    fig = go.Figure(data=data_g, layout=layout)
    off.plot(fig, filename=name)


def showChart():
    data = pd.read_csv('directory.csv', encoding='utf-8')

    # 创建关于国家名字数组
    grouped_by_country = data.groupby('Country')
    country = []
    for name, group in grouped_by_country:
        country.append(name)

    # pie_charts('busy')
    barCharts('countryShopAmount')
