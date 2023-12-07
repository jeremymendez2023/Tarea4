from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://pluto.tv/es/account/sign-in")
#Funcion para maximizar la pantalla
driver.maximize_window()
user= driver.find_element(By.XPATH,"//input[contains(@name,'userIdentity')]").send_keys("login.prueba.prog3@gmail.com")
password= driver.find_element(By.XPATH, "//input[contains(@name,'password')]").send_keys("HOLA")
#Tiempo de suspension de la pantalla (Segundos)
time.sleep(50)

#Cerrar ventana y finalizar prueba
driver.close()

