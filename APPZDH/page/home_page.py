from appium.webdriver.common.mobileby import By
from page.base_page import BasePage


class HomePage(BasePage):
    egg_loc = (By.XPATH,
               '//android.widget.GridView[@resource-id="com.meishio.app:id/product_recommend_home_gridview"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]')
    mine_loc = (By.XPATH,
                '//android.widget.LinearLayout[@resource-id="com.meishio.app:id/main_tool_bg"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')

    def Agg(self):
        '''
        点击首页上面的鸡蛋
        :return:
        '''
        self.find_element(self.egg_loc).click()

    def Mine(self):
        '''
        点击到我的页面
        :return:
        '''
        self.find_element(self.mine_loc).click()
    def ReFresh(self):
        '''
        刷新页面
        :return:
        '''
        self.driver.swipe(610, 380, 610, 1020, 500)




