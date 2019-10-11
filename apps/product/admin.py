from django.contrib import admin

# Register your models here.
import xadmin
from product.models import CategoryInfo, BannerAd, ProductInfo, ProductImage


class CategoryXadmin(object):
	list_display = ['name', 'add_time']


class BannerADXadmin(object):
	list_display = ['product', 'add_time']
	# style_fields = {'content': 'ueditor'}
	search_fields = ['product']
	list_editable = ['status', ]


class ProductXadmin(object):
	list_display = ['name', 'price', 'original_price', 'stock', 'status', 'add_time']
	search_fields = ['name']
	style_fields = {'summary': 'ueditor'}
	list_editable = ['name', 'price', 'original_price', 'stock', 'status', ]

class ProductImageXadmin(object):
	list_display = ['id','product','add_time']

xadmin.site.register(CategoryInfo, CategoryXadmin)
xadmin.site.register(BannerAd, BannerADXadmin)
xadmin.site.register(ProductInfo, ProductXadmin)
xadmin.site.register(ProductImage, ProductImageXadmin)
