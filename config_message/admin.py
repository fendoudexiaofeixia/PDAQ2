import xadmin
from django.contrib import admin

# Register your models here.

from config_message.models import Config_Message


@xadmin.sites.register(Config_Message)
class ConfigAdmin(object):
    list_display = (
        'IP_address', 'Serial_number', 'camera_model', 'unique_serial', 'program_version', 'create_time'
    )
    ordering = ('unique_serial',)
    '''快速显示详情的字段'''
    show_detail_fields = ('Serial_number',)
