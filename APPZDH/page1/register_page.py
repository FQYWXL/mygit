# -*- coding: utf-8 -*-
# @Time : 2020/12/19 21:56
# @Author : nichao
# @Email : 530504026@qq.com
# @File : register_page.py
# @Project : appAuto
from page.base_page import BasePage
from appium.webdriver.common.mobileby import By


class Register(BasePage):
    word_text_locator = (By.XPATH, '//android.widget.TextView[@resource-id="com.meishio.app:id/pay_title"]')

    def order_assert(self):
        return self.find_element(self.word_text_locator).text
