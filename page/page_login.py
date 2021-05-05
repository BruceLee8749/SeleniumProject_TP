from time import sleep

from base.base import Base
# 导入page包下的文件
import page
from base.get_driver import GetDriver
from base.get_logger import GetLogger

log = GetLogger().get_logger()


# 业务类--实现模拟人工操作
class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link(self):
        log.info("[page_login]:执行:{}点击链接操作".format(page.login_link))
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        log.info("[page_login]:对{}元素输入用户名：{}操作".format(page.login_username, username))
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        log.info("[page_login]:对{}元素输入密码：{}操作".format(page.login_pwd, pwd))
        self.base_input(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        log.info("[page_login]:对{}元素输入验证码：{}操作".format(page.login_verify_code, verify_code))
        self.base_input(page.login_verify_code, verify_code)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取错误提示信息
    def page_get_error_info(self):
        sleep(3)  # 睡3s让弹框显示出来
        return self.base_get_text(page.login_err_info)  # 需要再次return出去！！！

    # 点击错误提示框确定按钮
    def page_click_error_alert(self):
        self.base_click(page.login_err_ok_btn)

    # 判断是否登录成功（是否存在 用户名/安全退出 文字链接）
    def page_if_login_success(self):
        return self.base_element_is_exist(page.login_logout_link)  # 一定要return

    # 点击安全退出
    def page_click_logout_link(self):
        self.base_click(page.login_logout_link)

    # 判断是否退出成功(是否左上角存在 登录文字链接)
    def page_if_logout_success(self):
        return self.base_element_is_exist(page.login_logout_link)

    # 组合登录业务方法-->登录操作
    def page_login(self, username, pwd, verify_code):
        log.info("[page_login]:正在执行登录操作 用户名：{}，密码：{}，验证码：{}".format(username, pwd, verify_code))
        # 输入用户名
        self.page_input_username(username)
        # 输入密码
        self.page_input_pwd(pwd)
        # 输入验证码
        self.page_input_verify_code(verify_code)
        # 点击登录按钮
        self.page_click_login_btn()

    # 组合登录业务方法 -->给（购物车，订单模块，支付模块）直接登录使用
    def page_login_success(self, username='15062281268', pwd='123456', verify_code='8888'):
        log.info("[page_login]:正在执行登录操作 用户名：{}，密码：{}，验证码：{}".format(username, pwd, verify_code))
        # 判断是否登录，如果没登录-->点击登录链接执行登录操作，如果已经登录，无需再次登录
        if not self.page_if_login_success():
            print('点击了登陆成功方法--又输入一遍用户信息')
            # 点击登录链接
            self.page_click_login_link()
            # 输入用户名
            self.page_input_username(username)
            # 输入密码
            self.page_input_pwd(pwd)
            # 输入验证码
            self.page_input_verify_code(verify_code)
            # 点击登录按钮
            self.page_click_login_btn()
