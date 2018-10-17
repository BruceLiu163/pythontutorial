#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enum:枚举类
    name,value,members

"""
from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Sun
print(day1, day1.name, day1.value)
for name, member in Weekday.__members__.items():
    print(name, '==>', member, '==>', member.value)
