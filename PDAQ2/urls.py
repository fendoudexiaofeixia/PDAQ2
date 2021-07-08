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
from django.urls import path, re_path, include
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from PDAQ2 import settings
from PDAQ_hdtest.apis import PDAQList, CustomViewSet, SoftViewSet, get_nav, SearchViewSet
from PDAQ_hdtest.views import hwtest_list
from django.views.generic.base import TemplateView

from config_message.views import update_platform

router = DefaultRouter()
router.register(r'pdaq', PDAQList, basename='api-pdaq')
router.register(r'search', SearchViewSet, basename='search-pdaq')
router.register(r'custom', CustomViewSet, basename='custom list')
router.register(r'soft', SoftViewSet, basename='soft_config')

urlpatterns = [
    path('admin/', xadmin.site.urls),
    re_path(r'^docs/', include_docs_urls(title='pdaq2')),
    re_path(r'^api/', include((router.urls, 'router'), namespace='api')),
    # re_path(r'^api/pdaq', PDAQList, name='pdaq_list'),
    # re_path(r'^api/filter/', PDAQList, name='filter_recorder'),  # 此接口未使用，因目前实力不够，无法完成开发
    # re_path(r'^api/search/', name='serach'),
    # re_path(r'^api/custom', CustomMessage, name='custom_message'),
    # re_path(r'^api/soft', Soft_config, name='soft_config'),
    re_path(r'^model/get_nav', get_nav, name='get_nav'),
    re_path(r"media/(?P<path>.*)$", serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path(r'update_platform', update_platform),
]
urlpatterns += staticfiles_urlpatterns()
