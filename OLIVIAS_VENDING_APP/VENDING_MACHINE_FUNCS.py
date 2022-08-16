import sys
import math
from typing import final

class VENDING_MACHINE_FUNCS():

    def __init__(self):

        self.total_money = 0
        self.changedict = {}

    def insert_coin(self,coin,coin_accepted):
        no_coin = len(coin)
        for i in range(no_coin):
            print(coin[i])
            #valueError working good. removes coin updates. so will have to intergrate into GUI
            try:
                if coin[i] not in coin_accepted:
                    raise ValueError(f"{coin[i]} not accepted")
            except ValueError as e:
                print(e)
                coin.remove(coin[i])
                #this is where you need to add about self.change

            else:
                self.total_money = self.total_money +coin[i]
        return self.total_money

    def check_machine_coins(self,vending_coin,change):
        coins_inside = {20:1,15:0.5}

        for key, value in vending_coin.items():
            if value < 1:
                self.changedict[key] = 0
            else:
                self.changedict[key] = math.floor(change/key)
                change = change - math.floor(change/key)
        return self.changedict


    def get_change(self,value,money,coin_dict):
        try:
            if money<value:
                missing = value - money
                change = 0
                raise ValueError(f"{missing} is missing from total")
            elif money>value:
                change = money-value
            elif money==value:
                change = 0
        except ValueError as e:
            print(e)
        else:
            changes = self.check_machine_coins(coin_dict,change)
            print(changes)
            print(change)

    def coffee_machine(self,coin,product):
        hot_drinks = {'Coffee':1.5,'Hot Chocolate': 1.0,'Hot Water':0.5}
        allowed_coins = [1,0.5]
        coins_inside = {1:0,0.5:15}
        self.insert_coin(coin,allowed_coins)
        if product in hot_drinks:
            value = hot_drinks.get(product,0)
            change = self.get_change(value,self.total_money,coins_inside)
            print(change)

    def money inside(self):
        hot_drinks = {'Coffee':1.5,'Hot Chocolate': 1.0,'Hot Water':0.5}
        allowed_coins = [1,0.5]
        coins_inside = {'one':20,'fifty':15}


    def drink_machine(self,product):
        cold_drinks = {'Coke':1.20,'Water':0.75}
        allowed_coins = [1,0.5,0.2,0.1,0.05]

    def snack_machine(self,product):
        snacks = {'M&Ms':2.5,'Crisps':1.90,'Snickers':1.3,'Pantera Rosa':0.70}
        allowed_coins = [1,0.5,0.2,0.1]




coins = [1,1,1]
product = 'Coffee'
print(product)
obj = VENDING_MACHINE_FUNCS()
money = obj.coffee_machine(coins,product)
print(money)