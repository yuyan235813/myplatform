#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""

import xadmin
from xadmin import views


class BaseSettings:
    """
    基本配置
    """
    # 开启主题选择
    enable_themes = True
    # 动态加载网络主题，已经下载到本地所以看不用开启了
    # use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSettings)
