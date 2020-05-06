import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from business.login_business import login_business
from selenium import webdriver
import unittest
import HTMLTestRunner
import time
from log.user_log import userlog

class login_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs=[]
        self.driver = webdriver.Chrome()
        self.driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/login")
        self.login = login_business(self.driver)

    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_login_forward_process(self):
        self.logger.info("this is test_login_forward_process")
        sucess = self.login.login_forward_process("15011111111")
        self.assertTrue(sucess,"test_login_forward_process run")

    # 正常登陆账号
    def test_login_phone_number_error(self):
        self.logger.info("this is test_login_phone_number_error")
        result = self.login.login_error("手机号不存在","15011111112","1234")
        self.assertTrue(result,"test_login_phone_number_error run")

    # 验证码错误
    def test_login_code_error(self):
        self.logger.info("this is test_login_phone_number_error")
        result = self.login.login_error("验证码有误！","15011111111","123")
        self.assertTrue(result,"test_login_phone_number_error run")

    # 手机号正确，验证码错误
    def test_login_phone_and_code_error(self):
        self.logger.info("this is test_login_phone_number_error")
        result = self.login.login_error("验证码有误！","15011111112","123")
        self.assertTrue(result,"test_login_phone_number_error run")

    # 输入不存在手机号，验证码输入正确
    def test_login_phone_error(self):
        self.logger.info("this is test_login_phone_number_error")
        result = self.login.login_error("验证码有误！","15011111112","123")
        self.assertTrue(result,"test_login_phone_number_error run")
    

if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/login")
    # login = login_test(driver)
    # login.login_forward_process("16011111111","1234")
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
    suit.addTest(login_test("test_login_forward_process"))
    # suit.addTest(login_test("test_login_code_error"))
    #unittest.TextTestRunner().run(suit)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is login forward process",description="这个是我们第一次报告",verbosity=2)
    runner.run(suit)