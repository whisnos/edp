from django.contrib import admin

# Register your models here.
import xadmin
from trade.models import ShopingCart


class ShopingCartXadmin(object):
	list_display = ['user', 'product', 'nums', 'add_time']


xadmin.site.register(ShopingCart, ShopingCartXadmin)
