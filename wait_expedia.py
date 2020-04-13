import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")

driver.implicitly_wait(5)
driver.get("https://www.expedia.com/")
driver.maximize_window()
#driver.find_element_by_id("wizard-flight-pwa").click()
driver.find_element(By.ID,"tab-flight-tab-hp").click()
time.sleep(2)
driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO") # origin
time.sleep(2)
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC") # destination
driver.find_element_by_id("flight-departing-hp-flight").clear()

driver.find_element_by_id("flight-departing-hp-flight").send_keys("4/14/2020")
driver.find_element_by_id("flight-returning-hp-flight").clear()
returnDate=driver.find_element_by_id("flight-returning-hp-flight")
returnDate.send_keys(Keys.CONTROL+"a",Keys.DELETE)
returnDate.send_keys("4/15/2020")
#driver.find_element_by_id("flight-returning-hp-flight").send_keys("5/16/2020")
driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click() # search
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))
element.click()
time.sleep(3)
driver.close()