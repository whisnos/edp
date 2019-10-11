from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from user.models import UserProfile
from xadmin import views
import xadmin


# Register your models here.
# 设置主题
class BaseThemSet(object):
	enable_themes = True
	use_bootswatch = True


# 设置标题
class CommSetting(object):
	site_title = '后台管理系统'
	site_footer = 'XXX'
# menu_style = 'accordion'


class UserInfoAdmin(object):
	list_display = ['username', 'sex', 'openid', 'add_time']


xadmin.site.register(views.BaseAdminView, BaseThemSet)
xadmin.site.register(views.CommAdminView, CommSetting)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserInfoAdmin)
