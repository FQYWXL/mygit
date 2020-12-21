# -*- coding: utf-8 -*-
# @Time : 2020/12/19 16:51
# @Author : nichao
# @Email : 530504026@qq.com
# @File : home_page.py
# @Project : appAuto
from appium.webdriver.common.mobileby import By
from page.base_page import BasePage
from time import sleep


class HomePage(BasePage):
    egg_loc = (By.XPATH,
               '//android.widget.GridView[@resource-id="com.meishio.app:id/product_recommend_home_gridview"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]')
    mine_loc = (By.XPATH,
                '//android.widget.LinearLayout[@resource-id="com.meishio.app:id/main_tool_bg"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    search_locator = (By.XPATH, '//android.widget.TextView[@resource-id="com.meishio.app:id/home_search_des"]')
    keyword_input_locator = (By.XPATH, '//android.widget.EditText[@resource-id="com.meishio.app:id/search_keyword"]')
    sweet_potato_locator1 = (By.ID, 'com.meishio.app:id/goods_flowlayout')
    sweet_potato_locator2 = (By.ID, 'com.meishio.app:id/search_tag_text')
    wuhe_potato_locator1 = (By.ID, 'com.meishio.app:id/work_layout')
    wuhe_potato_locator2 = (By.ID, 'com.meishio.app:id/goods_item_name')
    # '我的'
    personal_locator = (By.XPATH,
                        '//android.widget.LinearLayout[@resource-id="com.meishio.app:id/main_tool_bg"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')

    def Agg(self):
        '''
        点击首页上面的鸡蛋
        :return:
        '''
        self.find_element(self.egg_loc).click()

    def Mine(self):
        '''
        点击到我的页面
        :return:
        '''
        self.find_element(self.mine_loc).click()

    def search_ele(self):
        """点击首页搜索框"""
        self.find_element(self.search_locator).click()

    def keyword_input_ele(self, keyword):
        """输入搜索内容"""
        self.find_element(self.keyword_input_locator).send_keys(keyword)
        self.driver.press_keycode(66)

    def sweet_potato_ele(self):
        """点击【红薯】"""
        self.find_element(self.sweet_potato_locator2, self.find_element(self.sweet_potato_locator1)).click()

    def wuhe_potato_ele(self):
        """点击【五河红薯】"""
        self.find_element(self.wuhe_potato_locator2, self.find_element(self.wuhe_potato_locator1)).click()

    def h_swipe(self):
        x, y = self.w_size()
        for i in range(4):
            self.driver.swipe(0.9 * x, 0.5 * y, 0.1 * x, 0.5 * y, 1500)
            sleep(3)
        self.driver.swipe(0.5 * x, 0.1 * y, 0.5 * x, 0.9 * y, 1500)

    def search_for(self, keyword):
        self.search_ele()
        sleep(1)
        self.keyword_input_ele(keyword)
        sleep(1)
        self.sweet_potato_ele()
        sleep(1)
        self.wuhe_potato_ele()

    def mybutton_ele(self):
        """点击首页【我的】"""
        self.find_element(self.personal_locator).click()
