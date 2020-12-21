from time import sleep
from appium import webdriver

def meishi():
    desired_capabilities = {
        # 测试机平台，Android or ios
        'platformName': 'Android',
        # 测试机名称，通过adb devices 获取，Android可以随便写，但必须有
        'deviceName': '127.0.0.1:62001',
        # 测试机的Android版本
        "platformVersion": '7.1.2',
        # 测试机的包名
        'appPackage': 'com.meishio.app',
        # 测试机的appium activity
        'appActivity': 'module.home.activity.SplashActivity',
        #输入中文
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        "noReset":True
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    sleep(8)

    return driver


