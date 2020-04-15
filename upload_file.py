import time
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:/My_programs/images (1).jfif")