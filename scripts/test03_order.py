# 运行该模块前需要运行test02_cart.py 添加商品到购物车
import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder

"""
由于不用参数化数据（需要调用多次test方法)，所以setUp/tearDown只会执行一次 和 setUpClass/tearDownClass效果等同.
"""


class TestOrder(unittest.TestCase):
    # setup
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver();
        print("打印订单模块driver",self.driver)
        # 调用登录模块PageLogin对象中登录组合方法，直接登录
        PageLogin(self.driver).page_login_success()
        # 实例化PageOrder类
        self.page_order = PageOrder(self.driver)
        # 跳转到首页
        self.page_order.base_index()

    # teardown
    def tearDown(self):
        sleep(3)
        GetDriver.quit_driver()

    # 新建 订单测试类方法
    def test_order(self):
        try:
            # 调用 下订单业务方法
            self.page_order.page_order()
            # 断言是否下订单成功
            msg = self.page_order.page_get_submit_result()
            print("msg=", msg)
            self.assertIn('订单提交成功', msg)
        except:
            self.page_order.base_get_image()
            # 截图完了 让控制台继续报异常
            raise
