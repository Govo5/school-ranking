import csv

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from school_ranking.settings import BASE_DIR
from .models import Code


# Create your views here.


def index(request):
    district = None
    with open(BASE_DIR + "/docs/법정동_행정동_맵핑.csv") as region:
        reader = csv.DictReader(region)
        with transaction.atomic():
            for row in reader:
                district = row
                code = Code()
                code.create(row)

    # district = get_object_or_404(District())
    context = {'district': district, }
    return render(request, 'district/index.html', context)
