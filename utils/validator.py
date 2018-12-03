#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  validator.py
@time: 2018/12/1 9:10
"""
from PyQt4.QtGui import QDoubleValidator
from PyQt4.QtGui import QRegExpValidator
from PyQt4.QtCore import QRegExp
from constant.window_cons import WindowCons

class DoubleValidator(QDoubleValidator):
    """双精度浮点数校验"""

    def __init__(self):
        QDoubleValidator.__init__(self)
        self.setRange(1.00, 999.00, 2)


class IntValidator(QDoubleValidator):
    """整数浮点数校验"""

    def __init__(self):
        QDoubleValidator.__init__(self)
        self.setRange(100, 99999999900, 0)


class RegExpValidator(QRegExpValidator):
    """股票代码校验规则"""
    def __init__(self):
        QRegExpValidator.__init__(self)
        self.setRegExp(QRegExp(WindowCons.SHARE_CODE_LEN_REG))
        # self.setRegExp(QRegExp(WindowCons.SHARE_CODE_REG))
