# 导入HTMLTestRunner 需要去网站上下载该文件
# 通过该类 调用自动化测试组件、生成自动化测试报告
from tools.HTMLTestRunner import HTMLTestRunner
import time
import unittest

# 定义测试套件suite   在scripts文件目录下：寻找所有以test开头的py文件。并将其中所有测试用例（test开头的方法） 添加到组件中。
suite = unittest.defaultTestLoader.discover('./', pattern='test*.py')  # discover('目录',pattern='py文件名')
# 报告生成目录和文件目录
dir_path = '../report/{}.html'.format(time.strftime('%Y_%m_%d %H_%M_%S'))
# 获取文件流并调用run运行测试组件suite
# wb是用二进制写
with open(dir_path,'wb') as f:
    HTMLTestRunner(stream=f,title='TPSHOP商城自动化测试报告',description='操作系统：win10 X64 author:LeiWei 2020-4-27').run(suite)