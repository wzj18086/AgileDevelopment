from plotly.graph_objs import *

def setMapData(lat_result,lon_result,lats,lons,datas):
    mapbox_access_token = 'pk.eyJ1Ijoid3pqMTgwODYiLCJhIjoiY2pmMHM2dmRoMDFsZjJ4dDdiaHZwMmpqayJ9.yBaHqF4D6JKBVe_kvTWAhw'
    data = Data([
            Scattermapbox(
                lat=lat_result,
                lon=lon_result,
                mode='markers',
                marker=Marker(
                    size=9
                ),
                text=datas,
            )
        ])
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=lats,
                lon=lons
            ),
            pitch=0,
            zoom=1
            ),
    )
    return data,layout