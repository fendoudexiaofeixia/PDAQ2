import json

import jsonify as jsonify
from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponse
from rest_framework import generics, viewsets, filters, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Custom.models import Custom
from PDAQ_hdtest.models import PDAQ_hd
from PDAQ_hdtest.serializers import PDAQSerializer, CustomSerializer, SoftSerializer
from config_message.models import Config_Message


# @api_view()
# def PDAQ_list(request):
#     pdaqs = PDAQ_hd.objects.all()
#     pdaq_serializers = PDAQSerializer(pdaqs, many=True)
#     return Response(pdaq_serializers.data)


class PDAQList(viewsets.ModelViewSet):
    if cache.get('pdaq_set') is None:
        cache.set('pdaq_set', PDAQ_hd.objects.get_queryset().all(), 60 * 60)
    queryset = cache.get('pdaq_set')
    serializer_class = PDAQSerializer


# 搜索接口定义 可以进行 IP 地址以及 ICCID 的搜索
class SearchViewSet(viewsets.generics.ListAPIView, viewsets.ViewSet):
    queryset = PDAQ_hd.objects.all()
    serializer_class = PDAQSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('IP_address', 'ICCID')


class CustomViewSet(viewsets.ModelViewSet):
    if cache.get('custom_set') is None:
        # queryset =
        cache.set('custom_set', Custom.objects.get_queryset().all(), 60 * 60)
    queryset = cache.get('custom_set')
    serializer_class = CustomSerializer


# @api_view()
# def Soft_config(request):
#     try:
#         soft = Config_Message.objects.all()
#     except Config_Message.DoesNotExist:
#         soft = None
#     soft_serializers = SoftSerializer(soft, many=True)
#     return Response(soft_serializers.data)


class SoftViewSet(viewsets.ModelViewSet):
    if cache.get('soft_set') is None:
        cache.set('soft_set', Config_Message.objects.get_queryset().all(), 60 * 60)
    queryset = cache.get('soft_set')
    serializer_class = SoftSerializer


@api_view()
def get_nav(request):
    # test_model = '模型'
    return Response(data=[{'name': '导航', 'children': '子类'}])


'''
下面的接口未使用，当前因前端功能开发未完成，目前搁置
使用 Q 函数进行模糊查询   下面的查询逻辑仍需继续优化
'''
