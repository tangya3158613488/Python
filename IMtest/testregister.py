__author__ = '320S-15'
# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://192.168.0.104:8080/register.html")
driver.find_element_by_link_text("register").click()
driver.find_element_by_id("Name").send_keys("yangmi")
driver.find_element_by_id("rPassword").send_keys("123456")
driver.find_element_by_id("rrPassword").send_keys("123456")
driver.find_element_by_id("rrPassword").send_keys(Keys.ENTER)
time.sleep(4)

driver.find_element_by_id("name").send_keys("yangmi")
time.sleep(3)
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("password").send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()