"""PDAQ2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from PDAQ2 import settings
from PDAQ_hdtest.apis import PDAQ_list, PDAQList, filter_pdaq, search_pdaq, CustomMessage, Soft_config,get_nav
from PDAQ_hdtest.views import hwtest_list
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', xadmin.site.urls),
    re_path(r'^api/pdaq', PDAQ_list, name='pdaq_list'),
    re_path(r'^api/filter/', filter_pdaq, name='filter_recorder'),  # 此接口未使用，因目前实力不够，无法完成开发
    re_path(r'^api/search', search_pdaq, name='serach_pdaq'),
    re_path(r'^api/custom', CustomMessage, name='custom_message'),
    re_path(r'^api/soft', Soft_config, name='soft_config'),
    re_path(r'^model/get_nav',get_nav,name='get_nav'),
    re_path(r"media/(?P<path>.*)$", serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns += staticfiles_urlpatterns()
