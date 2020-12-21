from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class Login1(BasePage):
    loc_my_locator = (By.XPATH,
                      '//android.widget.LinearLayout[@resource-id="com.meishio.app:id/main_tool_bg"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    # 点击登录注册
    login_locator = (By.XPATH, '//android.widget.TextView[@resource-id="com.meishio.app:id/user_name"]')
    # 输入用户名
    username_locator = (
        By.XPATH, '//android.widget.EditText[@resource-id="com.meishio.app:id/user_login_username_email_phone"]')
    # 输入密码
    password_locator = (By.XPATH, '//android.widget.EditText[@resource-id="com.meishio.app:id/user_login_password"]')
    # 点击登录按钮
    submit_locator = (By.XPATH, '//android.widget.Button[@resource-id="com.meishio.app:id/user_login_btn"]')

    def my(self):
        '''
    主页面商店我的中心
    :param self:
    :return:
    '''
        self.find_element(self.loc_my_locator).click()
        sleep(1)

    def login(self):
        '''
    点击登录按钮
    :param self:
    :return:
    '''
        self.find_element(self.login_locator).click()
        sleep(2)

    def click_username(self):
        self.find_element(self.username_locator).click()
        sleep(2)

    def input_username(self, username):
        '''
    用户输入框
    :param self:
    :param username:
    :return:
    '''
        self.find_element(self.username_locator).send_keys(username)
        sleep(2)

    def click(self):
        self.find_element(self.password_locator).click()
        sleep(2)

    def input_password(self, password):
        '''
    密码输入框
    :param self:
    :param password:
    :return:
    '''
        self.find_element(self.password_locator).send_keys(password)
        sleep(2)

    def submit(self):
        '''
    确认按钮
    :param self:
    :return:
    '''
        self.find_element(self.submit_locator).click()

    def logins(self, username, password):
        '''
       从我的进入到登录成功
       :param self:
       :param username:
       :param password:
       :return:
       '''
        self.my()
        self.login()
        self.input_username(username)
        self.input_password(password)
        self.submit()

    def zjlogin(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.submit()
