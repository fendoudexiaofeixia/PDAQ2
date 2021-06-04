from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from PDAQ_hdtest.models import PDAQ_hd
from PDAQ_hdtest.serializers import PDAQSerializer


@api_view()
def PDAQ_list(request):
    pdaqs = PDAQ_hd.objects.all()
    pdaq_serializers = PDAQSerializer(pdaqs, many=True)
    return Response(pdaq_serializers.data)


class PDAQList(generics.ListCreateAPIView):
    queryset = PDAQ_hd.objects.all()
    serializer_class = PDAQSerializer


def get_nav(request):
    return None