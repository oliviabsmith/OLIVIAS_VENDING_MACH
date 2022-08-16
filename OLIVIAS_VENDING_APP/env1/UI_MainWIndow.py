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
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:white")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(410, 50, 291, 481))
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
        self.coffee_drink.setObjectName("coffee_drink")
        self.hot_choc = QtWidgets.QPushButton(self.coffee)
        self.hot_choc.setGeometry(QtCore.QRect(90, 180, 101, 71))
        self.hot_choc.setObjectName("hot_choc")
        self.hot_water = QtWidgets.QPushButton(self.coffee)
        self.hot_water.setGeometry(QtCore.QRect(90, 320, 101, 71))
        self.hot_water.setObjectName("hot_water")
        self.back_btn = QtWidgets.QPushButton(self.coffee)
        self.back_btn.setGeometry(QtCore.QRect(210, 450, 75, 24))
        self.back_btn.setObjectName("back_btn")
        self.cost_coffee = QtWidgets.QLCDNumber(self.coffee)
        self.cost_coffee.setGeometry(QtCore.QRect(10, 30, 61, 51))
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
        self.MM.setObjectName("MM")
        self.crisps = QtWidgets.QPushButton(self.snack)
        self.crisps.setGeometry(QtCore.QRect(110, 160, 71, 51))
        self.crisps.setObjectName("crisps")
        self.snickers = QtWidgets.QPushButton(self.snack)
        self.snickers.setGeometry(QtCore.QRect(110, 260, 71, 51))
        self.snickers.setObjectName("snickers")
        self.pantera_rosa = QtWidgets.QPushButton(self.snack)
        self.pantera_rosa.setGeometry(QtCore.QRect(110, 370, 71, 51))
        self.pantera_rosa.setObjectName("pantera_rosa")
        self.cost_snack = QtWidgets.QLCDNumber(self.snack)
        self.cost_snack.setGeometry(QtCore.QRect(30, 30, 51, 51))
        self.cost_snack.setObjectName("cost_snack")
        self.label_cost_snack = QtWidgets.QLabel(self.snack)
        self.label_cost_snack.setGeometry(QtCore.QRect(30, 10, 47, 13))
        self.label_cost_snack.setObjectName("label_cost_snack")
        self.stackedWidget.addWidget(self.snack)
        self.drink = QtWidgets.QWidget()
        self.drink.setStyleSheet("background-color:greenyellow")
        self.drink.setObjectName("drink")
        self.coke = QtWidgets.QPushButton(self.drink)
        self.coke.setGeometry(QtCore.QRect(100, 70, 101, 91))
        self.coke.setObjectName("coke")
        self.water = QtWidgets.QPushButton(self.drink)
        self.water.setGeometry(QtCore.QRect(100, 270, 101, 91))
        self.water.setObjectName("water")
        self.cost_drink = QtWidgets.QLCDNumber(self.drink)
        self.cost_drink.setGeometry(QtCore.QRect(20, 30, 51, 51))
        self.cost_drink.setObjectName("cost_drink")
        self.label_cost_drink_2 = QtWidgets.QLabel(self.drink)
        self.label_cost_drink_2.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label_cost_drink_2.setObjectName("label_cost_drink_2")
        self.stackedWidget.addWidget(self.drink)
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
        self.fiftybtn.setGeometry(QtCore.QRect(270, 210, 41, 31))
        self.fiftybtn.setObjectName("fiftybtn")
        self.onebtn = QtWidgets.QPushButton(self.centralwidget)
        self.onebtn.setGeometry(QtCore.QRect(270, 150, 41, 31))
        self.onebtn.setObjectName("onebtn")
        self.twentybtn = QtWidgets.QPushButton(self.centralwidget)
        self.twentybtn.setGeometry(QtCore.QRect(270, 270, 41, 31))
        self.twentybtn.setObjectName("twentybtn")
        self.fivebtn = QtWidgets.QPushButton(self.centralwidget)
        self.fivebtn.setGeometry(QtCore.QRect(270, 400, 41, 31))
        self.fivebtn.setObjectName("fivebtn")
        self.tenbtn = QtWidgets.QPushButton(self.centralwidget)
        self.tenbtn.setGeometry(QtCore.QRect(270, 340, 41, 31))
        self.tenbtn.setObjectName("tenbtn")
        self.total_change = QtWidgets.QLabel(self.centralwidget)
        self.total_change.setGeometry(QtCore.QRect(240, 30, 47, 13))
        self.total_change.setObjectName("total_change")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
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
        self.coke.setText(_translate("MainWindow", "Coke"))
        self.water.setText(_translate("MainWindow", "Water"))
        self.label_cost_drink_2.setText(_translate("MainWindow", "Cost"))
        self.coffee_btn.setText(_translate("MainWindow", "Coffee Machine"))
        self.snack_btn.setText(_translate("MainWindow", "Snack Machine"))
        self.drink_btn.setText(_translate("MainWindow", "Drink Machine"))
        self.fiftybtn.setText(_translate("MainWindow", "$0.50"))
        self.onebtn.setText(_translate("MainWindow", "$1.00"))
        self.twentybtn.setText(_translate("MainWindow", "$0.20"))
        self.fivebtn.setText(_translate("MainWindow", "$0.05"))
        self.tenbtn.setText(_translate("MainWindow", "$0.10"))
        self.total_change.setText(_translate("MainWindow", "Total"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
