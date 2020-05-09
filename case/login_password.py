import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from business.login_password_business import login_business
from selenium import webdriver
import unittest
import HTMLTestRunner
import time
from log.user_log import userlog

class login_pw_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs=[]
        self.driver = webdriver.Chrome()
        self.driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/pwdlogin?qythc=")
        self.login = login_business(self.driver)

    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_login_forward_process(self):
        self.logger.info("this is test_login_forward_process")
        sucess = self.login.login_forward_process("15011111111","Aa111111")
        self.assertTrue(sucess,"test_login_forward_process run")

    # 切换到了验证码登陆界面
    def test_switch_code_mode(self):
        self.logger.info("this is test_switch_code_mode")
        result = self.login.click_code_mode_button()
        self.assertTrue(result,"test_switch_code_mode run")

    # 切换到找回密码界面
    def test_switch_retrieve_the_password_mode(self):
        self.logger.info("this is test_switch_retrieve_the_password_mode")
        result = self.login.click_retrieve_the_password_button()
        self.assertTrue(result,"test_switch_retrieve_the_password_mode run")


    def test_no_send_click_button(self):
        self.logger.info("this is test_no_send_click_button")
        result = self.login.click_button("账号或密码不存在")
        self.assertTrue(result,"test_no_send_click_button run")

    # 手机号正确密码错误
    def test_login_code_error(self):
        self.logger.info("this is test_login_phone_number_error")
        result = self.login.login_error("账号或密码不存在","15011111111","123")
        self.assertTrue(result,"test_login_phone_number_error run")

    # 手机号号错误，密码正确
    def test_login_phone_and_code_error(self):
        self.logger.info("this is test_login_phone_number_error")
        result = self.login.login_error("账号或密码不存在","15011111112","Aa111111")
        self.assertTrue(result,"test_login_phone_number_error run")

if __name__ == "__main__":
    report_file_path = os.path.join(os.getcwd()+"/report/"+"login.html")
    f = open(report_file_path,"wb")
    # unittest.main()
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
    suit.addTest(login_pw_test("test_no_send_click_button"))
    # suit.addTest(login_test("test_login_code_error"))
    #unittest.TextTestRunner().run(suit)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is login forward process",description="这个是我们第一次报告",verbosity=2)
    runner.run(suit)