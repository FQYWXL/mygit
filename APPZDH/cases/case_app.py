import unittest
from time import sleep
from selenium.webdriver.common.by import By
from model.browser import open_app
from page.App_login import Login
from page.App_register import AppRegister
from page.addshop import AddShop
from page.app_search import Search
from page.login_page import Login1
from page.out import ExitLodgin
from page.personal_page import Personal
from page.myorder_page import WoOrder
from model.browser import open_app
import unittest
from time import sleep
from page.home_page import HomePage
from page.Productdetails_page import Shop_Details
from page.shoppingcart_page import ShoppingCart
from page.confirm_order import ConfirmOrder
from page.register_page import CashRegister
from datas.toolsex import Dates
from page.shortapp import SwitchShop
class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=open_app()
    @unittest.skip("skip")
    def test_1rigister(self):
        ll=AppRegister(self.driver)
        ll.registor("lisss6","admin123",'admin123','9056668@qq.com')

    def test_2login(self):
        lg=Login(self.driver)
        lg.login("lisa","admin123")
        sleep(10)
    def test_3nquit(self):
        ll=ExitLodgin(self.driver)
        ll.extsubmit()
    def test_4orderlook(self):
        lp = Login(self.driver)
        lp.login('lisss','admin123')
        lp.look_order()
        ll = ExitLodgin(self.driver)
        ll.extsubmit()

    def test_5search(self):
        lpp=Search(self.driver)
        lpp.sea("红薯")
    # def test_6add_order(self):
    #     ip = HomePage(self.driver)
    #     sleep(3)
    #     ip.ReFresh()  # 在home页面里面刷新一下
    #     sleep(2)
    #     ip.Agg()  # 点击鸡蛋
    #     sleep(6)
    #     XQ = Shop_Details(self.driver)
    #     XQ.AddCart()  # 点击添加到购物车
    #     DL = Login1(self.driver)  # 提示要登录输入用户名和密码
    #     username, password = Dates.data_Dl_ex()[3]
    #     DL.zjlogin(username, password)
    #     sleep(3)
    #     XQ.AddCart()  # 再次添加到购物车里面
    #     sleep(3)
    #     XQ.Okbutton()  # 点击确认按钮
    #     sleep(4)
    #     XQ.SmallCart()  # 点击购物车
    #     SC = ShoppingCart(self.driver)
    #     SC.ChooseButton()  # 点击选择商品按钮
    #     sleep(1)
    #     SC.Settlemnet()  # 点击结算按钮
    #     sleep(1)
    #     TJ = ConfirmOrder(self.driver)
    #     TJ.DeliveryMethod()  # 选择配送方式
    #     sleep(1)
    #     TJ.ChooseButton()  # 提交订单
    #     sleep(1)
    #     TJ.SubmitOrder()
    #     sleep(8)
    #     CG = CashRegister(self.driver)
    #     actual = CG.SubmitteSuccessful().text  # 获取文本
    #     print(actual)
    #     expect = '订单提交成功，请您尽快付款。'
    #     self.assertIn(expect, actual, msg='提交失败')
    #     sleep(6)
    #     self.driver.quit()
    #     self.driver = open_app()
    #     ll = ExitLodgin(self.driver)
    #     ll.extsubmit()

    # def test_7ViewOrder(self):
    #     self.driver = open_app()  # 先开app
    #     # hp = LoadPage(self.driver)
    #     sleep(5)
    #     # hp.load()  # 在加载页面里面滑动三次
    #     ip = HomePage(self.driver)
    #     sleep(3)
    #     ip.ReFresh()  # 在home页面里面刷新一下
    #     ip.Agg()
    #     sleep(4)
    #     XQ = Shop_Details(self.driver)
    #     XQ.Favorites()  # 点击收藏
    #     DL = Login(self.driver)  # 提示要登录输入用户名和密码
    #     username, password = Dates.data_Dl_ex()[0]
    #     DL.zjlogin(username, password)
    #     sleep(2)
    #     XQ.Favorites()  # 再次进行收藏
    #     sleep(2)
    #     XQ.Return()  # 点击返回
    #     sleep(2)
    #     ip.Mine()  # 点击home页面我的
    #     sleep(8)
    #     # WD = Personal(self.driver)
    #     # WD.MyOrder()
    #     # Dd = WoOrder(self.driver)
    #     # actual = Dd.Order().text
    #     # expect = '我的订单'
    #     # self.assertIn(expect, actual, msg='提交失败')
    #     # sleep(6)
    #     self.driver.quit()
    #     self.driver = open_app()
    #     ll = ExitLodgin(self.driver)
    #     ll.extsubmit()

    def test_switchshop(self):

        sw=SwitchShop(self.driver)
        sw.switchover()
    def test_addshop(self):
        ll=AddShop(self.driver)
        ll.addshopp()
    def test_comment(self):
        a = self.driver.get_window_size(windowHandle='current')  # 获取当前窗口大小
        x = a['width']  # 宽度赋值为x
        y = a['height']  # 高度赋值为y
        sleep(8)
        self.driver.tap([(0.83 * x, 0.71 * y)], 500)  # 点击主页任意商品
        sleep(2)
        self.driver.tap([(0.5 * x, 0.06 * y)], 500)  # 点击商品详情
        sleep(2)
        self.driver.tap([(0.71 * x, 0.06 * y)], 500)  # 点击商品评价
        sleep(2)
        self.driver.tap([(0.38 * x, 0.14 * y)], 500)  # 点击“好评”
        sleep(2)
        self.driver.swipe(570, 1700, 570, 460, 500)  # 向上滑动查看
        sleep(3)
        self.driver.tap([(0.61 * x, 0.14 * y)], 500)  # 点击“中评”
        sleep(2)
        self.driver.swipe(570, 1700, 570, 460, 500)  # 向上滑动查看
        sleep(3)
        self.driver.tap([(0.85 * x, 0.14 * y)], 500)  # 点击“差评”
        sleep(2)
        self.driver.swipe(570, 1700, 570, 460, 500)  # 向上滑动查看
        sleep(2)
        self.driver.keyevent(4)  # 退出
        sleep(1)
        self.driver.keyevent(4)  # 再次退出到首页
        sleep(2)
    def tearDown(self):
        sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
