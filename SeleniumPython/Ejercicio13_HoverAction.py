import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")

	def test_usando_select(self):
		driver = self.driver
		driver.get("https://www.google.com.mx")
		time.sleep(3)
		elem = driver.find_element_by_link_text("Privacidad")
		hover = ActionChains(driver).move_to_element(elem)
		hover.perform()
		time.sleep(5)

if __name__ == '__main__':
	unittest.main()