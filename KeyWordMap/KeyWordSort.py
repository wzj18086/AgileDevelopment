import plotly
import pandas as pd
from plotly.graph_objs import *
import difflib
from math import *
from pandas import *

from Configuration.DataFilter import haveRSine
from Configuration.ReadCsv import ReadCsv


def keywordSort(lat, lon, k, key):
    def new_sort(x):
        return -x[-2], haveRSine(x[0], x[1], lat, lon)

    def readFile():
        file = ReadCsv("directory.csv")
        lat, lon, store_number, store_name, address, postcode, phone_number = file.getCsvData()
        list_semblance = [0] * len(lat)
        list_datas = [" "] * len(lat)
        result_list = [[a, b, c, d, e, f, g, h, i] for a, b, c, d, e, f, g, h, i in
                       zip(lon, lat, store_number, store_name, address, postcode, phone_number, list_semblance,
                           list_datas)]
        return result_list

    def solveData():
        temp_list = readFile()
        for x in temp_list:
            x[-1] = str(x[0]) + str(x[1]) + str(x[2]) + str(x[3]) + str(x[4]) + str(x[5]) + str(x[6])
        return temp_list

    def getSemblance(result_list, key):
        for line in result_list:
            line[-2] = difflib.SequenceMatcher(None, line[-1], key).quick_ratio()
        return result_list

    def link_data():
        temp_lat, temp_lon, datas = solveData()
        temp = getSemblance(datas, key)
        series = Series(datas, index=temp)
        return series



    result_list = getSemblance(solveData(), key)
    result_list = sorted(result_list, key=new_sort)
    return result_list[0:k]
