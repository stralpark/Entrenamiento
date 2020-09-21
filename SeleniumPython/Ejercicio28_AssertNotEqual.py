import unittest
from selenium import webdriver
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")

	def test_assert_equal(self):
		driver = self.driver
		driver.get("https://www.google.com.mx")
		tituloPag = driver.title
		self.assertNotEqual("Google",tituloPag,"El titulo de la pagina es igual")

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()