from time import sleep
import unittest
from homework.APP_model.base_case import BaseCase
from homework.APP_page import meishi


class AppTest(BaseCase):
    def test_search(self):
        driver = meishi()
        sleep(2)
        driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.meishio.app:id/lead_skip\"]').click()
        sleep(2)
        # 关键字搜索“红薯”
        driver.find_element_by_id('com.meishio.app:id/home_search_des').click()
        sleep(2)
        driver.find_element_by_xpath(
            '//android.widget.EditText[@resource-id=\"com.meishio.app:id/search_keyword\"]').send_keys("红薯")
        sleep(2)
        driver.keyevent(66)
    def test_search2(self):
        driver = meishi()
        sleep(2)
        # 搜索，热门搜索“龙虾”
        driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.meishio.app:id/lead_skip\"]').click()
        sleep(2)
        # 关键字搜索“龙虾”,
        # 进入搜索界面
        driver.find_element_by_id('com.meishio.app:id/home_search_des').click()
        sleep(2)
        # 点击热门搜索下的龙虾开始搜索
        driver.find_element_by_xpath('//android.widget.TextView[@text=\"龙虾\"]').click()
        sleep(2)
        # 查看龙虾详情
        driver.find_element_by_xpath(
            '//android.widget.ListView[@resource-id=\"com.meishio.app:id/listView_products\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
        sleep(3)
        # 加入购物车
        # driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.meishio.app:id/goods_detail_add_cart\"]').click()
        driver.tap([(350, 1550)], 500)
        sleep(2)
        # 输入用户名
        driver.find_element_by_xpath(
            '//android.widget.EditText[@resource-id=\"com.meishio.app:id/user_login_username_email_phone\"]').send_keys(
            "xiaoyou")
        sleep(2)
        # 输入密码
        driver.find_element_by_xpath(
            '//android.widget.EditText[@resource-id=\"com.meishio.app:id/user_login_password\"]').send_keys("admin123")
        sleep(2)
        # 点击登录
        driver.find_element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]').click()
        sleep(3)
        # 点击加入购物车
        # driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.meishio.app:id/goods_detail_add_cart\"]').click()
        driver.tap([(350, 1550)], 500)
        sleep(3)
        # 选择数量
        driver.find_element_by_xpath(
            '//android.widget.ImageView[@resource-id=\"com.meishio.app:id/product_properties_add\"]').click()
        sleep(2)
        # 点击确定按钮
        driver.find_element_by_xpath(
            '//android.widget.TextView[@resource-id=\"com.meishio.app:id/product_properties_done\"]').click()
        sleep(2)
        # 点击购物车查看
        driver.find_element_by_xpath('//android.widget.ImageView[@resource-id=\"com.meishio.app:id/goods_detail_cart_image\"]').click()
        sleep(3)


if __name__ == '__main__':
    unittest.main()
