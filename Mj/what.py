from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import csv
import os
import json

class MyTable(QTableWidget):
    def __init__(self,gradeList,parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("查询结果")
        self.resize(1400,950)
        self.setColumnCount(len(gradeList[0])+1)
        self.setRowCount(len(gradeList))
        #设置表格行列。
        self.setRowHeight(0, 80)
        #设置第一行高度为100px，第一列宽度为200px。

        self.table(gradeList)

    def table(self,gradeList):

        #添加表格的文字内容
        self.setItem(0, 0, QTableWidgetItem("店铺名"))
        self.setItem(0, 1, QTableWidgetItem("大众评分"))
        self.setItem(0, 2, QTableWidgetItem("评分次数"))
        self.setItem(0, 3, QTableWidgetItem("优质店铺"))
        self.setItem(0, 4, QTableWidgetItem("我的评分"))
        #表格数据填充
        k = 0
        for i in gradeList:
            k = k + 1
            #for j in range(0,4):
            twi = QTableWidgetItem((i['Store Name']))
            twi.setFont(QFont("Times", 10, ))
            self.setItem(k, 0, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            # for j in range(0,4):
            twi = QTableWidgetItem(str(i['Grade']))
            twi.setFont(QFont("Times", 10, ))
            self.setItem(k, 1, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            # for j in range(0,4):
            twi = QTableWidgetItem(str(i['N']))
            twi.setFont(QFont("Times", 10, ))
            self.setItem(k, 2, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            # for j in range(0,4):
            twi = QTableWidgetItem(str(i['Special']))
            twi.setFont(QFont("Times", 10, ))
            self.setItem(k, 3, twi)

        #k = 0
        #for i in range(1,len(gradeList)):
        #    k = k + 1
        #    # for j in range(0,4):
         #   twi = QTableWidgetItem(" ")
        #    twi.setFont(QFont("Times", 10, ))
        #    self.setItem(k, 4, twi)



