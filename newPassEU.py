import time
import string
import random
PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(PATH)
driver.get("https://comicstores.es/registro/formReinicioClaveSolicitud.php")
time.sleep(5)
user = driver.find_element_by_id("email")
user.clear()
user.send_keys("disom31955@mxgsby.com")
time.sleep(5)
forgor = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[2]/div/input")
forgor.click()
driver.get("https://comicstores.es/registro/formReiniciarClave.php?id=c17a03e90bea778f422c1f6c91df70b2e048c2ed9b67a9e284b6d1ccf59d1914")
password1 = driver.find_element_by_id("clave-registro")
password1.clear()
password1.send_keys("1234567890a!BDEGHY")
password2 = driver.find_element_by_id("clave-registro-repetida")
password2.clear()
password2.send_keys("1234567890a!BDEGHY")
time.sleep(5)
forgor2 = driver.find_element_by_xpath("/html/body/div[1]/div/form/div[3]/div/input")
forgor2.click()
time.sleep(5)