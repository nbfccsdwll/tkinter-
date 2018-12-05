#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter as tk
"""
program name :
last modification time :
changelog :
"""


class PageCount(tk.Frame):
    def __init__(self, master, **kwargs):
        """
        用户登录后的功能选择界面，可放置广告
        功能：(存/取款)、(转账)、(改密)、(账单详情)、(锁卡/挂失)、(销户) 括号代表另一界面

        :param master: 上层容器
        :param kwargs: config, height, width
        """
        # 建立框架本体
        super().__init__(master, height=kwargs["height"] if "height" in kwargs else None,
                         width=kwargs["width"] if "width" in kwargs else None)
        self.config = kwargs["config"]
        # 建立框架内容
        # 导入图片  预留：读取配置
        self.page_home_bg = tk.PhotoImage(file="%spage_count_bg.png" % self.config["image_path"])  # 背景路径
        self.image_label = tk.PhotoImage(file="%scount_label_bg.png" % self.config["image_path"])
        # 图片载体 框架靠此Label控制大小位置
        self.stage = tk.Label(self, height=kwargs["height"], width=kwargs["width"],
                              compound=tk.CENTER, image=self.page_home_bg)
        self.stage.pack()

        lb1 = tk.Label(self.stage,
                       text="卡号：%s     账户余额 ¥：%.2f" % (kwargs["card"].card_id, kwargs["card"].money),
                       compound=tk.CENTER, image=self.image_label,
                       font=("宋体", 18),
                       width=690,
                       height=30,
                       fg="red",
                       anchor="center")
        lb1.place(x=0, y=20)

