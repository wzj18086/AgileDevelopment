from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import csv
import os
import json
from Mj.ShowTable import *

class MyTable(QWidget):


    def __init__(self,gradeList,save_log):
        super().__init__()
        self.setWindowTitle("查询结果")
        self.resize(1400,950)
        self.table = QTableWidget(self)
        self.table.resize(1400,850)
        self.table.setColumnCount(len(gradeList[0])+1)
        #self.messageBox = QMessageBox(self)
        self.grade = gradeList
        self.log =save_log
        self.btn_save = QPushButton('保存')
        self.btn_save.clicked.connect(self.save)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.table)
        self.vbox.addWidget(self.btn_save)


        self.setLayout(self.vbox)

        #self.table.cellChanged.connect(self.getContent)
        self.table.setRowCount(len(gradeList)+1)
        # 设置表头
        self.table.setHorizontalHeaderLabels(['店铺名', '店铺号', '大众评分', '评分次数','优质店铺','我的评分'])

        self.table.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.table.editable = True
        # 设置为选中一行，默认为选中单格
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 添加表格的文字内容
        self.table.setItem(0, 0, QTableWidgetItem("店铺名"))
        self.table.setItem(0, 1, QTableWidgetItem("店铺号"))
        self.table.setItem(0, 2, QTableWidgetItem("大众评分"))
        self.table.setItem(0, 3, QTableWidgetItem("评分次数"))
        self.table.setItem(0, 4, QTableWidgetItem("优质店铺"))
        self.table.setItem(0, 5, QTableWidgetItem("我的评分"))
        # 表格数据填充
        k = 0
        for i in gradeList:
            k = k + 1
            # for j in range(0,4):
            twi = QTableWidgetItem((i['Store Name']))
            twi.setFont(QFont("Times", 10, ))
            self.table.setItem(k, 0, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            # for j in range(0,4):
            twi = QTableWidgetItem((i['Store Number']))
            twi.setFont(QFont("Times", 10, ))
            self.table.setItem(k, 1, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            # for j in range(0,4):
            twi = QTableWidgetItem(str(i['Grade']))
            twi.setFont(QFont("Times", 10, ))
            self.table.setItem(k, 2, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            twi = QTableWidgetItem(str(i['N']))
            twi.setFont(QFont("Times", 10, ))
            self.table.setItem(k, 3, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            # for j in range(0,4):
            if (i['Special'] == True):
                twi = QTableWidgetItem("√")
            else:
                twi = QTableWidgetItem(" ")
            twi.setFont(QFont("Times", 10, ))
            self.table.setItem(k, 4, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            twi = QTableWidgetItem("")
            twi.setFont(QFont("Times", 10, ))
            self.table.setItem(k, 5, twi)
        #设置表格行列。
        #设置第一行高度为100px，第一列宽度为200px。

        #self.button.clicked.connect(grade_save)
        #self.table(gradeList)

    def save(self):
        for i in range(1 ,len(self.grade)+1):
            if(self.table.item(i,5).text() != ""):
                txt = self.table.item(i,5).text()
                num = self.grade[i-1]['Store Number']
                n = self.grade[i-1]['N']
                grade = self.grade[i-1]['Grade']
                self.log = getItem(self.log,txt,num,n,grade)

        grade_save(self.log)



    def table(self,gradeList):

        #添加表格的文字内容
        self.table.setItem(0, 0, QTableWidgetItem("店铺名"))
        self.table.setItem(0, 1, QTableWidgetItem("店铺号"))
        self.table.setItem(0, 2, QTableWidgetItem("大众评分"))
        self.table.setItem(0, 3, QTableWidgetItem("评分次数"))
        self.table.setItem(0, 4, QTableWidgetItem("优质店铺"))
        self.table.setItem(0, 5, QTableWidgetItem("我的评分"))
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
            twi = QTableWidgetItem((i['Store Number']))
            twi.setFont(QFont("Times", 10, ))
            self.setItem(k, 1, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            # for j in range(0,4):
            twi = QTableWidgetItem(str(i['Grade']))
            twi.setFont(QFont("Times", 10, ))
            self.setItem(k, 2, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            twi = QTableWidgetItem(str(i['N']))
            twi.setFont(QFont("Times", 10, ))
            self.setItem(k, 3, twi)

        k = 0
        for i in gradeList:
            k = k + 1
            # for j in range(0,4):
            if(i['Special'] == True):
                twi = QTableWidgetItem("√")
            else:
                twi = QTableWidgetItem(" ")
            twi.setFont(QFont("Times", 10, ))
            self.setItem(k, 4, twi)

        #k = 0
        #for i in range(1,len(gradeList)):
        #    k = k + 1
        #    # for j in range(0,4):
         #   twi = QTableWidgetItem(" ")
        #    twi.setFont(QFont("Times", 10, ))
        #    self.setItem(k, 4, twi)



