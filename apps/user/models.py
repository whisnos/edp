from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
	add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

	def __str__(self):
		return self.username
