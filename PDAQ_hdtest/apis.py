import json

import jsonify as jsonify
from django.db.models import Q
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Custom.models import Custom
from PDAQ_hdtest.models import PDAQ_hd
from PDAQ_hdtest.serializers import PDAQSerializer, CustomSerializer, SoftSerializer
from config_message.models import Config_Message


@api_view()
def PDAQ_list(request):
    pdaqs = PDAQ_hd.objects.all()
    pdaq_serializers = PDAQSerializer(pdaqs, many=True)
    return Response(pdaq_serializers.data)


class PDAQList(generics.ListCreateAPIView):
    queryset = PDAQ_hd.objects.all()
    serializer_class = PDAQSerializer


@api_view()
def search_pdaq(request):
    IP = request.GET.get('IP_address')
    ICCID = request.GET.get('ICCID')
    print(ICCID)
    try:
        pdaq = PDAQ_hd.objects.filter(Q(IP_address=IP) | Q(ICCID=ICCID))
    except PDAQ_hd.DoesNotExist:
        pdaq = None
    pdaq_serializers = PDAQSerializer(pdaq, many=True)
    # print(Response(pdaq_serializers.data).data)
    return Response(pdaq_serializers.data)


@api_view()
def CustomMessage(request):
    try:
        custom = Custom.objects.all()
    except Custom.DoesNotExist:
        custom = None
    custom_serializers = CustomSerializer(custom, many=True)
    return Response(custom_serializers.data)


@api_view()
def Soft_config(request):
    try:
        soft = Config_Message.objects.all()
    except Config_Message.DoesNotExist:
        soft = None
    soft_serializers = SoftSerializer(soft, many=True)
    return Response(soft_serializers.data)


@api_view()
def get_nav(request):
    # test_model = '模型'
    return Response(data=[{'name': '导航', 'children': '子类'}])


'''
下面的接口未使用，当前因前端功能开发未完成，目前搁置
使用 Q 函数进行模糊查询   下面的查询逻辑仍需继续优化
'''


@api_view()
def filter_pdaq(request):
    pdaq = []
    js_str = request.GET
    # print('+++++++++++++++++++++++++++++++++++++++++', js_str.get('IP_address'))
    if js_str.get('test_result') is None and js_str.get('PCB版本') is None:
        # print(';;;;;;;;',1)
        pdaq = PDAQ_hd.objects.all()
    else:
        if js_str.get('test_result') and js_str.get('PCB版本'):
            pdaq = PDAQ_hd.objects.filter(test_result=js_str.get('test_result'), PCB版本__startswith=js_str.get('PCB版本'))
        elif js_str.get('test_result'):
            pdaq = PDAQ_hd.objects.filter(test_result=js_str.get('test_result'))
        elif js_str.get('PCB版本') != '0':
            # print('------------------------------------', 2)
            pdaq = PDAQ_hd.objects.filter(PCB版本__startswith=js_str.get('PCB版本'))

    pdaq_serializers = PDAQSerializer(pdaq, many=True)
    # print('-----------------------', pdaq_serializers.data)
    # print('*******************************', pdaq)
    return Response(pdaq_serializers.data)
