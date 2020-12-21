from appium import webdriver
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'platformVersion': '7.1.2',
    'deviceName': 'meishiyuan',
    'appPackage': 'com.meishio.app',
    'appActivity': 'module.home.activity.SplashActivity',
    'noReset': True,
    'unicodeKeyboard': True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)  # 隐式等待
a = driver.get_window_size(windowHandle='current')  # 获取当前窗口大小
x = a['width']  # 宽度赋值为x
y = a['height']  # 高度赋值为y
sleep(8)
driver.tap([(0.83 * x, 0.71 * y)], 500)  # 点击主页任意商品
sleep(2)
driver.tap([(0.5 * x, 0.06 * y)], 500)  # 点击商品详情
sleep(2)
driver.tap([(0.71 * x, 0.06 * y)], 500)  # 点击商品评价
sleep(2)
driver.tap([(0.38 * x, 0.14 * y)], 500)  # 点击“好评”
sleep(2)
driver.swipe(570, 1700, 570, 460, 500)  # 向上滑动查看
sleep(3)
driver.tap([(0.61 * x, 0.14 * y)], 500)  # 点击“中评”
sleep(2)
driver.swipe(570, 1700, 570, 460, 500)  # 向上滑动查看
sleep(3)
driver.tap([(0.85 * x, 0.14 * y)], 500)  # 点击“差评”
sleep(2)
driver.swipe(570, 1700, 570, 460, 500)  # 向上滑动查看
sleep(2)
driver.keyevent(4)  # 退出
sleep(1)
driver.keyevent(4)  # 再次退出到首页
sleep(2)
driver.quit()  # 退出app
print(a)