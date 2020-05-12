import os
import sys
sys.path.append(os.getcwd())
from handle.home_page_handle import Home_page
from selenium import webdriver
import time
import pymysql
from mysql.mysql_function import mysql_function

class home_page(object):
    def __init__(self,driver):
        self.home_page = Home_page(driver)

    def click_button(self,click_button,title_name):
        """
        click_button:brand_story
                     sharing_rule
                     business_academy
                     sleep_channel
                     product_world
                     cant_test
                     switch_class
                     title_name
        title_name:品牌故事，分享规则，商学院，享睡频道，产品世界，暂未开放（暂时无法点击，使用现有其他功能）, 类 型
        """
        self.home_page.click_button(click_button)
        return self.check_title_name(title_name)

    def check_title_name(self,title_name):
        """
        title_name include title and tabber's title
        """
        if self.home_page.get_title_name() == title_name:
            print("True")
            return True
        else:
            return False

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/home")
    a = home_page(driver)
    a.click_button("sharing_rule","分享规则")

    # from selenium import webdriver
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC

    # driver = webdriver.Firefox()
    # driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/article?aId=11")
    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "van-ellipsis"))
    #     )
    #     a=element.text
    #     print(a)
    # finally:
    #     driver.quit()