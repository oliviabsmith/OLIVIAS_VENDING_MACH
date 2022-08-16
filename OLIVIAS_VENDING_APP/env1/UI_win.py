# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:white")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(410, 20, 291, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setStyleSheet("background-color:white")
        self.home.setObjectName("home")
        self.label = QtWidgets.QLabel(self.home)
        self.label.setGeometry(QtCore.QRect(30, 160, 231, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.home)
        self.coffee = QtWidgets.QWidget()
        self.coffee.setStyleSheet("background-color:coral")
        self.coffee.setObjectName("coffee")
        self.coffee_drink = QtWidgets.QPushButton(self.coffee)
        self.coffee_drink.setGeometry(QtCore.QRect(90, 50, 101, 71))
        self.coffee_drink.setStyleSheet("background-color:white")
        self.coffee_drink.setObjectName("coffee_drink")
        self.hot_choc = QtWidgets.QPushButton(self.coffee)
        self.hot_choc.setGeometry(QtCore.QRect(90, 180, 101, 71))
        self.hot_choc.setStyleSheet("background-color:white")
        self.hot_choc.setObjectName("hot_choc")
        self.hot_water = QtWidgets.QPushButton(self.coffee)
        self.hot_water.setGeometry(QtCore.QRect(90, 320, 101, 71))
        self.hot_water.setStyleSheet("background-color:white")
        self.hot_water.setObjectName("hot_water")
        self.back_btn = QtWidgets.QPushButton(self.coffee)
        self.back_btn.setGeometry(QtCore.QRect(210, 450, 75, 24))
        self.back_btn.setStyleSheet("background-color:red")
        self.back_btn.setObjectName("back_btn")
        self.cost_coffee = QtWidgets.QLCDNumber(self.coffee)
        self.cost_coffee.setGeometry(QtCore.QRect(10, 30, 61, 51))
        self.cost_coffee.setSmallDecimalPoint(False)
        self.cost_coffee.setObjectName("cost_coffee")
        self.label_cost_coffee = QtWidgets.QLabel(self.coffee)
        self.label_cost_coffee.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_cost_coffee.setObjectName("label_cost_coffee")
        self.stackedWidget.addWidget(self.coffee)
        self.snack = QtWidgets.QWidget()
        self.snack.setStyleSheet("background-color:dodgerblue")
        self.snack.setObjectName("snack")
        self.MM = QtWidgets.QPushButton(self.snack)
        self.MM.setGeometry(QtCore.QRect(110, 60, 71, 51))
        self.MM.setStyleSheet("background-color:white")
        self.MM.setObjectName("MM")
        self.crisps = QtWidgets.QPushButton(self.snack)
        self.crisps.setGeometry(QtCore.QRect(110, 160, 71, 51))
        self.crisps.setStyleSheet("background-color:white")
        self.crisps.setObjectName("crisps")
        self.snickers = QtWidgets.QPushButton(self.snack)
        self.snickers.setGeometry(QtCore.QRect(110, 260, 71, 51))
        self.snickers.setStyleSheet("background-color:white")
        self.snickers.setObjectName("snickers")
        self.pantera_rosa = QtWidgets.QPushButton(self.snack)
        self.pantera_rosa.setGeometry(QtCore.QRect(110, 370, 71, 51))
        self.pantera_rosa.setStyleSheet("background-color:white")
        self.pantera_rosa.setObjectName("pantera_rosa")
        self.cost_snack = QtWidgets.QLCDNumber(self.snack)
        self.cost_snack.setGeometry(QtCore.QRect(30, 30, 51, 51))
        self.cost_snack.setObjectName("cost_snack")
        self.label_cost_snack = QtWidgets.QLabel(self.snack)
        self.label_cost_snack.setGeometry(QtCore.QRect(30, 10, 47, 13))
        self.label_cost_snack.setObjectName("label_cost_snack")
        self.backsnack_btn = QtWidgets.QPushButton(self.snack)
        self.backsnack_btn.setGeometry(QtCore.QRect(200, 440, 75, 23))
        self.backsnack_btn.setStyleSheet("background-color:red")
        self.backsnack_btn.setObjectName("backsnack_btn")
        self.stackedWidget.addWidget(self.snack)
        self.drink = QtWidgets.QWidget()
        self.drink.setStyleSheet("background-color:greenyellow")
        self.drink.setObjectName("drink")
        self.coke = QtWidgets.QPushButton(self.drink)
        self.coke.setGeometry(QtCore.QRect(100, 70, 101, 91))
        self.coke.setStyleSheet("background-color:white")
        self.coke.setObjectName("coke")
        self.water = QtWidgets.QPushButton(self.drink)
        self.water.setGeometry(QtCore.QRect(100, 270, 101, 91))
        self.water.setStyleSheet("background-color:white")
        self.water.setObjectName("water")
        self.cost_drink = QtWidgets.QLCDNumber(self.drink)
        self.cost_drink.setGeometry(QtCore.QRect(20, 30, 51, 51))
        self.cost_drink.setObjectName("cost_drink")
        self.label_cost_drink_2 = QtWidgets.QLabel(self.drink)
        self.label_cost_drink_2.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label_cost_drink_2.setObjectName("label_cost_drink_2")
        self.backdrink_btn = QtWidgets.QPushButton(self.drink)
        self.backdrink_btn.setGeometry(QtCore.QRect(210, 450, 75, 23))
        self.backdrink_btn.setStyleSheet("background-color:red")
        self.backdrink_btn.setObjectName("backdrink_btn")
        self.stackedWidget.addWidget(self.drink)
        self.change = QtWidgets.QWidget()
        self.change.setObjectName("change")
        self.change_label = QtWidgets.QLabel(self.change)
        self.change_label.setGeometry(QtCore.QRect(80, 50, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.change_label.setFont(font)
        self.change_label.setObjectName("change_label")
        self.change_table = QtWidgets.QTableWidget(self.change)
        self.change_table.setGeometry(QtCore.QRect(30, 170, 211, 191))
        self.change_table.setObjectName("change_table")
        self.change_table.setColumnCount(2)
        self.change_table.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.change_table.setItem(4, 0, item)
        self.change_table.verticalHeader().setVisible(False)
        self.change_table.verticalHeader().setHighlightSections(True)
        self.stackedWidget.addWidget(self.change)
        self.missing = QtWidgets.QWidget()
        self.missing.setObjectName("missing")
        self.continuebtn = QtWidgets.QPushButton(self.missing)
        self.continuebtn.setGeometry(QtCore.QRect(100, 80, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.continuebtn.setFont(font)
        self.continuebtn.setStyleSheet("background-color:Chartreuse")
        self.continuebtn.setObjectName("continuebtn")
        self.returnbtn = QtWidgets.QPushButton(self.missing)
        self.returnbtn.setGeometry(QtCore.QRect(90, 220, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.returnbtn.setFont(font)
        self.returnbtn.setStyleSheet("background-color:red")
        self.returnbtn.setObjectName("returnbtn")
        self.stackedWidget.addWidget(self.missing)
        self.coffee_btn = QtWidgets.QPushButton(self.centralwidget)
        self.coffee_btn.setGeometry(QtCore.QRect(70, 110, 101, 51))
        self.coffee_btn.setObjectName("coffee_btn")
        self.snack_btn = QtWidgets.QPushButton(self.centralwidget)
        self.snack_btn.setGeometry(QtCore.QRect(70, 250, 101, 51))
        self.snack_btn.setObjectName("snack_btn")
        self.drink_btn = QtWidgets.QPushButton(self.centralwidget)
        self.drink_btn.setGeometry(QtCore.QRect(70, 390, 101, 51))
        self.drink_btn.setObjectName("drink_btn")
        self.total_money = QtWidgets.QLCDNumber(self.centralwidget)
        self.total_money.setGeometry(QtCore.QRect(240, 50, 91, 51))
        self.total_money.setObjectName("total_money")
        self.fiftybtn = QtWidgets.QPushButton(self.centralwidget)
        self.fiftybtn.setEnabled(False)
        self.fiftybtn.setGeometry(QtCore.QRect(270, 210, 41, 31))
        self.fiftybtn.setObjectName("fiftybtn")
        self.onebtn = QtWidgets.QPushButton(self.centralwidget)
        self.onebtn.setEnabled(False)
        self.onebtn.setGeometry(QtCore.QRect(270, 150, 41, 31))
        self.onebtn.setObjectName("onebtn")
        self.twentybtn = QtWidgets.QPushButton(self.centralwidget)
        self.twentybtn.setEnabled(False)
        self.twentybtn.setGeometry(QtCore.QRect(270, 270, 41, 31))
        self.twentybtn.setObjectName("twentybtn")
        self.fivebtn = QtWidgets.QPushButton(self.centralwidget)
        self.fivebtn.setEnabled(False)
        self.fivebtn.setGeometry(QtCore.QRect(270, 400, 41, 31))
        self.fivebtn.setObjectName("fivebtn")
        self.tenbtn = QtWidgets.QPushButton(self.centralwidget)
        self.tenbtn.setEnabled(False)
        self.tenbtn.setGeometry(QtCore.QRect(270, 340, 41, 31))
        self.tenbtn.setObjectName("tenbtn")
        self.total_change = QtWidgets.QLabel(self.centralwidget)
        self.total_change.setGeometry(QtCore.QRect(240, 30, 47, 13))
        self.total_change.setObjectName("total_change")
        self.buybtn = QtWidgets.QPushButton(self.centralwidget)
        self.buybtn.setEnabled(False)
        self.buybtn.setGeometry(QtCore.QRect(240, 490, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buybtn.setFont(font)
        self.buybtn.setStyleSheet("background-color:Chartreuse")
        self.buybtn.setObjectName("buybtn")
        self.correct_money = QtWidgets.QLabel(self.centralwidget)
        self.correct_money.setGeometry(QtCore.QRect(350, 520, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.correct_money.setFont(font)
        self.correct_money.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.correct_money.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.correct_money.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.correct_money.setObjectName("correct_money")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choose Which Vending Machine To Use"))
        self.coffee_drink.setText(_translate("MainWindow", "Coffee"))
        self.hot_choc.setText(_translate("MainWindow", "Hot Chocolate"))
        self.hot_water.setText(_translate("MainWindow", "Hot Water"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.label_cost_coffee.setText(_translate("MainWindow", "Cost"))
        self.MM.setText(_translate("MainWindow", "M&M"))
        self.crisps.setText(_translate("MainWindow", "Crisps"))
        self.snickers.setText(_translate("MainWindow", "Snickers"))
        self.pantera_rosa.setText(_translate("MainWindow", "Pantera Rosa"))
        self.label_cost_snack.setText(_translate("MainWindow", "Cost"))
        self.backsnack_btn.setText(_translate("MainWindow", "Back"))
        self.coke.setText(_translate("MainWindow", "Coke"))
        self.water.setText(_translate("MainWindow", "Water"))
        self.label_cost_drink_2.setText(_translate("MainWindow", "Cost"))
        self.backdrink_btn.setText(_translate("MainWindow", "Back"))
        self.change_label.setText(_translate("MainWindow", "Change"))
        item = self.change_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.change_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.change_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.change_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.change_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.change_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Coin"))
        item = self.change_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Amount"))
        __sortingEnabled = self.change_table.isSortingEnabled()
        self.change_table.setSortingEnabled(False)
        item = self.change_table.item(0, 0)
        item.setText(_translate("MainWindow", "$1.00"))
        item = self.change_table.item(1, 0)
        item.setText(_translate("MainWindow", "$0.50"))
        item = self.change_table.item(2, 0)
        item.setText(_translate("MainWindow", "$0.20"))
        item = self.change_table.item(3, 0)
        item.setText(_translate("MainWindow", "$0.10"))
        item = self.change_table.item(4, 0)
        item.setText(_translate("MainWindow", "$0.05"))
        self.change_table.setSortingEnabled(__sortingEnabled)
        self.continuebtn.setText(_translate("MainWindow", "Continue?"))
        self.returnbtn.setText(_translate("MainWindow", "Return Money"))
        self.coffee_btn.setText(_translate("MainWindow", "Coffee Machine"))
        self.snack_btn.setText(_translate("MainWindow", "Snack Machine"))
        self.drink_btn.setText(_translate("MainWindow", "Drink Machine"))
        self.fiftybtn.setText(_translate("MainWindow", "$0.50"))
        self.onebtn.setText(_translate("MainWindow", "$1.00"))
        self.twentybtn.setText(_translate("MainWindow", "$0.20"))
        self.fivebtn.setText(_translate("MainWindow", "$0.05"))
        self.tenbtn.setText(_translate("MainWindow", "$0.10"))
        self.total_change.setText(_translate("MainWindow", "Total"))
        self.buybtn.setText(_translate("MainWindow", "BUY"))
        self.correct_money.setText(_translate("MainWindow", "Select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
