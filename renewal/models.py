from django.db import models
from common.models import CoreModel


# Create your models here.


class Project(CoreModel):
    name = models.CharField(max_length=100, null=True, verbose_name='项目名')
    description = models.CharField(max_length=2000, null=True, verbose_name='项目描述')
    last_pay_at = models.DateField(null=True, verbose_name='付款时间')
    next_pay_at = models.DateField(null=True, verbose_name='到期时间')
    remarks = models.CharField(max_length=3000, blank=True, null=True, verbose_name='备注')
    # 未通知=0 已通知 =1
    status = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ('next_pay_at',)
        verbose_name = '续费项目'
        verbose_name_plural = verbose_name
