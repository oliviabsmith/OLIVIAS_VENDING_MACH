#Python 3.9 - Vending Machine
#version 2.0
#By Olivia Bridgewater-Smith

import sys
import math
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QStackedWidget, QPushButton,QTableWidgetItem, QTableWidget, QTableWidgetSelectionRange, QWidget,QRadioButton,QCheckBox,QLabel,QListWidget,QFormLayout,QLineEdit,QHBoxLayout, QVBoxLayout

from UI_MainWindow import Ui_MainWindow

from VENDING_MACHINE_FUNCS import VendingApp

class MainWindow:

    def __init__(self):
        #set main window from UI_MainWindow
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        #Set stacked to index 0 (home page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.correct_money.setText('')

        self.total_button_dict = [self.ui.coffee_drink,self.ui.hot_choc,self.ui.hot_water,self.ui.MM,self.ui.crisps,self.ui.snickers,self.ui.pantera_rosa,self.ui.coke,self.ui.water]
        self.coffeedict = [self.ui.onebtn,self.ui.fiftybtn]
        self.drinkdict = [self.ui.onebtn,self.ui.fiftybtn,self.ui.twentybtn,self.ui.tenbtn]
        self.snackdict = [self.ui.onebtn,self.ui.fiftybtn,self.ui.twentybtn,self.ui.tenbtn,self.ui.fivebtn]
        
        self.coffee_machine = {'coins':{1:15,0.5:15},'produts':{'Coffee':0,'Hot Chocolate': 10,'Hot Water':5},'prices':{'Coffee':1.50,'Hot Chocolate': 1.0,'Hot Water':0.5}}
        self.drink_machine = {'coins':{1:15,0.5:15,0.2:5,0.1:3},'produts':{'Coke':12,'Water':7},'prices':{'Coke':1.20,'Water':0.70}}
        self.snack_machine = {'coins':{1:15,0.5:15,0.2:5,0.1:3,0.05:3},'produts':{'MM':25,'Crisps':19,'Snickers':130,'Pantera Rosa':70},'prices':{'MM':2.5,'Crisps':1.90,'Snickers':1.30,'Pantera Rosa':0.70}}

        #set totals
        self.input_total = 0
        self.buy_product = 0
        self.product_cost = 0
        self.machine = {}
        self.change = 0
        self.changedict = []
        self.vending_buttons()
        self.product_button()
        self.money_buttons()
        

        self.ui.buybtn.clicked.connect(self.buy_vending)

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

        self.ui.coffee_drink.clicked.connect(lambda: self.display_price(self.ui.coffee_drink,self.ui.cost_coffee,self.coffee_machine,self.coffee_prod))
        self.ui.hot_choc.clicked.connect(lambda: self.display_price(self.ui.hot_choc,self.ui.cost_coffee,self.coffee_machine,self.coffee_prod))
        self.ui.hot_water.clicked.connect(lambda: self.display_price(self.ui.hot_water,self.ui.cost_coffee,self.coffee_machine,self.coffee_prod))

        #snack buttons
        self.snack_prod = [self.ui.MM,self.ui.crisps,self.ui.snickers,self.ui.pantera_rosa]
        self.ui.MM.clicked.connect(lambda: self.display_price(self.ui.MM,self.ui.cost_snack,self.snack_machine,self.snack_prod))
        self.ui.crisps.clicked.connect(lambda: self.display_price(self.ui.crisps,self.ui.cost_snack,self.snack_machine,self.snack_prod))
        self.ui.snickers.clicked.connect(lambda: self.display_price(self.ui.snickers,self.ui.cost_snack,self.snack_machine,self.snack_prod))
        self.ui.pantera_rosa.clicked.connect(lambda: self.display_price(self.ui.pantera_rosa,self.ui.cost_snack,self.snack_machine,self.snack_prod))

        #drink buttons
        self.drink_prod = [self.ui.coke,self.ui.water]
        self.ui.coke.clicked.connect(lambda: self.display_price(self.ui.coke,self.ui.cost_drink,self.drink_machine,self.drink_prod))
        self.ui.water.clicked.connect(lambda: self.display_price(self.ui.water,self.ui.cost_drink,self.drink_machine,self.drink_prod))

    def money_buttons(self):
        self.ui.onebtn.clicked.connect(lambda: self.total_money(1.00))
        self.ui.fiftybtn.clicked.connect(lambda: self.total_money(0.50))
        self.ui.twentybtn.clicked.connect(lambda: self.total_money(0.2))
        self.ui.tenbtn.clicked.connect(lambda: self.total_money(0.10))
        self.ui.fivebtn.clicked.connect(lambda: self.total_money(0.05))

    def total_money(self,input):
        #cumulative total money entered so far
        self.input_total = self.input_total+input
        self.ui.total_money.display(self.input_total)

    def show(self):
        self.main_window.show()

    def update_button(self,dict,button):
        #update the buttons that can be pressed when choosing product
        for i in range(len(dict)):
            if dict[i] == button:
                dict[i].setEnabled(False)
            else:
                dict[i].setEnabled(True)

         
    def display_price(self,button,menu,dict_1,buttons):
        #display prices when a product button is pressed
        prices = dict_1['prices']
        for key, value in prices.items():
            if key==button.text():
                self.buy_product = key
                self.product_cost = value
                self.machine = dict_1
                self.update_button(buttons,button)   
                menu.display(self.product_cost)
                VendingApp.check_machine_product(self,self.buy_product)
                
        
    def go_back(self):
        #Event when a back button is pressed
        if self.input_total>0:
            self.ui.correct_money.setText(f"${self.input_total} is been returned")
            self.input_total = 0
            self.change = 0
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.snack_btn.setEnabled(True)
        self.ui.drink_btn.setEnabled(True)
        self.ui.coffee_btn.setEnabled(True)
        self.enable_buttons(self.snackdict,False)
        self.ui.cost_coffee.display(0.0)
        self.ui.cost_drink.display(0.0)
        self.ui.cost_snack.display(0.0)
        self.ui.total_money.display(0.0)
        self.buy_product = 0
        self.product_cost = 0
        self.machine = {}
        

    def enable_buttons(self,dict,input):
        #set enabled buttons for stacked widget layout
        for i in range(len(dict)):
            text = dict[i]
            text.setEnabled(input)

    #3 functions below to set individual layout when vending machine chosen
    def coffee_vending(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.coffee)
        self.ui.snack_btn.setEnabled(False)
        self.ui.drink_btn.setEnabled(False)
        #self.ui.buybtn.setEnabled(True)
        self.enable_buttons(self.coffeedict,True)

    def drink_vending(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.drink)
        self.ui.snack_btn.setEnabled(False)
        self.ui.coffee_btn.setEnabled(False)
        #self.ui.buybtn.setEnabled(True)
        self.enable_buttons(self.drinkdict,True)

    def snack_vending(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.snack)
        self.ui.coffee_btn.setEnabled(False)
        self.ui.drink_btn.setEnabled(False)
        #self.ui.buybtn.setEnabled(True)
        self.enable_buttons(self.snackdict,True)


    def buy_vending(self):
        #check what the change amount should be
        self.ui.buybtn.setEnabled(False)
        self.changeven = VendingApp.change_vending(self,self.input_total,self.product_cost)
        print(self.changeven)
        self.change = round(self.changeven[0],2)
            


        #check if they have entered enough money to buy product
        if self.change >= 0 and self.changeven[1]==False:
            self.change_coins = VendingApp.check_machine_coins(self,self.machine,self.change)
            print(self.change_coins)
            self.ui.stackedWidget.setCurrentWidget(self.ui.change)
            VendingApp.remove_product(self,self.buy_product,self.machine)
            self.add_items()
            self.ui.correct_money.setText(f"Thanks here is your ${self.change} change")
        else:
            self.ui.correct_money.setText(f"${self.change} missing from total.")# missing from total")
            self.ui.buybtn.setEnabled(True)

    def add_items(self):
        #add change array to the table on self.ui.change
        list_ch = self.change_coins[0]
        for i in range(len(list_ch)):
            item = QTableWidgetItem(str(list_ch[i]))
            self.ui.change_table.setItem((i), 1, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
