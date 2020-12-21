from time import sleep
from appium import webdriver

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

#多点触摸
# driver.tap([(200,200),(100,300)],500)
# sleep(2)
# #滚动导航
# ele1=driver.find_element_by_xpath('//android.widget.ListView[@resource-id=\"com.tencent.news:id/timeline_list\"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')
# ele2=driver.find_element_by_xpath('//android.widget.TextView[@text=\"汽车\"]')
# driver.scroll(ele1,ele2)
# 拖动
# driver.tap([(850,180)],500)
# sleep(2)
# ele3=driver.find_element_by_xpath('//android.widget.Button[@text=\"四川\"]')
# sleep(2)
# ele4=driver.find_element_by_xpath('//android.widget.Button[@text=\"宠物\"]')
# sleep(2)
# driver.drag_and_drop(ele3,ele4)