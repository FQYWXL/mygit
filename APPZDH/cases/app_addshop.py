from selenium.webdriver.common.by import By
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
a = driver.get_window_size(windowHandle="current")  # 获取当前窗口分辨率
x = a['width']  # 赋值宽度为x
y = a['height']  # 赋值高度为y
sleep(8)
driver.tap([(0.16 * x, 0.71 * y)], 500)  # 点击商品
sleep(2)
driver.tap([(390,1820)], 500)  # 点击加入购物车
driver.find_element(By.ID, 'com.meishio.app:id/product_properties_edit').click()  # 点击添加数量
driver.find_element(By.ID, 'com.meishio.app:id/product_properties_edit').clear()  # 清空输入框内默认数据
driver.find_element(By.ID, 'com.meishio.app:id/product_properties_edit').send_keys('5')  # 添加5个商品
sleep(1)
driver.find_element(By.ID, 'com.meishio.app:id/product_properties_done').click()  # 点击确定
sleep(1)
driver.find_element(By.ID, 'com.meishio.app:id/goods_detail_cart_image').click()  # 点击“购物车”图标查看商品是否添加成功
sleep(2)
driver.quit()  # 退出
