#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  gui_parts.py
@time: 2018/12/1 10:08
"""
from PyQt4.QtGui import QCompleter
from PyQt4.QtGui import QMessageBox


class Completer(QCompleter):
    """智能提示组件"""

    def __init__(self, *__args):
        QCompleter.__init__(self, *__args)
        self.setMaxVisibleItems(10)

        # self.thread()
        # self.setModelSorting(self.CaseInsensitivelySortedModel)
        # self.


class MessageBox(QMessageBox):
    """提示框"""
    OK_CN = "确定"
    CANCEL_CN = "取消"
    OK_NO = 0
    CANCEL_NO = 1
    POINT_OUT_TITLE = "提示"

    def __init__(self, widget):
        QMessageBox.__init__(self)
        self.widget = widget

    def point_out(self, message, *_args):
        """提示"""
        self.information(self.widget, self.POINT_OUT_TITLE, message, MessageBox.OK_CN, *_args)

    def ask_ok(self, message, *_args):
        """询问选择"""
        return self.question(self.widget, self.POINT_OUT_TITLE, message, MessageBox.OK_CN, MessageBox.CANCEL_CN, *_args)
