import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")

	def test_usando_select(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
		time.sleep(3)
		radioButton = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
		radioButton.click()
		time.sleep(2)
		radioButton = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[3]")
		radioButton.click()
		time.sleep(2)
		

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()