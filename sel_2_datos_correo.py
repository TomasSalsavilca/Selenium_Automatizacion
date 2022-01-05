from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#siempre declararlo
driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
driver.get("https://gmail.com")

usuario = driver.find_element_by_id('identifierId')
#manda info
usuario.send_keys('aquivatucorreo')
usuario.send_keys(Keys.ENTER) #Dar enter
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys('aquivatucontrasenia')
clave.send_keys(Keys.ENTER)

driver.close()