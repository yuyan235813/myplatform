#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/10 12:58
@Author  : lizhiran
@Email   : 794339312@qq.com
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]