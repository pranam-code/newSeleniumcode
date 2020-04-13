from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))
print("Displayed or not:",driver.find_element_by_id("RESULT_TextField-1").is_displayed()) #true/false

print("Enabled or not:",driver.find_element_by_id("RESULT_TextField-1").is_enabled()) #true/false

driver.find_element_by_id("RESULT_TextField-1").send_keys("Sonali")
driver.find_element_by_id("RESULT_TextField-2").send_keys("Garg")
driver.find_element_by_id("RESULT_TextField-3").send_keys("467892134")

