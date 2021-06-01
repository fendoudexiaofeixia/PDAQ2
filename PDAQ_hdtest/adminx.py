import xadmin
from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from xadmin import views
from xadmin.layout import Row, Fieldset

from PDAQ_hdtest.models import PDAQ_hd


@xadmin.sites.register(PDAQ_hd)
class PdaqAdmin(object):
    list_display = (
        'IP_address', 'ICCID', 'PCB版本', '添加时间', 'test_result_colour', 'file_link'
    )
    form_layout = (Fieldset(
        '基础设置：', Row(
            'IP_address', 'PCB版本', 'test_result',
        )),
                   Fieldset('写入测试',
                            'SATA写入速率', 'SATA读取速率', 'USB1读取速率', 'USB1写入速率', 'USB2写入速率', 'USB2读取速率', 'SD卡读取速率',
                            'SD卡写入速率', '网口速率',
                            ),
                   Fieldset('功能测试',
                            'GPS', '移动网速',
                            ),
    )

    # list_display_links = ('test_file', 'IP_address')
    autocomplete_fields = ('IP_address',)
    # raw_id_fields = ('IP_address',)
    search_fields = ('IP_address',)
    list_filter = ('test_result', 'PCB版本')
    ordering = ('添加时间',)
    '''快速显示详情的字段'''
    show_detail_fields = ('IP_address',)
    '''设置可直接配置的字段'''
    list_editable = ('file_link',)
    # prepopulated_fields =
    # exclude = ()
    # data_charts = {
    #     "user_count": {'title': u"出货总计",
    #                    "x-field": "IP_address",
    #                    "y-field": ("添加时间",),
    #                    },
    # }

    '''设置字段链接   可跳转'''

    def file_link(self, obj):
        # print('******************', obj.test_file)
        return format_html(
            "<a href='/media/{}'>{}</a>", obj.test_file, obj.test_file
        )

    file_link.short_description = '测试文件'

    def test_result_colour(self, obj):
        if obj.test_result == '合格':
            # print('*******', obj.test_result)
            color_code = 'green'
        else:
            color_code = 'red'
        return format_html(
            '<span style="color:{};">{}</span>', color_code, obj.test_result
        )

    test_result_colour.short_description = '测试结果'





class BaseSetting(object):
    enable_themes = True
    use_bootstrap = True
    reversion_enable = True
    show_bookmarks = True


class GlobalSetting(object):
    site_title = '测试信息管理系统2.0'
    site_footer = '技术支持  @testteam'
    # menu_style = 'accordion'  #设置菜单折叠功能


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
