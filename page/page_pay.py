"""
注意：以下流程 默认用户点击了去结算按钮并且提交订单成功
通过运行test03_order.py 提交订单模块-->让商品订单提交到后台。这时再需调用一次单独的登录方法。
"""
from time import sleep

import page
from base.base import Base


class PagePay(Base):
    # 在用户中心页 点击我的订单
    def page_click_my_order_link(self):
        self.base_click(page.pay_my_order)

    # 点击立即支付
    def page_click_now_payment(self):
        # 切换到指定窗口
        self.base_switch_to_window(page.pay_my_order_title)
        # 点击立即支付按钮
        self.base_click(page.pay_now_payment)

    # 点击 货到付款
    def page_click_pay_on_delivery(self):
        # 切换到指定窗口
        self.base_switch_to_window(page.pay_payment_title)
        # 点击货到付款按钮
        self.base_click(page.pay_on_delivery)

    # 点击 确认支付方式按钮
    def page_click_payment_mode(self):
        self.base_click(page.pay_confirm_payment)

    # 等几秒后 获取支付结果
    def page_get_payment_result(self):
        sleep(5)
        return self.base_get_text(page.pay_payment_result) # 一定一定要return该文本，好几次出错了！无语

    # 支付组合业务方法
    def page_pay(self):
        self.page_click_my_order_link()
        self.page_click_now_payment()
        self.page_click_pay_on_delivery()
        self.page_click_payment_mode()