import unittest

from VENDING_MACHINE_FUNCS import VendingApp

class test(unittest.TestCase):


    def test_change(self):

        inserted_money = 0.5

        product_value = 0.5

        result = VendingApp.change_vending(self,inserted_money,product_value)

        self.assertEqual(result,(0.0,False))




if __name__ == '__main__':
    unittest.main()



