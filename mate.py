import plotly
import pandas as pd
from plotly.graph_objs import *
import difflib
from math import *
from pandas import *

def keywordSort(lat,lon,k,key):
    def new_sort(x):
        return (-x[-2],haversine2(x))

    def readFile():
        df = pd.read_csv('directory.csv',encoding='utf-8')
        lat = df['Latitude']
        lon = df['Longitude']
        StoreNumber=df['Store Number'].fillna('unknown')
        StoreName=df['Store Name'].fillna('unknown')
        address=df['Street Address'].fillna('unknown')
        postcode=df['Postcode'].fillna('unknown')
        PhoneNumber=df['Phone Number'].fillna('unknown')
        list_similar=[0]*len(lat)
        list_datas=[" "]*len(lat)
        result_list = [[a, b, c, d, e, f, g, h, i] for a, b, c, d, e, f, g, h, i in
                       zip(lon, lat, StoreNumber, StoreName, address, postcode, PhoneNumber, list_similar,list_datas)]
        return result_list

    def SolveData():
        temp_list=readFile()
        datas=[]
        for x in temp_list:
            x[-1]=str(x[0])+str(x[1])+str(x[2])+str(x[3])+str(x[4])+str(x[5])+str(x[6])
        return temp_list

    def get_similar(result_list,key):
        for line in result_list:
            line[-2]=difflib.SequenceMatcher(None, line[-1], key).quick_ratio()
        return result_list

    def build_max_heap(build_list):
        #build_list为需要建立堆的列表
        #建立一个堆
        for i in range(int(len(build_list)/2-1),-1,-1):
            max_heap(build_list,len(build_list),i)


    def max_heap(adjust_list,heap_size,index):
        #调整列表中的元素保证index为根的堆是一个最大堆

        left_child = 2*index +1
        right_child = left_child+1
        if left_child<heap_size and adjust_list[left_child]<adjust_list[index]:
            smallest = left_child
        else:
            smallest = index
        if right_child<heap_size and adjust_list[right_child]<adjust_list[smallest]:
            smallest = right_child
        if smallest!=index:
            adjust_list[index],adjust_list[smallest] = adjust_list[smallest],adjust_list[index]
            max_heap(adjust_list,heap_size,smallest)

    def heap_sort(sort_list):
        #堆排序
        build_max_heap(sort_list)
        heap_size = len(sort_list)
        #调整后列表的第一个元素是这个列表的最大元素，将其与最后一个元素交换，然后继续调整
        for i in range(len(sort_list)-1,0,-1):
            sort_list[i],sort_list[0]=sort_list[0],sort_list[i]
            heap_size -=1
            max_heap(sort_list,heap_size,0)
        return sort_list

    def link_data():
        lat, lon, datas = SolveData()
        temp = get_similar(datas, key)
        series = Series(datas, index=temp)
        return series

    def deal_data(result_list,k):
        #处理相似度排序
        datalist = [] #储存k个最近的相似度的列表
        deal = [] #过渡的数组，用来储存末尾相同相似度的列表
        deal2 = []
        i = 0
        j = 0
        while(result_list[i] != result_list[int(k)]):
            datalist.append(result_list[i])
            i = i+1
            last = i

        if(len(datalist)<int(k)):
            middle = int(k)-len(datalist)

        while(result_list[last] == result_list[last+j]):
            deal.append(result_list[last+j])
            j = j+1
            sum = j

        series1 = link_data()

        deal2.append(series1[deal[sum-1]])

        print(deal2)

    def haversine2(x):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
        # 将十进制度数转化为弧度
        lon1, lat1, lon2, lat2 = map(radians, [x[0], x[1],lat,lon])

        # haversine公式
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # 地球平均半径，单位为公里
        return c * r * 1000

    result_list=get_similar(SolveData(),key)
    result_list=sorted(result_list,key=new_sort)
    return result_list[0:k]

