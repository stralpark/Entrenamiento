from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")
driver.get("file:///C:/Users/rjrtxh/Documents/SeleniumPython/alerta_simple.html")
time.sleep(5)
alertaSimple = driver.find_element_by_name("alert")
alertaSimple.click()
time.sleep(2)
alertaSimple = driver.switch_to_alert()
alertaSimple.dismiss()
time.sleep(2)
driver.close()