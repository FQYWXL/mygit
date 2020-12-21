# -*- coding: utf-8 -*-
# @Time : 2020/12/19 18:58
# @Author : nichao
# @Email : 530504026@qq.com
# @File : app_detailshop.py
# @Project : appAuto
from page.base_page import BasePage
from appium.webdriver.common.mobileby import By


class AppDetialshop(BasePage):
    detail_buy_locator = (By.ID, 'com.meishio.app:id/goods_detail_buy')  # 立即购买
    confirm_buy_locator = (By.ID, 'com.meishio.app:id/product_properties_done')  # 确认购买

    def shopcart_ele(self):
        """点击【加入购物车】"""
        self.tap_function(430, 1853)

    def detail_buy_ele(self):
        """点击立即购买"""
        self.find_element(self.detail_buy_locator).click()

    def confirm_buy_ele(self):
        """点击确定"""
        self.find_element(self.confirm_buy_locator).click()

    def appdetialshop_ele(self):
        self.detail_buy_ele()
        self.confirm_buy_ele()
