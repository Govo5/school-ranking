import json

from django.db.models import Q
from django.shortcuts import render

from district.models import Code


# Create your views here.

def index(request):
    district_code = Code.objects.values('sigungu', 'legal_name', 'administration_category') \
        .filter(~Q(sigungu='서울특별시'), sido='서울특별시').distinct()
    data = {}
    for code in district_code:
        data.setdefault(code['sigungu'], []).append({
            '법정동': code['legal_name'],
            '시군구코드': code['administration_category']
        })

    return render(request, 'map/index.html', {'district_code': json.dumps(data)})
