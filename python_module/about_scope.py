#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
private:
    可以通过_来定义变量或者函数，表示该变量和函数是private，只能在module内部使用

public:
    正常的函数名是public，可以被其它module访问

__xxx__:为特殊变量，可以直接被引用，但是又特殊含义
    __author__
    __name__
    __doc__

"""


def _private_1(name):
    print('Hello, %s!' % name)


def _private_2(name):
    print('Hi, %s!!' % name)


def greeting(name):
    if len(name) > 5:
        _private_1(name)
    else:
        _private_2(name)


greeting('Bruce Liu')
greeting('Tina')
