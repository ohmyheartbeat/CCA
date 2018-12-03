# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.py'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  menu.py
@time: 2018/11/14 17:37
"""
import os
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from interface.window import WINDOW
from interface.login_window import LoginWindow
from interface.login_window import WindowStatus
from constant.window_cons import WindowCons
from db.util.db_util import DbUtil
from db.domain.business_record import BusinessRecord
from tkinter.messagebox import askokcancel


def do_job():
    pass


class Menu(object):
    """菜单栏"""
    menubar = tk.Menu(WINDOW)
    add_business_frame = None  # 新增界面0
    query_business_frame = None  # 查询界面1
    delete_business_frame = None  # 删除界面2
    import_frame = None  # 导入界面3
    share_name = tk.StringVar()  # 股票名称
    share_code = tk.StringVar()  # 股票代码
    buy_date = tk.StringVar()  # 买入日期
    sale_date = tk.StringVar()  # 卖出日期
    buy_num = tk.IntVar()  # 买入数量
    sale_num = tk.IntVar()  # 卖出数量
    buy_price = tk.DoubleVar()  # 买入价格
    sale_price = tk.DoubleVar()  # 卖出价格
    buy_avg_price = tk.DoubleVar()  # 买入均价
    final_win = tk.DoubleVar()  # 最终盈利
    file_path = tk.StringVar()  # 文件路径
    can_sale_num = tk.IntVar()  # 可卖数量
    have_num = tk.IntVar()  # 持仓数量

    @classmethod
    def _init_menu(cls):
        cls.filemenu = tk.Menu(cls.menubar, tearoff=0)
        cls.menubar.add_cascade(label='编辑', menu=cls.filemenu)
        cls.filemenu.add_command(label='新增记录', command=cls._add_business_record_frame)
        cls.filemenu.add_command(label='查询记录', command=do_job)
        cls.filemenu.add_command(label='删除记录', command=do_job)
        cls.filemenu.add_separator()
        cls.filemenu.add_command(label='导入股票信息', command=cls._import_share_code_list)

        cls.toolmenu = tk.Menu(cls.menubar, tearoff=0)
        cls.menubar.add_cascade(label='工具', menu=cls.toolmenu)
        cls.toolmenu.add_command(label='登录', command=cls._login)
        cls.toolmenu.add_command(label='注销', command=cls._logout)
        cls.toolmenu.add_command(label='退出', command=WINDOW.quit)
        cls.helpmenu = tk.Menu(cls.menubar, tearoff=0)
        cls.menubar.add_cascade(label='帮助', menu=cls.helpmenu)
        cls.helpmenu.add_command(label='关于本程序', command=do_job)
        WINDOW.config(menu=cls.menubar)

    @classmethod
    def _login(cls):
        """登录按钮回调"""
        if not WindowStatus.login_window and not WindowCons.LOGIN_SUCCESS:
            LoginWindow.login_window()

    @classmethod
    def _logout(cls):
        """注销回调"""
        WindowCons.LOGIN_SUCCESS = False

    @classmethod
    def query_share_code(cls):
        """查询股票代码"""
        if cls.share_code.get() == '' or not cls.share_code.get().isdigit():
            messagebox.showinfo("提示", "请输入有效的股票代码")
        else:
            share_info = DbUtil.query_share_info_by_code(share_code=cls.share_code.get())
            if share_info:
                cls.share_name.set(share_info.share_name)
                buy_record = DbUtil.query_business_record(share_id=share_info.id)
                if isinstance(buy_record, list):
                    cls.__sum_share_info(buy_record)
                else:
                    if buy_record:
                        cls.can_sale_num.set(buy_record.buy_num)
                        cls.buy_avg_price.set(round(buy_record.buy_avg_price, 3))
            else:
                messagebox.showerror("错误", "股票代码无效！")
                return False

    @classmethod
    def _compute(cls):
        """计算最终盈利"""
        if cls.share_name.get() == "":
            messagebox.showinfo("提示", "请先查询股票信息")
            return
        if cls.sale_num.get() == 0:
            messagebox.showinfo("提示", "请卖出后再来统计收益吧！")
            return
        if cls.buy_num.get() != 0:
            messagebox.showinfo("提示", "买卖请分开记录！")
            return
        if cls.sale_num.get() > cls.can_sale_num.get():
            messagebox.showinfo("提示", "你的可卖数量不能超过已买数量！")
            return
        final_win = (cls.sale_price.get() - cls.buy_avg_price.get()) * 100 * cls.sale_num.get()
        # final_win -= 10 #手续费
        cls.final_win.set(round(final_win, 2))

    @classmethod
    def _save(cls):
        """保存记录到数据库"""
        file_path = cls.file_path.get()
        error_code_list = []
        if os.path.isfile(file_path):
            with open(file_path, mode="r") as f:
                data_list = f.readlines()
            if len(data_list) > 0:
                for data in data_list:
                    data_ = cls.__handle_origin_data(data)
                    if data_ == WindowCons.FALSE_NUMBER:
                        messagebox.showerror("错误", "数据文件有问题,请检查！")
                        return
                    if data_[0].isdigit() and len(data_[1].strip()) > 0 and len(data_[2].strip()):
                        DbUtil.import_share_info(cls.__handle_share_code(data_[0]), data_[1], data_[2])
                    else:
                        error_code_list.append(data_[0])
                messagebox.showinfo("提示", "数据导入成功")

    @classmethod
    def _select_file(cls):
        """查找文件"""
        try:
            file_path = askopenfile().name
            cls.file_path.set(file_path)
        except Exception:
            pass

    @classmethod
    def _destroy_frame(cls, frame_num):
        """销毁窗口"""
        frame_list = [cls.add_business_frame, cls.query_business_frame, cls.delete_business_frame, cls.import_frame]
        for index, frame in enumerate(frame_list):
            if index != frame_num and frame:
                frame.destroy()

    @classmethod
    def _add_business_record_frame(cls):
        """新增交易记录的窗口"""
        cls._destroy_frame(0)
        cls.add_business_frame = ttk.LabelFrame(WINDOW, text=WindowCons.ADD_BUSINESS_FRAME_NAME)
        cls.add_business_frame.grid(column=0, row=0, padx=8, pady=4)
        aa_label = ttk.Label(cls.add_business_frame, text='股票代码')
        aa_label.grid(column=0, row=1)
        share_code_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.share_code)
        share_code_enter.grid(column=1, row=1, padx=10, pady=4)

        aa_label = ttk.Label(cls.add_business_frame, text='股票名称')
        aa_label.grid(column=2, row=1)
        share_name_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.share_name)
        share_name_enter.grid(column=3, row=1, padx=10, pady=4)
        share_name_enter.configure(state='readonly')  # 禁用输入

        query_action = ttk.Button(cls.add_business_frame, text="查询", command=cls.query_share_code)
        query_action.grid(column=4, row=1)

        aa_label = ttk.Label(cls.add_business_frame, text='买入日期')
        aa_label.grid(column=0, row=2)
        share_code_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.buy_date)
        share_code_enter.grid(column=1, row=2, padx=10, pady=4)

        aa_label = ttk.Label(cls.add_business_frame, text='卖出日期')
        aa_label.grid(column=2, row=2)
        sale_date_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.sale_date)
        sale_date_enter.grid(column=3, row=2, padx=10, pady=4)

        aa_label = ttk.Label(cls.add_business_frame, text='买入价格')
        aa_label.grid(column=0, row=3)
        buy_price_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.buy_price)
        buy_price_enter.grid(column=1, row=3, padx=10, pady=4)

        aa_label = ttk.Label(cls.add_business_frame, text='卖出价格')
        aa_label.grid(column=2, row=3)
        sale_price_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.sale_price)
        sale_price_enter.grid(column=3, row=3, padx=10, pady=4)

        aa_label = ttk.Label(cls.add_business_frame, text='买入数量')
        aa_label.grid(column=0, row=4)
        buy_num_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.buy_num)
        buy_num_enter.grid(column=1, row=4, padx=10, pady=4)

        aa_label = ttk.Label(cls.add_business_frame, text='卖出数量')
        aa_label.grid(column=2, row=4)
        sale_num_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.sale_num)
        sale_num_enter.grid(column=3, row=4, padx=10, pady=4)
        title_enter = ttk.Label(cls.add_business_frame, width=16, text="单位:手(1手=100股)")
        title_enter.grid(column=4, row=4, padx=2, pady=4)
        title_enter.configure(state='disable')  # 禁用输入

        aa_label = ttk.Label(cls.add_business_frame, text='持仓均价')
        aa_label.grid(column=0, row=5)
        buy_avg_price_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.buy_avg_price)
        buy_avg_price_enter.grid(column=1, row=5, padx=10, pady=4)
        buy_avg_price_enter.configure(state='readonly')  # 禁用输入

        aa_label = ttk.Label(cls.add_business_frame, text='最终盈利')
        aa_label.grid(column=2, row=5)
        final_win_enter = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.final_win)
        final_win_enter.grid(column=3, row=5, padx=10, pady=4)
        final_win_enter.configure(state='readonly')  # 禁用输入

        aa_label = ttk.Label(cls.add_business_frame, text='持仓数量')
        aa_label.grid(column=0, row=6)
        can_sale_num = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.have_num)
        can_sale_num.grid(column=1, row=6, padx=10, pady=4)
        can_sale_num.configure(state='readonly')  # 禁用输入

        aa_label = ttk.Label(cls.add_business_frame, text='可卖数量')
        aa_label.grid(column=2, row=6)
        can_sale_num = ttk.Entry(cls.add_business_frame, width=15, textvariable=cls.can_sale_num)
        can_sale_num.grid(column=3, row=6, padx=10, pady=4)
        can_sale_num.configure(state='readonly')  # 禁用输入

        computer_action = ttk.Button(cls.add_business_frame, text="计算", command=cls._compute)
        computer_action.grid(column=4, row=5)
        save_action = ttk.Button(cls.add_business_frame, text="保存", command=cls._save_record_catch)
        save_action.grid(column=4, row=6)

    @classmethod
    def _import_share_code_list(cls):
        """导入股票信息"""
        if WindowCons.LOGIN_USER_ID != 2:
            messagebox.showerror("错误", "你没有这个权限")
            return
        cls._destroy_frame(3)
        cls.import_frame = ttk.LabelFrame(WINDOW, text=WindowCons.IMPORT_FRAME_NAME)
        cls.import_frame.grid(column=0, row=0, padx=8, pady=4)
        aa_label = ttk.Label(cls.import_frame, text='文件选择:')
        aa_label.grid(column=0, row=1)
        file_path_enter = ttk.Entry(cls.import_frame, width=20, textvariable=cls.file_path)
        file_path_enter.grid(column=1, row=1, padx=6, pady=4)

        select_action = ttk.Button(cls.import_frame, text="浏览文件", command=cls._select_file)
        select_action.grid(column=3, row=1)

        select_action = ttk.Button(cls.import_frame, text="导入", command=cls._save)
        select_action.grid(column=3, row=2)

    @classmethod
    def __handle_share_code(cls, share_code):
        """填充code"""
        return share_code.rjust(WindowCons.SHARE_CODE_LENGTH, WindowCons.CODE_FILL_STR)

    @classmethod
    def __handle_origin_data(cls, data):
        """处理原始数据"""
        data_ = WindowCons.FALSE_NUMBER
        if WindowCons.TRANSFER_SYMBOL in data:
            return data.split(WindowCons.TRANSFER_SYMBOL)
        elif WindowCons.COMMA_SYMBOL in data:
            return data.split(WindowCons.COMMA_SYMBOL)
        return data_

    @classmethod
    def __clean_and_refresh_data(cls):
        """清除并刷新数据"""
        cls.sale_num.set(0)
        cls.sale_price.set(0.0)
        cls.buy_num.set(0)
        cls.buy_price.set(0.0)
        cls.buy_date.set("")
        cls.sale_date.set("")
        cls.query_share_code()

    @classmethod
    def __sum_share_info(cls, record_list):
        """统计股票信息 卖出数量 买入数量 买入均价"""
        buy_num = 0
        sale_num = 0
        have_num = 0
        for index, record in enumerate(record_list):
            if index == (len(record_list) - 1):
                cls.buy_avg_price.set(round(record.buy_avg_price, 3))
                if record.final_profit:
                    cls.final_win.set(record.final_profit)
                else:
                    cls.final_win.set(0.0)
            if record.buy_num != 0 and record.buy_num:
                buy_num += record.buy_num
                if record.buy_time.date() < datetime.datetime.now().date():
                    have_num += record.buy_num
                continue
            elif record.sale_num != 0 and record.sale_num:
                sale_num += record.sale_num
                continue
        cls.can_sale_num.set(have_num - sale_num)
        cls.have_num.set(buy_num - sale_num)

    @classmethod
    def _save_record_catch(cls):
        """保存记录，抓取异常"""
        try:
            if cls.__save_record():
                messagebox.showinfo("提示", "保存成功！")
                cls.__clean_and_refresh_data()
            return True
        except Exception as e:
            print(e)
            messagebox.showerror("提示", "填写的交易信息有误,请重新填写")
            return False

    @classmethod
    def __save_record(cls):
        """保存记录"""
        if cls.share_name.get() is None:
            messagebox.showinfo("提示", "请先查询股票信息")
            return False
        if cls.sale_num.get() != 0 and cls.buy_num.get() != 0:
            messagebox.showinfo("提示", "买卖请分开记录！")
            return False
        if cls.sale_num.get() == 0 and cls.buy_num.get() == 0:
            messagebox.showinfo("提示", "请输入买卖数量(单位：手)")
            return False
        if cls.sale_num.get() > 0:
            if cls.sale_date.get() is None or cls.sale_date.get() == "":
                messagebox.showinfo("提示", "请填写交易日期,例20181123")
                return False
            if cls.sale_price.get() <= 0:
                messagebox.showerror("错误", "买入价格输入有误,请重新输入")
                return False
            try:
                sale_date = datetime.datetime.strptime(cls.sale_date.get(), "%Y%m%d").date()
                if sale_date > datetime.datetime.now().date() or int(sale_date.strftime("%w")) > 5:
                    raise Exception
            except:
                messagebox.showerror("提示", "交易日期有误,请重新填写")
                return False
            return cls._compute_avg_and_save(sale_num=cls.sale_num.get())

        if cls.buy_num.get() > 0:
            if cls.buy_date.get() is None or cls.buy_date.get() == "":
                messagebox.showinfo("提示", "请填写交易日期,例20181123")
                return False
            if cls.buy_price.get() <= 0:
                messagebox.showerror("提示", "买入价格输入有误,请重新输入")
                return False
            try:
                buy_date = datetime.datetime.strptime(cls.buy_date.get(), "%Y%m%d").date()
                if buy_date > datetime.datetime.now().date() or int(buy_date.strftime("%w")) > 5:
                    raise Exception
            except:
                messagebox.showerror("提示", "交易日期有误,请重新填写")
                return False
            return cls._compute_avg_and_save(buy_num=cls.buy_num.get())

    @classmethod
    def _compute_avg_and_save(cls, buy_num=0, sale_num=0):
        """计算买入平均价"""
        share_info = DbUtil.query_share_info_by_code(cls.share_code.get())
        record = DbUtil.query_last_business_record(share_info.id)
        if record:
            curr_num = record.curr_num + buy_num - sale_num
            avg_price = ((record.buy_avg_price * record.curr_num) + (cls.buy_num.get() * cls.buy_price.get()) - (
                cls.sale_num.get() * cls.sale_price.get())) / curr_num
        else:
            curr_num = cls.buy_num.get()
            avg_price = cls.buy_price.get()
        if not askokcancel("提示", "请确认数据无误后选择保存！"):
            return False
        if buy_num > 0:
            date_time = datetime.datetime.strptime(cls.buy_date.get(), "%Y%m%d")
            buiness_record = BusinessRecord(share_id=share_info.id, buy_time=date_time,
                                            buy_num=cls.buy_num.get(), buy_avg_price=avg_price, curr_num=curr_num,
                                            buy_price=cls.buy_price.get(),
                                            delate=WindowCons.FALSE_NUMBER)
            DbUtil.add_record(buiness_record)
        if sale_num > 0:
            date_time = datetime.datetime.strptime(cls.sale_date.get(), "%Y%m%d")
            buiness_record = BusinessRecord(share_id=share_info.id, buy_time=date_time,
                                            sale_num=cls.sale_num.get(), buy_avg_price=avg_price, curr_num=curr_num,
                                            sale_price=cls.sale_price.get(), final_profit=cls.final_win.get(),
                                            delate=WindowCons.FALSE_NUMBER)
            DbUtil.add_record(buiness_record)
        return True

