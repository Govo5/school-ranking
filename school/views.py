import json
import time

from django.http import HttpResponse

from school.parser import get_region_code, get_school_name
from school_ranking.settings import BASE_DIR
from . import parser


# Create your views here.

def index(request):
    json_data = open(BASE_DIR + '/school/school.json').read()
    items = json.loads(json_data)
    """
    1차분류 구별
    2차분류 동별(체크박스로 여러개 선택 가능하게)
    노원구
    1135010400: 하계동
    1135010500: 상계동
    1135010600: 중계동
    """

    성북구 = [
        '1129010100',  # 성북동
        '1129013300',  # 정릉동
        '1129010400',  # 동소문동 1가
        '1129013500',  # 종암동
        '1129013900',  # 석관동
        '1129010300',  # 돈암동
        '1129013700',  # 상월곡동
        '1129013600',  # 하월곡동
        '1129012200',  # 안암동
        '1129013800',  # 장위동
        '1129011200',  # 삼선동2가
        '1129011300',  # 삼선동3가
        '1129013400',  # 길음동
        '1129013200',  # 보문동3가
        '1129012900',  # 보문동7가
        '1129010400',  # 동소문동1가
        '1129010900',  # 동소문동6가'
    ]

    강북구 = [
        '1130510100',  # 미아동
        '1130510200',  # 번동
        '1130510300',  # 수유동
        '1130510400',  # 우이동
    ]

    노원구 = [
        '1135010200',  # 월계동
        '1135010300',  # 공릉동
        # '1135010400',  # 하계동
        # '1135010500',  # 상계동
        # '1135010600',  # 중계동
    ]

    html = ''
    for item in items['schoolList03']:
        if get_region_code(item) in 노원구:
            name = get_school_name(item)
            region_code = parser.middle_school_parse(2017, name).__str__()
            html += name + ": " + region_code + "<br>"
            time.sleep(1)

    return HttpResponse(html)
