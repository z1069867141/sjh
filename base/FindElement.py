import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from reading_mode.read_ini import ReadIni
from selenium import webdriver

class FindElement(object):
    def __init__(self, driver,file_path=None,node=None):
        self.driver = driver
        self.file_path = file_path
        self.node = node

    def get_element(self, key):
        read_ini = ReadIni(self.file_path,self.node)
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
            elif by == "tag_name":
                return self.driver.find_element_by_tag_name(value)
        except:
            return None

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/login")
    element_a = FindElement(driver)
    print(element_a.get_element("login_button").text)



# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__),".."))
# from reading_mode.read_ini import ReadIni
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class FindElement(object):
#     def __init__(self, driver,file_path=None,node=None):
#         self.driver = driver
#         self.file_path = file_path
#         self.node = node

#     def get_element(self, key):
#         read_ini = ReadIni(self.file_path,self.node)
#         data = read_ini.get_value(key)
#         data_list = data.split(">")
#         by = data_list[0]
#         value = data_list[1]
#         if by == "classnames":
#             No = int(data_list[2])
#         try:
#             if by == "id":
#                 return self.driver.find_element_by_id(value)
#             elif by == "name":
#                 return self.driver.find_element_by_name(value)
#             elif by == "classname":
#                 element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "van-ellipsis")))
#                 a= element.text
#                 print(a)
#                 return element
#             elif by == "classnames":
#                 return self.driver.find_elements_by_class_name(value)[No]
#             elif by == "xpath":
#                 return self.driver.find_element_by_xpath(value)
#             elif by == "tag_name":
#                 return self.driver.find_element_by_tag_name(value)
#         except:
#             return None

# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     driver.get("http://b2bsaas.qianyansoft.com/Sjh/#/article?aId=11")
#     file_path = os.path.join(os.getcwd()+"/config/"+"home_page_element.ini")
#     a = FindElement(driver,file_path=file_path,node="home_page")
#     a.get_element("title_name")