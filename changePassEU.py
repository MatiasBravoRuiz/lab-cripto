import time
import string
import random
PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(PATH)
driver.get("https://comicstores.es/registro/autenticacion.php")
time.sleep(5)
user = driver.find_element_by_id("email")
user.clear()
user.send_keys("disom31955@mxgsby.com")
password = driver.find_element_by_id("clave")
password.clear()
password.send_keys("1234567890a!BDEGHY")
register = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/form/div[3]/input")
time.sleep(5)
register.click()
driver.get("https://comicstores.es/registro/formCambiarClave.php")
password = driver.find_element_by_id("clave")
password.clear()
password.send_keys("1234567890aBDEGH")
password = driver.find_element_by_id("claveNueva")
password.clear()
password.send_keys("1234567890aBDEGHy")
password = driver.find_element_by_id("claveRepetida")
password.clear()
password.send_keys("1234567890aBDEGHy")
time.sleep(5)
clk2 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/div[4]/div[2]/input")
clk2.click()