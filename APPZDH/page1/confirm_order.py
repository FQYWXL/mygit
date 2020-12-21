# -*- coding: utf-8 -*-
# @Time : 2020/12/19 19:45
# @Author : nichao
# @Email : 530504026@qq.com
# @File : confirm_order.py
# @Project : appAuto
from page.base_page import BasePage
from appium.webdriver.common.mobileby import By


class ConfirmOrder(BasePage):
    shippingconfirm_locator = (By.ID, 'com.meishio.app:id/shipping_item_check')  # 选择中通
    submit_locator = (By.ID, 'com.meishio.app:id/order_confirm_submit')#提交订单
    def shippingmethod(self):
        """点击选择配送方式"""
        self.tap_function(843,860)
    def shippingconfirm_ele(self):
        """选择中通配送方式"""
        self.find_element(self.shippingconfirm_locator).click()

    def submit_order_ele(self):
        """点击【提交订单】"""
        self.find_element(self.submit_locator).click()

    def confirmorder(self):
        """"选择配送方式，提交订单"""
        self.tap_function(843, 860)
        self.shippingconfirm_ele()
        self.submit_order_ele()
