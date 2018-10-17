#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
os:
    环境信息
    环境变量
    dir

"""

import os

TEST_DIR = 'test_dir'

PATH_DIR = '/Users/BruceLiu/dev/python/PycharmProjects/pythontutorial/python_io'

print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))
print(os.path.join('%s' % PATH_DIR, '%s' % TEST_DIR))
if not os.path.exists(os.path.join(PATH_DIR, TEST_DIR)):
    os.mkdir(os.path.join(PATH_DIR, TEST_DIR))
os.rmdir(os.path.join(PATH_DIR, TEST_DIR))

# 合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
print('os.path.split(PATH_DIR)=', os.path.split(PATH_DIR))
print('os.path.splitext(PATH_DIR)=', os.path.splitext(PATH_DIR))
print('os.path.basename(PATH_DIR)=', os.path.basename(PATH_DIR))
print('os.path.isfile(PATH_DIR)=', os.path.isfile(PATH_DIR))
print('os.path.exists(PATH_DIR)=', os.path.exists(PATH_DIR))
print('os.path.dirname(PATH_DIR)=', os.path.dirname(PATH_DIR))
# print('os.path.commonpath(PATH_DIR)=', os.path.commonpath(PATH_DIR))
print('os.path.commonprefix(PATH_DIR)=', os.path.commonprefix(PATH_DIR))


# 一行打印当前目录下所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
