from time import sleep

from base.base import Base
import page
from base.get_driver import GetDriver

from base.get_logger import GetLogger

log = GetLogger().get_logger()


class PageCart(Base):
    # 再次打开首页
    def page_open_index(self):
        sleep(3)
        self.base_index()

    # 输入搜索内容-小米手机
    def page_input_search(self, value='小米手机'):
        self.base_input(page.cart_search, value)

    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click(page.cart_search_btn)

    # 点击添加购物车，跳转到商品详情页
    def page_click_add_cart_info(self):
        self.base_click(page.cart_add_info)

    # 点击加入购物车
    def page_click_add_cart(self):
        self.base_click(page.cart_add)

    # 获取添加结果
    def page_get_text(self):
        """
        # 切换frame表单 由于电脑配置问题，导致加载比较慢，不推荐使用
         self.base_switch_frame(page.cart_frame_name)
        下面方法以后再回来研究为啥这样：
        过了5天，偶然今天终于弄懂了：和时间关系不大，主要是switch_to.frame()方法用错了。下次一定要看报错信息！！！
        易错点：driver.switch_to.frame(id不要带# / name / 如果没有id或name写driver.find_element(By.xxx,value)这个框架元素）
        """
        sleep(5) # 让弹窗等一会再切进去
        # self.base_switch_frame(self.base_find(page.cart_frame_name))
        self.base_switch_frame(page.cart_frame_name)
        print('执行完了base_switch_frame')
        # 返回结果 --记住必须return出去
        return self.base_get_text(page.cart_add_result)

    # 关闭窗口操作
    def page_close_window(self):
        # 回到默认目录
        self.base_default_content()
        # 点击关闭按钮
        self.base_click(page.cart_close_window)

    # 组合业务调用方法(输入小米手机-点击搜索-点击添加购物车跳转-真正添加购物车操作)
    def page_add_cart(self):
        self.page_input_search()
        self.page_click_search_btn()
        self.page_click_add_cart_info()
        self.page_click_add_cart()
        print('调用 组合添加购物车业务方法执行完了')





