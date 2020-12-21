import unittest
from time import sleep

from model.browser import open_app
from page.home_page import HomePage
from page.app_detailshop import AppDetialshop
from page.personal_page import Personal
from page.confirm_order import ConfirmOrder
from page.register_page import Register
from page.myorder_page import MyOrder
from page.setup_page import SetUp


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app()

    def test_s(self):
        sleep(3)
        hp = HomePage(self.driver)
        hp.h_swipe()
        sleep(1)
        # 点击搜索框
        hp.search_for("红薯")
        sleep(1)
        ad=AppDetialshop(self.driver)
        # 点击加入购物车
        ad.shopcart_ele()
        sleep(1)
        #登录
        pl=Personal(self.driver)
        pl.plogin('username',123456)
        sleep(1)
        # 点击立即购买
        ad.appdetialshop_ele()
        sleep(1)
        #选择配送方式，提交订单
        co=ConfirmOrder(self.driver)
        co.confirmorder()
        sleep(3)
        rg=Register(self.driver)
        actul=rg.order_assert()
        expect='订单提交成功，请您尽快付款。'
        self.assertEqual(expect,actul,msg='提交订单失败')
    def test_order(self):
        sleep(3)
        hp = HomePage(self.driver)
        hp.h_swipe()
        sleep(1)
        #点击【我的】
        hp.mybutton_ele()
        sleep(3)
        pl = Personal(self.driver)
        #点击【登录按钮】
        pl.loginbutton_ele()
        sleep(1)
        pl.plogin('username', 123456)
        #获取取消前的待付款订单数量
        expected=pl.obligation_number_assert1()
        # 点击我的订单
        pl.myorder_button_ele()
        mo = MyOrder(self.driver)
        #取消第一个待付款的订单
        mo.confirm_cancel_ele()
        sleep(1)
        #返回到【我的】页面
        mo.return_my_ele()
        sleep(3)
        #获取取消后的待付款订单数量
        actual= pl.obligation_number_assert2()
        self.assertEqual(expected,actual,msg='订单取消失败')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
