from math import radians, sin, cos, asin, sqrt


# 计算两经纬度点之间的距离
def haveRSine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haveRSine公式
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000

def filter(la, lo, r, result_list):
    temp_list = []
    for x in result_list:
        if haveRSine(lo, la, float(x[1]), float(x[0])) <= 1000 * r:
            temp_list.append(x)
    return temp_list