import unittest
from time import sleep

import parameterized as parameterized

from base.get_driver import GetDriver
from page.page_login import PageLogin  # 将PageLogin类导入到该文件中
import json
from base.get_logger import GetLogger

log = GetLogger().get_logger()


def get_data():
    # username, pwd, verify_code, status, expect_result
    with open('../data/login.json', "r", encoding='UTF-8') as f:
        dict_data = json.load(f)
        list_data = list(dict_data.values())
    print(list_data)
    return list_data


# 流程 ：注意 默认一开始主页用户没有登录状态 很重要！否则需要很多判断
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            # 实例化对象并获取driver  -->GetDriver()对象会共享里面类对象的值
            cls.driver = GetDriver().get_driver()
            # 实例化PageLogin类 注意：用cls调用 用self也可以调类属性和类方法 反之不行
            cls.login = PageLogin(cls.driver)
            # cls.login.driver.maximize_window()
            # cls.login.driver.get('url')

            # 初始化 点击登录链接方法 注意：用cls调用  类方法只初始化一次
            cls.login.page_click_login_link()
        except Exception as e:
            log.error('错误：{}'.format(e))
            # 调用截图方法
            # TestLogin(unittest.TestCase).login.base_get_image() # 用实例和用类名调用类方法一样的效果。
            cls.login.base_get_image();

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器对象 让类变量重新为None，否则下条case中永远使用这一个窗口（因为不会生成新driver），流程会出错。
        GetDriver().quit_driver();
        pass

    @parameterized.parameterized.expand(get_data())
    def test_login(self, username, pwd, verify_code, status, expect_result):
        # 调用登录 操作组合业务方法（输入用户名,密码,验证码点击登录）
        self.login.page_login(username, pwd, verify_code)
        print('开始登录')
        # 正向用例
        if status:
            GetDriver().get_driver().implicitly_wait(10)
            # 判断是否登录成功
            self.assertTrue(self.login.page_if_login_success())
            # 点击退出登录
            GetDriver().get_driver().implicitly_wait(10)
            self.login.page_click_logout_link()
            print('是否退出成功', self.assertTrue(TestLogin.login.page_if_logout_success()))
            # 再次点击登录链接回到注册页面
            self.login.page_click_login_link()
        # 逆向用例
        else:
            # 获取错误提示信息
            msg = self.login.page_get_error_info()
            print("打印错误提示框文本", msg)
            self.assertEqual(msg, expect_result)
            # self.login.base_get_image()
            self.login.page_click_error_alert()
