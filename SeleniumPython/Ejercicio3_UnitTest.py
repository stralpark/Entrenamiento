import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usandoUnitTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")

	def test_buscar(self):
		driver = self.driver
		driver.get("http://www.google.com.mx")
		self.assertIn("Google",driver.title)
		elemento = driver.find_element_by_name("q")
		elemento.send_keys("selenium")
		elemento.send_keys(Keys.RETURN)
		time.sleep(2)
		assert "No se encontró el elemento:" not in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()