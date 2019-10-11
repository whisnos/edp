from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from trade.models import ShopingCart
from trade.serializers import ShopingCartDetailSerializer, ShopingCartSerializer
from utils.permissions import IsOwnerOrReadOnly


class ShopingCartViewSet(viewsets.ModelViewSet):

	def perform_create(self, serializer):

		new_shopcart = serializer.save()
		nums = new_shopcart.nums

		goods = new_shopcart.goods
		goods.goods_num -= nums
		goods.save()

	def perform_update(self, serializer):
		# 新购物车对象
		old_shopcart = ShopingCart.objects.get(id=serializer.instance.id)
		old_nums = old_shopcart.nums
		new_shopcart = serializer.save()

		# 新购物车 添加数量
		new_nums = new_shopcart.nums

		# 新 - 旧 查量   比如 5 =新10 -旧5 那就是 多购买5个 那库存就要 减5
		cha_nums = new_nums - old_nums
		goods = old_shopcart.goods
		goods.goods_num -= cha_nums
		goods.save()

	def perform_destroy(self, instance):
		nums = instance.nums
		goods = instance.goods
		goods.goods_num += nums
		goods.save()
		instance.delete()

	queryset = ShopingCart.objects.all()

	def get_queryset(self):
		print('self.request.user',self.request.user)
		return self.queryset.filter(user=self.request.user)

	# serializer_class = ShopingCartSerializer
	# 构建动态序列化器 因为购物车list的时候 需要展现产品信息
	def get_serializer_class(self):
		if self.action == 'list':
			return ShopingCartDetailSerializer
		else:
			return ShopingCartSerializer

	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
	authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

	# 记得把 id 改为 商品id
	# lookup_field = 'goods_id'