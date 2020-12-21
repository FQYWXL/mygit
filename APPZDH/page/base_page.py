# -*- coding: utf-8 -*-



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
