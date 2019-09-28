# -*- coding: utf-8 -*-
# @Time    : 2019-9-27 11:21
# @Author  : Jie Ke Man
# @FileName: 计算器2.py
# @Software: PyCharm
import re
s = '3-5-6-7-8-5-2'
while True:
    sub_regular = r'\-?\d*\.?\d*\-\-?\d*\.?\d*'
    sub_list = re.findall(sub_regular, s)
    for sub_str in sub_list:
        numbers = sub_str.split('-')
        if len(numbers) == 3:
            result = 0
            for v in numbers:
                if v:
                    result -= float(v)
        else:
            x, y = numbers
            result = float(x) - float(y)
    print(s)