import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from reading_mode.read_ini import ReadIni
from selenium import webdriver

class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key, node=None):
        read_ini = ReadIni(node)
        data = read_ini.get_value(key)
        data_list = data.split(">")
        by = data_list[0]
        value = data_list[1]
        if by == "classnames":
            No = int(data_list[2])
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "classname":
                return self.driver.find_element_by_class_name(value)
            elif by == "classnames":
                return self.driver.find_elements_by_class_name(value)[No]
            elif by == "xpath":
                return self.driver.find_element_by_xpath(value)
        except:
            return None

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/login")
    element_a = FindElement(driver)
    print(element_a.get_element("login_button").text)