#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  window.py
@time: 2018/11/14 15:32
"""
import sys
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore
from PyQt4.QtGui import QWidget,QApplication
from constant.window_cons import WindowCons

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

# WINDOW = tk.Tk()
# WINDOW.title(WindowCons.EXE_NAME)  # 设置名称
# WINDOW.geometry(WindowCons.WINDOW_SIZE)  # 设置初始窗口大小
APP = QApplication(sys.argv)

WINDOW = QMainWindow()
WINDOW.setObjectName(_fromUtf8("MainWindow"))
WINDOW.resize(960,540)

CENTRAL_WIDGET = QWidget(WINDOW)
CENTRAL_WIDGET.setObjectName(_fromUtf8("centralwidget"))

# def callback():
#     """关闭回调"""
#     if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
#         WINDOW.destroy()


# canvas = tk.Canvas(WINDOW, width=900, height=500, bd=0, highlightthickness=0)
# imgpath = './resource/backgroud.png'
# img = Image.open(imgpath)
# photo = ImageTk.PhotoImage(img)
#
# canvas.create_image(900, 500, image=photo)
# canvas.pack()
# WINDOW.protocol(WindowCons.QUIT_ACTION, callback)
