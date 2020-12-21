from time import sleep
from appium import webdriver

def meishi():
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        "platformVersion": '7.1.2',
        'appPackage': 'com.meishio.app',
        'appActivity': 'module.home.activity.SplashActivity',
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    sleep(8)
    return driver