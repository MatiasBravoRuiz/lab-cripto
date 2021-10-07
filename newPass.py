import time
import string
import random
PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(PATH)
driver.get("https://konohastore.cl/my-account/lost-password/")
time.sleep(5)
user = driver.find_element_by_id("user_login")
user.clear()
user.send_keys("disom31955@mxgsby.com")
forgor = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div/main/article/div/div/form/p[3]/button")
forgor.click()
driver.get("https://konohastore.cl/my-account/lost-password/?key=getNFyAF9s6H43dgwnul&id=1375")
password1 = driver.find_element_by_id("password_1")
password1.clear()
password1.send_keys("1234567890a!BDEGHY")
password2 = driver.find_element_by_id("passord_2")
password2.clear()
password2.send_keys("1234567890a!BDEGHY")
time.sleep(5)
forgor2 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div/main/article/div/div/form/p[4]/button")
forgor2.click()
time.sleep(5)