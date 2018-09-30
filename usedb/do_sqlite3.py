#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入mysql驱动
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 创建表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录 占位符是%s
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
cursor.rowcount

# 提交事务
conn.commit()
cursor.close()

# query data
cursor = conn.cursor()
cursor.execute('select * from user where id = ?', ('1',))
values = cursor.fetchall()
print(values)
# close cursor and conn
cursor.close()
conn.close



