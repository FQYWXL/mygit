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
sleep(8)
a = driver.get_window_size(windowHandle='current')
x = a['width']
y = a['height']
driver.tap([(0.37 * x, 0.96 * y)], 500)  # 点击商品分类
sleep(2)
driver.find_element(By.XPATH,  # 点击“五河特产”
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView').click()
driver.find_element(By.XPATH,  # 点击“全部商品”
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView').click()
sleep(2)
driver.find_element(By.ID, 'com.meishio.app:id/search_back').click()  # 点击左上角返回
driver.find_element(By.XPATH,  # 切换到“农家良品”
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView').click()
sleep(2)
driver.find_element(By.XPATH,  # 点击”全部商品“
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView').click()
sleep(3)
driver.swipe(570, 1700, 570, 460, 500)  # 先上滑动查看列表
sleep(2)
driver.find_element(By.ID, 'com.meishio.app:id/search_back').click()  # 点击左上角返回
driver.quit()  # 退出app
