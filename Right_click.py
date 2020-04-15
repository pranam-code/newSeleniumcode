import time
from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
button=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
action=ActionChains(driver)
action.context_click(button).perform()