__author__ = '320S-15'
#coding=utf-8
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("D:\\Users\\320S-15\\seleniumTestHTML\\drop_down.html")
driver.get(file_path)
driver.maximize_window()
WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id("ShippingMethod"))
#通过xpath定位
ship = driver.find_element_by_id("ShippingMethod")
ship.find_element_by_xpath("//option[@value='10.69']").click()
lists = driver.find_elements_by_tag_name("option")
#根据属性定位
# for list in lists:
#     if list.get_attribute('value') == "10.69":
#        list.click()
#利用数组下标定位
#lists[2].click()

time.sleep(8)
driver.quit()