from appium.webdriver.common.mobileby import By
from page.base_page import BasePage


class Shop_Details(BasePage):
    cart_loc = (By.ID, 'com.meishio.app:id/goods_detail_cart_image')
    return_loc = (By.XPATH,
                  '//android.widget.ImageView[@resource-id="com.meishio.app:id/goods_detail_head_tab_return_img"]')

    okbutton_loc = (By.ID, 'com.meishio.app:id/product_properties_done')

    def SmallCart(self):
        '''
        点击详情页面里面的小购物车
        :return:
        '''
        self.find_element(self.cart_loc).click()

    def Return(self):
        '''
        点击左上角的返回按钮
        :return:
        '''
        self.find_element(self.return_loc).click()

    def Okbutton(self):
        '''
        点击加入购物车里面后面的确认按钮
        :return:
        '''
        self.find_element(self.okbutton_loc).click()

    def AddCart(self):
        size = self.driver.get_window_size(windowHandle='current')
        print(size)
        x = size['width']
        y = size['height']
        self.driver.tap([(0.463 * x, 0.98 * y)], 500)

    def Favorites(self):
        size = self.driver.get_window_size(windowHandle='current')
        print(size)
        x = size['width']
        y = size['height']
        self.driver.tap([(0.91 * x, 0.74 * y)], 500)
