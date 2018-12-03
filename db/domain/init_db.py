#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  init_db.py
@time: 2018/11/13 20:55
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.domain.user import User
from db.domain.business_record import BusinessRecord
from db.domain.share_info import ShareInfo
from db.domain.base import BASE

if __name__ == "__main__":
    engine = create_engine('sqlite:///../cca.db', echo=True)
    BASE.metadata.create_all(bind=engine)
