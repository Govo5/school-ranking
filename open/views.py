from pprint import pprint

from django.http import HttpResponse

from .models import TransactApi


# Create your views here.


def index(request):
    transaction_api = TransactApi()

    apt = transaction_api.아파트매매상세()
    apt.set_parameters({
        'LAWD_CD': '1130500000',
        'DEAL_YMD': '201804',
    })
    pprint(apt.get_content())
    return HttpResponse(transaction_api)
