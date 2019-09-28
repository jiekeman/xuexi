# -*- coding: utf-8 -*-
# @Time    : 2019-9-24 9:14
# @Author  : Jie Ke Man
# @FileName: day2 练习.py
# @Software: PyCharm


# def bar():
#     print('ok1')
#     count = yield 1
#     print(count)
#
#     yield 2
#
#
# b = bar()
#
# b.send(None)
# ret = b.send('eee')
# print(ret)

# import time
# # print(help(time))
# # print(time.gmtime())
# # print(help(time.strftime))
# # print(time.ctime(2))
# print(help(time.mktime))
#
# import random
# print(help(random.choice))
# import os
# help(os)
# import sys
# print(sys.argv)


# import logging


# # def logger():
# logger = logging.getLogger()
# # 创建一个handler.用于写入日志文件
# fh = logging.FileHandler('test.log')
#
# # 创建一个handler  用于输出到控制台
# ch = logging.StreamHandler()
#
# formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s ')
#
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# logger.setLevel(logging.DEBUG)
#
# logger.debug('logger debug message')
# logger.info('info debug message')
# logger.warning('warning debug message')
# logger.error('error debug message')
# logger.critical('critical debug message')

# import configparser
#
# config = configparser.ConfigParser()


# import re

# s = 'hello world'

# ret = re.findall('w..l', 'hello world')
# print(ret)
# ret = re.findall('alex', 'sdalalexdsadealexsdadwxada')
# print(ret)

# ret = re.findall('^h...o', 'headollo world')
# print(ret)

# ret = re.findall('[a-z]', 'aex')
# print(ret)

# print(re.findall('\\d{11}', '12346123123123123'))

# s = 'hello world'
# print(s.find('l'))

# import re

# print(re.findall('[w,]', 'w,wr'))
# ret = re.search('\\d[^()]\\d', '1+(5+(5+5)+3)').group()
# x, y = ret.split('+')
# z = float(x) + float(y)
# print(z)
import re

# a = 'life is short , i use python.i love python'
#
# r1 = re.search('life(.*)python(.*)python', a)
# print(r1)
# # print(r1.group(0))  # 全打印
# # print(r1.group(1))  # 打印第一个组
# # print(r1.group(2))  # 打印第二个组
# print(r1.group(0, 1, 2))  # group可以连续打印

# ret = re.findall('(as)+', 'sdadasfasf')
# print(ret)

# ret = re.search('(?P<id>\\d{3})/(?P<name>\\w{3})', 'weeew34ttt123/ooo')
# print(ret.group())  # 123/ooo
# print(ret.group('id'))  # 123
# print(ret.group('name'))  # ooo
# ret = re.match('asd', 'asdfhdsasd')
# print(ret.group())
# ret = re.split('[j,s]', 'djksal')
# print(ret)
import re
# ret = re.search('\\([^()]\\)', '2+3+(5+(3+8))')
# print(ret)
# s = '234'
source = '5+3+(60-30+(-9-2-5-0.5*3-5/3-40*4/2-3/5+6*3))'
# ret = re.search('\\([^()].*\\)', source).group()
# print(ret.count('*'))
# regular = '\\d*\\.?\\d*[*/]\\d*\\.?\\d*'
# ret = re.search(regular, source).group()
# print(ret.count('*'))

# def mul_div(string):
#     # 从字符串中获取一个乘法或者除法的表达式
#     regular = '\\d*\\.?\\d*[*/]\\d*\\.?\\d*'
#     # 使用一个while循环检测
#     while re.findall(regular, string):
#         expression = re.search(regular, string).group()   # 这是一个列表
#         # print(type(expression))
#         # 检测如果是乘法 用乘法计算
#         if expression.count('*') == 1:
#             x, y = expression.split('*')
#             mul_result = str(float(x)*float(y))
#             string = string.replace(expression, mul_result)
#
#         if expression.count('/') == 1:
#             x, y = expression.split('/')
#             mul_result = str(float(x)/float(y))
#             string = string.replace(expression, mul_result)
#
#     return string
#
# mul_div(source)
x == 6.3
y == 3.5
print(x*y)
