import os

import django.db.models.signals
from django.core.signals import request_started
from django.dispatch import receiver

# Create your views here.
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


@receiver(django.db.models.signals.post_save, sender=Config_Message)
def update_platform(sender, instance, **kwargs):
    # print('++++++++++++', sender, instance)
    pdaq_message = Config_Message.objects.filter(Serial_number=instance).values('IP_address__IP_address',
                                                                                'Serial_number', 'camera_model',
                                                                                'custom__shorthand', 'custom__name',
                                                                                )
    pro_name = Config_Message.objects.get(Serial_number=instance).get_product_name_display()
    pro_stat = Config_Message.objects.get(Serial_number=instance).get_product_status_display()
    cloud_msg = [i for i in pdaq_message][0]
    cloud_msg['product_name'], cloud_msg['product_status'] = pro_name, pro_stat
    print(cloud_msg)
    # 首先查询平台是否存在设备
    # start_update(cloud_msg['custom__name'], cloud_msg['IP_address__IP_address'], cloud_msg['product_name'],
    #              cloud_msg['Serial_number'], cloud_msg['product_status'])
    # pdaq_process('192.168.196.220', cloud_msg['Serial_number']).update_pdaq_json()
    # start_main(i['IP_address__IP_address'], i['camera_model'], i['Serial_number'], i['custom__name'])


# @receiver(request_started)
# def jug_online(**kwargs):
#     product = Config_Message.objects.get_queryset().values('IP_address__IP_address')
#     pro_list = [i for i in product]
#     for pdaq in pro_list:
#         # print(pdaq['IP_address__IP_address'])
#         res = os.system('fping {} -c 1 -t 50>> /dev/null'.format(pdaq['IP_address__IP_address']))
#         # print(**kwargs)
#         if res == 0:
#             return '在线'
#         else:
#             return '离线'
