from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("https://www.amazon.ca/")
driver.maximize_window()
# capture all the cookies created by browser
cookies=driver.get_cookies()
print("Before adding cookie:",len(cookies))
print(cookies) # print all the cookie pairs captured by the web page
cookie={'name':'Mycookie','value':'12345'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print("After adding cookie:",len(cookies)) # print after adding new cookie
print(cookies) # print all the cookie pairs captured by the web page

# delete the cookie
driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()
print("After deleting cookie:",len(cookies))
print(cookies) # print all the cookie pairs captured by the web page

driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
