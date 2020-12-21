from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class AppRegister(BasePage):
    #我的
    my_locator=(By.XPATH,'//android.widget.LinearLayout[@resource-id="com.meishio.app:id/main_tool_bg"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    #登录注册
    regstor_locator=(By.XPATH,'//android.widget.TextView[@resource-id="com.meishio.app:id/user_name"]')
    #点击“快速注册”
    regis_locator=(By.XPATH,'//android.widget.TextView[@resource-id="com.meishio.app:id/user_top_view_right"]')
    #点击邮箱
    eamil_loactor=(By.XPATH,'//android.widget.TextView[@resource-id="com.meishio.app:id/user_register_email_title"]')
    #输入用户名
    username_locator=(By.XPATH,'//android.widget.EditText[@resource-id="com.meishio.app:id/user_register_nickname"]')
    #输入密码
    password_locator=(By.XPATH,'//android.widget.EditText[@resource-id="com.meishio.app:id/user_register_password_email"]')
    #输入确认密码
    passwd_locator=(By.XPATH,'//android.widget.EditText[@resource-id="com.meishio.app:id/user_register_password_confirm_email"]')
    #输入邮箱
    eami_loactor=(By.XPATH,'//android.widget.EditText[@resource-id="com.meishio.app:id/user_register_email"]')
    #点击注册按钮
    regi_locatir=(By.XPATH,'//android.widget.Button[@resource-id="com.meishio.app:id/user_register_confirm_email"]')
    def my_lic(self):
        self.find_element(self.my_locator).click()
        sleep(1)
    def regi(self):
        self.find_element(self.regstor_locator).click()
        sleep(1)
    def regist(self):
        self.find_element(self.regis_locator).click()
        sleep(1)
    def eami(self):
        self.find_element(self.eamil_loactor).click()
        sleep(1)
    def input_username(self,username):
        element=self.find_element(self.username_locator)
        element.send_keys(username)
        sleep(1)
    def input_password(self,password):
        ele=self.find_element(self.password_locator)
        ele.send_keys(password)
        sleep(1)
    def input_passwd(self,passwd):
        ele=self.find_element(self.passwd_locator)
        ele.send_keys(passwd)
        sleep(1)
    def input_eaml(self,eamil):
        ele=self.find_element(self.eami_loactor)
        ele.send_keys(eamil)
        sleep(1)
    def regi_locator(self):
        self.find_element(self.regi_locatir).click()
        sleep(1)

    def registor(self,username,password,passwd,email):
        self.my_lic()
        self.regi()
        self.regist()
        self.eami()
        self.input_username(username)
        self.input_password(password)
        self.input_passwd(passwd)
        self.input_eaml(email)
        self.regi_locator()
        self.driver.press_keycode(4)


    # #输入手机号
    # driver.find_element_by_xpath('//android.widget.EditText[@resource-id=\"com.meishio.app:id/complete_information_child_edit\"]').send_keys(13208163923)
    # sleep(3)
    # #点击确定按钮
    # driver.find_element_by_xpath('//android.widget.Button[@resource-id="com.meishio.app:id/complete_information_done"]').click()
    # sleep(3)