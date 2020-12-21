# -*- coding: utf-8 -*-
# @Time : 2020/12/20 3:08
# @Author : nichao
# @Email : 530504026@qq.com
# @File : setup_page.py
# @Project : appAuto
from page.base_page import BasePage
from appium.webdriver.common.mobileby import By
class SetUp(BasePage):
    quit_locator = (By.ID, 'com.meishio.app:id/user_exit_btn')  # 退出登录
    def setup_login(self):
        self.find_element(self.quit_locator).click()