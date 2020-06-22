__author__ = '320S-15'
#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os,sys,csv
from ddt import ddt, data, unpack ,file_data
def getCsv(file_name):
     rows=[]
     path=sys.path[0].replace('\test','')
     print(path)
     with open(path+'/data/'+file_name,'rb') as f:
         readers=csv.reader(f,delimiter=',',quotechar='|')
         next(readers,None)
         for row in readers:
            temprows=[]
            for i in row:
                temprows.append(i.decode('gbk'))
            rows.append(temprows)
         return rows
#引入ddt
@ddt
class Testddt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    @data(*getCsv('test_baidu_data.csv'))
    #@file_data('test_baidu_data.json')
    @unpack
    #@data(u"王俊凯",u"宋祖儿",u"陈哲远")
    def test_hao(self,value,expected_value):
        #def test_hao(self,value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(2)
        print(value)
        # self.assertEqual(expected_value, driver.title)
        # print expected_value
        print driver.title
        #判断element是否存在，可删除
    def is_element_present(self, how, what):
         try: self.driver.find_element(by=how, value=what)
         except NoSuchElementException as e: return False
         return True
         #判断alert是否存在，可删除
    def is_alert_present(self):
        try: self.driver.switch_to.alert
        except NoAlertPresentException as e:return False
        return True
    #关闭alert，可删除
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    #test fixture，清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    def savescreenshot(self,driver,file_name):
        if not os.path.exists('./image'):
            os.makedirs('./image')
            now=time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
            #截图保存
            driver.get_screenshot_as_file('./image/'+now+'-'+file_name)
            time.sleep(1)
if __name__ == "__main__":
#执行用例
    unittest.main(verbosity=2)

