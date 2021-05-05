# 运行该模块前需要运行test03_cart.py 提交订单
import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_pay import PagePay


class TestPay(unittest.TestCase):
    def setUp(self):
        self.driver = GetDriver.get_driver()
        self.page_pay = PagePay(self.driver)
        # 点击登录链接 输入用户信息 点击登录
        PageLogin(self.driver).page_login_success()

    def tearDown(self):
        sleep(3)
        GetDriver.quit_driver()

    def test_pay(self):
        try:
            # 调用支付组合业务方法
            self.page_pay.page_pay()
            msg = self.page_pay.page_get_payment_result()
            print('打印支付结果 msg=', msg)
            # 断言支付结果是否正确
            self.assertIn('我们将在第一时间给你发货', msg)
        except:
            self.page_pay.base_get_image()
            raise
