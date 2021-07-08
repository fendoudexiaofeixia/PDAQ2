import os
import platform

import django.db.models.signals
from django.core.cache import cache
from django.core.signals import request_finished, request_started
from django.dispatch import receiver
from apscheduler.scheduler import Scheduler
# Create your views here.
from django.utils.html import format_html

from cloud_plaform.pdaq_update import pdaq_process
from config_message.models import Config_Message
from cloud_plaform.cloud_platform import cloud_platform, start_update

""" 云平台更新函数
    使用 signal 函数，当触发save()时，直接将参数传给云平台，直接更新。 
"""

""" 使用信号功能，此处一共可以传递 6 个参数，无法进行更多的参数传递


        注意此函数一定要在urls.py中进行注册，否则不会触发，可以不写路由规则
    云平台查询链接：注意参数的使用
    Request URL: http://cloud.calmcar.com:5003/product/searchByPage?pagesize=10&&pagenum=1&&name=&&code=&&
    alias=&&company=&&ip=192.168.194.172&&plate_number=&&type=&&vboxversion=&&calmcarversion=&&filesysversion=&&hardwareversion=&&online=
"""


# 在项目进行初始化的时候，对目标字段进行缓存
@receiver(django.db.models.signals.post_init, sender=Config_Message)
def init_serialnumber(instance, **kwargs):
    instance.__original_Serial_number = instance.Serial_number


# 若上面的函数缓存的初始值没有变化，则不会触发下面的函数，否则在进行保存提交的时候，会触发此函数，并同步更新云平台
@receiver(django.db.models.signals.post_save, sender=Config_Message)
def update_platform(sender, instance, created, **kwargs):
    if not created and instance.__original_Serial_number != instance.Serial_number:
        print('++++++++++++', sender, instance)
        pdaq_message = Config_Message.objects.filter(Serial_number=instance).values('IP_address__IP_address',
                                                                                    'Serial_number', 'camera_model',
                                                                                    'custom__shorthand', 'custom__name',
                                                                                    )
        pro_name = Config_Message.objects.get(Serial_number=instance).get_product_name_display()
        pro_stat = Config_Message.objects.get(Serial_number=instance).get_product_status_display()
        cloud_msg = [i for i in pdaq_message][0]
        cloud_msg['product_name'], cloud_msg['product_status'] = pro_name, pro_stat
        # print(cloud_msg)
        # 首先查询平台是否存在设备
        # start_update(cloud_msg['custom__name'], cloud_msg['IP_address__IP_address'], cloud_msg['product_name'],
        #               cloud_msg['Serial_number'], cloud_msg['product_status'])
        # pdaq_process(cloud_msg['IP_address__IP_address'], cloud_msg['Serial_number']).update_pdaq_json()
        # start_main(i['IP_address__IP_address'], i['camera_model'], i['Serial_number'], i['custom__name'])


# 自动定期执行任务，用来判断设备是否在线，将结果写入到 redis 中


sch = Scheduler()


def jug_online():
    # set_ip = Config_Message.objects.get_queryset().values('IP_address__IP_address')
    set_ip = Config_Message.ip_set()
    for ip in set_ip:
        IP = ip['IP_address__IP_address']
        # print(IP)
        visit_IP = os.popen('ping -c 1 %s' % IP)
        result = visit_IP.read()
        visit_IP.close()
        obj = Config_Message.objects.get(IP_address__IP_address=IP)
        if 'ttl' in result:
            # cache.set('{}'.format(IP), '在线', 60)
            obj.online_status = '在线'
            obj.save()

        else:
            # cache.set('{}'.format(IP), '离线', 60)
            obj.online_status = '离线'
            obj.save()

            # print(cache.get('{}'.format(IP)))
            # print(('{}'.format(IP)))

# @sch.interval_schedule(seconds=10)
# def my_task():
#     jug_online()
#
#
# sch.start()
