import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from base.FindElement import FindElement
from selenium import webdriver
import time

class Home_page(object):
    def __init__(self,driver):
        self.driver = driver
        self.file_path = os.path.join(os.getcwd()+"/config/"+"home_page_element.ini")
        self.home_page = FindElement(self.driver,file_path=self.file_path,node="home_page")

    def click_button(self,button):
        if button == "brand_story":
            self.click_brand_story()
        elif button == "sharing_rule":
            self.click_sharing_rule()
        elif button == "business_academy":
            self.click_business_academy()
        elif button == "sleep_channel":
            self.click_sleep_channel()
        elif button == "product_world":
            self.click_product_world()
        elif button == "cant_test":
            self.click_cant_test()
        elif button == "switch_class":
            self.click_switch_class()

    def click_brand_story(self):
        self.home_page.get_element("brand_story").click()

    def click_sharing_rule(self):
        self.home_page.get_element("sharing_rule").click()

    def click_business_academy(self):
        self.home_page.get_element("business_academy").click()

    def click_sleep_channel(self):
        self.home_page.get_element("sleep_channel").click()

    def click_product_world(self):
        self.home_page.get_element("product_world").click()

    def click_cant_test(self):
        self.home_page.get_element("cant_test").click()

    def click_switch_class(self):
        self.home_page.get_element("switch_class").click()

    def get_title_name(self):
        try:
            time.sleep(2)
            text = self.home_page.get_element("title_name").text
            print(text)
            return text
        except:
            return None


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/article?aId=11")
    a = Home_page(driver)
    # time.sleep(2)
    a.get_title_name()

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
#     print(element.text)
# finally:
#     driver.quit()