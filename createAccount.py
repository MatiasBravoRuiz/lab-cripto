import time
import string
import random
PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(PATH)
driver.get("https://konohastore.cl/my-account/")
time.sleep(5)
user = driver.find_element_by_id("reg_username")
user.clear()
user.send_keys("disom31955")
email = driver.find_element_by_id("reg_email")
email.clear()
email.send_keys("disom31955@mxgsby.com")
password = driver.find_element_by_id("reg_password")
password.clear()
password.send_keys("1234567890a!BDEGHY")
register = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div/main/article/div/div/div[2]/div[2]/form/p[4]/button")
register.click()