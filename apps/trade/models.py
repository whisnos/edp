from datetime import datetime

from django.db import models

# Create your models here.
from product.models import ProductInfo
from user.models import UserProfile


class ShopingCart(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name='所属用户')
	product = models.ForeignKey(ProductInfo, verbose_name='购买商品')
	nums = models.IntegerField(default=1, verbose_name='购买数量')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	class Meta:
		verbose_name = "购物车管理"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.product.name