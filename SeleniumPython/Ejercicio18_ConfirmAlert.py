from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")
driver.get("file:///C:/Users/rjrtxh/Documents/SeleniumPython/Confirm_Alert.html")
time.sleep(5)
confirmAlert = driver.find_element_by_name("alert")
confirmAlert.click()
time.sleep(2)
confirmAlert = driver.switch_to_alert()
time.sleep(2)
confirmAlert.dismiss()
time.sleep(2)

confirmAlert = driver.find_element_by_name("alert")
confirmAlert.click()
time.sleep(2)
confirmAlert = driver.switch_to_alert()
time.sleep(2)
confirmAlert.accept()
time.sleep(2)

driver.close()