import django_filters

from PDAQ_hdtest.models import PDAQ_hd


class PdaqFilter(django_filters.FilterSet):
    class Meta:
        model = PDAQ_hd
        fields = ['IP_address', 'ICCID']
