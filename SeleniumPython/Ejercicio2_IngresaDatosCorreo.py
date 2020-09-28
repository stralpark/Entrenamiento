#Este es el ejercicio 2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")
driver.get("https://gmail.com")

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("stralpark@ciencias.unam.mx")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

contraseña = driver.find_element_by_name("password")
contraseña.send_keys("w6hqWYEu_p")
contraseña.send_keys(Keys.ENTER)

