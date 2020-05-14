import os
import sys
sys.path.append(os.getcwd())
from handle.login_handle import Login_password_Handle
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class login_business(object):
    def __init__(self,driver):
        self.login_h = Login_password_Handle(driver)
    
    def user_base(self):
        try:
            self.login_h.send_phone_number("15011111111")
            self.login_h.send_password_element("Aa111111")
            self.login_h.click_button()
            return True
        except:
            return False