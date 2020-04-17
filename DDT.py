import xlUtils
from selenium import webdriver


driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
path="C:/test/DDt.xlsx"
rows=xlUtils.getRowCount(path,'Sheet1')
for r in range(2,rows+1):
    username=xlUtils.readData(path,"Sheet1",r,1)
    password=xlUtils.readData(path,"Sheet1",r,2)
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()
    if driver.title=="Find a Flight: Mercury Tours:":
        print("test is passed")
        xlUtils.writeData(path,"Sheet1",r,3,"test passed")
    else:
        print("test failed")
        xlUtils.writeData(path,"Sheet1",r,3,"test failed")
    driver.find_element_by_link_text("Home").click()
