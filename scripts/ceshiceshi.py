import json
from time import sleep

from selenium import webdriver

"""
class A:
    def get_data(self):
        # username, pwd, verify_code, status, expect_result
        with open('../data/login.json', "r", encoding='UTF-8') as f:
            dict_data = json.load(f)
            list_data = list(dict_data.values())
        print(dict_data)
        print(list_data)
    def compatrestr(self):
        if('True' == 1):
            print('True==1')
        if('True' == True):
            print('True == True')
        if("1" == 1):
            print("True == 1")
        if(True == 10):
            print("True == 10")
        if(True ==1):
            print('True==1')

if __name__ == '__main__':
    a = A()
    a.get_data()
    a.compatrestr()
"""

"""
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.quit()
print(driver)
driver = None
print('再次打印',driver)
if driver == True:
   print(driver)
"""

# driver.get('http://www.taobao.com')
# sleep(3)
# driver.quit()

"""
# 案例一：如果在Base初始化方法中直接初始化webdriver，那么每当实例化一个Base的子类后都会调用一次webdriver.Firefox() 
# 每次调用webdriver.Firefox()方法都会新生成一个webdriver（他们是两个完全不同的webdriver）--->相当于新开一个浏览器
# 如果多个对象使用同一个webdriver，就相当于在同一个浏览器下进行各种操作。
class Base:
    def __init__(self):
        self.driver = webdriver.Firefox()


class C(Base):
    def printC(self):
        print('This is C')
        print(c.driver)


class D(Base):
    def printD(self):
        print('This is D')
        print(d.driver)


if __name__ == '__main__':
    c = C()
    c.printC()
    d = D()
    d.printD()
    if c.driver != d.driver:
        print('c.driver != d.driver')
    sleep(10)
    c.driver.quit()
    d.driver.quit()

"""


# 案例二：通过静态变量(类变量)，实现多个实例化对象共用一个webdriver（不是子类！如果子类继承需要使用别的方式）
class Base:
    # driver = None
    #
    # @classmethod
    # def get_driver(cls):
    #     # cls.driver = webdriver.Firefox()  # 每当调用一次webdriver.Firefox()方法，都会新生成一个webdriver（新启动一个浏览器）
    #     if cls.driver is None:
    #         cls.driver = webdriver.Firefox()  # 每当调用一次webdriver.Firefox()方法，都会新生成一个webdriver（新启动一个浏览器）
    #         print('driver 为空')
    driver = None

    def get_driver(self):
        if Base.driver is None:
            Base.driver = webdriver.Firefox()  # 每当调用一次webdriver.Firefox()方法，都会新生成一个webdriver（新启动一个浏览器）
            print('driver 为空')


class C(Base):
    def printC(self):
        print('This is C')
        print(self.driver)


class D(Base):
    def printD(self):
        print('This is D')
        print(self.driver)


if __name__ == '__main__':
    # c1 = C()
    # c1.get_driver)
    # print(c1.driver)
    # c2 = C()
    # c2.get_driver()
    # print(c2.driver)
    c1 = C()
    c1.get_driver()
    print(c1.driver)
    d1 = D()
    d1.get_driver()
    print(d1.driver)
    """
    base1 = Base()
    base1.get_driver()
    print('base1->driver is',base1.driver)1`
    sleep(5)
    base2 = Base()
    base2.get_driver()
    print('base2->driver is', base2.driver)
    base2.driver.get('http://www.baidu.com')
    sleep(3)
    base1.driver.get('http://www.taobao.com')
    if base1.driver != base2.driver:
        print('c.driver != d.driver')
    else:
        print('c.driver == d.driver')
    sleep(10)
    base1.driver.quit()
    base2.driver.quit()
    """

    """
    c = C()
    c.get_driver()
    c.printC()
    d = D()
    d.get_driver()
    d.printD()
    if c.driver != d.driver:
        print('c.driver != d.driver')
    else:
        print('c.driver == d.driver')
    sleep(10)
    c.driver.quit()
    d.driver.quit()
    """
