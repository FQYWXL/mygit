# -*- coding: utf-8 -*-
# @Time : 2020/12/19 16:54
# @Author : nichao
# @Email : 530504026@qq.com
# @File : personal_page.py
# @Project : appAuto
from page.base_page import BasePage
from appium.webdriver.common.mobileby import By


class Personal(BasePage):
    lusername_locator = (By.ID, 'com.meishio.app:id/user_login_username_email_phone')
    lpassword_locator = (By.ID, 'com.meishio.app:id/user_login_password')
    lsubmit_locator = (By.ID, 'com.meishio.app:id/user_login_btn')
    # 登录
    loginbutton_locator = (By.ID, 'com.meishio.app:id/user_name')
    # 我的订单
    myorder_locator = (By.ID, 'com.meishio.app:id/myorder_title')
    setup_locator = (By.ID, 'com.meishio.app:id/user_photo_setting')  # 设置
    obligation_number_locator = (By.ID, 'com.meishio.app:id/paid_num')  # 待付款的订单的数值

    def lusername_ele(self, username):
        """输入用户名"""
        self.find_element(self.lusername_locator).send_keys(username)

    def lpassword_ele(self, password):
        """输入密码"""
        self.find_element(self.lpassword_locator).send_keys(password)

    def lsubmit_ele(self):
        """点击【登录】"""
        self.find_element(self.lsubmit_locator).click()

    def plogin(self, username, password):
        """登录"""
        self.lusername_ele(username)
        self.lpassword_ele(password)
        self.lsubmit_ele()

    def loginbutton_ele(self):
        """点击【我的】页面【登录】按钮"""
        self.find_element(self.loginbutton_locator).click()

    def myorder_button_ele(self):
        """点击我的订单"""
        self.find_element(self.myorder_locator).click()

    def setup_ele(self):
        """点击设置按钮"""
        self.find_element(self.setup_locator).click()

    def obligation_number_assert1(self):
        """获取取消前的待付款订单的数量"""
        return self.find_element(self.obligation_number_locator).text

    def obligation_number_assert2(self):
        """获取取消后的待付款订单的数量"""
        return str(int(self.find_element(self.obligation_number_locator).text) + 1)
