from datetime import datetime

from django.db import models


# Create your models here.
class CategoryInfo(models.Model):
	name = models.CharField(max_length=15, verbose_name='类目')
	weight = models.IntegerField(default=1, verbose_name='权重')
	status = models.BooleanField(default=1, verbose_name='状态')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')


class ProductInfo(models.Model):
	category = models.ForeignKey(CategoryInfo, on_delete=models.CASCADE, verbose_name='类目')
	name = models.CharField(max_length=100, verbose_name='标题')
	price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='售价')
	original_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='原价')
	main_image = models.ImageField(upload_to='product/images/', verbose_name="封面图")
	summary = models.TextField(max_length=500, verbose_name='商品描述', null=True, blank=True, )
	stock = models.IntegerField(default=0, verbose_name='库存量')
	# tags = db.Column(db.String(200), nullable=False)
	status = models.BooleanField(default=1, verbose_name='状态')
	# month_count = db.Column(db.Integer, default=0)
	# total_count = db.Column(db.Integer, default=0)
	# view_count = db.Column(db.Integer, default=0)
	# comment_count = db.Column(db.Integer, default=0)
	# updated_time = db.Column(db.DateTime, nullable=False)
	add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
