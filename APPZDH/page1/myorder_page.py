# -*- coding: utf-8 -*-
# @Time : 2020/12/20 2:04
# @Author : nichao
# @Email : 530504026@qq.com
# @File : myorder_page.py
# @Project : appAuto
from page.base_page import BasePage
from appium.webdriver.common.mobileby import By


class MyOrder(BasePage):
    # 待付款
    obligation_locator = (By.ID, 'com.meishio.app:id/twoTab')
    # 取消订单
    cancel_order_locator1 = (By.ID, 'com.meishio.app:id/listView_orders')
    cancel_order_locator2 = (By.ID, 'com.meishio.app:id/orders_item_cancel')
    finish_locator = (By.ID, 'com.meishio.app:id/order_cancel_sure')  # 完成
    # return_locator=(By.ID,'com.meishio.app:id/user_top_view_back')#我的订单返回按钮
    return_locator=(By.XPATH,'//android.widget.ImageView[@resource-id="com.meishio.app:id/user_top_view_back"]')


    def obligation_ele(self):
        """点击待付款"""
        self.find_element(self.obligation_locator).click()

    def cancel_order_ele(self):
        """点击取消订单"""
        self.find_element(self.cancel_order_locator2, self.find_element(self.cancel_order_locator1)).click()

    def cancelorder_finish_ele(self):
        """点击完成取消订单"""
        self.find_element(self.finish_locator).click()
    def confirm_cancel_ele(self):
        """取消待付款订单"""
        self.obligation_ele()
        self.cancel_order_ele()
        self.cancelorder_finish_ele()
    def return_my_ele(self):
        """取消订单后点击返回【我的】页面"""
        self.tap_function(62,136)
