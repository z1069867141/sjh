import sys
import os
import configparser

class ReadIni(object):
    def __init__(self,file_path=None,node=None):
        if file_path == None:
            sys.path.append(os.path.join(os.path.dirname(__file__),".."))
            self.file_path = ".\\config\\login_element.ini"
            #C:\\Users\\Akien\\Desktop\\项目\\丝柔菲\\AT\\config\\local_element.ini
        else:
            self.file_path = file_path
        if node == None:
            self.node = "LogSMSElement"
        else:
            self.node = node
        self.cf = self.load_ini(self.file_path)

    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data

if __name__ == "__main__":
    read_ini = ReadIni(node="LogPasswordElement")
    print(read_ini.get_value("error_message"))