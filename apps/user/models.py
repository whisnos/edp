from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

CHOICE_TYPE = {
	(0, '未知'),
	(1, '男'),
	(2, '女'),
}
# Create your models here.
class UserProfile(AbstractUser):
	mobile = models.CharField(max_length=15, null=True, blank=True, verbose_name='手机号码')
	sex = models.IntegerField(default=0, choices=CHOICE_TYPE, verbose_name='性别')
	avatar = models.CharField(max_length=200, verbose_name='头像', null=True, blank=True)
	openid = models.CharField(max_length=100, verbose_name='openid', null=True, blank=True)
	add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

	def __str__(self):
		return self.username
