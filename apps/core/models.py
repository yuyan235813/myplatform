from django.db import models
from django.contrib.auth.models import AbstractUser
from conf.constant import FIRST_USER_ID
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    """
    扩展用户信息
    """
    user_id = models.BigIntegerField(u'用户iD', default=FIRST_USER_ID)
    real_name = models.CharField(u'真实姓名', max_length=32, blank=True, null=True)
    nick_name = models.CharField(u'昵称', max_length=20, blank=True, null=True)
    birthday = models.DateTimeField(u'生日', blank=True, null=True)
    gender = models.CharField(u'性别', max_length=10, choices=(('male', u'男'), ('female', u'女')), default='male')
    last_ip = models.GenericIPAddressField(u'上次登录IP', blank=True, null=True)
    amount = models.FloatField(u'账户余额', default=0., blank=True)
    level = models.IntegerField(u'用户等级', default=1, blank=True)
    phone_number = models.BigIntegerField(u'手机号码', null=True)
    home_address = models.CharField(u'户籍地址', max_length=100, null=True)
    house_address = models.CharField(u'现在地址', max_length=100, null=True)
    card_number = models.CharField(u'身份证号', max_length=18, default=0)
    qq_number = models.BigIntegerField(u'QQ号码', blank=True, null=True)
    wechat = models.CharField(u'微信帐号', max_length=32, blank=True, null=True)
    remarks = models.TextField(u'备注信息', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if self.user_id <= FIRST_USER_ID:
            last_user = UserProfile.objects.all().order_by('user_id').last()
            if not last_user:
                self.user_id = FIRST_USER_ID
            else:
                last_user_id = last_user.user_id
                self.user_id = int(last_user_id) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Inventory(models.Model):
    """
    仓库信息表
    """
    pass


class GoodsCategory(models.Model):
    """
    商品类型表
    """
    icon = models.FilePathField(u'图片地址', default='')
    name = models.CharField(u'类型名称', max_length=32, default='')
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    state = models.IntegerField(_('节点状态'), choices=(('有效', 1),  ('无效', 0)), default=1)


class Goods(models.Model):
    """
     商品信息表
    """
    code = models.CharField(_('商品编号'), max_length=32, unique=True)
    inventory_quantity = models.IntegerField(_('库存量'), default=0)
    last_purchasing_price = models.FloatField(_('最后进货价'), blank=True, default=0.)
    min_num = models.IntegerField(_('库存下限'), blank=True, default=0)
    model = models.CharField(_('规格型号'), max_length=64, blank=True, default=0)
    name = models.CharField(_('商品名称'), max_length=64, default='')
    producer = models.CharField(_('生产商'), blank=True, default=0)
    purchasing_price = models.FloatField(_('进货单价'), default=0)
    selling_price = models.FloatField(_('销售单价'), default=0)
    state = models.IntegerField(_('商品状态'), choices=(('有效有货', 1), ('无效', 2), ('无货', 0)), default=1)
    unit = models.CharField(_('基本单位'), blank=True, default=u'个')
    default_inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name=u'默认仓库')
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name=u'商品类型')







