from time import sleep

from selenium.webdriver.common.by import By

from driver.app_driver import meishi
from page.base_page import BasePage


class Search(BasePage):

    sera_locator=(By.XPATH,'//android.widget.TextView[@resource-id="com.meishio.app:id/home_search_des"]')
    #输入搜索内容
    sumt_locator=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.EditText')
    # driver.keyevent(66)
    summ_locator=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView')
    def seach(self):
        self.find_element(self.sera_locator).click()
        sleep(2)
    def input_seach(self,search):
        ele=self.find_element(self.sumt_locator)
        ele.send_keys(search)
        sleep(2)
    def subm(self):
        self.find_element(self.summ_locator).click()
        sleep(2)
    def sea(self,search):
        self.seach()
        self.input_seach(search)
        sleep(2)
        self.driver.keyevent(66)
        sleep(6)
        self.subm()