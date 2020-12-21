from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class SwitchShop(BasePage):
    # 点击“五河特产”
    wuhe_locator = (By.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView')
    # 点击“全部商品”
    all_shop = (By.XPATH,
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView')
    # 点击左上角返回
    back_locator = (By.ID, 'com.meishio.app:id/search_back')
    # 切换到“农家良品”
    nong_locator = (By.XPATH,
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView')

    # 点击”全部商品“
    # 先上滑动查看列表
    # 点击左上角返回

    def top(self):
        a = self.driver.get_window_size(windowHandle='current')
        x = a['width']
        y = a['height']
        self.driver.tap([(0.37 * x, 0.96 * y)], 500)  # 点击商品分类
        sleep(2)

    def wuhe_sub(self):
        self.find_element(self.wuhe_locator).click()
        sleep(2)

    def shopall(self):
        self.find_element(self.all_shop).click()
        sleep(2)

    def back(self):
        self.find_element(self.back_locator).click()
        sleep(2)

    def nong(self):
        self.find_element(self.nong_locator).click()
        sleep(2)
        sleep(2)
        self.driver.swipe(570, 1700, 570, 460, 500)
        sleep(2)
        sleep(2)

    def switchover(self):
        self.top()
        self.wuhe_sub()
        self.shopall()
        self.back()
        self.shopall()
        self.back()
        self.shopall()
        self.back()
