# -*- coding: utf-8 -*-
# @Time : 2020/12/21 18:06
# @Author : yanlong
# @Email : tangli@tmail.com
# @File : test_xxx.py
# @Project : APPZDH
import unittest

from model.browser import open_app
from page.App_login import Login


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=open_app()

    def test_2login(self):
        lg=Login(self.driver)
        lg.login("lisa","admin123")
if __name__ == '__main__':
    unittest.main()