import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()