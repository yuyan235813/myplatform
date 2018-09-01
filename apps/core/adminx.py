#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""

import xadmin
from xadmin import views
from .models import *
from xadmin.plugins.auth import UserAdmin
from .forms import (
    MyUserChangeForm, MyUserCreationForm
)
from xadmin.layout import Fieldset, Main, Side, Row, FormHelper
from django.utils.translation import ugettext as _


class BaseSettings:
    """
    基本配置
    """
    # 开启主题选择
    enable_themes = True
    # 动态加载网络主题，已经下载到本地所以看不用开启了
    # use_bootswatch = True


class GlobalSettings:
    """
    后台修改
    """
    site_title = '进销存管理平台'
    site_footer = '进销存管理平台'
    # 开启分组折叠
    menu_style = 'accordion'


class UserProfileAdmin(UserAdmin):
    """
    重载 xadmin 中 User 的管理器
    """
    list_display = ('username', 'user_id', 'phone_number', 'real_name', 'last_login')

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset(_('登录信息'),
                             'username', 'password',
                             ),
                    Fieldset(_('Personal info'),
                             'user_id',
                             'nick_name',
                             Row('last_name', 'first_name', 'real_name'),
                             'card_number',
                             'gender',
                             'birthday',
                             'email',
                             'phone_number',
                             'home_address',
                             'house_address',
                             'qq_number',
                             'wechat'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()

    def get_model_form(self, **kwargs):
        """
        使用自定义的 UserCreationForm 和 UserChangeForm
        :param kwargs:
        :return:
        """
        if self.org_obj is None:
            self.form = MyUserCreationForm
        else:
            self.form = MyUserChangeForm
        return super(UserAdmin, self).get_model_form(**kwargs)


class GoodsAdmin:
    """
    商品管理
    """
    list_display = ['code', 'name', 'producer', 'purchasing_price']
    list_filter = ['code', 'name', 'producer']
    search_fields = ['code', 'name', 'producer']
    model_icon = 'fa fa-star'


class StateAdmin:
    """
    商品状态mapping表
    """
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    model_icon = 'fa fa-star'


class InventoryAdmin:
    """
    仓库信息表
    """
    list_display = ['code', 'name', 'inventory_category', 'address', 'phone_number']
    list_filter = ['code', 'name', 'inventory_category']
    search_fields = ['code', 'name', 'inventory_category']
    model_icon = 'fa fa-star'


class SupplierAdmin:
    """
    供应商信息表
    """
    list_display = ['name', 'contact', 'contact_number', 'address']
    list_filter = ['name', 'contact']
    search_fields = ['name', 'contact']
    model_icon = 'fa fa-star'


class GoodsCategoryAdmin:
    """
    商品类型表
    """
    list_display = ['name', 'parent', 'level', 'state']
    list_filter = ['name', 'level', 'state']
    search_fields = ['name']
    model_icon = 'fa fa-star'


class StockinAdmin:
    """
    入库信息表
    """
    list_display = ['order_id', 'comment', 'order_sn', 'add_time', 'stockin_type']
    list_filter = ['order_id', 'comment', 'order_sn', 'add_time', 'stockin_type']
    search_fields = ['order_id']
    model_icon = 'fa fa-star'




xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsUnit, StateAdmin)
xadmin.site.register(GoodsState, StateAdmin)
xadmin.site.register(CategoryState, StateAdmin)
xadmin.site.register(StockinState, StateAdmin)
xadmin.site.register(Inventory, InventoryAdmin)
xadmin.site.register(Supplier, SupplierAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Stockin, StockinAdmin)