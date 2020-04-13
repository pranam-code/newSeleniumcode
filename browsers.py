import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from webdriverdownloader import GeckoDriverDownloader # vs ChromeDriverDownloader vs OperaChromiumDriverDownloader
# gdd = GeckoDriverDownloader()
# gdd.download_and_install()
driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Firefox(
# executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/geckodriver-v0.26.0-win64/geckodriver.exe")

driver.get("http://newtours.demoaut.com/")
user_ele=driver.find_element_by_name("userName")
print(user_ele.is_displayed()) #returns true or false based on element satatus
print(user_ele.is_enabled()) #returns true/false
pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed()) #returns true or false based on element satatus
print(pwd_ele.is_enabled()) #returns true/false

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element_by_name("login").click()
round_elem=driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of round trip radio button:",round_elem.is_selected())
onetrip_elem=driver.find_element_by_css_selector("input[value=oneway]")
print("status of one tip radio button:",onetrip_elem.is_selected())


# print(driver.title)  # Title of the page
# driver.back()  # navigate on the back page,
# driver.forward()  # navigate on the forward page

# print(driver.current_url)  # returns the url of the page

# print(driver.page_source) # HTML code for the page

# driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

# time.sleep(5)

# driver.quit()  # close all the windows

# driver.close() # only close one browser
