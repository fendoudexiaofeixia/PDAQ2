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
    if request.method == 'GET':
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

