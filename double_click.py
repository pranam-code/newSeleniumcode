import time
from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
elem=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
action=ActionChains(driver)
action.double_click(elem).perform()
