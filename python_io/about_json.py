#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
json:
    处理json格式，json和python对象间的对应关系如下：

    JSON类型      Python类型
    {}              dict
    []              list
    "string"        str
    1234.56         int/float
    true/false      True/False
    null            None

json模块的dumps()和loads()函数是定义得非常好的接口的典范。
当我们使用时，只需要传入一个必须的参数。
但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
既做到了接口简单易用，又做到了充分的扩展性和灵活性。

"""
import json

dict_1 = dict(name='Bruce', age=20, score=100)
json_1 = json.dumps(dict_1)
print(json_1)

dict_2 = json.loads(json_1)
print(dict_2)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'name=%s, age=%s, score=%s' % (self.name, self.age, self.score)

    __repr__ = __str__


stu_1 = Student('Bruce', 30, 99)

json_2 = json.dumps(stu_1, default=lambda obj: obj.__dict__)
print(json_2)


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


stu_2 = json.loads(json_2, object_hook=dict2student)
print('stu_2=', stu_2)
