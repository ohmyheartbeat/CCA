#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  window_cons.py
@time: 2018/11/14 15:44
"""
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import QSizePolicy
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class WindowCons(object):
    """窗口的常量"""
    EXE_NAME = "驰骋A股"  # exe程序左上角的名称
    WINDOW_SIZE = "960x540"  # 初始窗口大小
    LOGIN_SIZE = "640x320"  # 登录窗口大小
    LOGIN_NAME = "Username"
    LOGIN_PASSWORD = "Password"
    QUIT_ACTION = "WM_DELETE_WINDOW"
    LOGIN_SUCCESS = False  # 记录登录状态
    LOGIN_USER_ID = None  # 记录id
    ADD_BUSINESS_FRAME_NAME = "新增交易记录"
    LOGIN_STATUS_FILE = "./cache.data"
    IMPORT_FRAME_NAME = "导入股票信息"
    SPACE_SYMBOL = " "
    COMMA_SYMBOL = ","
    TRANSFER_SYMBOL = "\t"  # 文件中的转义字符
    FALSE_NUMBER = 0
    TRUE_NUMBER = 1
    SHARE_CODE_LENGTH = 6
    CODE_FILL_STR = "0"
    MONO_FAMILY = "Microsoft YaHei"
    YAHEI_UI_FAMILY = "Microsoft YaHei UI"
    YAHEI_LIGHT_FAMILY = "Microsoft YaHei UI Light"
    JUI_LIGHT_FAMILY = "Microsoft JhengHei UI Light"
    LIGHT_BLUE_STYLE = "QLabel{color:rgb(137, 207, 240)}"  # 淡蓝色
    WHITE_STYLE = "QLabel{color:rgb(255, 255, 255)}"  # 白色
    SKY_BLUE_STYLE = "QLabel{color:rgb(35, 25, 220)}"
    WEI_BLUE_STYLE = "QLabel{color:rgb(255, 255, 255)}"
    TRANSPARENT = "QTextEdit{background: transparent;color:rgb(255,255,255)}"
    RED_STYLE = "#statusbar{color:rgb(255,0,0)}"
    PRICE_DEFAULT = "0.000"
    WIN_DEFAULT = "0.00"
    SHARE_CODE_REG = "300[0-9]{3}|600[0-9]{3}|000[0-9]{3}|601[0-9][3]|002[0-9]{3}|000[0-9]{3}"
    SHARE_CODE_LEN_REG = "[0-9]{6}"

    @classmethod
    def get_font(cls, size=14, bold=False, italic=False, weight=75, family=MONO_FAMILY):
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(family))
        font.setPointSize(size)
        font.setBold(bold)
        font.setItalic(italic)
        font.setWeight(weight)
        return font

    @classmethod
    def get_size_policy(cls, date_input):
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(20)
        size_policy.setHeightForWidth(date_input.sizePolicy().hasHeightForWidth())
        return size_policy

    @classmethod
    def button_style(cls):
        # 正常状态下：黑底（背景色），白字（前景色），圆角，向外凸起
        # 鼠标停留：背景和前景都反色
        # 鼠标按下：背景色变为淡蓝色，向内凹陷
        button_style = (
            "QPushButton{background-color:black; color:white; border-radius:10px; border:2px groove gray; border-style:outset;}"
            "QPushButton:hover{background-color:white; color:black;}"
            "QPushButton:pressed{background-color:rgb(85, 170, 255); border-style:inset; }")

        return button_style

    @classmethod
    def background_image(cls):
        """增加背景图片 D:/CProject/gallopAShare/CCA"""
        bg_image = ("#add_record{border-image:url(:backgroud.png)}")

        return bg_image
