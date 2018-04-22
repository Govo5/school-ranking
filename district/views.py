import csv

from django.db import transaction
from django.shortcuts import render

from school_ranking.settings import BASE_DIR
from .models import Code


# Create your views here.

def create(request):
    """
    코드 csv 파일 업로드 페이지
    :param request:
    :return:
    """
    return render(request, 'district/create.html')


def store(request):
    """
    법정동, 행정동 코드 삽입을 위한 view /docs/법정동_행정동_맵핑.csv 를 파싱해서 추가한다.
    링크주소: http://kssc.kostat.go.kr/ksscNew_web/kssc/common/CommonBoardList.do?gubun=1&strCategoryNameCode=019&strBbsId=kascrr&categoryMenu=014
    :param request:
    :return:
    """
    district = []
    """
    https://docs.djangoproject.com/ko/2.0/topics/http/file-uploads/
    위에 자료 보고 forms 을 구현해서 파일 저장시키고 지금은 그냥 업로드 하기
    print(request.FILES['code'])
    """
    with open(BASE_DIR + "/docs/법정동_행정동_맵핑.csv", encoding='utf-8') as region:
        reader = csv.DictReader(region)
        with transaction.atomic():
            for row in reader:
                district.append(Code().create(row))
    context = {'district_count': format(len(district), ","), }

    return render(request, 'district/done.html', context)
