from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class ConfirmOrder(BasePage):
    choosebutton_loc = (By.ID, 'com.meishio.app:id/shipping_item_check')
    submitorder_loc = (By.ID, 'com.meishio.app:id/order_confirm_submit')

    def DeliveryMethod(self):
        size = self.driver.get_window_size(windowHandle='current')
        print(size)
        x = size['width']
        y = size['height']
        self.driver.tap([(0.745 * x, 0.44 * y)], 500)

    def ChooseButton(self):
        self.find_element(self.choosebutton_loc).click()

    def SubmitOrder(self):
        self.find_element(self.submitorder_loc).click()
