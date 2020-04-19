import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")

driver.implicitly_wait(4)
driver.get("https://www.expedia.com/")
driver.maximize_window()
# driver.find_element_by_id("wizard-flight-pwa").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click()
time.sleep(2)
driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")  # origin
time.sleep(2)
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")  # destination
driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("4/20/2020")  # select the deaparting date
returnDate = driver.find_element_by_id("flight-returning-hp-flight")
returnDate.send_keys(Keys.CONTROL + "a", Keys.DELETE)  # use keys class to select the text in drop down
returnDate.send_keys("4/22/2020")  # slect the return date
traveller = driver.find_element_by_xpath("//*[@id='traveler-selector-hp-flight']/div/ul/li/button")
traveller.send_keys(Keys.CONTROL + "a", Keys.DELETE)  # select the drop down using keys class
traveller.click()  # click on drop down to select
# click on adult button
driver.find_element_by_xpath(
    "//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button").click()
# click on child button
driver.find_element_by_xpath(
    "//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[2]/div[1]/div[4]/button").click()
age = Select(driver.find_element_by_xpath("//*[@id='flight-age-select-1-hp-flight']"))
age.select_by_visible_text("6")  # selct age from drop down
# driver.find_element_by_id("flight-returning-hp-flight").send_keys("5/16/2020")
driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()  # search
try:  # click for non stop flight
    wait = WebDriverWait(driver, 20)
    non_stop = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
    non_stop.click()
except:  # if non stop flight is not present then go for one stop search
    wait = WebDriverWait(driver, 20)
    one_stop = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-1']")))
    one_stop.click()

time.sleep(3)
driver.quit()
