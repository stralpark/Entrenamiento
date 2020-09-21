import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")

	def test_subir_archivo(self):
		self.driver.get("https://mdbootstrap.com/plugins/jquery/file-upload/")
		time.sleep(8)
		self.driver.find_element_by_id("input-file-now-custom-2").send_keys("C:\\Users\\rjrtxh\\Documents\\SeleniumPython\\EjemploPytesseract.PNG")
		time.sleep(8)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()