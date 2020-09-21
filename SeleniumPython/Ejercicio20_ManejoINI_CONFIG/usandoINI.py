import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_unittest(unittest.TestCase):
		
	def setUp(self):
		configuracion = configparser.ConfigParser()
		configuracion.read('Configuracion.ini')
		configuracion.sections()
		obtenerNavegador = configuracion['General']['chrome']
		self.page = configuracion['Paginas']['page']
		self.driver = webdriver.Chrome(executable_path = obtenerNavegador)
		self.page1 = configuracion['Paginas']['page1']


	def test_usando_implicit_wait(self):
		driver = self.driver
		driver.implicitly_wait(5)
		driver.get(self.page)
		#myDynamicElement = driver.find_element_by_name("q")
		driver.execute_script("window.open('');")
		driver.implicitly_wait(5)
		driver.switch_to.window(driver.window_handles[1])
		driver.get(self.page1)
		driver.implicitly_wait(5)
		myDynamicElement = driver.find_element_by_name("q")


if __name__ == '__main__':
	unittest.main()