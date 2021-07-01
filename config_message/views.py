import django.db.models.signals
from django.core.signals import request_finished
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from automatic_configuration_tool.python.main_process import start_main
from config_message.models import Config_Message

""" 云平台更新函数
    使用 signal 函数，当触发save()时，直接将参数传给云平台，直接更新。 
"""

""" 使用信号功能，此处一共可以传递 6 个参数，无法进行更多的参数传递


        注意此函数一定要在urls.py中进行注册，否则不会触发，可以不写路由规则
 
"""


@receiver(django.db.models.signals.post_save, sender=Config_Message)
def update_platform(sender, instance, **kwargs):
    # print('++++++++++++', sender, instance)
    pdaq_message = Config_Message.objects.filter(Serial_number=instance).values('IP_address__IP_address',
                                                                                'Serial_number', 'camera_model',
                                                                                'custom__shorthand', 'custom__name')
    for i in pdaq_message:
        print(i)
        # start_main(i['IP_address__IP_address'], i['camera_model'], i['Serial_number'], i['custom__name'])
