from selenium import webdriver
class Base:
    driver = 1

    @classmethod
    def get_driver(cls):
        # cls.driver = webdriver.Firefox()  # 每当调用一次webdriver.Firefox()方法，都会新生成一个webdriver（新启动一个浏览器）
        if cls.driver == 1:
            cls.driver = cls.driver + 1  # 每当调用一次webdriver.Firefox()方法，都会新生成一个webdriver（新启动一个浏览器）


class C(Base):
    def printC(self):
        print('This is C')
        print(self.driver)


class D(Base):
    def printD(self):
        print('This is D')
        print(self.driver)


if __name__ == '__main__':
    c = C()
    c.get_driver()
    c.printC()
    d = D()
    d.get_driver()
    d.printD()