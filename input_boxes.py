from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print("No of text boxes on the page:",len(inputboxes))
print("Text Field Displayed or not:", driver.find_element_by_id("RESULT_TextField-1").is_displayed())  # true/false

print("Text field Enabled or not:", driver.find_element_by_id("RESULT_TextField-1").is_enabled())  # true/false

driver.find_element_by_id("RESULT_TextField-1").send_keys("Sonali")
driver.find_element_by_id("RESULT_TextField-2").send_keys("Garg")
driver.find_element_by_id("RESULT_TextField-3").send_keys("467892134")

# working with radio buttons ####
print("status of radio button before selected:",driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected())
button=driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-7_0']")
driver.execute_script("arguments[0].click();",button)
print("status of radio button After selected :",driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected())

# working with checkboxes ########
button1=driver.find_element_by_id("RESULT_CheckBox-8_0")
button2=driver.find_element_by_id("RESULT_CheckBox-8_6")
driver.execute_script("arguments[1].click();arguments[0].click()",button1,button2)
# working with drop-down list
drp=Select(driver.find_element_by_id("RESULT_RadioButton-9"))
#drp.select_by_visible_text("Morning")
# select by index
#drp.select_by_index(3)
# select by value
drp.select_by_value("Radio-2")
# count no of options
print("No of options in the drop down:",len(drp.options))
# capture all the options and print them
all_options=drp.options #list variable created
for option in all_options: # fetch the text values from the list
    print(option.text)
