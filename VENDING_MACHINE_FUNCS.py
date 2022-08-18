#Python 3.9 - Vending Machine Functions
#version 1.0
#By Olivia Bridgewater-Smith

import sys
import math
from typing import final

class VendingApp:
    #def __init__(self):
    #    self.changedict = []

    def change_vending(self):
        
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
        dict_1 = self.machine['coins']
        for key, value in dict_1.items():

            if value < 1 or self.change==0:
                self.changedict.append(0)
            else:
                coin_amount = math.floor(self.change/key)
                dict_1[key]=value-coin_amount
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
        #Check if machine still has enough product stock
        dict_2 = self.machine['produts']
        value = dict_2[key]
        self.ui.buybtn.setEnabled(True)
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


    def remove_product(self,key):
        #Once item has been purchased remove item from stock
        dict_3 = self.machine['produts']
        value = dict_3[key]
        try:
            if value<1:
                raise ValueError(f"{value} of products is not correct")
        except ValueError as e:
            print(e)
        else:
            dict_3[key]=value-1
