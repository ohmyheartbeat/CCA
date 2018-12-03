#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  login_window.py
@time: 2018/11/14 15:42
"""
import tkinter as tk
from tkinter import ttk
from interface.window import WINDOW
from constant.window_cons import WindowCons
from db.util.db_util import DbUtil
from tkinter import messagebox


class WindowStatus(object):
    """记录窗口状态"""
    login_window = False


class LoginWindow(object):
    """登录窗口类"""

    window_signin = None

    @classmethod
    def login_window(cls):
        """登录窗口"""
        cls.window_signin = tk.Toplevel(WINDOW)
        cls.window_signin.geometry(WindowCons.LOGIN_SIZE)
        cls.window_signin.attributes('-toolwindow', -1)
        ttk.Label(cls.window_signin, text=WindowCons.LOGIN_NAME).place(relx=0.3, rely=0.3)
        ttk.Label(cls.window_signin, text=WindowCons.LOGIN_PASSWORD).place(relx=0.3, rely=0.4)
        var_usr_name = tk.StringVar()
        entry_usr_name = ttk.Entry(cls.window_signin, textvariable=var_usr_name)
        entry_usr_name.place(relx=0.4, rely=0.3)
        var_usr_pwd = tk.StringVar()
        entry_usr_pwd = ttk.Entry(cls.window_signin, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(relx=0.4, rely=0.4)

        def login():
            """登录"""
            username = var_usr_name.get()
            password = var_usr_pwd.get()
            if username is None or username.strip() == '' or password is None or password.strip() == '':
                messagebox.showerror("ERROR", "username or password need to fill")
            else:
                user = DbUtil.query_user(username, password)
                if user:
                    messagebox.showinfo("Welcome", "Login successful!")
                    WindowStatus.login_window = False
                    WindowCons.LOGIN_SUCCESS = True  # 登录成功
                    WindowCons.LOGIN_USER_ID = user.id
                    cls.window_signin.destroy()
                else:
                    messagebox.showerror("ERROR", "Username or Password is invalid!")
                    WindowStatus.login_window = True

        btn_login = tk.Button(cls.window_signin, text='Login', command=login)
        btn_login.place(relx=0.45, rely=0.5)
        cls.window_signin.protocol(WindowCons.QUIT_ACTION, cls.login_quit_callback)

    @classmethod
    def login_quit_callback(cls):
        """登录窗口关闭回调"""
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            WindowStatus.login_window = False
            cls.window_signin.destroy()

    @classmethod
    def _login_success(cls, username, password):
        """登录成功后保存用户状态"""
        pass
