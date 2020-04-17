from selenium import webdriver
import pyautogui

driver = webdriver.Chrome(
    executable_path="C:/Users/manoj/eclipse/java-2019-12/eclipse/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/mercurywelcome.php")
driver.maximize_window()
#driver.save_screenshot("C:/test/home3.png")
#driver.get_screenshot_as_file("C:/test/home4.png")
#pyautogui.screenshot(r"C:/test/ss1.png")
# to capture the full page screenshot use pyautogui
im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('my_screenshot.png')  # image name will be as per parameter
im3 = pyautogui.screenshot(region=(100,100,500,500)) # mention spedific region to get the screenshot
print(im1.size)  # will return a dimension of image as a tuple
im2.save("C:/test/new.png") # save the image
im3.getpixel((100, 200)) # return color value of the point mentioned
im3.save("C:/test/new3.png")