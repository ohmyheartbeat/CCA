#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  app.py.py
@time: 2018/11/13 10:52
"""
import sys
from interface.window import APP
from interface.window import WINDOW
from interface.menu_qt import MenuQt


def main():
    """
    主程序入口
    """
    MenuQt.init_window()
    WINDOW.show()
    sys.exit(APP.exec_())


if __name__ == "__main__":
    main()
