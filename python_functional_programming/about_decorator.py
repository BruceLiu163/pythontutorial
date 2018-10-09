#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Decorator:装饰器
    是一个返回函数的高阶函数，接受一个函数，返回一个函数
    代码运行期动态增加的功能的方式，称之为装饰器
"""
import functools


def now():
    print('2018-10-09')


f = now
print(f.__name__)
print(now.__name__)


def log(func):
    """能打印日志的decorator"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


def log_params(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, ** kwargs)
        return wrapper
    return decorator


# @log 相当于执行了 my_now = log(my_now)
@log
def my_now():
    print('2018-10-09')


@log_params('execute')
def your_now():
    print('2018-10-09')


my_now()
your_now()
print(my_now.__name__)
print(your_now.__name__)
