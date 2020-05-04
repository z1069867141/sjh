import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from handle.login_handle import LoginHandle
from selenium import webdriver
import time

class login_business(object):
    def __init__(self,driver):
        self.login_h = LoginHandle(driver)
    
    def user_base(self,phone_number,phone_code):
        self.login_h.send_phone_number(phone_number)
        self.login_h.send_phone_code_element(phone_code)
        self.login_h.click_button()

    def login_forward_process(self,phone_number,phone_code):
        self.user_base(phone_number,phone_code)
        time.sleep(2)
        if self.login_h.get_login_button_text() == None:
            print("成功")
            return True
        else:
            print("失败")
            return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/login")
    login = login_business(driver)
    login.login_forward_process("15011111111","1234")