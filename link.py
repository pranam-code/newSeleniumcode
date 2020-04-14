import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
links=driver.find_elements(By.TAG_NAME,"a")
print("Total no of links present on the page:",len(links)) # count links
for link in links:
    print(link.text)
#driver.find_element(By.LINK_TEXT,"REGISTER").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()