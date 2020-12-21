from time import sleep
from appium import webdriver
from homework.APP_page.app_tenxunxinwen import tenxunxinwen
# desired_capabilities={
#     'platformName':'Android',
#     'platformVersion':'7.1.2',
#     'deviceName':'127.0.0.1:62001',
#     'appPackage':'com.tencent.news',
#     'appActivity':'com.tencent.news.activity.SplashActivity',
#     'unicodeKeyboard':True
# }
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

driver=tenxunxinwen(self=webdriver)
sleep(4)
# tap
driver.tap([(730,1543)],500)
sleep(3)
driver.tap([(156,443)],443)
sleep(3)
driver.tap([(156,443)],443)
















# 滚动导航
# ele1=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]')
# sleep(2)
# ele2=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[8]')
# sleep(2)
# driver.scroll(ele1,ele2)
# sleep(2)
#  # 拖到
# driver.tap([(845,175)],500)
# sleep(2)
# ele1=driver.find_element_by_xpath('//android.widget.Button[@text=\"抗疫\"]')
# sleep(1)
# ele2=driver.find_element_by_xpath('//android.widget.Button[@text=\"宠物\"]')
# sleep(1)
# driver.drag_and_drop(ele1,ele2)
# sleep(3)
#
# # 滚动
#
# driver.swipe(0,0,845,1300,2000)



