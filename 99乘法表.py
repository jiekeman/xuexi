# -*- coding: utf-8 -*-
# @Time    : 2019-9-28 10:07
# @Author  : Jie Ke Man
# @FileName: 99乘法表.py
# @Software: PyCharm
# count1 = 1
# while count1 <= 9:
#     print(count1, end='')
#     count = 1
#     while count <= 9:
#         print('*', end='')
#         count += 1
#     print()
#     count1 += 1

# hight_s = int(input('输入一个高度:'))
# wigth_s = int(input('输入一个宽度'))
# count = 1
# while count <= hight_s:
#     count1 = 0
#     while count1 < wigth_s:
#         print('*', end='')
#         count1 += 1
#     print()
#     count += 1
line = 1
while line < 9:
    # print('*')
    temp = line
    while temp > 0:
        print('*', end='')
        temp -= 1
    print()
    line += 1
# first = 1
# while first <= 9:
#     sec = 1
#     while sec <= first:
#         print(str(sec) + '*' + str(first) + '=', sec * first, end='\t')
#         sec += 1
#     print()
#     first += 1
