from plotly.graph_objs import *

mapbox_access_token = 'pk.eyJ1Ijoid3pqMTgwODYiLCJhIjoiY2pmMHM2dmRoMDFsZjJ4dDdiaHZwMmpqayJ9.yBaHqF4D6JKBVe_kvTWAhw'


def setMapData(lat_result, lon_result, lats, lons, datas):
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
    return data, layout


def setCountryMapData(country_list, values, color_scale,title):
    data = [
        dict(
            type='choropleth',
            colorscale=color_scale,
            reversescale=True,
            autocolorscale=False,
            locations=country_list,
            locationmode="ISO-3",
            z=values,
        )
    ]
    layout = Layout(
        title=title,
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0,
            zoom=1
        )
    )
    return data, layout


def setLogLatMapData(attr, df, color_scale,title):
    data = Data(
        [Scattermapbox(
            lon=df['Longitude'],  # 经度
            lat=df['Latitude'],  # 纬度
            mode='markers',
            marker=Marker(
                size=9,
                # 颜色槽
                colorscale=color_scale,
                cmin=df[attr].min(),
                color=df[attr],
                cmax=df[attr].max(),
                colorbar=dict(
                    title=attr
                )
            ),
            text=df['text'],  # 提示信息
        )])
    layout = Layout(
        autosize=True,
        title=title,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0,
            zoom=1
        ),
    )
    return data, layout


def setLoopData(map_group, name, color):
    data = Scattermapbox(
        lon=map_group['Longitude'],  # 经度
        lat=map_group['Latitude'],  # 纬度
        mode='markers',
        marker=Marker(size=9, color=color),
        name=name,  # 菜单栏内容
        text=map_group['Text'],  # 提示信息
        hoverinfo="Text",
    )
    return data


def setLoopDataLayout(title):
    layout = Layout(
        autosize=True,
        # 标题
        title=title,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0,
            zoom=1
        ),
    )
    return layout
