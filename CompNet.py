# Form implementation generated from reading ui file 'CompNet.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 533)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 651, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 220, 621, 111))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 131, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 40, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 40, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 40, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(400, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(520, 20, 47, 13))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(270, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 340, 311, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 30, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 340, 271, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 631, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 631, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 340, 311, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 30, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 220, 621, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(40, 20, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(220, 20, 111, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(190, 40, 161, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.lineEdit_12.setGeometry(QtCore.QRect(412, 40, 131, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(410, 20, 131, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 70, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(370, 340, 271, 91))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.tab_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 10, 631, 192))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 220, 101, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 261, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(270, 290, 231, 61))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(110, 370, 131, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(270, 370, 191, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(270, 410, 113, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_13 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(120, 410, 111, 16))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CompNet"))
        self.groupBox.setTitle(_translate("MainWindow", "Добавить"))
        self.lineEdit.setText(_translate("MainWindow", "PC"))
        self.label.setText(_translate("MainWindow", "Тип"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_3.setText(_translate("MainWindow", "Максимальная нагрузка"))
        self.lineEdit_2.setText(_translate("MainWindow", "M34"))
        self.lineEdit_3.setText(_translate("MainWindow", "100"))
        self.lineEdit_4.setText(_translate("MainWindow", "A1"))
        self.lineEdit_5.setText(_translate("MainWindow", "A2"))
        self.label_4.setText(_translate("MainWindow", "Вход"))
        self.label_5.setText(_translate("MainWindow", "Выход"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Удалить по номеру"))
        self.label_6.setText(_translate("MainWindow", "Удалить по №"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Удалить все"))
        self.pushButton_3.setText(_translate("MainWindow", "Удалить все"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Максимальная нагрузка"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Вход"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Выход"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Элементы компьютерной сети"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Входной порт"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Выходной порт"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Максимальная нагрузка"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Удалить по номеру"))
        self.label_7.setText(_translate("MainWindow", "Удалить по №"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Добавить"))
        self.lineEdit_8.setText(_translate("MainWindow", "A0"))
        self.label_8.setText(_translate("MainWindow", "Входной порт"))
        self.label_9.setText(_translate("MainWindow", "Выходной порт"))
        self.lineEdit_9.setText(_translate("MainWindow", "А0"))
        self.lineEdit_12.setText(_translate("MainWindow", "500"))
        self.label_12.setText(_translate("MainWindow", "Максимальная нагрузка"))
        self.pushButton_5.setText(_translate("MainWindow", "Добавить"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Удалить все"))
        self.pushButton_6.setText(_translate("MainWindow", "Удалить все"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Нагрузка"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Входной порт"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Выходной порт"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Максимальная нагрузка"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Общая нагрузка на систему"))
        self.pushButton_7.setText(_translate("MainWindow", "Расчитать"))
        self.label_10.setText(_translate("MainWindow", "Оптимальная последовательность соединения"))
        self.label_11.setText(_translate("MainWindow", "Максимальная нагрузка"))
        self.label_13.setText(_translate("MainWindow", "Уязвим к поражению"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Расчеты"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
