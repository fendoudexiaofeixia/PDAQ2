from django.shortcuts import render

# Create your views here.
from PDAQ_hdtest.models import PDAQ_hd


def hwtest_list(request, pdaq_id=None):
    pdaq = PDAQ_hd.get_by_all()
    print('*********************', pdaq)
    context = {
        'pdaq': pdaq,
    }
    return render(request, '', context=context)
