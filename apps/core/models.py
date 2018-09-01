from django.db import models
from django.utils import timezone
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
    last_ip = models.GenericIPAddressField(u'上次登录IP', default='127.0.0.1')
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

# https://www.processon.com/view/56c409abe4b0e2317a865295
# https://www.processon.com/view/56c480e0e4b0e5041c358d9e
# https://www.processon.com/view/5b04237fe4b01f32972cc7d3
# https://www.processon.com/view/5899659be4b0c87c6402178f


class GoodsState(models.Model):
    """
    商品状态mapping表
    """
    name = models.CharField(u'商品状态', unique=True, max_length=32, default='')

    class Meta(AbstractUser.Meta):
        verbose_name = '商品状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsUnit(models.Model):
    """
    商品单位mapping表
    """
    name = models.CharField(u'商品单位', unique=True, max_length=32, default='')

    class Meta(AbstractUser.Meta):
        verbose_name = '商品单位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CategoryState(models.Model):
    """
    商品类型状态mapping表
    """
    name = models.CharField(u'商品类型状态', unique=True, max_length=32, default='')

    class Meta(AbstractUser.Meta):
        verbose_name = '商品类型状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class StockinState(models.Model):
    """
    入库状态mapping表
    """
    name = models.CharField(u'入库状态', unique=True, max_length=32, default='')

    class Meta(AbstractUser.Meta):
        verbose_name = '入库状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Inventory(models.Model):
    """
    仓库信息表
    """
    code = models.CharField(u'仓库编码', max_length=32)
    name = models.CharField(u'仓库名称', max_length=32)
    inventory_category = models.CharField(u'仓库类型', max_length=32, default=u'普通仓')
    address = models.CharField(u'仓库地址', max_length=64, blank=True, null=True)
    phone_number = models.BigIntegerField(u'联系电话', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = '仓库信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Supplier(models.Model):
    """
    供应商信息表
    """
    name = models.CharField(u'供应商名', max_length=64)
    contact = models.CharField(u'联系人', max_length=32)
    contact_number = models.BigIntegerField(u'联系电话')
    address = models.CharField(u'地址', max_length=64, blank=True, null=True)
    remarks = models.TextField(u'备注', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        verbose_name = '供应商信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategory(models.Model):
    """
    商品类型表
    """
    icon = models.ImageField(u'图片地址', upload_to="media")
    name = models.CharField(u'类型名称', max_length=32, default='', unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'上级分类')
    level = models.IntegerField(u'类型级别', default=1)
    state = models.ForeignKey(CategoryState, on_delete=models.CASCADE, verbose_name=u'节点状态')

    class Meta(AbstractUser.Meta):
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


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
    producer = models.CharField(_('生产商'), max_length=128, blank=True, default=0)
    purchasing_price = models.FloatField(_('进货单价'), default=0)
    selling_price = models.FloatField(_('销售单价'), default=0)
    state = models.ForeignKey(GoodsState, on_delete=models.CASCADE, verbose_name=u'商品状态')
    unit = models.ForeignKey(GoodsUnit, on_delete=models.CASCADE, verbose_name=u'基本单位')
    default_inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name=u'默认仓库')
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name=u'商品类型')

    class Meta(AbstractUser.Meta):
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Stockin(models.Model):
    """
    入库信息表
    """
    order_id = models.BigIntegerField(u'入库单ID')
    comment = models.CharField(u'描述', max_length=256, blank=True, null=True)
    order_sn = models.CharField(u'订单号', max_length=64)
    add_time = models.DateTimeField(u'添加时间', default=timezone.now)
    out_time = models.DateTimeField(u'出库时间', null=True, blank=True)
    stockin_type = models.CharField(u'入库类型', max_length=32, default=u'入库')
    inventory = models.ForeignKey(Inventory,  on_delete=models.CASCADE, verbose_name=u'仓库')
    state = models.ForeignKey(StockinState, on_delete=models.CASCADE, verbose_name=u'入库状态')
    add_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'添加人')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name=u'供应商')

    class Meta(AbstractUser.Meta):
        verbose_name = '入库信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_id









