from appium.webdriver.common.mobileby import By
from page.base_page import BasePage


class WoOrder(BasePage):
    woorder_loc=(By.ID,'com.meishio.app:id/user_top_view_title')

    def Order(self):
        element=self.find_element(self.woorder_loc)
        return element
