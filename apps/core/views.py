#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/10 12:56
@Author  : lizhiran
@Email   : 794339312@qq.com
"""

from django.http import HttpResponse, HttpRequest


def index(reqeust: HttpRequest):
    print(reqeust.POST.dict())
    return HttpResponse('hello world')