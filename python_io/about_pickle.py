#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pickle:
    python的序列化，反序列化
"""
import pickle

dict_1 = dict(name='Bruce', age=20, gender='F')
dict_2 = {'name': 'Bruce', 'age': 20, 'gender': 'F'}

print(dict_1)
print(dict_2)

print(pickle.dumps(dict_1))

with open('dump.txt', 'wb') as f:
    pickle.dump(dict_1, f)

with open('dump.txt', 'rb') as ff:
    dict_3 = pickle.load(ff)

print(dict_3)
