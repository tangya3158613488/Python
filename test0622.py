__author__ = '320S-15'
#coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
######################�ٶ������Ķ�λ��ʽ#################
#ͨ��id��λ
driver.find_element_by_id("kw").send_keys("selenium")
#ͨ��name��λ
driver.find_element_by_name("wd").send_keys(u"CSDN����") #u��ʾ��utf-8�ĸ�ʽ����
#ͨ��tag name��λ
driver.find_element_by_tag_name("input").send_keys("Python")
#ͨ��class name��λ
driver.find_element_by_class_name("s_ipt").send_keys("Java")
#ͨ��CSS��λ
driver.find_element_by_css_selector("#kw").send_keys("C++")
#ͨ��xpath��λ
driver.find_element_by_xpath("//*[@id=kw]").send_keys(u"C����")
#ͨ��link test��λ
driver.find_element_by_link_text("hao123").click()
#ͨ��partial link test��λ
driver.find_element_by_partial_link_text("hao").click()
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()


