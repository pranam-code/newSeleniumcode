import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("file:///C:/My_programs/table_demo.html")
driver.maximize_window()
rows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr")) # count no of rows in the table
cols=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")) # count the total columns
print(rows)
print(cols)
print("Product"+"  "+"Article"+"   "+"Price")
for r in range(2,rows+1):
    for c in range(1,cols+1):
       value= driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
       print(value,end='  ')
    print()