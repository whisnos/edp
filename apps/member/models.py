from datetime import datetime

from django.db import models

CHOICE_TYPE = {
	(0, '未知'),
	(1, '男'),
	(2, '女'),
}


# Create your models here.
class Member(models.Model):
	nickname = models.CharField(max_length=100, verbose_name='名称')
	mobile = models.CharField(max_length=15, null=True, blank=True, verbose_name='手机号码')
	sex = models.IntegerField(default=0, choices=CHOICE_TYPE, verbose_name='性别')
	avatar = models.CharField(max_length=200, verbose_name='头像')
	# reg_ip = db.Column(db.String(100), nullable=True)
	# status = db.Column(db.Integer, nullable=False, default=1)
	# updated_time = db.Column(db.DateTime, nullable=False)
	# created_time = db.Column(db.DateTime, index=True, default=datetime.now)
	add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
