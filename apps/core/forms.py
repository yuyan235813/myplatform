#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from core.models import UserProfile
from django import forms
from django.contrib.auth.forms import (
    UserChangeForm, UserCreationForm, ReadOnlyPasswordHashField
)
from django.utils.translation import gettext, gettext_lazy as _


class MyUserChangeForm(UserChangeForm):
    """
    更改用户信息的Form
    """
    username = forms.IntegerField(label=u'用户名', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            u"不存储明文密码！如需修改，请转到"
            "<a href=\"{}\">修改密码</a>页面."
        ),
    )
    user_id = forms.CharField(label=u'员工号',widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_login = forms.DateTimeField(label=u'上次登录时间', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    date_joined = forms.DateTimeField(label=u'加入时间', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_ip = forms.GenericIPAddressField(label=u'上次登录IP', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields ='__all__'


class MyUserCreationForm(UserCreationForm):
    """
    创建用户的Form
    """
    class Meta(UserCreationForm.Meta):
        # fields = ('username', )
        model = UserProfile

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     try:
    #         UserProfile.objects.get(username=username)
    #     except UserProfile.DoesNotExist:
    #         return username
    #     raise forms.ValidationError(self.error_messages['duplicate_username'])