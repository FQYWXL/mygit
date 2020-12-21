from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class Login(BasePage):
    loc_my_locator = (By.XPATH,
                      '//android.widget.LinearLayout[@resource-id="com.meishio.app:id/main_tool_bg"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    # 点击登录注册
    # loc_my_locator=(By.ID,'com.meishio.app:id/tab_one_icon')
    login_locator = (By.XPATH, '//android.widget.TextView[@resource-id="com.meishio.app:id/user_name"]')
    # 输入用户名
    username_locator = (
    By.XPATH, '//android.widget.EditText[@resource-id="com.meishio.app:id/user_login_username_email_phone"]')
    # 输入密码
    password_locator = (By.XPATH, '//android.widget.EditText[@resource-id="com.meishio.app:id/user_login_password"]')
    # 点击登录按钮
    submit_locator = (By.XPATH, '//android.widget.Button[@resource-id="com.meishio.app:id/user_login_btn"]')
    # 点击订单
    order_locator = (By.XPATH, '//android.widget.TextView[@resource-id="com.meishio.app:id/myorder_all"]')
    # 查看订单
    xinxin_locator = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView')
    sleep(2)

    def my(self):
        self.find_element(self.loc_my_locator).click()
        sleep(2)

    def loggn(self):
        self.find_element(self.login_locator).click()
        sleep(2)

    def input_username(self, username):
        ele = self.find_element(self.username_locator)
        ele.send_keys(username)
        sleep(2)

    def input_password(self, password):
        ele = self.find_element(self.password_locator)
        ele.send_keys(password)
        sleep(2)

    def submit_loc(self):
        self.find_element(self.submit_locator).click()
        sleep(3)

    def login(self, username, password):
        print("5555")
        self.my()
        print('2222')
        self.loggn()
        print('111')
        self.input_username(username)
        self.input_password(password)
        self.submit_loc()

    def order_lok(self):
        self.find_element(self.order_locator).click()
        sleep(2)

    def order_xinxin(self):
        self.find_element(self.xinxin_locator).click()
        sleep(1)

    def look_order(self):
        self.order_lok()
        self.order_xinxin()
        sleep(4)
        self.driver.keyevent(4)
        sleep(2)
        self.driver.keyevent(4)

