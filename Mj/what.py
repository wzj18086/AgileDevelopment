from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MyTable(QTableWidget):
    def __init__(self,resultlist,parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("查询结果")
        self.resize(1400,950)
        self.setColumnCount(len(resultlist[0]))
        self.setRowCount(len(resultlist))
        #设置表格行列。
        self.setColumnWidth(4, 350)
        self.setRowHeight(0, 80)
        #设置第一行高度为100px，第一列宽度为200px。

        self.table(resultlist)

    def table(self,resultlist):

        #添加表格的文字内容
        self.setItem(0, 0, QTableWidgetItem("Latitude"))
        self.setItem(0, 1, QTableWidgetItem("Longitude"))
        self.setItem(0, 2, QTableWidgetItem("StoreNumber"))
        self.setItem(0, 3, QTableWidgetItem("StoreName"))
        self.setItem(0, 4, QTableWidgetItem("Address"))
        self.setItem(0, 5, QTableWidgetItem("Postcode"))
        self.setItem(0, 6, QTableWidgetItem("Score"))
        #表格数据填充
        k = 0
        for i in resultlist:
            k = k + 1
            for j in range(0, 7):
                twi = QTableWidgetItem(str(i[j]))
                twi.setFont(QFont("Times", 10, ))
                self.setItem(k, j, twi)




#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    myTable = MyTable()
#    myTable.show()
#    app.exit(app.exec_())