import time
from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
source_elem=driver.find_element_by_xpath("//*[@id='box6']")
target=driver.find_element_by_xpath("//*[@id='box106']")
action=ActionChains(driver)
action.drag_and_drop(source_elem,target).perform()