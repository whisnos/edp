from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

from product.filters import ProductFilter
from product.models import CategoryInfo, ProductInfo, BannerAd
from product.serializers import CategorySerializer, ProductSerializer, BannerSerializer, ProductRetrieveSerializer


class ProductListSetPagination(PageNumberPagination):
	page_size = 12
	page_query_param = 'page'
	page_size_query_param = 'page_size'  # 配置动态显示条数
	max_page_size = 100

class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,):
	queryset = CategoryInfo.objects.all()
	serializer_class = CategorySerializer
	# 返回首页 不能有分页
	# pagination_class = GoodsCategoryPagination

	# filter_backends = (filters.DjangoFilterBackend, SearchFilter)
	# search_fields = ['name']

# CacheResponseMixin
class ProductListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
	queryset = ProductInfo.objects.all()
	pagination_class = ProductListSetPagination
	filter_backends = (DjangoFilterBackend,SearchFilter)
	filter_class = ProductFilter
	search_fields = ('name',)
	def get_serializer_class(self):
		if self.action == 'retrieve':
			return ProductRetrieveSerializer
		return ProductSerializer
	# throttle_classes = (AnonRateThrottle,UserRateThrottle)
	# Token 认证 有缺点 下面 用jwt认证
	# authentication_classes = (TokenAuthentication,)
	# authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)

	# # 第一种 原始重写
	# # def get_queryset(self):
	# # 	pricemin = self.request.query_params.get('pricemin')
	# # 	if pricemin:
	# # 		return self.queryset.filter(shop_price=int(pricemin))
	# # 	return self.queryset
	#
	# # 第二种 采用 django_filters 缺陷 不能模糊查询 和 区间
	# filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
	# # filterset_fields = ('name', 'shop_price', 'category')
	#
	# search_fields = ['name', 'goods_brief', 'goods_desc']
	# ordering_fields = ['shop_price', 'sold_num']
	# # 第三种 重写过滤器 能达到 区间过滤
	# filter_class = GoodFilter

class BannerViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
	queryset = BannerAd.objects.all()
	serializer_class = BannerSerializer