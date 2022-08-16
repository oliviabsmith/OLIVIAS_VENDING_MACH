
#version 3.0
#Author Olivia Bsmith
import sys
import math
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QStackedWidget, QPushButton,QTableWidgetItem, QTableWidget, QTableWidgetSelectionRange, QWidget,QRadioButton,QCheckBox,QLabel,QListWidget,QFormLayout,QLineEdit,QHBoxLayout, QVBoxLayout

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
        self.vending_products = {'Coffee':1.50,'Hot Chocolate': 1.0,'Hot Water':0.5,'Coke':1.20,'Water':0.75,'MM':2.5,'Crisps':1.90,'Snickers':1.30,'Pantera Rosa':0.70}

        #set totals
        self.input_total = 0
        self.changedict = {}

        self.vending_buttons()
        self.product_button()
        self.money_buttons()

        self.ui.buybtn.clicked.connect(self.change_vending)

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
        self.coffee_prod = [self.ui.coffee_drink,self.ui.hot_choc,self.ui.hot_water]
        self.ui.coffee_drink.clicked.connect(lambda: self.display_price(self.ui.coffee_drink,self.ui.cost_coffee,self.coffee_prod))
        self.ui.hot_choc.clicked.connect(lambda: self.display_price(self.ui.hot_choc,self.ui.cost_coffee,self.coffee_prod))
        self.ui.hot_water.clicked.connect(lambda: self.display_price(self.ui.hot_water,self.ui.cost_coffee,self.coffee_prod))

        #snack buttons
        self.snack_prod = [self.ui.MM,self.ui.crisps,self.ui.snickers,self.ui.pantera_rosa]
        self.ui.MM.clicked.connect(lambda: self.display_price(self.ui.MM,self.ui.cost_snack,self.snack_prod))
        self.ui.crisps.clicked.connect(lambda: self.display_price(self.ui.crisps,self.ui.cost_snack,self.snack_prod))
        self.ui.snickers.clicked.connect(lambda: self.display_price(self.ui.snickers,self.ui.cost_snack,self.snack_prod))
        self.ui.pantera_rosa.clicked.connect(lambda: self.display_price(self.ui.pantera_rosa,self.ui.cost_snack,self.snack_prod))

        #drink buttons
        self.drink_prod = [self.ui.coke,self.ui.water]
        self.ui.coke.clicked.connect(lambda: self.display_price(self.ui.coke,self.ui.cost_drink,self.drink_prod))
        self.ui.water.clicked.connect(lambda: self.display_price(self.ui.water,self.ui.cost_drink,self.drink_prod))

    def money_buttons(self):
        self.ui.onebtn.clicked.connect(lambda: self.total_money(1.00))
        self.ui.fiftybtn.clicked.connect(lambda: self.total_money(0.50))
        self.ui.twentybtn.clicked.connect(lambda: self.total_money(0.2))
        self.ui.tenbtn.clicked.connect(lambda: self.total_money(0.10))
        self.ui.fivebtn.clicked.connect(lambda: self.total_money(0.05))

    def total_money(self,input):
        self.input_total = self.input_total+input
        self.ui.total_money.display(self.input_total)

    def show(self):
        self.main_window.show()

    def update_button(self,dict,button):
        for i in range(len(dict)):
            if dict[i] == button:
                dict[i].setEnabled(False)
            else:
                dict[i].setEnabled(True)

    def display_price(self,button,menu,dict):
        for key, value in self.vending_products.items():
            if key==button.text():
                displaymoney = value
        self.update_button(dict,button)
                
        menu.display(displaymoney)
        
        
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
        self.ui.buybtn.setEnabled(False)
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
        self.ui.buybtn.setEnabled(True)
        self.enable_buttons(self.coffeedict)

    def drink_vending(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.drink)
        self.ui.snack_btn.setEnabled(False)
        self.ui.coffee_btn.setEnabled(False)
        self.ui.buybtn.setEnabled(True)
        self.enable_buttons(self.drinkdict)

    def snack_vending(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.snack)
        self.ui.coffee_btn.setEnabled(False)
        self.ui.drink_btn.setEnabled(False)
        self.ui.buybtn.setEnabled(True)
        self.enable_buttons(self.snackdict)

    def change_vending(self):
        self.ui.buybtn.setEnabled(False)
        inserted_money = self.ui.total_money.value()
        coins_inside = {1:15,0.5:15}
        value = self.ui.cost_coffee.value()
        try:
            if inserted_money<value:
                missing = value - inserted_money
                change = 0
                raise ValueError(f"{missing} cents is missing from total")
            elif inserted_money>value:
                change = inserted_money-value
            elif inserted_money==value:
                change = 0
        except ValueError as e:
            self.ui.correct_money.setText(f"${missing} is")# missing from total")
        else:
            changes = self.check_machine_coins(coins_inside,change)
            #print(changes.get(1))
            self.ui.stackedWidget.setCurrentWidget(self.ui.change)
            #item = QTableWidget()
            #item.setItem(changes.get(1))
            self.ui.change_table.
            print(item)
            self.ui.change_table.setItem(1, 1, item)
            self.ui.correct_money.setText('Entered enough money')

    def check_machine_coins(self,vending_coin,change):
        coins_inside = {20:1,15:0.5}

        for key, value in vending_coin.items():
            if value < 1:
                self.changedict[key] = 0
            else:
                self.changedict[key] = math.floor(change/key)
                change = change - math.floor(change/key)
        return self.changedict




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
