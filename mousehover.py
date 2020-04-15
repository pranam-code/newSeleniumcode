import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermt=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermt).move_to_element(user).click().perform()
