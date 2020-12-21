from time import sleep
from appium import webdriver

# #进入首页
from driver.app_driver import meishi
#
# driver=meishi()

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
sleep(9)
# driver.implicitly_wait(30)
print('xxx')
# driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.meishio.app:id/lead_skip\"]').click()
# sleep(2)
# print("出问题了")
## 注册
# 点击我的
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView").click()
# driver.find_element_by_android_uiautomator('new UiSelector()checked(true).instance(17)').click()
driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
sleep(4)
#点击登录注册
driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.meishio.app:id/user_name"]').click()
sleep(4)
#点击“快速注册”
driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.meishio.app:id/user_top_view_right"]').click()
sleep(1)
#点击邮箱
driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.meishio.app:id/user_register_email_title"]').click()
sleep(1)
#输入用户名
driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.meishio.app:id/user_register_nickname"]').send_keys('li9')
sleep(1)
#输入密码
driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.meishio.app:id/user_register_password_email"]').send_keys('admin123')
sleep(1)
#输入确认密码
driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.meishio.app:id/user_register_password_confirm_email"]').send_keys('admin123')
sleep(1)
#输入邮箱
driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.meishio.app:id/user_register_email"]').send_keys('917767548@qq.com')
sleep(1)
#点击注册按钮
driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.meishio.app:id/user_register_confirm_email"]').click()
sleep(5)
print(222)
driver.press_keycode(4)
driver.quit()
# #输入手机号
# driver.tap([(388,306)])
# driver.find_element_by_id('com.meishio.app:id/complete_information_child_edit').send_keys(1234567865)
# driver.find_element_by_id('com.meishio.app:id/complete_information_child_edit').click()
# print(111)
# driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/complete_information_body\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').send_keys("1234567865")
#
# aa.find_element_by_xpath('//android.widget.EditText[@resource-id=\"com.meishio.app:id/complete_information_child_edit\"]').send_keys(13208163923)
# sleep(3)
# # 点击确定按钮
# driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.meishio.app:id/complete_information_done"]').click()
# sleep(3)
# pp=AppRegister(driver)
# username,password,passwd,eamil=('lisiyu','admin123','admin123','12343123@qq.com')
# pp.registor(username,password,passwd,eamil)
#### 登录
# driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="com.meishio.app:id/main_tool_bg"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
# sleep(1)
# #点击登录注册
# driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.meishio.app:id/user_name"]').click()
# sleep(3)
# #输入用户名
# driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.meishio.app:id/user_login_username_email_phone"]').send_keys("lisa")
# sleep(1)
# #输入密码
# driver.find_element_by_xpath('//android.widget.EditText[@resource-id=\"com.meishio.app:id/user_login_password\"]').send_keys("admin123")
# sleep(1)
# #点击登录按钮
# driver.find_element_by_xpath('//android.widget.Button[@resource-id=\"com.meishio.app:id/user_login_btn\"]').click()
# sleep(1)
# pp=Login()
# username,password=('lisa','admin123')
# pp.login(username,password)
####搜索商品
# 点击搜索
# driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.meishio.app:id/home_search_des"]').click()
# sleep(2)
# #输入搜索内容
# driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.meishio.app:id/search_keyword"]').send_keys("红薯")
# sleep(2)
# driver.keyevent(66)

# # #driver.tap([(50,35)],10)
# # #driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"android:id/title\"]').click()
# ## driver.find_element_by_xpath('//android.widget.ListView[@resource-id=\"android:id/select_dialog_listview\"]/android.widget.LinearLayout[2]/android.widget.RadioButton[1]').click()
# #模拟点击enter
# #选择商品
# driver.find_element_by_xpath('//android.view.ViewGroup[@resource-id="com.meishio.app:id/goods_flowlayout"]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
# sleep(2)
#
#
#
#
#
#
#
