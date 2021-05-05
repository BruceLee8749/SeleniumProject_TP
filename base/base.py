from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from base.get_logger import GetLogger
import page
import time

log = GetLogger().get_logger()

# Tips: 方法.点XXX 提示不出来是因为暂时还没有给self.driver赋值Webdriver.FireFox()的原因 不用慌赋值后正常调用 了解即可
class Base:
    # 如果实例化多个对象，就会生成多个新的webdriver浏览器窗口，不推荐在父类中初始化webdriver.Firefox() 使用driver单独用方法封装
    def __init__(self, driver):
        log.info('[base]:正在获取初始化driver对象：{}'.format(driver))
        self.driver = driver;

    # 获取元素方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info('[base:]:正在定位:{}元素，定位位超时时间：{}'.format(loc, timeout))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))  # 使用*表示参数解耦  driver.find_element(*loc) <==>driver.find_element（By.xxx,value)

    # 点击元素方法封装
    def base_click(self, loc):
        log.info('[base:]:正在对:{}元素，进行点击'.format(loc))
        self.base_find(loc).click()

    # 输入元素方法封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空元素
        log.info('[base:]:正在对:{}元素，进行清空操作'.format(loc))
        el.clear()
        # 输入元素
        el.send_keys(value)

    # 获取文本信息方法封装
    def base_get_text(self, loc):
        # 获取元素文本
        log.info('[base:]:正在对:{}元素，获取文本'.format(loc))
        return self.base_find(loc).text

    # 截图方法封装
    def base_get_image(self):
        log.info('[base:]:断言出错，调用截图')
        # 必须这样命名 Y_%m_%d %H_%M_%S.png 否则用 2021-4-20 17:32.png这样命名 文件名会不支持
        self.driver.get_screenshot_as_file('../image/{}.png'.format(time.strftime('%Y_%m_%d %H_%M_%S')))

    # 判断指定元素是否存在
    def base_element_is_exist(self, loc):
        try:
            log.info('[base:]:{}元素查找成功'.format(loc))
            self.base_find(loc, timeout=2)
            return True
        except:
            log.info('[base:]:{}元素查找失败'.format(loc))
            return False

    # 判断是否登录成功（是否存在 用户名/安全退出 文字链接）
    def page_if_login_success(self):
        return self.base_element_is_exist(page.login_logout_link)  # 一定要return

    """
    以下是购物车方法
    """

    # 回到首页（购物车，下订单，支付）都需要用到该方法
    def base_index(self):
        sleep(3)
        self.driver.get(page.url)

    # 切换frame表单方法（可以找到添加购物车成功文字）
    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)

    # 回到默认目录方法（跳出Frame）
    def base_default_content(self):
        self.driver.switch_to.default_content()

    """
    以下为支付模块方法
    """

    # 切换窗口方法
    def base_switch_to_window(self,title):
        log.info('[base:]:{}正在执行切换窗口方法，title值='.format(title))
        self.base_get_title_handle(title)

    # 获取指定title页面的handle
    def base_get_title_handle(self,title):
        # 获取所有handles
        for handle in self.driver.window_handles:
            print('当前窗口的handle',handle)
            # 切换handle
            self.driver.switch_to.window(handle)
            # 获取当前窗口title 并判断是否等于指定参数
            if self.driver.title == title:
                # 返回handle 直接退出整个方法
                return handle


