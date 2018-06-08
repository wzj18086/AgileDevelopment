
from Configuration.SetMapData import setMapData
from GUI import *
from GUI import Initialize
from KeyWordMap.KeyWordSort import keywordSort
import plotly.graph_objs
import plotly.offline


def keyWordSelect():
    x = Initialize.initialize()
    lats = (int)(x.enter_latidtude.get())
    lons = (int)(x.enter_longitude.get())
    ks = (int)(x.k_value.get())
    keyword=x.key_word_enter.get()
    result=keywordSort(lats,lons,ks,keyword)
    final_lat=[]
    final_lon=[]
    final_data=[]
    for x in result:
        Lat=x[0]
        Lon=x[1]
        s='StoreNumber:'+x[2]+'</br>'+'StoreName:'+x[3]+'</br>'+'Postcode:'+x[4]+'</br>'+'PhoneNumber:'+x[5]+'</br>'+'Address:'+x[6]
        final_data.append(s)
        final_lat.append(Lat)
        final_lon.append(Lon)
    return lats,lons,final_lat,final_lon,final_data

def showKeyWordMap():
    lats, lons, lat, lon, datas = keyWordSelect()
    data, layout = setMapData(lat, lon, lats, lons, datas)
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='result1.html')