import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from base.FindElement import FindElement
from selenium import webdriver
import time

class class_list(object):
    def __init__(self,driver):
        self.driver = driver
        self.file_path = os.path.join(os.getcwd()+"/config/"+"class_element.ini")
        self.cl = FindElement(self.driver,file_path=self.file_path,node="class_list")

    def click_class_1(self):
        self.cl.get_element("class_1").click()

    def click_class_2(self):
        self.cl.get_element("class_2").click()

    def get_sorting_text(self):
        try:
            time.sleep(2)
            text = self.cl.get_element("sorting_text").text
            if text == "综合排序":
                return True
            else:
                return False
        except:
            return False

    def click_QR_tabber(self):
        try:
            self.cl.get_element("QR_code").click()
            time.sleep(2)
            text = self.cl.get_element("title_text").text
            if text == "分 享":
                return True
            else:
                return False
        except:
            return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    base = login_business(driver)
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/pwdlogin?qythc=")
    base.user_base()
    time.sleep(1)
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/category")
    a = class_list(driver)
    # time.sleep(2)
    a.click_QR_tabber()