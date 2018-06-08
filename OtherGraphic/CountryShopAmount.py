
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as off

from Configuration.ReadCsv import ReadCsv


def init():

  data =ReadCsv("directory.csv").readCsv()
  grouped = data.groupby('Country').size()  # series 类型，国家星巴克数量

  # 创建关于国家名字数组
  grouped1 = data.groupby('Country')
  country = []
  return country,grouped

#绘制条形图
def bar_charts(name):
  '''
  绘制柱状图
  '''
  country, grouped = init()
  dataset = {'x': country,
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

#绘制饼图
def pie_charts(name):
  country,grouped=init()
  dataset = {'labels':country,
        'values':grouped}
  data_g = []
  tr_p = go.Pie(
    labels = dataset['labels'],
    values = dataset['values']
  )
  data_g.append(tr_p)
  layout = go.Layout(title="country pie")
  fig = go.Figure(data=data_g, layout=layout)
  off.plot(fig, filename=name)
def showChart():

  data = pd.read_csv('directory.csv', encoding='utf-8')

    # 创建关于国家名字数组
  grouped1 = data.groupby('Country')
  country = []
  for name,group in grouped1:
      country.append(name)

  #pie_charts('busy')
  bar_charts('countryShopAmount')
