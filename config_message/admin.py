import os
from ftplib import FTP

import xadmin
from django import forms
from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

import config_message
from config_message.models import Config_Message
# from config_message.views import jug_online


class ConfigForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)
        """ 获取目前唯一序列号的最大值 """
        help_text = Config_Message.objects.order_by('-unique_serial').first()
        # print('*******************', help_text)
        if help_text:
            self.fields['unique_serial'].help_text = "推荐目前唯一序列号为 %s" % str(int(help_text.unique_serial) + 1)
            self.fields['Serial_number'].help_text = "序列号格式为 XX(相机模式)-XX(硬件版本)-XXXX（出厂日期）-XXX（唯一序列号）"
            # print('+++++++++++++++', self.fields['unique_serial'].help_text)
        self.fields['unique_serial'].help_text = format_html(
            '<p style="color: red;"> {} !</p>'.format(self.fields['unique_serial'].help_text))
        self.fields['Serial_number'].help_text = format_html(
            '<p style="color: red;"> {} !</p>'.format(self.fields['Serial_number'].help_text)
        )
    # a = jug_online()
    # print(a)

    class Meta:
        model = Config_Message
        exclude = ()


@xadmin.sites.register(Config_Message)
class ConfigAdmin(object):
    list_display = (
        'IP_address', 'Serial_number', 'product_name', 'product_status', 'camera_model', 'unique_serial',
        'program_version', 'create_time'
    )
    ordering = ('unique_serial',)
    '''快速显示详情的字段'''
    show_detail_fields = ('Serial_number',)
    form = ConfigForm

