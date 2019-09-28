# -*- coding: utf-8 -*-
# @Time    : 2019-9-23 16:11
# @Author  : Jie Ke Man
# @FileName: 装饰器.py
# @Software: PyCharm
import time


def foo():
    # start = time.time()
    print('foo...')
    time.sleep(2)
    # end = time.time()
    # print('spend %s' % (end - start))


def show_time():

    # def inner():
    start = time.time()
    foo()
    end = time.time()
    print('spend %s' % (end - start))
    # return inner()


show_time(foo())


