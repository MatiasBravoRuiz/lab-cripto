import time
import string
import random
PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(PATH)
driver.get("https://konohastore.cl/my-account/")
time.sleep(5)
user = driver.find_element_by_id("username")
user.clear()
user.send_keys("disom31955")
password = driver.find_element_by_id("password")
password.clear()
password.send_keys("1234567890a!BDEGHY")
register = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div/main/article/div/div/div[2]/div[1]/form/p[3]/button")
register.click()
clk = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div/main/article/div/div/nav/ul/li[5]/a")
clk.click()
password = driver.find_element_by_id("password_current")
password.clear()
password.send_keys("1234567890a!BDEGHY")
password = driver.find_element_by_id("password_1")
password.clear()
password.send_keys("1234567890a!BDEGH")
password = driver.find_element_by_id("password_2")
password.clear()
password.send_keys("1234567890a!BDEGH")
clk2 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div/main/article/div/div/div/form/p[5]/button")
clk2.click()
