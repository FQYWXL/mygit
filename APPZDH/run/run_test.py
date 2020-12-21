import unittest   #引入自动化测试框架
import time      #引入时间模块
from BeautifulReport import BeautifulReport  #引入自动化测试报告模板
suite=unittest.defaultTestLoader.discover("../cases","case*.py")  #
now=time.strftime("%Y%m%d%H%M%S")
filename="crm-report-{}.html".format(now)
runner=BeautifulReport(suite)
runner.report(description="登录用例",
              filename=filename,
              report_dir="../report")

