__author__ = '320S-15'
#coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
######################百度输入框的定位方式#################
#通过id定位
driver.find_element_by_id("kw").send_keys("selenium")
#通过name定位
driver.find_element_by_name("wd").send_keys(u"CSDN博客") #u表示以utf-8的格式输入
#通过tag name定位
driver.find_element_by_tag_name("input").send_keys("Python")
#通过class name定位
driver.find_element_by_class_name("s_ipt").send_keys("Java")
#通过CSS定位
driver.find_element_by_css_selector("#kw").send_keys("C++")
#通过xpath定位
driver.find_element_by_xpath("//*[@id=kw]").send_keys(u"C语言")
#通过link test定位
driver.find_element_by_link_text("hao123").click()
#通过partial link test定位
driver.find_element_by_partial_link_text("hao").click()
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()


