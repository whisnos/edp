from django_filters import rest_framework as filters

from product.models import ProductInfo


class ProductFilter(filters.FilterSet):
	category = filters.NumberFilter(field_name='category', help_text="根据类目")

	class Meta:
		model = ProductInfo
		fields = ['category',]

