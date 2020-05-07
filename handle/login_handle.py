import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from base.FindElement import FindElement
from selenium import webdriver
import time

class LoginHandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.Login = FindElement(self.driver)

    # 输入手机号
    def send_phone_number(self,phone_number):
        self.Login.get_element("phone_number").send_keys(phone_number)

    # 获取验证码
    def get_phone_code(self):
        self.Login.get_element("get_code").click()

    # 输入验证码
    def send_phone_code_element(self,code):
        self.Login.get_element("Verification_code").send_keys(code)
    
    # 点击登录
    def click_button(self):
        self.Login.get_element("login_button").click()

    # 获取错误信息
    def get_error_message(self):
        time.sleep(2)
        message = self.Login.get_element("error_message").text
        return message
    
    # 获取登录按钮文本
    def get_login_button_text(self):
        try:
            text = self.Login.get_element("login_button").text
            return text
        except:
            return None

    # 切换密码登录
    def click_switch_password(self):
        self.Login.get_element("get_password_mode").click()

    # 获取密码登录文案
    def click_switch_password_text(self):
        try:
            text = self.Login.get_element("get_password_mode").text
            return text
        except:
            return None
            
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/login")
    element_a = LoginHandle(driver)
    element_a.send_phone_number("15011111111")
    element_a.send_phone_code_element("1235")
    element_a.click_button()
    print(element_a.get_error_message())