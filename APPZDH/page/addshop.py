from time import sleep
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class AddShop(BasePage):

    addshop_locator=(By.ID, 'com.meishio.app:id/product_properties_edit')  # 点击添加数量
    clear_pocator=(By.ID,'com.meishio.app:id/product_properties_edit')  # 清空输入框内默认数据
    addfive_locator=(By.ID,'com.meishio.app:id/product_properties_edit')  # 添加5个商品
    sure_locator=(By.ID, 'com.meishio.app:id/product_properties_done')  # 点击确定

    carshop_locator=(By.ID, 'com.meishio.app:id/goods_detail_cart_image') # 点击“购物车”图标查看商品是否添加成功
    sleep(2)

    def top(self):
        a = self.driver.get_window_size(windowHandle="current")  # 获取当前窗口分辨率
        x = a['width']  # 赋值宽度为x
        y = a['height']  # 赋值高度为y
        sleep(8)
        self.driver.tap([(0.16 * x, 0.71 * y)], 500)  # 点击商品
        sleep(6)
        self.driver.tap([(0.361*x, 0.95*y)], 500)  # 点击加入购物车
        sleep(2)
    def shopadd(self):
        self.find_element(self.addshop_locator).click()
        sleep(3)
    def clear_sub(self):
        self.find_element(self.clear_pocator).click()
        sleep(3)
    def fiveadd(self):
        self.find_element(self.addfive_locator).send_keys('5')
        sleep(3)
    def sure_aub(self):
        self.find_element(self.sure_locator).click()
        sleep(3)
    def shopcar(self):
        self.find_element(self.carshop_locator).click()
        sleep(3)
    def addshoping(self):
        self.top()

    def addshopp(self):
        self.top()
        self.shopadd()
        self.clear_sub()
        self.fiveadd()
        self.sure_aub()
        self.shopcar()

