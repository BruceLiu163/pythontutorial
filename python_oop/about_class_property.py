#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
property:
    使用property装饰器，定义属性
    @property装饰器就是负责把一个方法变成属性调用

    Python内置的@property装饰器就是负责把一个方法变成属性调用
    Python内置的@property装饰器就是负责把一个方法变成属性调用
    Python内置的@property装饰器就是负责把一个方法变成属性调用
"""


class Student(object):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('---name must be str!!---')
        self._name = name


stu1 = Student()
stu1.name = 'Bruce Liu'
print(stu1.name)
