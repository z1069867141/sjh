import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
import handle.login_handle as login_handle
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class login_business(object):
    def __init__(self,driver):
        self.login_h = login_handle.LoginSMSHandle(driver)
    
    def user_base(self,phone_number,phone_code):
        self.login_h.send_phone_number(phone_number)
        self.login_h.send_phone_code_element(phone_code)
        self.login_h.click_button()

    def login_forward_process(self,phone_number):
        self.login_h.send_phone_number(phone_number)
        self.login_h.get_phone_code()
        mysql = mysql_function()
        phone_code = mysql.search_sms_log(phone_number)
        self.login_h.send_phone_code_element(phone_code)
        self.login_h.click_button()
        time.sleep(2)
        if self.login_h.get_login_button_text() == None:
            return True
        else:
            return False

    def login_switch_sms_to_password(self):
        self.login_h.click_switch_password()
        if self.login_h.click_switch_password_text == None:
            return False
        else:
            return True

    def click_button(self,error_message):
        self.login_h.click_button()
        if self.login_h.get_error_message() == error_message:
            return True
        else:
            return False

    def login_error(self,error_message,phone_number,phone_code):
        self.user_base(phone_number,phone_code)
        if self.login_h.get_error_message() == error_message:
            return True
        else:
            return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/login")
    login = login_business(driver)
    login.login_error("验证码有误！","15011111111","123")