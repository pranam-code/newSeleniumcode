import unittest
def setUpModule(): #will be executed before class execution starts
    print("setup module")
def tearDownModule(): # will execute after completing everything present in python module
    print("teardown module")

class Apptesting(unittest.TestCase):

    def setUp(self):  # execute before all the test methods
        print("this is login test")

    def tearDown(self):  # execute after all the test methods
        print("this is logout test")

    @classmethod
    def setUpClass(cls):  # execute once the class started
        print("open application")

    @classmethod
    def tearDownClass(cls): # execute after the class is completed
        print("close application")
    def test_search(self):
        print("this is search test")

    def test_advancesearch(self):
        print("this is advance search test")

    def test_prepaidRecharge(self):
        print("this is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("this is postpaid recharge test")


if __name__ == "__main__":
    unittest.main()
