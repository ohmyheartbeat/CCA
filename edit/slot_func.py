#!/usr/bin /env  python
# coding:utf-8
"""

@version:  3.4.4
@author:  Long
@file:  slot_func.py
@time: 2018/11/30 11:25
"""
import datetime
from PyQt4.QtGui import QStringListModel
from PyQt4.QtCore import QDate
from db.util.db_util import DbUtil
from db.domain.business_record import BusinessRecord
from constant.window_cons import WindowCons
from utils.gui_parts import Completer
from utils.gui_parts import MessageBox


class SlotFunc(object):
    """页面的槽函数"""

    def __init__(self, menu_qt):
        """
        初始化槽函数
        :param menu_qt:
        """
        self.menu_qt = menu_qt
        self.share_code_list = Completer()
        self.menu_qt.share_code_input.setCompleter(self.share_code_list)  # 将字典添加到lineEdit中
        self.message_box = MessageBox(self.menu_qt.add_record)

    def query_share_code(self):
        """查询股票代码"""
        if self.menu_qt.share_code_input.text() == '' or not self.menu_qt.share_code_input.text().isdigit():
            # QMessageBox.showinfo("提示", "请输入有效的股票代码")
            return False
        else:
            self.fill_share_info()
            share_info = DbUtil.query_share_info_by_code(share_code=self.menu_qt.share_code_input.text())
            if share_info:
                self.menu_qt.share_name_show.setText(share_info.share_name)
                buy_record = DbUtil.query_business_record(share_id=share_info.id)
                if isinstance(buy_record, list) and len(buy_record) > 1:
                    self.__sum_share_info(buy_record)
                else:
                    if buy_record:
                        self.menu_qt.can_sale_num_show.setText(buy_record.buy_num)
                        self.menu_qt.buv_avg_price_show.setText(round(buy_record.buy_avg_price, 3))
                    else:
                        self.menu_qt.win_show.setText("0")
                        self.menu_qt.buv_avg_price_show.setText("0.000")
                        self.menu_qt.can_sale_num_show.setText("0")
                        self.menu_qt.have_num_show.setText("0")

    def fill_share_info(self):
        """智能提示code"""
        share_list = self.package_share_info()
        if share_list:
            self.share_code_list.setModel(share_list)

    def package_share_info(self):
        """组装股票信息list"""
        str_list = []
        share_info_list = DbUtil.query_share_info_like_code(share_code=self.menu_qt.share_code_input.text())
        if len(share_info_list) > 0:
            for share_info in share_info_list:
                str = share_info.share_code + WindowCons.SPACE_SYMBOL + share_info.share_name
                str_list.append(str)
            return QStringListModel(str_list)
        else:
            return False

    def __sum_share_info(self, record_list):
        """统计股票信息 卖出数量 买入数量 买入均价"""
        buy_num = 0
        sale_num = 0
        have_num = 0
        for index, record in enumerate(record_list):
            if index == (len(record_list) - 1):
                self.menu_qt.buv_avg_price_show.setText(str(round(record.buy_avg_price, 3)))
                if record.final_profit:

                    self.menu_qt.win_show.setText(str(record.final_profit))
                    # print(self.menu_qt.win_show.text())
                else:
                    self.menu_qt.win_show.setText("0.0")
            if record.buy_num != 0 and record.buy_num:
                buy_num += record.buy_num
                if record.buy_time.date() < datetime.datetime.now().date():
                    have_num += record.buy_num
                continue
            elif record.sale_num != 0 and record.sale_num:
                sale_num += record.sale_num
                continue
        if self.menu_qt.buv_avg_price_show.text() == "":
            self.menu_qt.buv_avg_price_show.setText(WindowCons.PRICE_DEFAULT)
        if self.menu_qt.win_show.text() == "":
            self.menu_qt.win_show.setText(WindowCons.WIN_DEFAULT)
        self.menu_qt.can_sale_num_show.setText(str(have_num - sale_num))
        self.menu_qt.have_num_show.setText(str(buy_num - sale_num))

    def save_record(self):
        """保存记录,并清空部分数据和刷新数据"""
        result = self._save_record()
        try:
            if result:
                self.message_box.point_out("保存成功！")
        except Exception as e:
            print(e)
        # self.query_share_code()
        if result:
            self.menu_qt.sale_date_input.setDate(QDate(2018, 11, 11))
            self.menu_qt.buy_date_input.setDate(QDate(2018, 11, 11))
            self.menu_qt.share_code_input.setText("")
            self.menu_qt.share_name_show.setText("")
            self.menu_qt.have_num_show.setText("0")
            self.menu_qt.can_sale_num_show.setText("0")
            self.menu_qt.win_show.setText("0")
            self.menu_qt.buy_num_input.setText("100")
            self.menu_qt.sale_num_input.setText("100")
            self.menu_qt.buv_avg_price_show.setText("0.000")
            self.menu_qt.sale_price_input.setText("0.00")
            self.menu_qt.buy_price_input.setText("0.00")

    def _save_record(self):
        """保存记录"""
        if self.menu_qt.share_name_show.text() == "":
            self.message_box.point_out("请先输入股票代码信息")
            return False
        sale_num_text = self.menu_qt.sale_num_input.text()
        buy_num_text = self.menu_qt.buy_num_input.text()
        if self.match_num(sale_num_text) and self.match_num(buy_num_text, is_buy=False):
            self.message_box.point_out("买卖请分开记录！")
            return False
        try:
            sale_num = int(self.menu_qt.sale_num_input.text())
        except ValueError:
            sale_num = WindowCons.FALSE_NUMBER
        if sale_num != WindowCons.FALSE_NUMBER:
            if not SlotFunc.compare_date(self.menu_qt.sale_date_input.text()):
                self.message_box.point_out("交易日期输入有误")
                return False
            elif not self.match_num(sale_num, is_buy=False):
                self.message_box.point_out("请输入正确的交易数量！")
                return False
            elif not self.decide_price(self.menu_qt.sale_price_input.text()):
                self.message_box.point_out("输入的价格有误")
                return False
            self._compute_avg_and_save(sale_num=sale_num)
        try:
            buy_num = int(self.menu_qt.buy_num_input.text())
        except ValueError:
            buy_num = WindowCons.FALSE_NUMBER
        if buy_num != WindowCons.FALSE_NUMBER:
            if not SlotFunc.compare_date(self.menu_qt.buy_date_input.text()):
                self.message_box.point_out("交易日期输入有误")
                return False
            elif not self.match_num(buy_num):
                self.message_box.point_out("请输入正确的交易数量！")
                return False
            elif not self.decide_price(self.menu_qt.buy_price_input.text()):
                self.message_box.point_out("输入的价格有误")
                return False
            return self._compute_avg_and_save(buy_num=buy_num)
        self.message_box.point_out("请输入正确的交易数量")
        return False

    def _compute_avg_and_save(self, buy_num=0, sale_num=0):
        """计算买入平均价"""
        share_info = DbUtil.query_share_info_by_code(self.menu_qt.share_code_input.text())
        record = DbUtil.query_last_business_record(share_info.id)
        buy_price = float(self.menu_qt.buy_price_input.text())
        sale_price = float(self.menu_qt.sale_price_input.text())
        if record:
            curr_num = record.curr_num + buy_num - sale_num
            if curr_num != 0:
                avg_price = ((record.buy_avg_price * record.curr_num) + (buy_num * buy_price) - (
                    sale_num * sale_price)) / curr_num
            else:
                avg_price = 0.000
        else:
            curr_num = buy_num
            avg_price = buy_price
        if not self.compute_win(record.final_profit):
            return False
        save_confirm = self.message_box.ask_ok("请确认数据无误后点击确定")
        if save_confirm == MessageBox.CANCEL_NO:
            return False
        if buy_num > 0:
            try:
                date_time = datetime.datetime.strptime(self.menu_qt.buy_date_input.text(), "%Y/%m/%d").date()
            except:
                date_time = datetime.datetime.strptime(self.menu_qt.buy_date_input.text(), "%Y-%m-%d").date()
            buiness_record = BusinessRecord(share_id=share_info.id, buy_time=date_time,
                                            buy_num=buy_num, buy_avg_price=avg_price, curr_num=curr_num,
                                            buy_price=buy_price, final_profit=float(self.menu_qt.win_show.text()),
                                            delate=WindowCons.FALSE_NUMBER)
            DbUtil.add_record(buiness_record)
        if sale_num > 0:
            try:
                date_time = datetime.datetime.strptime(self.menu_qt.sale_date_input.text(), "%Y/%m/%d").date()
            except:
                date_time = datetime.datetime.strptime(self.menu_qt.sale_date_input.text(), "%Y-%m-%d").date()
            buiness_record = BusinessRecord(share_id=share_info.id, buy_time=date_time,
                                            sale_num=sale_num, buy_avg_price=avg_price, curr_num=curr_num,
                                            sale_price=sale_price, final_profit=float(self.menu_qt.win_show.text()),
                                            delate=WindowCons.FALSE_NUMBER)
            DbUtil.add_record(buiness_record)
        return True

    def compute_win(self, last_win):
        """计算盈利"""
        try:
            sale_num = int(self.menu_qt.sale_num_input.text())
            sale_price = float(self.menu_qt.sale_price_input.text())
            avg_price = float(self.menu_qt.buv_avg_price_show.text())
            can_sale_num = int(self.menu_qt.can_sale_num_show.text())
        except Exception as e:
            print(e)
            return False
        if sale_num == 0:
            return True
        if sale_num > can_sale_num:
            self.message_box.point_out("你的卖出数量不能超过可卖数量!")
            return False
        if sale_num != 0 and sale_num >= 100 and avg_price != 0 and sale_price > 0:
            win = round((sale_price - avg_price) * sale_num, 3)
            self.menu_qt.win_show.setText(str(win + last_win))
            return True

    @staticmethod
    def compare_date(date_str):
        """比较日期是否符合"""
        sale_date = datetime.datetime.strptime(date_str, "%Y/%m/%d").date()
        if sale_date > datetime.datetime.now().date() or int(sale_date.strftime("%w")) > 5 or int(
                sale_date.strftime("%w")) == 0:
            return False
        return sale_date

    def decide_price(self, price):
        if isinstance(price, str):
            try:
                price_ = float(price)
            except ValueError:
                return False
        else:
            price_ = price
        if price_ < 0 or price_ == 0:
            return False
        return True

    def match_num(self, num, is_buy=True):
        """判断数量"""
        if isinstance(num, str):
            try:
                number = int(num)
            except:
                return False
        else:
            number = num
        if is_buy:
            if number % 100 != 0:
                # self.message_box.point_out("买入数量应为100的整数倍")
                return False
        else:
            if number < 100:
                # self.message_box.point_out("卖出数量应大于100")
                return False
        return number
