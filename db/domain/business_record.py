#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  business_record.py
@time: 2018/11/13 20:40
"""
import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from db.domain.base import BASE


class BusinessRecord(BASE):
    """
    交易记录
    """

    __tablename__ = 'business_record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    share_id = Column(Integer(), ForeignKey("share_info.id"), nullable=False)
    buy_time = Column(DateTime())
    sale_time = Column(DateTime())
    buy_price = Column(Float())
    sale_price = Column(Float())
    buy_num = Column(Integer())
    sale_num = Column(Integer())
    curr_num = Column(Integer())
    buy_avg_price = Column(Float())
    final_profit = Column(Float())
    create_time = Column(DateTime, default=datetime.datetime.now())
    creater_id = Column(Integer, ForeignKey("user.id"))
    delate = Column(Boolean())
