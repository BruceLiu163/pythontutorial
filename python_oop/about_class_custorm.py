#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用class提供的内置变量和方法
__slots__:限制类的实例属性
__len__():让class能作用于len()方法
__str__():返回用户看到的字符串
__repr__():返回程序看到的字符串
__iter__():
    如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
    该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
    直到遇到StopIteration错误时退出循环。
__next__():迭代对象的获取下一个值

__getItem__():
    让类拥有通过下标获取元素的能力

__getattr__():动态获取属性,或者方法
__call__():直接在实例上进行调用，不用显示声明方法
    直接在实例上使用()调用
    stu_1 = Student()
    stu_1()    默认会进行__call__()方法的调用

    对实例进行直接调用就好比对一个函数进行调用一样，
    所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

    通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
    通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
    通过callable()函数，我们就可以判断一个对象是否是“可调用”对象

"""


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
            return a


for n in Fib():
    print(n)

f = Fib()
print(f[1], f[2], f[5])


class Student(object):
    # __slots__ = ('name', 'age', 'gender')

    def __init__(self, name='Bruce', age=0, gender='F'):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __repr__(self):
        self.__str__()

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'address':
            return lambda: 'Shanghai'
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

    def __call__(self, *args, **kwargs):
        print('My name is %s.' % self.name)


print(Student()())


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def users(self, name):
        return Chain('%s/%s' % (self._path, name))

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().status.users('Bruce').timeline.list)
