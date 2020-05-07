import unittest
import os
from login_code import login_test
import HTMLTestRunner

report_file_path = os.path.join(os.getcwd()+"/report/"+"login.html")
f = open(report_file_path,"wb")
case_01 = unittest.TestLoader().loadTestsFromTestCase(login_test)
suote = unittest.TestSuite([case_01])  # 添加到套件里面
# unittest.TextTestRunner().run(suote)  # 执行所有的
runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is login forward process",description="这个是我们第一次报告",verbosity=2)
runner.run(suote)