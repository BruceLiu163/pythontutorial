#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
function params:
1、位置参数
2、默认参数  默认参数必须放在位置参数的后面     默认参数可以降低函数的难度   默认参数必须是不可变对象
3、可变参数  *param  如果已经有了一个list或者tuple，可以在变量前面添加*变为可变参数
    可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
4、关键字参数 **kw
    关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
    如果已经有一个dict变量，可以使用**dict作为参数传入
5、命名关键字 *, age, job    或者 *args, age, job
    使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符
    命名关键字参数可以有缺省值   命名关键字参数可以有缺省值   命名关键字参数可以有缺省值
    命名关键字参数可以有缺省值   命名关键字参数可以有缺省值   命名关键字参数可以有缺省值
    命名关键字参数可以有缺省值   命名关键字参数可以有缺省值   命名关键字参数可以有缺省值


参数组合问题：
    顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数
    顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数
    顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数
    顺序：必须参数、默认参数、可变参数、命名关键字参数、关键字参数
    顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数


对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

"""


def my_calc(*numbers):
    """使用可变参数"""
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n
    return sum1


def person(name, age, **kw):
    """使用关键字参数"""
    print('name:', name, 'age:', age, 'other:', kw)


def my_person(name, age, *, city='Beijing', job):
    """命名关键字参数"""
    print(name, age, city, job)


# def f1(name, age, *, city='Beijing', job, **kw):
#     print(name, age, city, job, kw)
#
#
# def f2(name, age, *args, city='Beijing', job, **kwargs):
#     print(name, age, args, city, job, kwargs)

def f1(a, b, c=0, *args, **kwargs):
    print(a, b, c, args, kwargs)


def f2(a, b, c=0, *args, city='Beijing', job, **kwargs):
    print(a, b, c, args, city, job, kwargs)


print(my_calc(1, 3, 5))

L = [1, 3, 5, 7]
print(my_calc(*L))

person('Bruce', 30)
person('Bruce', 30, city='Shanghai')
person('Bruce', 30, city='Shanghai', job='Manager')

D = {'city': 'Shanghai', 'job': 'Manager', 'score': 90}
person('Bruce', 40, **D)


my_person('Bruce', 30, job='Manager')
my_person('Bruce', 30, city='Shanghai', job='Manager')

f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b', 'c', age=18)

f2(1, 2, 3, 4, 5, 6, job='Manager', zipcode='111111')
f2(1, 2, 3, 4, 5, 6, city='Shanghai', job='Manager', zipcode='111111')



