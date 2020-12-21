from appium.webdriver.common.mobileby import By
from page.base_page import BasePage


class Personal(BasePage):
    myorder_loc = (By.XPATH, '//android.widget.TextView[@resource-id="com.meishio.app:id/myorder_all"]')

    def MyOrder(self):
        self.find_element(self.myorder_loc).click()
