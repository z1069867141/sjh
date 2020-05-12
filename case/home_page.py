import os
import sys
sys.path.append(os.getcwd())
from business.home_page_business import home_page
from selenium import webdriver
import unittest
import HTMLTestRunner
import time
from log.user_log import userlog

class login_c_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs=[]
        self.driver = webdriver.Chrome()
        self.driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/home")
        self.hp = home_page(self.driver)

    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_brand_story(self):
        self.logger.info("this is test_brand_story")
        result = self.hp.click_button("brand_story","品牌故事")
        self.assertTrue(result,"test_brand_story run")

    def test_sharing_rule(self):
        self.logger.info("this is test_sharing_rule")
        result = self.hp.click_button("sharing_rule","分享规则")
        self.assertTrue(result,"test_sharing_rule run")

    def test_business_academy(self):
        self.logger.info("this is test_business_academy")
        result = self.hp.click_button("business_academy","商学院")
        self.assertTrue(result,"test_business_academy run")

    def test_sleep_channel(self):
        self.logger.info("this is test_sleep_channel")
        result = self.hp.click_button("sleep_channel","享睡频道")
        self.assertTrue(result,"test_sleep_channel run")

    def test_product_world(self):
        self.logger.info("this is test_product_world")
        result = self.hp.click_button("product_world","产品世界")
        self.assertTrue(result,"test_product_world run")

    def test_switch_class(self):
        self.logger.info("this is test_switch_class")
        result = self.hp.click_button("switch_class","分 类")
        self.assertTrue(result,"test_switch_class run")

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
    # suit.addTests(login_test("test_login_forward_process"))
    # suit.addTest(login_test("test_login_switch_sms_to_password"))
    # suit.addTest(login_test("test_login_switch_sms_to_password"))
    # suit.addTest(login_test("test_login_switch_sms_to_password"))
    suit.addTest(login_c_test("test_product_world"))
    # suit.addTest(login_test("test_login_code_error"))
    #unittest.TextTestRunner().run(suit)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is login forward process",description="这个是我们第一次报告",verbosity=2)
    runner.run(suit)