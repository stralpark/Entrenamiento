from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")
driver.get("https://www.w3schools.com/")
time.sleep(5)
encontrarLink = driver.find_element_by_link_text("Learn SQL")
encontrarLink.click()
time.sleep(5)
driver.close()