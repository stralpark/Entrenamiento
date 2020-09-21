from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")
driver.get("file:///C:/Users/rjrtxh/Documents/SeleniumPython/PrompAlert.html")
time.sleep(5)
alert = driver.find_element_by_name("promp_alert")
alert.click()
time.sleep(3)
alert = driver.switch_to_alert()
alert.accept()
time.sleep(3)
driver.close()