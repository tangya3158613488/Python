__author__ = '320S-15'
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('D:\\Users\\320S-15\\seleniumTestHTML\\alert.html')
dr.get(file_path)
# 点击链接弹出alert
dr.find_element_by_id('tooltip').click()
sleep(2)
alert = dr.switch_to_aler
alert.accept()
sleep(2)
dr.quit()