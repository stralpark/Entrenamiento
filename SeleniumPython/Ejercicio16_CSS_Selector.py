from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")
driver.get("https://www.w3schools.com/css/default.asp")
time.sleep(5)
content = driver.find_element_by_css_selector("a.w3-blue")
content.click()
time.sleep(2)
driver.close()