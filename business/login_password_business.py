import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from handle.login_handle import Login_password_Handle
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class login_business(object):
    def __init__(self,driver):
        self.login_h = Login_password_Handle(driver)
    
    def user_base(self,phone_number,password):
        self.login_h.send_phone_number(phone_number)
        self.login_h.send_password_element(password)
        self.login_h.click_button()

    def login_forward_process(self,phone_number,password):
        self.user_base(phone_number,password)
        if self.login_h.get_login_button_text() == None:
            return True
        else:
            return False

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
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/pwdlogin?qythc=")
    login = login_business(driver)
    login.login_error("1","15011111111","Aa11111")