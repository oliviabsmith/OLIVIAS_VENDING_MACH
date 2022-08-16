import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QStackedWidget, QPushButton, QWidget,QRadioButton,QCheckBox,QLabel,QListWidget,QFormLayout,QLineEdit,QHBoxLayout, QVBoxLayout

from UI_MainWindow import Ui_MainWindow

class MainWindow:

    def __init__(self):
        #set main window from UI_MainWindow
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        #Set stacked to index 0 (home page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.coffeedict = [self.ui.onebtn,self.ui.fiftybtn]
        self.snackdict = [self.ui.onebtn,self.ui.fiftybtn,self.ui.twentybtn,self.ui.tenbtn]
        self.drinkdict = [self.ui.onebtn,self.ui.fiftybtn,self.ui.twentybtn,self.ui.tenbtn,self.ui.fivebtn]
        self.vending_products = {'Coffee':1.5,'Hot Chocolate': 1.0,'Hot Water':0.5,'Coke':1.20,'Water':0.75,'MM':2.5,'Crisps':1.90,'Snickers':1.3,'Pantera Rosa':0.70}

        #set totals
        self.input_total = 0

        self.vending_buttons()
        self.product_button()
        self.money_buttons()

    def vending_buttons(self):
        #Set event when button clicked
        self.ui.coffee_btn.clicked.connect(self.coffee_vending)
        self.ui.snack_btn.clicked.connect(self.snack_vending)
        self.ui.drink_btn.clicked.connect(self.drink_vending)
        self.ui.back_btn.clicked.connect(self.go_back)
        self.ui.backdrink_btn.clicked.connect(self.go_back)
        self.ui.backsnack_btn.clicked.connect(self.go_back)

    def product_button(self):
        #coffee buttons
        self.ui.coffee_drink.clicked.connect(lambda: self.display_price(self.ui.coffee_drink,self.ui.cost_coffee))
        self.ui.hot_choc.clicked.connect(lambda: self.display_price(self.ui.hot_choc,self.ui.cost_coffee))
        self.ui.hot_water.clicked.connect(lambda: self.display_price(self.ui.hot_water,self.ui.cost_coffee))

        #snack buttons
        self.ui.MM.clicked.connect(lambda: self.display_price(self.ui.MM,self.ui.cost_snack))
        self.ui.crisps.clicked.connect(lambda: self.display_price(self.ui.crisps,self.ui.cost_snack))
        self.ui.snickers.clicked.connect(lambda: self.display_price(self.ui.snickers,self.ui.cost_snack))
        self.ui.pantera_rosa.clicked.connect(lambda: self.display_price(self.ui.pantera_rosa,self.ui.cost_snack))

        #drink buttons
        self.ui.coke.clicked.connect(lambda: self.display_price(self.ui.coke,self.ui.cost_drink))
        self.ui.water.clicked.connect(lambda: self.display_price(self.ui.water,self.ui.cost_drink))

    def money_buttons(self):
        self.ui.onebtn.clicked.connect(lambda: self.total_money(1))
        self.ui.fiftybtn.clicked.connect(lambda: self.total_money(0.5))
        self.ui.twentybtn.clicked.connect(lambda: self.total_money(0.2))
        self.ui.tenbtn.clicked.connect(lambda: self.total_money(0.1))
        self.ui.fivebtn.clicked.connect(lambda: self.total_money(0.05))

    def total_money(self,input):
        self.input_total = self.input_total+input
        self.ui.total_money.display(self.input_total)

    def show(self):
        self.main_window.show()

    #def update_button(self):

    def display_price(self,button,menu):
        for key, value in self.vending_products.items():
            if key==button.text():
                displaymoney = value
        menu.display(displaymoney)
        button.setEnabled(False)
        
    def go_back(self):
        #Event when a back button is pressed
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.snack_btn.setEnabled(True)
        self.ui.drink_btn.setEnabled(True)
        self.ui.coffee_btn.setEnabled(True)
        self.ui.onebtn.setEnabled(False)
        self.ui.fiftybtn.setEnabled(False)
        self.ui.twentybtn.setEnabled(False)
        self.ui.tenbtn.setEnabled(False)
        self.ui.fivebtn.setEnabled(False)
        self.ui.cost_coffee.display(0.0)
        self.ui.cost_drink.display(0.0)
        self.ui.cost_snack.display(0.0)
        #change function

    def enable_buttons(self,dict):
        #set enabled buttons for dict
        for i in range(len(dict)):
            text = dict[i]
            text.setEnabled(True)

    def coffee_vending(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.coffee)
        self.ui.snack_btn.setEnabled(False)
        self.ui.drink_btn.setEnabled(False)
        self.enable_buttons(self.coffeedict)

    def drink_vending(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.drink)
        self.ui.snack_btn.setEnabled(False)
        self.ui.coffee_btn.setEnabled(False)
        self.enable_buttons(self.drinkdict)

    def snack_vending(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.snack)
        self.ui.coffee_btn.setEnabled(False)
        self.ui.drink_btn.setEnabled(False)
        self.enable_buttons(self.snackdict)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
