# -*- coding: utf-8 -*-
# @Time    : 2019-9-28 14:28
# @Author  : Jie Ke Man
# @FileName: 邀请嘉宾小程序.py
# @Software: PyCharm
# guest_list = ['tom', 'jane', 'nike']
# print(guest_list)
# guest_list[1] = 'patrick'
# print(guest_list)
# guest_list.insert(0, 'jake')
# print(guest_list)
# guest_list.append('tim')
# print(guest_list)
# print(guest_list.pop())
# print(guest_list.pop())
# print(guest_list.pop())
# print(guest_list.pop())
# print(guest_list.pop())
# print(guest_list)

#
# digits = [-3, 3, 2, 1, 0]
# print(sum(digits))
#
# for value in range(3,30,3):
#     print(value)

# name_list = ['admin','tom','alex']
#
# if name_list == []:
#     print('We need to find some users')
# else:
#     for name in name_list:
#         if name == 'admin':
#             print('Hello ' + name + ', would you like to see a status report?')
#         else:
#             print('hello ' + name + ' thank you for logging in again')

# current_users = ['admin','tom','alex','jerry','dived']
# new_users = ['admin','tom','alex','patrick','angel']
# for user in new_users:
#     if user.lower() in current_users:
#         print('this '+ user + ' had been used,pls input another name')
#     else:
#         print('this '+ user + ' have not use')
#
# name_list = ['admin','tom','alex']
# newList = []
#
#
# def show_magicians(name1):
#     for magic_name in name1:
#         s = magic_name
#
#     return s
#
#
# def make_great(name):
#         for v in name:
#             name = name.append('the great')
#             print(name)
#
#
#
#
#
# make_great(name_list)

# def build_profile(first,last,**user_info):
#     profile ={}


# def san_list(*food_ing):
#     print(food_ing)
#
#
# san_list('huotui','eggs')
#
# def build_profile(first, last, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics', hobby='girl',film='alex')
# print(user_profile)

# 8-14

def make_car(first,second,**car_info):
    car_list ={}
    car_list['car_name'] = first
    car_list['car_place'] = second
    for key,value in car_info.items():
        car_list[key]=value
    return car_list


car = make_car('BMW','outback',color='blue',model='suv')
print(car)