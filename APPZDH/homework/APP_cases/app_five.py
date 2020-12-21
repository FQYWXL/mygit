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
#刷新
# driver.swipe(500,400,500,1000,2000)
# sleep(2)
count=0
for i in range(1,10):
    driver.swipe(500,500,100,500,500)
    sleep(1)
    count+=1
print(count)

print(driver.contexts)