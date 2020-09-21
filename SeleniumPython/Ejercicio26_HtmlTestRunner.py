import unittest
from selenium import webdriver
import time
import HtmlTestRunner

class suite(unittest.TestCase):
	def setUp(self):
		self.cDriver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe")

	def test_busqueda(self):
		self.cDriver.get("https://www.google.com.mx/")
		self.busqueda = self.cDriver.find_element_by_name("q")
		self.busqueda.send_keys("selenium")
		self.busqueda.submit()
		time.sleep(3)

	def test_usando_select(self):
		self.cDriver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
		time.sleep(3)
		radioButton = self.cDriver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
		radioButton.click()
		time.sleep(2)
		radioButton = self.cDriver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[3]")
		radioButton.click()
		time.sleep(2)

	def test_scrollDown(self):
		self.cDriver.get("https://www.amazon.com.mx/")
		time.sleep(3)
		self.cDriver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(3)

	def test_HyperlinkByLinkText(self):
		self.cDriver.get("https://www.w3schools.com/")
		time.sleep(5)
		encontrarLink = self.cDriver.find_element_by_link_text("Learn SQL")
		encontrarLink.click()
		time.sleep(5)

	def tearDown(self):
		self.cDriver.quit()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = 'TestResult'))