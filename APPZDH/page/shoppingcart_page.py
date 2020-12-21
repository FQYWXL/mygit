from selenium.webdriver.common.by import By
from page.base_page import BasePage


class ShoppingCart(BasePage):
    choosebutton_loc = (By.ID, 'com.meishio.app:id/shop_cart_goods_item_choice')
    settlement_loc = (By.ID, 'com.meishio.app:id/shop_cart_view_balance')

    def ChooseButton(self):
        self.find_element(self.choosebutton_loc).click()

    def Settlemnet(self):
        self.find_element(self.settlement_loc).click()
