#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


# 定义User对象
class User(Base):
    # 定义表名
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:000000@localhost:3306/python_db')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 添加一行记录
session = DBSession()
# new_usr = User(id='4', name='Bob')
# session.add(new_usr)
# session.commit()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '5').one()
print(user.name, user.id)

session.close()

