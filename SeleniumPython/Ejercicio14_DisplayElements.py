from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")
driver.get("https://www.google.com.mx")
time.sleep(5)
displayedElements = driver.find_element_by_name("btnI")
print(displayedElements.is_displayed()) #El valor que regresa is_displayed es un booleano (true o false) si ya se cargo el elemento 
print(displayedElements.is_enabled()) #El valor que regresa is_enable es un booleano (true o false) si el elemento está disponible
driver.close()