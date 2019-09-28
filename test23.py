# -*- coding: utf-8 -*-
# @Time    : 2019-9-27 13:37
# @Author  : Jie Ke Man
# @FileName: test23.py
# @Software: PyCharm
import re


# def format_check(string):
#     string = string.replace('++', '+')
#     string = string.replace('-+', '-')
#     string = string.replace('--', '+')
#     string = string.replace('+-', '-')
#     string = string.replace('*+', '*')
#     string = string.replace('/+', '/')
#     string = string.replace(' ', '')
#     return string


# s = '5+3+5+4+2+6+9+5'

# sub_check = '[\\-]?\\d+\\.?\\d*\\-[\\-]?\\d+\\.?\\d*'


# def add_result(s):
#
#     while 1:
#         add_check = '[\\-]?\\d+\\.?\\d*\\+[\\-]?\\d+\\.?\\d*'
#         s1_list = re.findall(add_check, s)
#         for s1_value in s1_list:
#             x, y = s1_value.split('+')
#             result = str(float(x)+float(y))
#             s = s.replace(s1_list, result)
#             s = format_check(s)
#     return s
#
#
#
#
# s1 = add_result('5+3+4')
# print(s1)


# else:
#     s2 = re.search(sub_check, s).group()
#     x, y = s2.split('-')
#     result = '-' + str(float(x) - float(y))
#     s = s.replace(s2, result)
#     s = format_check(s)
#     print(s)
# for i in range(1, 9):
# i = 0
# while i < 9:
#     print('*')
#     i += 1
#     z = 0
#     while z < 5:
#         print('+', end='')
#         z += 1


s = 'ssda'
