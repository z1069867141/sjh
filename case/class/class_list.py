import os
import sys
sys.path.append(os.getcwd())
from business.class_business.class_list_bussiness import class_list_b
from business.login_common_business import login_business
from selenium import webdriver
import unittest
import HTMLTestRunner
import time
from log.user_log import userlog

class class_list_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs=[]
        self.driver = webdriver.Chrome()
        self.base = login_business(self.driver)
        self.driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/pwdlogin?qythc=")
        self.base.user_base()
        time.sleep(1)
        self.driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/category")
        self.cl = class_list_b(self.driver)

    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_click_class_1(self):
        self.logger.info("this is test_click_class_1")
        result = self.cl.click_class_1()
        self.assertTrue(result,"test_click_class_1 run")

    def test_click_class_2(self):
        self.logger.info("this is test_click_class_2")
        result = self.cl.click_class_2()
        self.assertTrue(result,"test_click_class_2 run")

    def test_click_tabber(self):
        self.logger.info("this is test_click_tabber")
        result = self.cl.click_tabber()
        self.assertTrue(result,"test_click_tabber run")

if __name__ == "__main__":
    report_file_path = os.path.join(os.getcwd()+"/report/"+"login.html")
    f = open(report_file_path,"wb")
    # suit = unittest.main()
    """
    指定执行的test
    suit = unittest.TestSuite()
    suit.addTests(login_test("test_login_forward_process"))
    unittest.TextTestRunner().run(suit)
    """
    suit = unittest.TestSuite()
    suit.addTest(class_list_test("test_click_tabber"))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is login forward process",description="这个是我们第一次报告",verbosity=2)
    runner.run(suit)