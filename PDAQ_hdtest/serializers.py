from rest_framework import serializers
from .models import PDAQ_hd


class PDAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDAQ_hd
        fields = ('IP_address', 'ICCID', 'PCB版本', '添加时间', 'test_result')
