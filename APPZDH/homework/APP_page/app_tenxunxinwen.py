from time import sleep
from appium import webdriver

def tenxunxinwen():
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
        "unicodeKeyboard": True,
        "noReset":True
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    sleep(4)
    return driver