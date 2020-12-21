from time import sleep

from appium import webdriver

desired_capabilities={
    'platformName':'Android',
    'platformVersion':'7.1.2',
    'deviceName':'127.0.0.1:62001',
    'appPackage':'com.tencent.news',
    'appActivity':'com.tencent.news.activity.SplashActivity',
    'unicodeKeyboard':True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
sleep(4)
# #点击我
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.LinearLayout').click()
# sleep(5)
# #点击钱包
# locator = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout')
# locator.find_element_by_id('com.tencent.news:id/my_wallet').click()
# sleep(3)
# #点击关闭按钮
# driver.find_element_by_id('com.tencent.news:id/title_right_btn_close').click()
# sleep(2)
# tap
driver.tap([(730,1543)],500)
sleep(3)




driver.quit()
