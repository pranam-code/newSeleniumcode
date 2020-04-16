import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"C:\Sonali"})

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe",options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
# download txt file
driver.find_element_by_id("textbox").send_keys("Hi Selenium there:")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
# download pdf file
driver.find_element_by_id("pdfbox").send_keys("welcome to selenium")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
# download at expected location with chrome options
