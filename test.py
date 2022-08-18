import unittest

from VENDING_MACHINE_FUNCS import VendingApp

class test(unittest.TestCase):


    def test_change(self):

        inserted_money = 0.5

        product_value = 0.5

        result = VendingApp.change_vending(self,inserted_money,product_value)

        self.assertEqual(result,(0.0,False))

    def test_change2(self):

        inserted_money = 1.5

        product_value = 0.5

        result = VendingApp.change_vending(self,inserted_money,product_value)

        self.assertEqual(result,(1.0,False))

    def test_change3(self):

        inserted_money = 0.5

        product_value = 1.5

        result = VendingApp.change_vending(self,inserted_money,product_value)

        self.assertEqual(result,(-1.0,True))

    def check_coins(self):
        machine = {'coins':{1:0,0.5:0},'produts':{'Coffee':0,'Hot Chocolate': 10,'Hot Water':5},'prices':{'Coffee':1.50,'Hot Chocolate': 1.0,'Hot Water':0.5}}
        
        change = 10.0
        result = VendingApp.check_machine_coins(self,machine,change)
        #result = VendingApp.check_machine_coins(self,machine,change)

        self.assertEqual(result,([0,0],True))
        #self.assertFalse(result[1])


if __name__ == '__main__':
    unittest.main()



