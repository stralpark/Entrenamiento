import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class usando_unittest(unittest.TestCase):
	#La funcion setUp sirve para cargar el driver de chrome
	def setUp(self):
		chromeOptions = Options()
		chromeOptions.add_experimental_option("prefs",{"download.default_directory" : "C:\\DriverChrome\\"})
		self.driver = webdriver.Chrome(executable_path = r"C:\DriverChrome\chromedriver.exe", chrome_options = chromeOptions)

	#La funcion descarga_archivo sirve para descargar un archivo desde una pagina web
	def test_descarga_archivo(self):
		driver = self.driver
		driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")
		time.sleep(3)
		driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div/iframe"))
		time.sleep(3)
		driver.find_element_by_xpath("/html/body/p[2]/a/img").click()
		time.sleep(15)

	#La función tearDown sirve para cerrar el driver de chrome
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()