import unittest
from selenium import webdriver
import time


class Searchengine_test(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(
            executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page:" + self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(
            executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title of the page:" + self.driver.title)
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
