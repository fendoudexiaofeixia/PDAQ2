from django.db import models

# Create your models here.
from django.utils.html import format_html


class PDAQ_hd(models.Model):
    def __str__(self):
        return self.IP_address

    IP_address = models.CharField(max_length=20, unique=True, verbose_name='IP地址')
    hd_version = models.CharField(max_length=10, verbose_name='硬件版本', blank=True, null=True)
    系统自启 = models.CharField(max_length=20, null=True, blank=True, verbose_name='系统自启')
    时间同步 = models.CharField(max_length=20, null=True, blank=True, verbose_name='时间同步')
    相机接口 = models.CharField(max_length=20, null=True, blank=True, verbose_name='相机接口')
    GPS = models.CharField(max_length=20, null=True, blank=True, verbose_name='GPS')
    SATA写入速率 = models.CharField(max_length=30, null=True, blank=True, verbose_name='SATA写入速率')
    SATA读取速率 = models.CharField(max_length=30, null=True, blank=True, verbose_name='SATA读取速率')
    USB1读取速率 = models.CharField(max_length=30, null=True, blank=True, verbose_name='USB1读取速率')
    USB1写入速率 = models.CharField(max_length=30, null=True, blank=True, verbose_name='USB1写入速率')
    USB2写入速率 = models.CharField(max_length=30, null=True, blank=True, verbose_name='USB2写入速率')
    USB2读取速率 = models.CharField(max_length=30, null=True, blank=True, verbose_name='USB2读取速率')
    SD卡读取速率 = models.CharField(max_length=30, null=True, blank=True, verbose_name='SD卡读取速率')
    SD卡写入速率 = models.CharField(max_length=30, null=True, blank=True, verbose_name='SD卡写入速率')
    网口速率 = models.CharField(max_length=30, null=True, blank=True, verbose_name='网口速率')
    移动网速 = models.CharField(max_length=30, null=True, blank=True, verbose_name='4G速率')
    ICCID = models.CharField(max_length=30, null=True, blank=True, verbose_name='ICCID')
    MEID = models.CharField(max_length=30, null=True, blank=True, verbose_name='MEID')
    IMEI = models.CharField(max_length=30, null=True, blank=True, verbose_name='IMEI')
    CAN板状态 = models.CharField(max_length=30, null=True, blank=True, verbose_name='CAN板状态')
    系统版本 = models.CharField(max_length=50, null=True, blank=True, verbose_name='系统版本')
    内核版本 = models.CharField(max_length=50, null=True, blank=True, verbose_name='内核版本')
    PCB版本 = models.CharField(max_length=50, null=True, blank=True, verbose_name='PCB版本')
    添加时间 = models.DateField(auto_now_add=True, verbose_name='添加时间')
    test_result = models.CharField(max_length=5, verbose_name='测试结果', blank=False, null=False)
    Operators = models.CharField(max_length=20, null=True, blank=True, verbose_name='运行商')
    Activation_time = models.CharField(max_length=50, blank=True, null=True, verbose_name='激活时间')
    Expiration_time = models.CharField(max_length=50, blank=True, null=True, verbose_name='过期时间')
    Card_status = models.CharField(max_length=20, blank=True, null=True, verbose_name='卡片状态')
    Set_meal = models.CharField(max_length=10, null=True, blank=True, verbose_name='套餐')
    Set_meal_used = models.CharField(max_length=20, null=True, blank=True, verbose_name='套餐已用')
    test_file = models.FileField(verbose_name='测试文件', upload_to='test_file', blank=True, null=True)

    class Meta:
        verbose_name_plural = verbose_name = 'PDAQ硬件测试信息'

    @staticmethod
    def get_by_all():
        try:
            pdaq = PDAQ_hd.objects.all()
            print(pdaq.count())
        except PDAQ_hd.DoesNotExist:
            pdaq = None
        return pdaq
