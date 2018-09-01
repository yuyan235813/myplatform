#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
http://www.aaron-zhao.com/post/7/
"""

import datetime
from django.utils import timezone
from django.core.cache import cache
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from .models import UserProfile


class UserProfileMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        处理登录请求
        :param request:
        :return:
        """
        if request.user.is_authenticated:
            cache_key = '%s_last_login' % request.user.username
            now = timezone.now()
            last_ip = request.META['REMOTE_ADDR']
            # 用户是第一次登录、或者是缓存过期、或者是服务器重启导致缓存消失
            if not cache.get(cache_key):
                # print('#### cache not found #####')
                obj, created = UserProfile.objects.get_or_create(username=request.user)
                if not created:
                    # print("#### login before #####")
                    obj.last_login = now
                    obj.last_ip = last_ip
                    obj.save()
                cache.set(cache_key, now, settings.USER_LAST_LOGIN_EXPIRE)
            else:
                # print("##### cache found ######")
                limit = now - datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)
                # 距离上一次发送request请求的时间 超过了TIMEOUT，更新上一次login的时间
                if cache.get(cache_key) < limit:
                    # print("#### renew login #####")
                    obj = UserProfile.objects.get(username=request.user)
                    obj.last_login = now
                    obj.last_ip = last_ip
                    obj.save()
                cache.set(cache_key, now, settings.USER_LAST_LOGIN_EXPIRE)
        return None