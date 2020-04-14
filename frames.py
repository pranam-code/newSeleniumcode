import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.maximize_window()
driver.switch_to.frame("packageListFrame") # first frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame") # second frame
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame("classFrame") # third frame
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
time.sleep(3)

