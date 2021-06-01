import xadmin
from django.contrib import admin

# Register your models here.
from Custom.models import Custom


@xadmin.sites.register(Custom)
class CustomAdmin(object):
    list_display = (
        'name', 'shorthand', 'create_time'
    )
    reversion_enable = True
