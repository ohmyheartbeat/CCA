#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  menu_qt.py
@time: 2018/11/29 11:39
"""
import datetime
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QFrame
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QDateEdit
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QTextEdit
from PyQt4.QtGui import QMenuBar
from PyQt4.QtGui import QAction
from PyQt4.QtGui import QMenu
from PyQt4.QtGui import QStatusBar
from PyQt4.QtGui import QPalette
from PyQt4.QtGui import QBrush
from PyQt4.QtGui import QPixmap
from PyQt4.QtCore import QRect
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QDate
from PyQt4.QtCore import QMetaObject
from interface.window import WINDOW
from interface.window import CENTRAL_WIDGET
from constant.window_cons import _fromUtf8
from constant.window_cons import _translate
from constant.window_cons import WindowCons
from utils.validator import IntValidator
from utils.validator import DoubleValidator
from utils.validator import RegExpValidator
from edit.slot_func import SlotFunc
from resource import bg


class MenuQt(object):
    """主菜单"""
    add_record = QFrame(CENTRAL_WIDGET)  # 增加交易记录的界面
    grid_layout_widget = QWidget(add_record)  # title的container
    grid_layout = QGridLayout(grid_layout_widget)
    title = QLabel(grid_layout_widget)
    statusbar = QStatusBar(WINDOW)
    # 股票代码的title以及输入框
    grid_layout_widget_2 = QWidget(add_record)
    grid_layout_2 = QGridLayout(grid_layout_widget_2)
    share_code_title = QLabel(grid_layout_widget_2)
    grid_layout_widget_14 = QWidget(add_record)
    grid_layout_14 = QGridLayout(grid_layout_widget_14)
    share_code_input = QLineEdit(grid_layout_widget_14)
    # 股票名称的title和显示框
    grid_layout_widget_12 = QWidget(add_record)
    grid_layout_12 = QGridLayout(grid_layout_widget_12)
    share_name_title = QLabel(grid_layout_widget_12)
    grid_layout_widget_21 = QWidget(add_record)
    grid_layout_21 = QGridLayout(grid_layout_widget_21)
    share_name_show = QLineEdit(grid_layout_widget_21)
    # 买入日期的title和输入框
    grid_layout_widget_3 = QWidget(add_record)
    grid_layout_3 = QGridLayout(grid_layout_widget_3)
    buy_date_title = QLabel(grid_layout_widget_3)
    grid_layout_widget_15 = QWidget(add_record)
    grid_layout_15 = QGridLayout(grid_layout_widget_15)
    buy_date_input = QDateEdit(grid_layout_widget_15)
    # 卖出日期的title和输入框
    grid_layout_widget_10 = QWidget(add_record)
    grid_layout_10 = QGridLayout(grid_layout_widget_10)
    sale_date_title = QLabel(grid_layout_widget_10)
    grid_layout_widget_20 = QWidget(add_record)
    grid_layout_20 = QGridLayout(grid_layout_widget_20)
    sale_date_input = QDateEdit(grid_layout_widget_20)
    # 买入数量的title和输入框
    grid_layout_widget_5 = QWidget(add_record)
    grid_layout_5 = QGridLayout(grid_layout_widget_5)
    buy_num_title = QLabel(grid_layout_widget_5)
    grid_layout_widget_16 = QWidget(add_record)
    grid_layout_16 = QGridLayout(grid_layout_widget_16)
    buy_num_input = QLineEdit(grid_layout_widget_16)
    # 卖出数量的title和输入框
    grid_layout_widget_25 = QWidget(add_record)
    grid_layout_25 = QGridLayout(grid_layout_widget_25)
    sale_num_input = QLineEdit(grid_layout_widget_25)
    grid_layout_widget_13 = QWidget(add_record)
    grid_layout_13 = QGridLayout(grid_layout_widget_13)
    sale_num_title = QLabel(grid_layout_widget_13)
    # 买入价格的title和输入框
    grid_layout_widget_4 = QWidget(add_record)
    grid_layout_4 = QGridLayout(grid_layout_widget_4)
    buy_price_title = QLabel(grid_layout_widget_4)
    grid_layout_widget_17 = QWidget(add_record)
    grid_layout_17 = QGridLayout(grid_layout_widget_17)
    buy_price_input = QLineEdit(grid_layout_widget_17)
    # 卖出价格和输入框
    grid_layout_widget_11 = QWidget(add_record)
    grid_layout_11 = QGridLayout(grid_layout_widget_11)
    sale_price_title = QLabel(grid_layout_widget_11)
    grid_layout_widget_22 = QWidget(add_record)
    grid_layout_22 = QGridLayout(grid_layout_widget_22)
    sale_price_input = QLineEdit(grid_layout_widget_22)
    # 持仓价格和显示框
    grid_layout_widget_6 = QWidget(add_record)
    grid_layout_6 = QGridLayout(grid_layout_widget_6)
    have_avg_price = QLabel(grid_layout_widget_6)
    grid_layout_widget_19 = QWidget(add_record)
    grid_layout_19 = QGridLayout(grid_layout_widget_19)
    buv_avg_price_show = QLineEdit(grid_layout_widget_19)
    # 持仓数量和显示框
    grid_layout_widget_7 = QWidget(add_record)
    grid_layout_7 = QGridLayout(grid_layout_widget_7)
    have_num_title = QLabel(grid_layout_widget_7)
    grid_layout_widget_18 = QWidget(add_record)
    grid_layout_18 = QGridLayout(grid_layout_widget_18)
    have_num_show = QLineEdit(grid_layout_widget_18)
    # 当前盈利和显示框
    grid_layout_widget_8 = QWidget(add_record)
    grid_layout_8 = QGridLayout(grid_layout_widget_8)
    win_title = QLabel(grid_layout_widget_8)
    grid_layout_widget_24 = QWidget(add_record)
    grid_layout_24 = QGridLayout(grid_layout_widget_24)
    win_show = QLineEdit(grid_layout_widget_24)
    # 可卖数量和显示框
    grid_layout_widget_9 = QWidget(add_record)
    grid_layout_9 = QGridLayout(grid_layout_widget_9)
    can_sale_num_title = QLabel(grid_layout_widget_9)
    grid_layout_widget_23 = QWidget(add_record)
    grid_layout_23 = QGridLayout(grid_layout_widget_23)
    can_sale_num_show = QLineEdit(grid_layout_widget_23)
    # 查询按钮 计算按钮 保存按钮
    # grid_layout_widget_26 = QWidget(add_record)
    # grid_layout_26 = QGridLayout(grid_layout_widget_26)
    # query_button = QPushButton(grid_layout_widget_26)

    # grid_layout_widget_27 = QWidget(add_record)
    # grid_layout_27 = QGridLayout(grid_layout_widget_27)
    # compute_button = QPushButton(grid_layout_widget_27)

    grid_layout_widget_28 = QWidget(add_record)
    grid_layout_28 = QGridLayout(grid_layout_widget_28)
    save_button = QPushButton(grid_layout_widget_28)

    grid_layout_widget_29 = QWidget(add_record)
    grid_layout_29 = QGridLayout(grid_layout_widget_29)
    text_edit = QTextEdit(grid_layout_widget_29)
    menubar = QMenuBar(WINDOW)
    edit = QMenu(menubar)
    tool = QMenu(menubar)
    program = QMenu(menubar)
    help = QMenu(menubar)
    add = QAction(WINDOW)
    query = QAction(WINDOW)
    delete_record = QAction(WINDOW)
    add_share = QAction(WINDOW)
    import_share = QAction(WINDOW)
    login = QAction(WINDOW)
    logout = QAction(WINDOW)
    exit = QAction(WINDOW)
    about = QAction(WINDOW)
    slot_func = None

    @classmethod
    def init_window(cls):
        cls.slot_func = SlotFunc(cls)
        cls.init_widget()
        cls.init_button()
        cls.init_menu()
        cls.set_style_sheet()
        cls.init_text()
        cls.add_slot_func()
        QMetaObject.connectSlotsByName(WINDOW)

    @classmethod
    def init_menu(cls):
        WINDOW.setCentralWidget(CENTRAL_WIDGET)
        cls.menubar.setGeometry(QRect(0, 0, 960, 23))
        cls.menubar.setObjectName(_fromUtf8("menubar"))
        cls.edit.setObjectName(_fromUtf8("edit"))
        cls.tool.setObjectName(_fromUtf8("tool"))
        cls.program.setObjectName(_fromUtf8("program"))
        cls.help.setObjectName(_fromUtf8("help"))
        WINDOW.setMenuBar(cls.menubar)
        cls.statusbar.setObjectName(_fromUtf8("statusbar"))
        WINDOW.setStatusBar(cls.statusbar)
        cls.add.setObjectName(_fromUtf8("add"))
        cls.query.setObjectName(_fromUtf8("query"))
        cls.delete_record.setObjectName(_fromUtf8("delete_record"))
        cls.add_share.setObjectName(_fromUtf8("add_share"))
        cls.import_share.setObjectName(_fromUtf8("import_share"))
        cls.login.setObjectName(_fromUtf8("login"))
        cls.logout.setObjectName(_fromUtf8("logout"))
        cls.exit.setObjectName(_fromUtf8("exit"))
        cls.about.setObjectName(_fromUtf8("about"))
        cls.edit.addAction(cls.add)
        cls.edit.addAction(cls.query)
        cls.edit.addAction(cls.delete_record)

        cls.tool.addAction(cls.add_share)
        cls.tool.addAction(cls.import_share)
        cls.tool.addSeparator()
        cls.tool.addAction(cls.login)
        cls.tool.addAction(cls.logout)

        cls.program.addAction(cls.exit)
        cls.help.addAction(cls.about)

        cls.menubar.addAction(cls.edit.menuAction())
        cls.menubar.addAction(cls.tool.menuAction())
        cls.menubar.addAction(cls.program.menuAction())
        cls.menubar.addAction(cls.help.menuAction())

    @classmethod
    def add_slot_func(cls):
        """增加槽函数"""
        cls.share_code_input.textChanged.connect(cls.slot_func.query_share_code)
        cls.save_button.clicked.connect(cls.slot_func.save_record)

    @classmethod
    def init_button(cls):
        """初始化按钮"""
        # cls.grid_layout_widget_26.setGeometry(QRect(160, 390, 121, 50))
        # cls.grid_layout_widget_26.setObjectName(_fromUtf8("grid_layout_widget_26"))
        # cls.grid_layout_26.setObjectName(_fromUtf8("grid_layout_26"))
        # cls.query_button.setFont(WindowCons.get_font(bold=True))
        # cls.query_button.setFlat(False)
        # cls.query_button.setObjectName(_fromUtf8("query_button"))
        # cls.grid_layout_26.addWidget(cls.query_button, 0, 0, 1, 1)
        # cls.grid_layout_widget_27.setGeometry(QRect(300, 390, 121, 50))
        # cls.grid_layout_widget_27.setObjectName(_fromUtf8("grid_layout_widget_27"))
        # cls.grid_layout_27.setObjectName(_fromUtf8("grid_layout_27"))
        # cls.compute_button.setFont(WindowCons.get_font(bold=True))
        # cls.compute_button.setObjectName(_fromUtf8("compute_button"))
        # cls.grid_layout_27.addWidget(cls.compute_button, 0, 0, 1, 1)
        cls.grid_layout_widget_28.setGeometry(QRect(440, 390, 121, 50))
        cls.grid_layout_widget_28.setObjectName(_fromUtf8("grid_layout_widget_28"))
        cls.grid_layout_28.setObjectName(_fromUtf8("grid_layout_28"))
        cls.save_button.setFont(WindowCons.get_font(bold=True))
        cls.save_button.setObjectName(_fromUtf8("save_button"))
        cls.grid_layout_28.addWidget(cls.save_button, 0, 0, 1, 1)
        cls.grid_layout_widget_29.setGeometry(QRect(570, 390, 160, 73))
        cls.grid_layout_widget_29.setObjectName(_fromUtf8("grid_layout_widget_29"))
        cls.grid_layout_29.setObjectName(_fromUtf8("grid_layout_29"))
        cls.text_edit.setEnabled(False)
        cls.text_edit.setReadOnly(True)
        cls.text_edit.setFrameShape(False)
        cls.text_edit.setObjectName(_fromUtf8("textEdit"))
        cls.grid_layout_29.addWidget(cls.text_edit, 0, 0, 1, 1)

    @classmethod
    def set_style_sheet(cls):
        """设置样式"""
        # cls.query_button.setStyleSheet(WindowCons.button_style())
        cls.save_button.setStyleSheet(WindowCons.button_style())
        # cls.compute_button.setStyleSheet(WindowCons.button_style())
        cls.add_record.setStyleSheet(WindowCons.background_image())

        cls.title.setStyleSheet(WindowCons.LIGHT_BLUE_STYLE)
        cls.sale_num_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.share_name_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.sale_price_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.buy_date_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.win_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.buy_num_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.can_sale_num_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.have_num_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.share_code_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.buy_price_title.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.have_avg_price.setStyleSheet(WindowCons.WHITE_STYLE)
        cls.sale_date_title.setStyleSheet(WindowCons.WHITE_STYLE)
        # cls.text_edit.setAttribute(Qt.WA_TranslucentBackground, True)
        # cls.text_edit.repaint()
        cls.text_edit.setStyleSheet(WindowCons.TRANSPARENT)
        palette1 = QPalette()
        palette1.setBrush(cls.add_record.backgroundRole(),
                          QBrush(QPixmap(':backgroud.png').scaled(cls.add_record.size())))
        cls.add_record.setPalette(palette1)
        cls.add_record.setStyleSheet(WindowCons.background_image())

    @classmethod
    def init_widget(cls):
        CENTRAL_WIDGET.setObjectName(_fromUtf8("centralwidget"))
        cls.add_record.setGeometry(QRect(-1, -1, 961, 561))
        cls.add_record.setObjectName(_fromUtf8("add_record"))
        cls.grid_layout_widget.setGeometry(QRect(50, 10, 314, 50))
        cls.grid_layout_widget.setObjectName(_fromUtf8("gridLayoutWidget"))
        cls.grid_layout.setObjectName(_fromUtf8("gridLayout"))
        cls.title.setFont(WindowCons.get_font(size=16, weight=50))
        cls.title.setTextFormat(Qt.PlainText)
        cls.title.setScaledContents(False)
        cls.title.setAlignment(Qt.AlignCenter)
        cls.title.setObjectName(_fromUtf8("title"))
        cls.grid_layout.addWidget(cls.title, 0, 0, 1, 1)
        cls._init_labels()

    @classmethod
    def init_text(cls):
        """初始化文字"""
        WINDOW.setWindowTitle(_translate("MainWindow", "驰骋A股", None))
        cls.title.setText(_translate("MainWindow", "新增交易记录", None))
        cls.share_code_title.setText(_translate("MainWindow", "股票代码", None))
        cls.buy_date_title.setText(_translate("MainWindow", "买入日期", None))
        cls.buy_price_title.setText(_translate("MainWindow", "买入价格", None))
        cls.buy_num_title.setText(_translate("MainWindow", "买入数量", None))
        cls.have_avg_price.setText(_translate("MainWindow", "持仓均价", None))
        cls.have_num_title.setText(_translate("MainWindow", "持仓数量", None))
        cls.win_title.setText(_translate("MainWindow", "当前盈利", None))
        cls.can_sale_num_title.setText(_translate("MainWindow", "可卖数量", None))
        cls.sale_date_title.setText(_translate("MainWindow", "卖出日期", None))
        cls.sale_price_title.setText(_translate("MainWindow", "卖出价格", None))
        cls.share_name_title.setText(_translate("MainWindow", "股票名称", None))
        cls.sale_num_title.setText(_translate("MainWindow", "卖出数量", None))
        # cls.query_button.setText(_translate("MainWindow", "查询", None))
        # cls.compute_button.setText(_translate("MainWindow", "计算", None))
        cls.save_button.setText(_translate("MainWindow", "保存", None))
        cls.text_edit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">数量单位:手(1手=100股)</p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">货币单位:元</p></body></html>",
                                         None))
        cls.edit.setTitle(_translate("MainWindow", "编辑", None))
        cls.tool.setTitle(_translate("MainWindow", "工具", None))
        cls.program.setTitle(_translate("MainWindow", "程序", None))
        cls.help.setTitle(_translate("MainWindow", "帮助", None))

        cls.add.setText(_translate("MainWindow", "新增交易记录", None))
        cls.query.setText(_translate("MainWindow", "查询交易记录", None))
        cls.delete_record.setText(_translate("MainWindow", "删除交易记录", None))
        cls.add_share.setText(_translate("MainWindow", "新增股票信息", None))
        cls.import_share.setText(_translate("MainWindow", "导入股票信息", None))
        cls.login.setText(_translate("MainWindow", "登录", None))
        cls.logout.setText(_translate("MainWindow", "注销", None))
        cls.exit.setText(_translate("MainWindow", "退出", None))
        cls.about.setText(_translate("MainWindow", "关于", None))
        cls.statusbar.showMessage("本程序仅限内部人员使用，如作他用所承受的法律责任一概与作者无关（使用即代表你同意上述观点）")
        cls.statusbar.setStyleSheet(WindowCons.RED_STYLE)

    @classmethod
    def _init_labels(cls):
        """初始化页面的label"""
        cls.__init_share_code()  # 初始化股票代码以及输入框
        cls.__init_share_name()  # 初始化股票名称以及显示框
        cls.__init_buy_date()  # 初始化买入日期以及输入框
        cls.__init_sale_date()  # 初始化卖出日期以及输入框
        cls.__init_buy_num()  # 初始化买入数量以及输入框
        cls.__init_sale_num()  # 初始化卖出数量以及输入框
        cls.__init_buy_price()  # 初始化买入价格以及输入框
        cls.__init_sale_price()  # 初始化卖出价格以及输入框
        cls.__init_buy_avg_price()  # 初始化平均价以及显示框
        cls.__init_have_num()  # 初始化持仓数量以及显示框
        cls.__init_have_win()  # 初始化当前股票盈利情况以及显示框
        cls.__can_sale_num()  # 初始化可卖数量以及显示框

    @classmethod
    def __init_share_code(cls):
        cls.grid_layout_widget_2.setGeometry(QRect(160, 60, 101, 41))
        cls.grid_layout_widget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        cls.grid_layout_2.setObjectName(_fromUtf8("gridLayout_2"))
        cls.share_code_title.setFont(WindowCons.get_font(bold=True))
        cls.share_code_title.setTextFormat(Qt.PlainText)
        cls.share_code_title.setAlignment(Qt.AlignCenter)
        cls.share_code_title.setObjectName(_fromUtf8("share_code_title"))
        cls.grid_layout_2.addWidget(cls.share_code_title, 0, 0, 1, 1)
        cls.grid_layout_widget_14.setGeometry(QRect(280, 60, 141, 50))
        cls.grid_layout_widget_14.setObjectName(_fromUtf8("gridLayoutWidget_14"))
        cls.grid_layout_14.setObjectName(_fromUtf8("gridLayout_14"))
        cls.share_code_input.setFont(WindowCons.get_font(weight=50, family=WindowCons.YAHEI_UI_FAMILY))
        cls.share_code_input.setObjectName(_fromUtf8("share_code_input"))
        cls.share_code_input.setValidator(RegExpValidator())
        cls.grid_layout_14.addWidget(cls.share_code_input, 0, 0, 1, 1)

    @classmethod
    def __init_share_name(cls):
        cls.grid_layout_widget_12.setGeometry(QRect(450, 60, 101, 41))
        cls.grid_layout_widget_12.setObjectName(_fromUtf8("gridLayoutWidget_12"))
        cls.grid_layout_12.setObjectName(_fromUtf8("gridLayout_12"))
        cls.share_name_title.setFont(WindowCons.get_font(bold=True))
        cls.share_name_title.setTextFormat(Qt.PlainText)
        cls.share_name_title.setAlignment(Qt.AlignCenter)
        cls.share_name_title.setObjectName(_fromUtf8("share_name_title"))
        cls.grid_layout_12.addWidget(cls.share_name_title, 0, 0, 1, 1)

        cls.grid_layout_widget_21.setGeometry(QRect(570, 60, 141, 50))
        cls.grid_layout_widget_21.setObjectName(_fromUtf8("grid_layout_widget_21"))
        cls.grid_layout_21.setObjectName(_fromUtf8("grid_layout_21"))
        cls.share_name_show.setEnabled(True)
        cls.share_name_show.setFont(WindowCons.get_font(weight=50, family=WindowCons.YAHEI_LIGHT_FAMILY))
        cls.share_name_show.setReadOnly(True)
        cls.share_name_show.setFrame(False)
        cls.share_name_show.setObjectName(_fromUtf8("share_name_show"))
        cls.grid_layout_21.addWidget(cls.share_name_show, 0, 0, 1, 1)

    @classmethod
    def __init_buy_date(cls):
        cls.grid_layout_widget_3.setGeometry(QRect(160, 110, 101, 41))
        cls.grid_layout_widget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        cls.grid_layout_3.setObjectName(_fromUtf8("gridLayout_3"))
        cls.buy_date_title.setFont(WindowCons.get_font(bold=True))
        cls.buy_date_title.setTextFormat(Qt.PlainText)
        cls.buy_date_title.setAlignment(Qt.AlignCenter)
        cls.buy_date_title.setObjectName(_fromUtf8("buy_date_title"))
        cls.grid_layout_3.addWidget(cls.buy_date_title, 0, 0, 1, 1)

        cls.grid_layout_widget_15.setGeometry(QRect(280, 110, 141, 41))
        cls.grid_layout_widget_15.setObjectName(_fromUtf8("gridLayoutWidget_15"))
        cls.grid_layout_15.setObjectName(_fromUtf8("gridLayout_15"))
        cls.buy_date_input.setEnabled(True)
        size_policy = WindowCons.get_size_policy(cls.buy_date_input)
        cls.buy_date_input.setSizePolicy(size_policy)
        cls.buy_date_input.setFont(WindowCons.get_font(family=WindowCons.YAHEI_LIGHT_FAMILY,size=12))
        cls.buy_date_input.setWrapping(False)
        cls.buy_date_input.setCalendarPopup(True)
        cls.buy_date_input.setFrame(False)
        cls.buy_date_input.setDate(QDate(datetime.datetime.date(datetime.datetime.now())))
        cls.buy_date_input.setObjectName(_fromUtf8("buy_date_input"))
        cls.grid_layout_15.addWidget(cls.buy_date_input, 0, 0, 1, 1)

    @classmethod
    def __init_sale_date(cls):
        cls.grid_layout_widget_10.setGeometry(QRect(450, 110, 101, 41))
        cls.grid_layout_widget_10.setObjectName(_fromUtf8("gridLayoutWidget_10"))
        cls.grid_layout_10.setObjectName(_fromUtf8("gridLayout_10"))
        cls.sale_date_title.setFont(WindowCons.get_font(bold=True))
        cls.sale_date_title.setTextFormat(Qt.PlainText)
        cls.sale_date_title.setAlignment(Qt.AlignCenter)
        cls.sale_date_title.setObjectName(_fromUtf8("buy_date_title_2"))
        cls.grid_layout_10.addWidget(cls.sale_date_title, 0, 0, 1, 1)

        cls.grid_layout_widget_20.setGeometry(QRect(570, 110, 141, 41))
        cls.grid_layout_widget_20.setObjectName(_fromUtf8("gridLayoutWidget_20"))
        cls.grid_layout_20.setObjectName(_fromUtf8("gridLayout_20"))
        cls.sale_date_input.setFont(WindowCons.get_font(size=12, family=WindowCons.YAHEI_LIGHT_FAMILY))
        cls.sale_date_input.setWrapping(False)
        cls.sale_date_input.setFrame(False)
        cls.sale_date_input.setCalendarPopup(True)
        cls.sale_date_input.setDate(QDate(datetime.datetime.date(datetime.datetime.now())))
        cls.sale_date_input.setObjectName(_fromUtf8("sale_date_input"))
        cls.grid_layout_20.addWidget(cls.sale_date_input, 0, 0, 1, 1)

    @classmethod
    def __init_buy_num(cls):
        cls.grid_layout_widget_5.setGeometry(QRect(160, 210, 101, 41))
        cls.grid_layout_widget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        cls.grid_layout_5.setObjectName(_fromUtf8("gridLayout_5"))
        cls.buy_num_title.setFont(WindowCons.get_font(bold=True))
        cls.buy_num_title.setTextFormat(Qt.PlainText)
        cls.buy_num_title.setAlignment(Qt.AlignCenter)
        cls.buy_num_title.setObjectName(_fromUtf8("buy_num_title"))
        cls.grid_layout_5.addWidget(cls.buy_num_title, 0, 0, 1, 1)

        cls.grid_layout_widget_16.setGeometry(QRect(280, 210, 141, 41))
        cls.grid_layout_widget_16.setObjectName(_fromUtf8("gridLayoutWidget_16"))
        cls.grid_layout_16.setObjectName(_fromUtf8("gridLayout_16"))
        cls.buy_num_input.setValidator(IntValidator())
        cls.buy_num_input.setText("100")
        cls.buy_num_input.setFont(WindowCons.get_font(family=WindowCons.JUI_LIGHT_FAMILY))
        cls.buy_num_input.setFrame(False)
        cls.buy_num_input.setObjectName(_fromUtf8("buy_num_input"))
        cls.grid_layout_16.addWidget(cls.buy_num_input, 0, 0, 1, 1)

    @classmethod
    def __init_sale_num(cls):
        # 初始化卖出数量以及输入框
        cls.grid_layout_widget_25.setGeometry(QRect(570, 210, 141, 41))
        cls.grid_layout_widget_25.setObjectName(_fromUtf8("gridLayoutWidget_25"))
        cls.grid_layout_25.setObjectName(_fromUtf8("gridLayout_25"))
        cls.sale_num_input.setValidator(IntValidator())
        cls.sale_num_input.setText("100")
        cls.sale_num_input.setFont(WindowCons.get_font(family=WindowCons.JUI_LIGHT_FAMILY))
        cls.sale_num_input.setFrame(False)
        cls.sale_num_input.setObjectName(_fromUtf8("sale_num_input"))
        cls.grid_layout_25.addWidget(cls.sale_num_input, 0, 0, 1, 1)

        cls.grid_layout_widget_13.setGeometry(QRect(450, 210, 101, 41))
        cls.grid_layout_widget_13.setObjectName(_fromUtf8("gridLayoutWidget_13"))
        cls.grid_layout_13.setObjectName(_fromUtf8("gridLayout_13"))
        cls.sale_num_title.setFont(WindowCons.get_font(bold=True))
        cls.sale_num_title.setTextFormat(Qt.PlainText)
        cls.sale_num_title.setAlignment(Qt.AlignCenter)
        cls.sale_num_title.setObjectName(_fromUtf8("buy_num_title_2"))
        cls.grid_layout_13.addWidget(cls.sale_num_title, 0, 0, 1, 1)

    @classmethod
    def __init_buy_price(cls):
        # 初始化买入价格以及输入框
        cls.grid_layout_widget_4.setGeometry(QRect(160, 160, 101, 41))
        cls.grid_layout_widget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        cls.grid_layout_4.setObjectName(_fromUtf8("gridLayout_4"))
        cls.buy_price_title.setFont(WindowCons.get_font(bold=True))
        cls.buy_price_title.setTextFormat(Qt.PlainText)
        cls.buy_price_title.setAlignment(Qt.AlignCenter)
        cls.buy_price_title.setObjectName(_fromUtf8("buy_price_title"))
        cls.grid_layout_4.addWidget(cls.buy_price_title, 0, 0, 1, 1)

        cls.grid_layout_widget_17.setGeometry(QRect(280, 160, 141, 41))
        cls.grid_layout_widget_17.setObjectName(_fromUtf8("gridLayoutWidget_17"))
        cls.grid_layout_17.setObjectName(_fromUtf8("gridLayout_17"))
        cls.buy_price_input.setFont(WindowCons.get_font(family=WindowCons.YAHEI_LIGHT_FAMILY))
        cls.buy_price_input.setFrame(False)
        cls.buy_price_input.setValidator(DoubleValidator())
        cls.buy_price_input.setText("0.00")
        cls.buy_price_input.setObjectName(_fromUtf8("buy_price_input"))
        cls.grid_layout_17.addWidget(cls.buy_price_input, 0, 0, 1, 1)

    @classmethod
    def __init_sale_price(cls):
        # 初始化卖出价格以及输入框
        cls.grid_layout_widget_11.setGeometry(QRect(450, 160, 101, 41))
        cls.grid_layout_widget_11.setObjectName(_fromUtf8("gridLayoutWidget_11"))
        cls.grid_layout_11.setObjectName(_fromUtf8("gridLayout_11"))
        cls.sale_price_title.setFont(WindowCons.get_font(bold=True))
        cls.sale_price_title.setTextFormat(Qt.PlainText)
        cls.sale_price_title.setAlignment(Qt.AlignCenter)
        cls.sale_price_title.setObjectName(_fromUtf8("cls.sale_price_title"))
        cls.grid_layout_11.addWidget(cls.sale_price_title, 0, 0, 1, 1)

        cls.grid_layout_widget_22.setGeometry(QRect(570, 160, 141, 41))
        cls.grid_layout_widget_22.setObjectName(_fromUtf8("grid_layout_widget_22"))
        cls.grid_layout_22.setObjectName(_fromUtf8("grid_layout_22"))
        cls.sale_price_input.setFont(WindowCons.get_font(family=WindowCons.YAHEI_LIGHT_FAMILY))
        cls.sale_price_input.setFrame(False)
        cls.sale_price_input.setText("0.00")
        cls.sale_price_input.setValidator(DoubleValidator())
        cls.sale_price_input.setObjectName(_fromUtf8("sale_price_input"))
        cls.grid_layout_22.addWidget(cls.sale_price_input, 0, 0, 1, 1)

    @classmethod
    def __init_buy_avg_price(cls):
        # 初始化平均价以及显示框
        cls.grid_layout_widget_6.setGeometry(QRect(160, 260, 101, 41))
        cls.grid_layout_widget_6.setObjectName(_fromUtf8("grid_layout_widget_6"))
        cls.grid_layout_6.setObjectName(_fromUtf8("grid_layout_6"))
        cls.have_avg_price.setFont(WindowCons.get_font(bold=True))
        cls.have_avg_price.setTextFormat(Qt.PlainText)
        cls.have_avg_price.setAlignment(Qt.AlignCenter)
        cls.have_avg_price.setObjectName(_fromUtf8("have_avg_price"))
        cls.grid_layout_6.addWidget(cls.have_avg_price, 0, 0, 1, 1)

        cls.grid_layout_widget_19.setGeometry(QRect(280, 260, 141, 41))
        cls.grid_layout_widget_19.setObjectName(_fromUtf8("grid_layout_widget_19"))
        cls.grid_layout_19.setObjectName(_fromUtf8("grid_layout_19"))
        cls.buv_avg_price_show.setEnabled(True)
        cls.buv_avg_price_show.setFont(WindowCons.get_font(family=WindowCons.JUI_LIGHT_FAMILY))
        cls.buv_avg_price_show.setReadOnly(True)
        cls.buv_avg_price_show.setFrame(False)
        cls.buv_avg_price_show.setObjectName(_fromUtf8("buv_avg_price_show"))
        cls.grid_layout_19.addWidget(cls.buv_avg_price_show, 0, 0, 1, 1)

    @classmethod
    def __init_have_num(cls):
        # 初始化持仓数量以及显示框
        cls.grid_layout_widget_7.setGeometry(QRect(160, 310, 101, 41))
        cls.grid_layout_widget_7.setObjectName(_fromUtf8("grid_layout_widget_7"))
        cls.grid_layout_7.setObjectName(_fromUtf8("grid_layout_7"))
        cls.have_num_title.setFont(WindowCons.get_font(bold=True))
        cls.have_num_title.setTextFormat(Qt.PlainText)
        cls.have_num_title.setAlignment(Qt.AlignCenter)
        cls.have_num_title.setObjectName(_fromUtf8("have_num_title"))
        cls.grid_layout_7.addWidget(cls.have_num_title, 0, 0, 1, 1)

        cls.grid_layout_widget_18.setGeometry(QRect(280, 310, 141, 41))
        cls.grid_layout_widget_18.setObjectName(_fromUtf8("grid_layout_widget_18"))
        cls.grid_layout_18.setObjectName(_fromUtf8("grid_layout_18"))
        cls.have_num_show.setFont(WindowCons.get_font(family=WindowCons.JUI_LIGHT_FAMILY))
        cls.have_num_show.setReadOnly(True)
        cls.have_num_show.setFrame(False)
        cls.have_num_show.setObjectName(_fromUtf8("have_num_show"))
        cls.grid_layout_18.addWidget(cls.have_num_show, 0, 0, 1, 1)

    @classmethod
    def __init_have_win(cls):
        # 初始化当前股票盈利情况以及显示框
        cls.grid_layout_widget_8.setGeometry(QRect(450, 260, 101, 41))
        cls.grid_layout_widget_8.setObjectName(_fromUtf8("grid_layout_widget_8"))
        cls.grid_layout_8.setObjectName(_fromUtf8("grid_layout_8"))
        cls.win_title.setFont(WindowCons.get_font(bold=True))
        cls.win_title.setTextFormat(Qt.PlainText)
        cls.win_title.setAlignment(Qt.AlignCenter)
        cls.win_title.setObjectName(_fromUtf8("win_title"))
        cls.grid_layout_8.addWidget(cls.win_title, 0, 0, 1, 1)

        cls.grid_layout_widget_24.setGeometry(QRect(570, 260, 141, 41))
        cls.grid_layout_widget_24.setObjectName(_fromUtf8("grid_layout_widget_24"))
        cls.grid_layout_24.setObjectName(_fromUtf8("grid_layout_24"))
        cls.win_show.setEnabled(True)
        cls.win_show.setFont(WindowCons.get_font(family=WindowCons.JUI_LIGHT_FAMILY))
        cls.win_show.setReadOnly(True)
        cls.win_show.setObjectName(_fromUtf8("win_show"))
        cls.win_show.setFrame(False)
        cls.grid_layout_24.addWidget(cls.win_show, 0, 0, 1, 1)

    @classmethod
    def __can_sale_num(cls):
        # 初始化可卖数量以及显示框
        cls.grid_layout_widget_9.setGeometry(QRect(450, 310, 101, 41))
        cls.grid_layout_widget_9.setObjectName(_fromUtf8("grid_layout_widget_9"))
        cls.grid_layout_9.setObjectName(_fromUtf8("gridLayout_9"))
        cls.can_sale_num_title.setFont(WindowCons.get_font(bold=True))
        cls.can_sale_num_title.setTextFormat(Qt.PlainText)
        cls.can_sale_num_title.setAlignment(Qt.AlignCenter)
        cls.can_sale_num_title.setObjectName(_fromUtf8("can_sale_num_title"))
        cls.grid_layout_9.addWidget(cls.can_sale_num_title, 0, 0, 1, 1)

        cls.grid_layout_widget_23.setGeometry(QRect(570, 310, 141, 41))
        cls.grid_layout_widget_23.setObjectName(_fromUtf8("gridLayoutWidget_23"))
        cls.grid_layout_23.setObjectName(_fromUtf8("grid_layout_23"))
        cls.can_sale_num_show.setEnabled(True)
        cls.can_sale_num_show.setFont(WindowCons.get_font(family=WindowCons.JUI_LIGHT_FAMILY))
        cls.can_sale_num_show.setReadOnly(True)
        cls.can_sale_num_show.setFrame(False)
        cls.can_sale_num_show.setObjectName(_fromUtf8("can_sale_num_show"))
        cls.grid_layout_23.addWidget(cls.can_sale_num_show, 0, 0, 1, 1)
