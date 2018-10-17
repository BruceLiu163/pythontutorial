#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
静态语言与动态语言的区别之一：
    函数与类的定义，不是编译而是运行期动态创建的

type():
    通过type()函数可以判断对象类型，或者通过type()可以创建类对象；
metaclass():
    define class, init class, init instance
    we can use metaclass define a class.

    metaclass总是以一个metaclass结尾，方便认识


"""


def fn(self, name='world'):
    print('Hello, %s.' % name)


"""
first param:class name
second param:extend object
third param:method name and method
"""
Hello = type('Hello', (object,), dict(hello=fn))  # 通过type定义一个class
h = Hello()
h.hello()
h.hello('Bruce Liu')


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)
