#Python 3.9 - Vending Machine Functions
#version 1.0
#By Olivia Bridgewater-Smith

import sys
import math
from typing import final

class VendingApp:

    def change_vending(self):
        self.changedict = []
        self.ui.buybtn.setEnabled(False)

        inserted_money = round(self.input_total,2)
        value = round(self.product_cost,2)
        try:
            if inserted_money<value:
                missing = value - inserted_money
                change = -missing
                raise ValueError(f"{missing} cents is missing from total")
        except ValueError as e:
            self.ui.correct_money.setText(f"${missing} missing from total.")# missing from total")
            self.ui.buybtn.setEnabled(True)
        else:
            #changes = self.check_machine_coins(coins_inside,change)
            change = round(inserted_money-value,2)
            self.ui.correct_money.setText(f"Thanks here is your ${change} change")
        return change



    def check_machine_coins(self):
        #for key, value in vending_coin.items():
        dict = self.machine['coins']
        for key, value in dict.items():

            if value < 1:
                self.changedict.append(0)
            else:
                coin_amount = math.floor(self.change/key)
                dict[key]=value-coin_amount
                self.changedict.append(coin_amount)
                self.change = round(self.change - (coin_amount*key),2)
                print(self.change)
        try:
            if self.change != 0:
                self.ui.correct_money.setText(f"change not available")
                raise ValueError(f"Coins returned. not enough change, insert exact amount")
        except ValueError as e:
            print(e)
        return self.changedict


    def check_machine_product(self,key):
        dict = self.machine['produts']
        value = dict[key]
        try:            
            if value <= 0:
                self.ui.correct_money.setText(f"product not available")
                self.ui.buybtn.setEnabled(False)
                raise ValueError(f"{key} has no stock")
        except ValueError as e:
            print(e)
        else:
            self.ui.correct_money.setText(f"product available")
            self.ui.buybtn.setEnabled(True)


    #def remove_product(self,key):
    #    dict = self.machine['produts']
    #    value = dict[key]
    #    try:
    #        if value<1:
    #            raise ValueError(f"{value} of products is not correct")
    #    except ValueError as e:
    #        print(e)
    #    else:
    #        dict[key]=value-1




    #def check_machine_product(self,button):
    #    dict = self.machine['produts']
    #    bool_1 = True
    #    for key, value in dict.items():
    #        if value <= 0 and button.text()==key:
    #            self.ui.correct_money.setText(f"product not available")
    #            bool_1 = False
    #    if bool_1 == False:
    #        self.ui.correct_money.setText(f"product not available")
    #        self.ui.buybtn.setEnabled(False)
    #    else:
    #        self.ui.correct_money.setText(f"product available")
    #        self.ui.buybtn.setEnabled(True)
            #coffee_coins = {1:15,0.5:15}
        #snack_coins = {1:15,0.5:15,0.2:5,0.1:3,0.05:3}
        #drink_coins = {1:15,0.5:15,0.2:5,0.1:3}