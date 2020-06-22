__author__ = '320S-15'
# -*- coding: utf-8 -*-
import unittest
import time
import testbaidu1
import testbaidu2
#手工添加案例到套件，
def createsuite():
    # suite = unittest.TestSuite()
    # #将测试用例加入到测试容器（套件）中
    # suite.addTest(unittest.makeSuite(testbaidu1.Baidu1))
    # suite.addTest(unittest.makeSuite(testbaidu2.Baidu2))
    # return suite

     suite1 = unittest.TestLoader().loadTestsFromTestCase(testbaidu1.Baidu1)
     suite2 = unittest.TestLoader().loadTestsFromTestCase(testbaidu2.Baidu2)
     suite = unittest.TestSuite([suite1, suite2])
     return suite

if __name__=="__main__":
     suite = createsuite()
     runner = unittest.TextTestRunner(verbosity=2)
     runner.run(suite)
