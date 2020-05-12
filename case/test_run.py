import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from case.login.login_code import login_c_test
from case.login.login_password import login_pw_test
from case.login.login_Retrieve_password import login_Retriveve_test
from case.home_page import login_c_test
import HTMLTestRunner

report_file_path = os.path.join(os.getcwd()+"/report/"+"login.html")
f = open(report_file_path,"wb")
case_01 = unittest.TestLoader().loadTestsFromTestCase(login_c_test)
case_02 = unittest.TestLoader().loadTestsFromTestCase(login_pw_test)
case_03 = unittest.TestLoader().loadTestsFromTestCase(login_Retriveve_test)
case_04 = unittest.TestLoader().loadTestsFromTestCase(login_c_test)
# suote = unittest.TestSuite([case_01,case_02,case_03,case_04])  # 添加到套件里面
suote = unittest.TestSuite([case_04])
# unittest.TextTestRunner().run(suote)  # 执行所有的
runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is login forward process",description="这个是我们第一次报告",verbosity=2)
runner.run(suote)