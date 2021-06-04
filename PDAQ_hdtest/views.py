import base64
import json
from io import BytesIO

from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from matplotlib import pyplot as plt
from numpy.matlib import randn

from PDAQ_hdtest.models import PDAQ_hd


def hwtest_list(request, pdaq_id=None):
    # print(request.method)
    # if request.method == 'GET':
    dic = {}
    pdaq = PDAQ_hd.get_by_all()
    # print(pdaq)
    n = 0
    for i in pdaq:
        # print('**************************', dic, i)
        dic[n] = str(i)
        n += 1
    # print(dic)
        print(JsonResponse({'data': str(i)}))
        return JsonResponse({
            'data': str(i)
        })

# def pdaq_num(request):
#     pdaq_n, pass_num = PDAQ_hd.get_pdaq_message()
#     # print('**************************************', test_num)
#     pass_rate = pass_num / pdaq_n * 100
#     defect_rate = 100 - pass_rate
#     context = {
#         'pdaq_num': pdaq_n,
#         'pass_rate': pass_rate,
#         'defect_rate': defect_rate,
#     }
#     return render(request, context=context)
