from selenium import webdriver
import page

# 对driver进行封装 使用类变量--保证多个对象操作同一个webdriver（如果使用同一个webdriver，就相当于多个对象使用同一个打开的浏览器进行各种操作）
# 如果在base初始化方法中直接初始化webdriver，那么每当实例化base的子类后都会生成一个新的webdriver ---且每次新生成的webdriver都是两个完全不同的webdriver
"""
每当实例化一个Base的子类后都会调用一次webdriver.Firefox() 
每次调用webdriver.Firefox()方法都会新生成一个webdriver（他们是两个完全不同的webdriver）--->相当于新开一个浏览器
如果多个对象使用同一个webdriver，就相当于多个对象在同一个浏览器下进行各种操作。
"""


class GetDriver:
    # 将driver变成类变量：通过类名.类变量 所有此类的实例均可以共享这一个driver并修改类变量。
    driver = None

    @classmethod
    # 如果没有生成driver，就初始化一个webdriver；如果已经有了webdriver直接返回该driver即可。
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Firefox()
            # cls.driver.maximize_window()
            # 打開首頁
            cls.driver.get(page.url)
        return cls.driver

    # 关闭driver也要封装。直接quit()，driver不会为None --->导致调用get_driver()方法driver生成不了
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit() # 用例执行完退出浏览器窗口
            cls.driver = None # 虽然quit了driver-->即：退出了浏览器，但driver变量还存在。需再次手动赋值为None，调用get_driver方法才能重新生成一个driver

