import os
import sys
sys.path.append(os.getcwd())
from handle.class_list_handle import class_list
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class class_list_b(object):
    def __init__(self,driver):
        self.cl_b = class_list(driver)

    def click_class_1(self):
        self.cl_b.click_class_1()
        return self.cl_b.get_sorting_text()

    def click_class_2(self):
        self.cl_b.click_class_2()
        return self.cl_b.get_sorting_text()

    def click_tabber(self):
        return self.cl_b.click_QR_tabber()