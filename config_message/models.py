from django.core.cache import cache
from django.db import models

# Create your models here.
from PDAQ_hdtest.models import PDAQ_hd
from Custom.models import Custom


class Config_Message(models.Model):
    camera_model = 1
    Forward_view_mode = 2
    camera_forward = 3
    look_forward = 4
    back_forward = 5
    BSD = 6
    MODELS_ITEMS = {
        (camera_model, '相机模式（01）'),
        (Forward_view_mode, '前视模式（02）'),
        (camera_forward, '相机+前视（03）'),
        (look_forward, '环视（04）'),
        (back_forward, '后视（05）'),
        (BSD, 'BSD（06）'),
    }
    calmcar = 1
    vbox = 2
    NAME_ITEMS = {
        (calmcar, 'calmcar'),
        (vbox, 'vbox')
    }
    production = 1
    test = 2
    develop = 3
    STATUS_ITEMS = {
        (production, '生产模式'),
        (test, '测试'),
        (develop, '开发模式')
    }
    # hard_number = models.CharField(max_length=5, verbose_name='硬件版本', )
    IP_address = models.OneToOneField(PDAQ_hd, on_delete=models.PROTECT, verbose_name='IP地址', related_name='ip_address')
    custom = models.ForeignKey(Custom, related_name='custom', verbose_name='客户', on_delete=models.CASCADE,
                               db_constraint=False)
    product_name = models.IntegerField(verbose_name='产品名称', default=vbox, choices=NAME_ITEMS)
    product_status = models.IntegerField(default=production, choices=STATUS_ITEMS, verbose_name='产品状态')
    # product_time = models.CharField(max_length=8, verbose_name='出厂日期')
    create_time = models.DateTimeField(verbose_name='出厂日期')
    # add_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')
    camera_model = models.IntegerField(default=camera_model, choices=MODELS_ITEMS, verbose_name='相机模式')
    Serial_number = models.CharField(max_length=50, unique=True, verbose_name='序列号')
    unique_serial = models.CharField(max_length=5, unique=True, verbose_name='唯一序列号')
    resolution = models.CharField(max_length=10, blank=True, null=True, verbose_name='相机分辨率', default='1280x1080')
    camera_num = models.CharField(max_length=3, blank=True, null=True, verbose_name='相机数量', default=6)
    image_format = models.CharField(max_length=10, blank=True, null=True, verbose_name='图像格式', default='YUYV')
    program_version = models.CharField(max_length=50, blank=True, null=True, verbose_name='程序版本')
    online_status = models.CharField(max_length=10, null=True, blank=True, verbose_name='在线状态', default='离线')

    def __str__(self):
        return self.Serial_number

    class Meta:
        verbose_name_plural = verbose_name = '软件配置信息'

    @classmethod
    def ip_set(cls):
        result = cache.get('ip_set')
        if not result:
            set_ip = cls.objects.get_queryset().values('IP_address__IP_address')
            cache.set('ip_set', set_ip, 60 * 60)
        return result
