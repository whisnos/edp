from datetime import datetime

from django.db import models


# Create your models here.
from DjangoUeditor.models import UEditorField


class CategoryInfo(models.Model):
	name = models.CharField(max_length=15, verbose_name='类目')
	weight = models.IntegerField(default=1, verbose_name='权重')
	status = models.BooleanField(default=1, verbose_name='状态')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '类别管理'
		verbose_name_plural = verbose_name


class ProductInfo(models.Model):
	category = models.ForeignKey(CategoryInfo, on_delete=models.CASCADE, verbose_name='类目')
	name = models.CharField(max_length=100, verbose_name='标题')
	price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='售价')
	original_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='原价')
	main_image = models.ImageField(upload_to='product/images/', verbose_name="封面图",null=True, blank=True,)
	# summary = models.TextField(max_length=500, verbose_name='商品描述', null=True, blank=True, )
	summary = UEditorField('商品描述', width=900, height=400, toolbars='full', imagePath='ueditor/image/',
							  filePath='ueditor/file/', null=True, blank=True)
	stock = models.IntegerField(default=0, verbose_name='库存量')
	# tags = db.Column(db.String(200), nullable=False)
	status = models.BooleanField(default=1, verbose_name='状态')
	# month_count = db.Column(db.Integer, default=0)
	# total_count = db.Column(db.Integer, default=0)
	# view_count = db.Column(db.Integer, default=0)
	# comment_count = db.Column(db.Integer, default=0)
	# updated_time = db.Column(db.DateTime, nullable=False)
	add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '产品中心'
		verbose_name_plural = verbose_name

class ProductImage(models.Model):
	product = models.ForeignKey(ProductInfo, verbose_name='所属商品', related_name="images")
	image = models.ImageField(upload_to='product/banner_images/', verbose_name='商品导图', null=True, blank=True, )
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	class Meta:
		verbose_name = "商品图片"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.product.name

# 首页广告图
class BannerAd(models.Model):
	product = models.ForeignKey(ProductInfo, verbose_name='所属商品', unique=True)
	image = models.ImageField(upload_to='banner/images/', verbose_name='导航图', )
	status = models.BooleanField(default=True, verbose_name='状态')
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name = '首页幻灯片'
		verbose_name_plural = verbose_name

class BannerAd1(models.Model):
	product = models.ForeignKey(ProductInfo, verbose_name='所属商品', unique=True)
	status = models.BooleanField(default=True, verbose_name='状态')
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")