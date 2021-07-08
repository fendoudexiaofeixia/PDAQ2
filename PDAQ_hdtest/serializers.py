from rest_framework import serializers

from Custom.models import Custom
from config_message.models import Config_Message
from .models import PDAQ_hd


class PDAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDAQ_hd
        fields = '__all__'


class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = '__all__'


class SoftSerializer(serializers.ModelSerializer):
    IP_address = serializers.StringRelatedField()  # 此方法可以用来显示外键关系中对应的真实数据，而非表中显示的id
    custom = serializers.StringRelatedField()
    camera_model = serializers.CharField(source='get_camera_model_display')
    product_name = serializers.CharField(source='get_product_name_display')
    product_status = serializers.CharField(source='get_product_status_display')

    class Meta:
        model = Config_Message
        fields = '__all__'
