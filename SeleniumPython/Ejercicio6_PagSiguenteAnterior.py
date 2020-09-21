import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")

	def test_pag_siguiente_anterior(self):
		driver = self.driver
		driver.get("http://www.gmail.com")
		time.sleep(3)
		driver.get("http://www.youtube.com")
		time.sleep(3)
		driver.get("https://capacitateparaelempleo.org/index.php")
		time.sleep(3)
		driver.back()
		time.sleep(5)
		driver.back()
		time.sleep(5)
		driver.forward()
		time.sleep(5)

if __name__ == '__main__':
	unittest.main()