from rest_framework import serializers

from product.models import CategoryInfo, ProductInfo, BannerAd, ProductImage


class CategorySerializer(serializers.ModelSerializer):
	add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

	class Meta:
		model = CategoryInfo
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
	# many 默认是False 商品页 关联显示上级 一个产品多 1个类别 many 为False
	# category = GoodsCategorySerializer(many=False)
	# 一个产品对 多张轮播图片 所以 many为True
	# images = GoodImageSerializer(many=True)
	add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

	class Meta:
		model = ProductInfo
		# fields=['name','desc']
		fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductImage
		fields = ['image']


class ProductRetrieveSerializer(serializers.ModelSerializer):
	# many 默认是False 商品页 关联显示上级 一个产品多 1个类别 many 为False
	# category = GoodsCategorySerializer(many=False)
	# 一个产品对 多张轮播图片 所以 many为True
	add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
	images = ProductImageSerializer(many=True)

	class Meta:
		model = ProductInfo
		# fields=['name','desc']
		fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
	add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

	class Meta:
		model = BannerAd
		fields = '__all__'
