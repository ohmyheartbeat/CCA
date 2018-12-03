#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  user.py
@time: 2018/11/13 20:25
"""
import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DATETIME
from sqlalchemy import Boolean
from db.domain.base import BASE


class User(BASE):
    """
    用户信息表
    """
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(16))
    password = Column(String(16))
    admin = Column(Boolean())
    creater_id = Column(Integer())
    create_time = Column(DATETIME,default=datetime.datetime.now())
    enable = Column(Boolean())

