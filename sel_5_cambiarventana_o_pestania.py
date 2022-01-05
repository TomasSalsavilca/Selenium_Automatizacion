import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\\dchrome\\chromedriver.exe")

	def test_cambiar_ventana(self):
		driver = self.driver
		#ventana cero
		driver.get("http://www.google.com")
		time.sleep(3)
		#ventana 1
		driver.execute_script("window.open('');")#instruccion de python para abrir nueva ventana
		time.sleep(3)
		driver.switch_to.window(driver.window_handles[1])#posicionate en la ventana 1
		#hace nueva búsqueda
		driver.get("http://stackoverflow.com")
		time.sleep(3)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(3)

if __name__ == '__main__':
	unittest.main()