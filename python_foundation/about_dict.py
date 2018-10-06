#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dict: key-value {key:value, key:value} key 必须是不可变对象
d = {key1:value1, key2:value2}
访问使用：d[key]
不允许有重复的key，key必须是不可变对象

内置函数：len(dict),str(dict),type(variable)
len(dict):计算字典个数
str(dict):输出字典
type(variable):返回输入变量的类型

内置方法：get(),pop(),clear(),copy(),fromkeys(),items(),keys(),popitem(),setdefault(),update(),values()
get():返回指定键的值，如果没有则使用默认值
pop():删除指定Key的字典
clear():删除字典所有的元素
copy():返回一个字典的浅复制（拷贝父对象，不会拷贝对象的内部的子对象；当子对象变更时候，会同时变更，因为指向了同一个引用）
fromkeys(seq):创建新的字典，以seq中元素做字典的键，value为字典所有的键对应的初始值
items():返回可遍历的元组数组（元组列表）
keys():返回一个迭代器，使用list()转换为列表
popitem():随机返回并删除字典中的一对键和值
setdefault():和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
update(dict2):把字典dict2的键/值对更新到dict里
values():返回一个迭代器，可以使用 list() 来转换为列表
"""

d = {'Rachel': 99, 'Bruce': 88, 'Tina': 92}
# d.pop('Bruce')
print(d['Rachel'], d.get('Rachel'))
d['Test_key'] = 100
print(d)
del d['Test_key']
print(d)

print(d.items())

seq = ('name', 'age', 'sex')
d = dict.fromkeys(seq)
print("新的字典为 : %s" % str(d))

d = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(d))
