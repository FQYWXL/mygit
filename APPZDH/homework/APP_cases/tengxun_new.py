from appium import webdriver
from time import sleep
import unittest
from homework.APP_page import app_tenxunxinwen


class AppTest(unittest.TestCase):
    def test_click(self):
    #     """点击"""
    #     # 组装 capabilities
        desired_capabilities = {
        # 测试机平台，Android or ios
        'platformName': 'Android',
        # 测试机名称，通过adb devices 获取，Android可以随便写，但必须有
        'deviceName': '127.0.0.1:62001',
        # 测试机的Android版本
        "platformVersion": '7.1.2',
        # 测试机的包名
        'appPackage': 'com.tencent.news',
        # 测试机的appium activity
        'appActivity': 'com.tencent.news.activity.SplashActivity',
        "unicodeKeyboard": True
        }
        # 启动Appium，url为测试的地址
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        sleep(18)
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[5]").click()
        sleep(18)
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.TextView[1]").click()
        sleep(15)
        # driver.find_element_by_id("com.tencent.news:id/video_play_normal").click()
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout").click()
        sleep(10)
    # def test_sera(self):
    #     """搜索"""
    #     # 组装 capabilities
    #     desired_capabilities = {
    #         # 测试机平台，Android or ios
    #         'platformName': 'Android',
    #         # 测试机名称，通过adb devices 获取，Android可以随便写，但必须有
    #         'deviceName': '127.0.0.1:62001',
    #         # 测试机的Android版本
    #         "platformVersion": '7.1.2',
    #         # 测试机的包名
    #         'appPackage': 'com.tencent.news',
    #         # 测试机的appium activity
    #         'appActivity': 'com.tencent.news.activity.SplashActivity',
    #         "unicodeKeyboard": True
    #     }
    #     # 启动Appium，url为测试的地址
    #     driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    #     sleep(18)
    #     #搜索
    #     driver.find_element_by_id("com.tencent.news:id/search_page_box").click()
    #     sleep(2)
    #     driver.find_element_by_id("com.tencent.news:id/search_page_box").send_keys("足球")
    #     sleep(2)
    #     driver.keyevent(66)
    def test_2sera(self):
        """搜索"""
        # 组装 capabilities
        # desired_capabilities = {
        #     # 测试机平台，Android or ios
        #     'platformName': 'Android',
        #     # 测试机名称，通过adb devices 获取，Android可以随便写，但必须有
        #     'deviceName': '127.0.0.1:62001',
        #     # 测试机的Android版本
        #     "platformVersion": '7.1.2',
        #     # 测试机的包名
        #     'appPackage': 'com.tencent.news',
        #     # 测试机的appium activity
        #     'appActivity': 'com.tencent.news.activity.SplashActivity',
        #     "unicodeKeyboard": True
        # }
        # 启动Appium，url为测试的地址

        # driver.implicitly_wait(30)
        #搜索
        lp= app_tenxunxinwen
        driver = webdriver.Remote("http://localhost:4723/wd/hub")
        pass

        driver.find_element_by_id("com.tencent.news:id/channelbar_text").click()
        sleep(2)
        driver.find_element_by_id('com.tencent.news:id/title_text').click()
        sleep(2)
        driver.find_element_by_id('omFollowBtnLink').click()
        sleep(2)
        driver.find_element_by_id('com.tencent.news:id/title_right_btn_close').click()
        sleep(3)
        driver.find_element_by_id('com.tencent.news:id/title_bar_btn_back').click()
        # driver.keyevent(66)  #点击按钮
    # def tearDown(self):
    #     pass

if __name__ == '__main__':
    unittest.main()







