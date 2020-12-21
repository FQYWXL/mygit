from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class ExitLodgin(BasePage):
    # 点击我的
    # loc_my_locator = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView')
        # 设置
    loc_my_locator = (By.XPATH,
                      '//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')

    set_locator = (By.XPATH, '//android.widget.ImageView[@resource-id="com.meishio.app:id/user_photo_setting"]')
    # 点击退出
    ext_locator = (By.XPATH, '//android.widget.Button[@resource-id="com.meishio.app:id/user_exit_btn"]')
    # 确认
    aff_tocator = (By.XPATH, '//android.widget.TextView[@resource-id="com.meishio.app:id/yes"]')
    # 返回
    dret_locator = (By.XPATH, '//android.widget.ImageView[@resource-id="com.meishio.app:id/user_top_view_back"]')

    def mine(self):
        self.find_element(self.loc_my_locator).click()
        sleep(2)

    def set_sub(self):
        self.find_element(self.set_locator).click()
        sleep(2)

    def ext_sub(self):
        self.find_element(self.ext_locator).click()
        sleep(2)

    def affie_sub(self):
        self.find_element(self.aff_tocator).click()
        sleep(2)

    def dret_sub(self):
        self.find_element(self.dret_locator).click()
        sleep(2)

    def extsubmit(self):
        self.mine()
        self.set_sub()
        self.ext_sub()
        self.affie_sub()
        self.dret_sub()


