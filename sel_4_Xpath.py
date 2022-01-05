import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_buscar_por_xpath(self):
		driver = self.driver
		driver.get("http://www.google.com")
		time.sleep(3)
		buscar_por_xpath = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
		buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN)#baja el buscador
		time.sleep(3)
		buscar_por_xpath.send_keys(Keys.ENTER)
		time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()


#xpath es una estructura de objetos
#xpath relativo: busca de acuerdo al último nodo./html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input

#xpath absoluto	: busca de acuerdo a todos los nodos