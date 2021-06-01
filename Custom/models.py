from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Custom(models.Model):
    name = models.CharField(max_length=30, verbose_name='客户名称')
    shorthand = models.CharField(max_length=10, verbose_name='客户简写')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, db_constraint=False, verbose_name='创建者', null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = '客户信息'
