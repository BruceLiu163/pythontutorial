#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
try:
except:
else:
finally:
"""

try:
    print('try...')
    r = 10 / int(-2)
    print(r)
except ValueError as e:
    print('ValueError', e)
except ZeroDivisionError as ze:
    print('ZeorDivisionError', ze)
else:
    print('no error')
finally:
    print('finally...')
print('end...')
