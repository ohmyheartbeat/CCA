#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  db_util.py
@time: 2018/11/14 11:22
"""
import os
import sys
import shutil
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from db.domain.base import BASE
from db.domain.user import User
from db.domain.share_info import ShareInfo
from db.domain.business_record import BusinessRecord
from constant.window_cons import WindowCons

if getattr(sys, 'frozen', False):
    db_dir = "/./cca.db"
else:
    db_dir = '/../CCA/db/cca.db'


class DbUtil(object):
    """
    操作数据库的类
    """
    engine = create_engine('sqlite://' + db_dir)
    db_session = sessionmaker(bind=engine)
    session = db_session()

    @classmethod
    def add_record(cls, object):
        """
        向数据表中增加记录
        :param kwargs: 参数
        """
        cls.session = cls.db_session()
        cls.session.add(object)
        cls.__commit()

    @classmethod
    def query_share_info_by_code(cls, share_code):
        """根据股票代码查询股票信息"""
        cls.session = cls.db_session()
        share_info = cls.session.query(ShareInfo).filter_by(share_code=share_code).first()
        cls.session.close()
        return share_info

    @classmethod
    def query_share_info_like_code(cls, share_code):
        """模糊查询股票信息"""
        cls.session = cls.db_session()
        share_info_list = cls.session.query(ShareInfo).filter(ShareInfo.share_code.like("%" + share_code + "%")).all()
        cls.session.close()
        return share_info_list

    @classmethod
    def query_business_record(cls, **kwargs):
        """查询所有股票交易记录"""
        cls.session = cls.db_session()
        business_record = cls.session.query(BusinessRecord).filter_by(**kwargs).all()
        cls.session.close()
        return business_record

    @classmethod
    def query_last_business_record(cls, share_id):
        """查询最后一条交易记录"""
        cls.session = cls.db_session()
        business_record = cls.session.query(BusinessRecord).filter_by(share_id=share_id).order_by(
            BusinessRecord.id.desc()).first()
        cls.session.close()
        return business_record

    @classmethod
    def import_share_info_list(cls, share_info_list):
        """导入新的股票信息"""
        if len(share_info_list) == 0:
            return False
        cls.session = cls.db_session()
        cls.session.add_all(share_info_list)
        cls.__commit()
        return True

    @classmethod
    def query_user(cls, username, password):
        """查询用户是否存在"""
        cls.session = cls.db_session()
        user = cls.session.query(User).filter_by(username=username, password=password, enable=1).first()
        cls.session.close()
        return user

    @classmethod
    def import_share_info(cls, share_code, share_name, share_type):
        """新增股票信息"""
        share_info = ShareInfo(share_code=share_code, share_name=share_name, share_type=share_type,
                               delete=WindowCons.TRUE_NUMBER)
        cls.session = cls.db_session()
        cls.session.add(share_info)
        cls.session.commit()
        cls.session.close()

    @classmethod
    def __commit(cls):
        cls.session.commit()
        cls.session.close()
