# -*- coding: utf-8 -*-
# @Time    : 2019-9-23 9:50
# @Author  : Jie Ke Man
# @FileName: day1 练习.py
# @Software: PyCharm


# def print_info(name, age, sex='male'):
#     print('Name: %s' % name)
#     print('Age: %d' % age)
#
#
# def add(*args):
#     sum1 = 0
#     for i in args:
#         sum1 += i
#     print(sum1)
#
#
# add(1, 2, 3)


# if True:
#     x = 3
#
# print(x)

#
# def f2(**kwargs):
#     print(kwargs)


# def f(n):
#     return n*n
#
#
# def foo(a, b, func):
#     func(a)+func(b)
#     ret = func(a)+func(b)
#     return ret
#
#
# print(foo(1, 2, f))


# def fan(n):
#     if n == 1:
#         return 1
#     return n*fan(n-1)
#
#
# print(fan(10))

# str1 = ['a', 'b', 'c']
#
#
# def fun2(s):
#     return s + 'alvin'
#
#
# ret = map(fun2, str1)
# print(list(ret))

import time


def show_time(f):

    def inner():
        start = time.time()
        f()
        end = time.time()
        print('spend:%ss' % (end - start))

    return inner


@show_time
def foo():
    print('foo.....')
    time.sleep(2)


@show_time
def bar():
    time.sleep(3)
    print('bar....')


foo()
bar()





