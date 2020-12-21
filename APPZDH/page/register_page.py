from selenium.webdriver.common.by import By
from page.base_page import BasePage


class CashRegister(BasePage):
    SubmitteSuccessful_loc = (By.XPATH, '//android.widget.TextView[@resource-id="com.meishio.app:id/pay_title"]')

    def SubmitteSuccessful(self):
        element = self.find_element(self.SubmitteSuccessful_loc)
        return element
