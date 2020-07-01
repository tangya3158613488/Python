__author__ = '320S-15'
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://192.168.0.104:8080/login.html")
time.sleep(5)
driver.find_element_by_id("name").send_keys("zhangsan")
time.sleep(3)
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("password").send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()

