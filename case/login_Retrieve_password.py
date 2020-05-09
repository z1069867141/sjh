import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from business.login_Retrieve_password_business import login_business
from selenium import webdriver
import unittest
import HTMLTestRunner
import time
from log.user_log import userlog

class login_Retriveve_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = userlog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.imgs=[]
        self.driver = webdriver.Chrome()
        self.driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/changepwd")
        self.login = login_business(self.driver)

    # 找回密码界面需要等待60s时间再一次获取验证码
    def tearDown(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        time.sleep(60)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_login_forward_process(self):
        self.logger.info("this is test_login_forward_process")
        sucess = self.login.login_forward_process("15011111111","Aa111111","Aa111111")
        self.assertTrue(sucess,"test_login_forward_process run")

    # 手机号不输入获取验证码
    def test_donot_send_phone_get_verification(self):
        self.logger.info("this is test_donot_send_phone_get_verification")
        result = self.login.donot_send_phone_get_verification("手机号不能为空")
        self.assertTrue(result,"test_login_forward_process run")

    # 输入错误验证码
    def test_send_error_verification(self):
        self.logger.info("this is test_send_error_verification")
        result = self.login.verification_error_message("验证码不存在或已过期","15011111111","156","123456","123456")
        self.assertTrue(result,"test_send_error_verification run")

    # 输入不符合规格的密码
    def test_no_send_click_button(self):
        self.logger.info("this is test_no_send_click_button")
        result = self.login.verification_error_message("请输入6位或以上密码","15011111111","on","1","1")
        self.assertTrue(result,"test_no_send_click_button run")

    # 输入错误的重复密码
    def test_login_code_error(self):
        self.logger.info("this is test_login_phone_number_error")
        result = self.login.verification_error_message("两次输入的密码不一致","15011111111","on","111111","11111")
        self.assertTrue(result,"test_login_phone_number_error run")

    # 不输入新密码和重复输入密码
    def do_not_send_password_and_confirm_password(self):
        self.logger.info("this is do_not_send_password_and_confirm_password")
        result = self.login.verification_error_message("请输入新密码","15011111111","on","","")
        self.assertTrue(result,"do_not_send_password_and_confirm_password run")

    # 输入密码不输入重复密码
    def do_not_send_confirm_password(self):
        self.logger.info("this is do_not_send_confirm_password")
        result = self.login.verification_error_message("两次输入的密码不一致","15011111111","on","111111","")
        self.assertTrue(result,"do_not_send_password_and_confirm_password run")

    # 点击返回登录
    def test_return_password_mod(self):
        self.logger.info("this is test_return_password_mod")
        result = self.login.click_return_password_mode_button()
        self.assertTrue(result,"test_return_password_mod run")

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
    suit.addTest(login_Retriveve_test("test_return_password_mod"))
    # suit.addTest(login_test("test_login_code_error"))
    #unittest.TextTestRunner().run(suit)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is login forward process",description="这个是我们第一次报告",verbosity=2)
    runner.run(suit)