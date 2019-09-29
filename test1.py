# -*- coding: utf-8 -*-
# @Time    : 2019-9-27 10:44
# @Author  : Jie Ke Man
# @FileName: test1.py
# @Software: PyCharm
import re


# def add_sub(string):
#     add_regular = ']?\\d*\\.?\\d \\+ [-]?\\d*\\.?\\d '
#     sub_regular = '[-]?\\d*\\.?\\d \\- [-]?\\d*\\.?\\d'
#     # 一个一个找出加法的格式计算并替换
#     while re.findall('add_regular', string):
#         add_list = re.search(add_regular, string).group()
#         x, y = add_list.split('+')
#         add_result = str(float(x) + float(y))
#         string = string.replace(add_list, add_result)
#
#     while re.findall('sub_regular', string):
#         sub_list = re.search('sub_regular', string).group()
#         for sub_str in sub_list:
#             numbers = sub_str.split('-')
#             if len(numbers) == 3:
#                 result = 0
#                 for v in numbers:
#                     if v:
#                         result -= float(v)
#             else:
#                 x, y = numbers
#                 result = float(x)-float(y)
#         string = string.replace(sub_str, '+' + str(result))
#
#     return string


# add_sub('5+3-4')
s='1+34.0'
sub_regular = r'[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*'
s1=re.search(sub_regular,s).group()
x, y = s1.split('+')
s2= str(float(x)+float(y))
print(s2)