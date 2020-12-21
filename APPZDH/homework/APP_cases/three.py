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
            "unicodeKeyboard": True,

}
# driver=webdriver.Remote("http://localhost:4723/wb/hub",desired_capabilities)
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities)
driver.implicitly_wait(30)
# 1、进入搜索框
# 2、输入数据“嫦娥5号”
# 3、点击搜索按钮
# 5、点击“嫦娥5号回家了”
# 6、点击关注
# 7、点击【取消】按钮
# 8、点击返回
#进入搜索框
driver.find_element_by_id('com.tencent.news:id/single_image').click()
sleep(3)
#输入数据“嫦娥5号”
driver.find_element_by_id('android.widget.EditText').send_keys("嫦娥5号")
sleep(2)
#点击【搜索】按钮
driver.find_element_by_id('com.tencent.news:id/search_page_logo').click()
sleep(3)
#点击嫦娥5号回家了
driver.find_element_by_id('com.tencent.news:id/title_text').click()
sleep(3)
#点击【点赞】按钮
driver.find_element_by_id('com.tencent.news:id/bottom_bar').click()
#点击【取消】按钮
driver.find_element_by_id('com.tencent.news:id/title_right_btn_close').click()
#点击返回按钮
driver.find_element_by_id('com.tencent.news:id/video_cover').click()
sleep(3)
