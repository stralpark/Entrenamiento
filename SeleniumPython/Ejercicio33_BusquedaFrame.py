import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")

	def test_buscar_frame(self):
		driver = self.driver
		driver.get("https://www.google.com.mx")
		time.sleep(5)
		click1 = driver.find_element_by_id("gbwa")
		time.sleep(5)
		click1.click()
		time.sleep(3)
		driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div[3]/iframe"))
		time.sleep(3)
		click2 = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/ul[1]/li[4]/a/div/span")
		time.sleep(3)
		click2.click()
		time.sleep(5)

if __name__ == '__main__':
	unittest.main()