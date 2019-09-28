# -*- coding: utf-8 -*-
# @Time    : 2019-9-26 9:04
# @Author  : Jie Ke Man
# @FileName: 简单计算器.py
# @Software: PyCharm

# 1+2+(3*5)+5


import re


# 定义检查函数
def check_expression(string):
    check_result = True
    if string.count('(') != string.count(')'):
        print('Unclosed parentheses')
        check_result = False
    if re.findall('[a-zA-Z]', string):
        print('unallowable character')
        check_result = False

    return check_result


# 定义格式化输出
def format_result(string):
    string = string.replace('++', '+')
    string = string.replace('-+', '-')
    string = string.replace('--', '+')
    string = string.replace('+-', '-')
    string = string.replace('*+', '*')
    string = string.replace('/+', '/')
    string = string.replace(' ', '')
    return string


# 定义乘除法
def mul_div(string):
    # 从字符串中获取一个乘法或者除法的表达式
    regular = '\\d*\\.?\\d*[*/]\\d*\\.?\\d*'
    # 使用一个while循环检测
    while re.findall(regular, string):
        expression = re.search(regular, string).group()
        # print(type(expression))
        # 检测如果是乘法 用乘法计算
        if expression.count('*') == 1:
            x, y = expression.split('*')
            mul_result = str(float(x)*float(y))
            string = string.replace(expression, mul_result)
            string = format_result(string)

        if expression.count('/') == 1:
            x, y = expression.split('/')
            mul_result = str(float(x)/float(y))
            string = string.replace(expression, mul_result)
            string = format_result(string)

    return string


# 定义加减法
def add_sub(string):
    add_regular = '[\\-]?\\d*\\.?\\d \\+ [-]?\\d*\\.?\\d '
    sub_regular = r'\-?\d*\.?\d*\-\-?\d*\.?\d*'
    # 一个一个找出加法的格式计算并替换
    while re.findall(add_regular, string):
        add_list = re.findall(add_regular, string)
        for add_str in add_list:
            x, y = add_str.split('+')
            add_result = '+' + str(float(x) + float(y))
            string = string.replace(add_str, add_result)
        string = format_result(string)

    while re.findall(sub_regular, string):
        sub_list = re.findall(sub_regular, string)
        for sub_str in sub_list:
            numbers = sub_str.split('-')
            if len(numbers) == 3:
                result = 0
                for v in numbers:
                    if v:
                        result -= float(v)
            else:
                x, y = numbers
                result = float(x)-float(y)
            string = string.replace(sub_str, '+' + str(result))
        string = format_result(string)

    return string


source = '1-2*(60-30+(-9-2-5-2*3-6/3-40*4/2-10/5+6*3))'
if check_expression(source):
    print('source:', source)
    print('eval result:', eval(source))
    source = format_result(source)
    print(source)

    while source.count('(') > 0:  # 拿到了括号最里层的3*5
        strs1 = re.search('\\([^()]*\\)', source).group()  # 拿到了括号最里层的3*5
        replace_str = mul_div(strs1)
        replace_str = add_sub(replace_str)
        source = format_result(source.replace(strs1, replace_str[1:-1]))

    else:
        replace_str = mul_div(source)
        replace_str = add_sub(replace_str)
        source = source.replace(source, replace_str)

    print('my result', source.replace('+', ''))


