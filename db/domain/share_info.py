#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  share_info.py
@time: 2018/11/13 20:36
"""
import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy.sql.expression import text
from .base import BASE


class ShareInfo(BASE):
    """
    股票代码信息类
    """
    __tablename__ = "share_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    share_code = Column(String(7), unique=True, index=True)
    share_name = Column(String(64), nullable=False)
    share_type = Column(String(64), nullable=False)
    add_time = Column(DateTime, default=datetime.datetime.now())
    delete = Column(Boolean)
