import unittest
from selenium import webdriver

class assertion_Test(unittest.TestCase):
    def test_name(self):
        driver = webdriver.Chrome(
            executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
        driver.get("https://www.google.com/")
        #driver=None
        #self.assertEqual(driver.title,"Google","webpage not find")
        # self.assertNotEqual("Google1",driver.title,"webpage not found")
        #self.assertTrue(driver.title=="Google") # expression will become true,checks the conditions
        #self.assertFalse(driver.title=="Google1") # expression will become false
        #self.assertIsNone(driver) # passed if the parameter is none
        #self.assertIsNotNone(driver)

        # to verify presence of a value in a list,tuple,set and dictionary
    def test_name(self):
        list={"python","selenium","java"}
        #self.assertIn("python",list)
        self.assertNotIn("c#",list) # the value is not present IN THE LIST
        # Relational comparison thru assertion
    def test_relation(self):
        #self.assertGreater(100,10) # first value has to be greater
        #self.assertGreaterEqual(100,10) # first value greater or equal
        #self.assertLess(10,100) # first number has to be lesser
        self.assertLessEqual(10,100) # lesser or equal



if __name__ == "__main__":
    unittest.main()
