# -*- coding: utf-8 -*-
# @Time : 2020/12/19 16:50
# @Author : nichao
# @Email : 530504026@qq.com
# @File : basepage.py
# @Project : appAuto
from model.browser import open_app
from selenium.webdriver.common.by import By
from appium import webdriver


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, element=None):
        '''
        查找元素，要求传入定位器，如果只传入定位器，整个浏览器找。
        如果传入定位器，并且传入一个元素对象，就在这个元素上再查找元素
        :param locator:
        :param element:
        :return:
        '''
        if element:
            return element.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def w_size(self):
        size = self.driver.get_window_size()
        # x = size['width']
        # y = size['height']
        return (size['width'], size['height'])

    def tap_function(self, width, height):
        x, y = self.w_size()
        self.driver.tap([((width / x) * x, (height / y) * y)], 500)
