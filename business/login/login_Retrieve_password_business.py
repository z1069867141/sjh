import os
import sys
sys.path.append(os.getcwd())
from handle.login_handle import Login_retireve_password_Handle
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class login_business(object):
    def __init__(self,driver):
        self.login_h = Login_retireve_password_Handle(driver)

    def get_verification(self,phone_number):
        mysql = mysql_function()
        phone_code = mysql.search_sms_log(phone_number)
        return phone_code
    
    def user_base(self,phone_number,verification_code,password,confirm_password):
        """
        verification:
            on：获取验证码，
            off:直接跳过验证码
            其他情况:输入验证码
        """
        self.login_h.send_phone_number(phone_number)
        if verification_code == "on":
            self.login_h.click_get_verification_code()
            phone_code = self.get_verification(phone_number)
            self.login_h.send_phone_code(phone_code)
        elif verification_code == "off":
            pass
        else:
            self.login_h.send_phone_code(verification_code)
        self.login_h.send_password(password)
        self.login_h.send_password_confirm(confirm_password)
        self.login_h.click_button()

    def login_forward_process(self,phone_number,password,confirm_password):
        self.user_base(phone_number,"on",password,confirm_password)
        if self.login_h.get_return_password_button_text() == None:
            return True
        else:
            return False

    def donot_send_phone_get_verification(self,error_massage):
        self.login_h.click_get_verification_code()
        if self.login_h.get_error_message()==error_massage:
            return True
        else:
            return False
    
    def verification_error_message(self,error_massage,phone,verification,password,confirm_password):
        self.user_base(phone,verification,password,confirm_password)
        if self.login_h.get_error_message()==error_massage:
            return True
        else:
            return False

    def click_return_password_mode_button(self):
        self.login_h.click_return_password_mode()
        if self.login_h.get_return_password_button_text() == None:
            return True
        else:
            return False
        

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/pwdlogin?qythc=")
    login = login_business(driver)
    login.login_error("1","15011111111","Aa11111")