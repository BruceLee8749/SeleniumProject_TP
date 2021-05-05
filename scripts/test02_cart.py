# 定义测试类
import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin


class TestCart(unittest.TestCase):
    # 定义setup
    # 由于添加购物车只用一次，没有多组参数化数据，所以setUpClass和setUp用哪个都一样。
    # 如果有多组参数化数据:意味着每次执行一组参数化数据,都会执行一次测试购物车方法--->每次都会调用setUp和tearDown方法！！！
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化PageCart
        self.cart = PageCart(self.driver)
        # 调用登录组合业务方法直接登录
        PageLogin(self.driver).page_login_success()
        # 现在是在我的订单信息页面，需要再次跳转到首页
        self.cart.page_open_index()

    # 定义teardown
    def tearDown(self):
        # 关闭driver
        sleep(3)
        # GetDriver().quit_driver()

    # 定义测试购物车方法
    def test_add_cart(self):
        # 调用 组合添加购物车业务方法
        self.cart.page_add_cart()
        sleep(10)
        # 断言是否添加成功
        msg = self.cart.page_get_text()
        print('打印购物车模块msg', msg)
        self.assertEqual(msg, '添加成功')
        # 关闭购物车窗口
        self.cart.page_close_window()
