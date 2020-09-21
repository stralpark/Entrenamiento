import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")

	def test_manejando_ventanas(self):
		self.driver.get("https://www.google.com/intl/es/gmail/about/#")
		time.sleep(5)
		siguiente = self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/ul[1]/li/div/div/div[1]/div/div[3]/a[1]")
		time.sleep(2)
		siguiente.click()
		time.sleep(2)
		print(self.driver.current_window_handle)
		time.sleep(3)

		handles = self.driver.window_handles
		for h in handles:
			self.driver.switch_to.window(h)
			print(self.driver.title)
			time.sleep(1)

	#def tearDown(self):
		#self.driver.close()

if __name__ == '__main__':
	unittest.main()