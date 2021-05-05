import page
from base.base import Base
from base.get_driver import GetDriver


class PageOrder(Base):
    """
    注意：以下流程 默认用户已经登录成功且购物车里已经买了东西
    通过运行test02_cart.py 添加购物车模块-->让购物车里添加小米手机。这时再需调用一次单独的登录方法。
    """
    # 打开首页
    def page_click_index(self):
        self.base_index()

    # 点击 我的购物车
    def page_click_my_cart(self):
        self.base_click(page.order_my_cart)

    # 点击 全选复选框
    def page_click_all_select(self):
        # 判断是否选中
        if not self.base_find(page.order_all).is_selected():
            # 如果没选中 就点击复选框
            self.base_click(page.order_all)

    # 点击 去结算
    def page_click_account(self):
        self.base_click(page.order_account)

    # 备用 查找收货人-->动态解决收货人加载慢的问题 由于使用sleep浪费时间，
    # 现在思路：先在 收货人信息页面上通过 显示等待 查找到收件人姓名（如果暂时找不到会等30s）---然后再点击提交订单按钮
    def page_find_person(self):
        self.base_find(page.order_person)

    # 点击 提交订单 页面加载比较慢
    def page_click_submit_order(self):
        self.base_click(page.order_submit)

    # 获取订单提交结果
    def page_get_submit_result(self):
        return self.base_get_text(page.order_submit_result)

    # 订单组合业务类方法
    def page_order(self):
        # 点击我的购物车
        self.page_click_my_cart()
        # 点击 全选复选框
        self.page_click_all_select()
        # 点击 去结算
        self.page_click_account()
        # 点击查找收件人姓名
        self.page_find_person()
        # 点击 提交订单 页面加载比较慢
        self.page_click_submit_order()