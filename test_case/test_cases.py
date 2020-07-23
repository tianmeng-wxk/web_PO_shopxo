import unittest
from page_object.login_page import LoginPage
from page_object.user_center_page import UserCenterPage
from page_object.search_page import SearchPage
from page_object.shop_page import Shop
from page_object.add_cart_page import AddCart
from page_object.register_page import Register
from common.common import browser_type,SendEmail
from ddt import ddt, data, file_data, unpack


@ddt
class TestCase(unittest.TestCase):

    def setUp(self) -> None:

        self.driver = browser_type("chr")
        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()
        self.lp = LoginPage(self.driver,LoginPage.url)
        self.ip = UserCenterPage(self.driver,UserCenterPage.url)
        self.sp = SearchPage(self.driver,SearchPage.url)
        self.add = AddCart(self.driver,AddCart.url)
        self.shop = Shop(self.driver,Shop.url)
        self.r = Register(self.driver,Register.url)

    def tearDown(self) -> None:
        self.driver.quit()

    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        # 发送邮件
        SendEmail().send_email('../report/2020_07_09_18_55_46_html_report.html')

    #登录
    @file_data("../config/login.yaml")
    def test_01_login(self,**kwargs):
        self.lp.login(kwargs["username"], kwargs["password"])
        self.assertTrue(self.lp.assert_text(kwargs["validata"]["type"], kwargs["validata"]["value"], kwargs["validata"]["expect"]))


    #注册
    @file_data("../config/register.yaml")
    def test_04_register(self,**kwargs):
        self.r.register(kwargs["username"],kwargs["password"])
        self.assertTrue(self.r.assert_text(kwargs["validata"]["type"], kwargs["validata"]["value"], kwargs["validata"]["expect"]))



    #搜索
    @file_data("../config/search.yaml")
    def test_02_search(self, **kwargs):
        self.sp.search_shop(kwargs["search_content"])
        #self.assertTrue(self.sp.assert_text(kwargs["validata"]["type"], kwargs["validata"]["value"], kwargs["validata"]["expect"]))




    #个人中心
    @file_data("../config/user_center.yaml")
    def test_03_user_center(self, **kwargs):
        #正常登录
        self.lp.login("666666", "111111")
        #搜索订单号
        self.ip.search_infor(kwargs['search_content'])

    #加入购物车
    def test_03_add_shop_cart(self):
        #正常登录
        self.lp.login("666666", "111111")
        #选择商品
        self.shop.click_shop()
        #切换句柄
        headle = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(headle[2])
        #选择规格加入购物车
        self.add.add_shop_cart()


if __name__ == '__main__':
    unittest.main()

