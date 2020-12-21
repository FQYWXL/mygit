from appium import webdriver
from time import sleep
import unittest
class AppTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_sear(self):
        """搜索"""
        # 组装 capabilities
        desired_capabilities = {
            # 测试机平台，Android or ios
            'platformName': 'Android',
            # 测试机名称，通过adb devices 获取，Android可以随便写，但必须有
            'deviceName': '127.0.0.1:62001',
            # 测试机的Android版本
            "platformVersion": '7.1.2',
            # 测试机的包名
            'appPackage': 'cn.missfresh.application',
            # 测试机的appium activity
            'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity',
            "unicodeKeyboard":True
        }
        # 启动Appium，url为测试的地址
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        driver.find_element_by_id("cn.missfresh.application:id/tv_double_btn_ok").click()
        sleep(2)
        driver.find_element_by_id("cn.missfresh.application:id/tv_next").click()
        sleep(2)
        driver.find_element_by_id("cn.missfresh.application:id/close_btn").click()
        sleep(2)
        driver.find_element_by_id("cn.missfresh.application:id/tv_search_text").click()
        sleep(2)
        driver.find_element_by_id("cn.missfresh.application:id/search_view").clear()
        sleep(2)
        driver.find_element_by_id("cn.missfresh.application:id/search_view").send_keys("牛肉")
        sleep(2)
        driver.keyevent(66)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
