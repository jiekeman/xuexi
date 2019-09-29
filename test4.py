# -*- coding: utf-8 -*-
# @Time    : 2019-9-27 15:03
# @Author  : Jie Ke Man
# @FileName: test4.py
# @Software: PyCharm

import re
string = '1-120.0-30-9-2-5-6.0-2.0-80.0'
sub_regular = r'\-?\d*\.?\d*\-\-?\d*\.?\d*'
while re.findall(sub_regular, string):
    sub_value = re.search(sub_regular, string).group() # -1-120.0
    if sub_value.count('-')==2:
        x,y,z = sub_value.split('-')
        sub_resu = '-'+str(float(y)+float(z))
        string = string.replace(sub_value, sub_resu)
    else:
        x,y = sub_value.split('-')
        sub_resu =str(float(x)-float(y))
        string=string.replace(sub_value,sub_resu)

print(string)