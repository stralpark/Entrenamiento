import unittest
from selenium import webdriver
from selenium. webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")
	
	def test_buscar_por_xpath(self):
		driver = self.driver
		driver.get("http://www.google.com.mx")
		time.sleep(3)
		buscar_por_xpath =  driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
		time.sleep(3)
		buscar_por_xpath.send_keys("selenium",Keys.ARROW_DOWN)
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()