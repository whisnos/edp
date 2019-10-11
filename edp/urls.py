"""edp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from rest_framework.routers import DefaultRouter

import xadmin
from edp.settings import MEDIA_ROOT
from product.views import CategoryViewSet, ProductListViewSet, BannerViewSet
from trade.views import ShopingCartViewSet
from user.views import LoginView, CheckView

route = DefaultRouter()
# route = SimpleRouter()
route.register(r'categorys', CategoryViewSet)
route.register(r'product', ProductListViewSet)
route.register(r'banners', BannerViewSet)
route.register(r'shopcarts', ShopingCartViewSet)
urlpatterns = [
	url(r'^', include(route.urls)),
	url(r'^ueditor/', include('DjangoUeditor.urls')),
	url('admin/', xadmin.site.urls),
	url(r'^api-auth/', include('rest_framework.urls')),
	url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
	url(r'^member/check', CheckView.as_view()),
	url(r'^member/login', LoginView.as_view()),
]
