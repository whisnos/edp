from rest_framework import serializers

from product.models import ProductInfo
from product.serializers import ProductSerializer
from trade.models import ShopingCart


class ShopingCartDetailSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False)

	class Meta:
		model = ShopingCart
		fields = '__all__'


class ShopingCartSerializer(serializers.Serializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	product = serializers.PrimaryKeyRelatedField(required=True, queryset=ProductInfo.objects.all())
	nums = serializers.IntegerField(required=True, min_value=1, help_text='购买商品数量')

	def create(self, validated_data):
		user = self.context['request'].user
		product = validated_data['product']
		nums = validated_data['nums']
		exisited = ShopingCart.objects.filter(user=user, product=product)
		if exisited:
			exisited = exisited[0]
			exisited.nums += nums
			exisited.save()  # 记得返回对象
		else:
			exisited = ShopingCart()
			exisited.nums = nums
			exisited.product = product
			exisited.user = user
			exisited.save()  # 记得返回对象
		return exisited

	# 因为用的是Serializer 灵活 所以创建购物车需要 重写 create保存，并且需要把对象返回

	# 因为继承的序列化器不是model 所以当操作修改的时候 也需要重写保存
	def update(self, instance, validated_data):
		nums = validated_data['nums']
		instance.nums = nums
		instance.save()
		return instance
