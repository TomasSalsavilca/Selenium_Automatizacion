import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para mandar acciones de teclado
import time

class usando_unittest(unittest.TestCase):

	def setUp(self): #inicializar nuestro driver
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
	#después del setUp poner a las funciones el nombre test
	def test_buscar(self):
		driver = self.driver
		driver.get("http://www.google.com")
		self.assertIn("Google", driver.title) #valida el ingreso a la web indicada
		elemento = driver.find_element_by_name("q")
		elemento.send_keys("selenium")
		elemento.send_keys(Keys.RETURN)#enter
		time.sleep(5)
		assert "No se encontro el elemento" not in driver.page_source

	def tearDown(self):#apaga todo
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
