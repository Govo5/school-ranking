import os
import sys
import json
import requests

from pprint import pprint
from bs4 import BeautifulSoup

from school_ranking.settings import BASE_DIR
from .models import EnrollHighSchool


# http://www.schoolinfo.go.kr/  학교 알리미 홈
# http://www.schoolinfo.go.kr/ei/ss/Pneiss_b01_s0.do?HG_CD=B100005180  삼각산중학교

def school_parser():
    sido_code = 1100000000  # 시도는 서울시로 고정
    gugun_code = 1130500000  # 구군은 강북구(원하는 구로 변환가능)

    url = "http://www.schoolinfo.go.kr/ei/ss/Pneiss_a01_l0.do"  # 학교 알리미 검색홈
    data = {
        'GS_HANGMOK_CD': '',
        'GS_HANGMOK_NM': '',
        'GUGUN_CODE': gugun_code,
        'GU_GUN_CODE': gugun_code,
        'HG_CD': '',
        'HG_JONGRYU_GB': '',
        'SEARCH_KIND': '',
        'SIDO_CODE': sido_code,
        'SRC_HG_NM': ''
    }
    # HTTP GET Request
    request = requests.post(url, data=data)

    # HTML 소스 가져오기
    status_code = request.status_code
    json = request.text
    if status_code == 200:
        f = open('./school.json', 'w')
        f.write(json)
        f.close()
        print('파싱성공!!!')
        print('"school.json" 파일을 생성했습니다.')
    else:
        raise Exception('파싱에 실패하였습니다')

    sys.exit()
    """
    schoolList02: 초등학교
    schoolList03: 중학교
    schoolList04: 고등학교
    schoolList05: 특수학교/각종학교/기타
    """

    # BeautifulSoup 으로 html 소스를 python 객체로 변환
    # 첫 인자는 html 소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시
    # 이글에서는 Python 내장파서인 "html.parser" 를 이용함
    soup = BeautifulSoup(html, 'html.parse')

    # HTTP Header 가져오기
    header = request.header

    # HTTP Status 가져오기 (200: 정상)
    status = request.status_code

    # HTTP가 정상적으로 되었는지
    is_ok = request.ok

    return html


# 1. school.json 만들기
# school_parser()

# 2. 개별 학교 정보 html 파싱하기
# http://www.schoolinfo.go.kr/ei/ss/Pneiss_b01_s0.do?HG_CD=B100005180 삼각산중학교 학교 상세 페이지
def get_school_web_html(year, info):
    # HTTP GET Request
    url = 'http://www.schoolinfo.go.kr/ei/pp/Pneipp_b06_s0p.do'
    data = {
        'HG_NM': get_school_name(info),
        'HG_CD': get_school_code(info),
        'GS_BURYU_CD': 'JG040',
        'GS_HANGMOK_CD': '06',
        'JG_BURYU_CD': 'JG130',
        'JG_HANGMOK_CD': 52,
        'JG_GUBUN': 1,
        'GS_HANGMOK_NO': '13-다',
        'GS_HANGMOK_NM': '졸업생의 진로 현황',
        'JG_YEAR2': year,
        'GS_TYPE': 'Y',
        'JG_YEAR': year,
        'SORT': 'BR',
        'CHOSEN_JG_YEAR': year,
        'PRE_JG_YEAR': year
    }

    return requests.post(url, data=data)


def get_dict_from_parsed_html(info, year, statistics_number):
    table_data = [[cell.get('title') + ":" + cell.text for cell in row("td") if cell.text]
                  for row in statistics_number[0]("tr")]
    data = []
    data_type = ['', '', '', '', '남', '여', '총합', '통계']
    for index, item in enumerate(table_data):
        if index < 4:
            continue
        row = {
            '학교명': get_school_name(info),
            '지번': get_jibun(info),
            '도로명': get_road(info),
            '년도': year,
            '학교코드': get_school_code(info),
            '지역코드': get_region_code(info),
            '형태': data_type[index]
        }
        for col in item:
            string = col.split(":")
            row.setdefault(string[0], string[1])
        data.append(row)

    enroll_high_school = None
    for index in range(0, len(data)):
        pprint(data[index])
        enroll_high_school = EnrollHighSchool().create(data[index])
        enroll_high_school.save()

    return enroll_high_school


def middle_school_parse(year, name):
    info = get_middle_school_info(name)
    request = get_school_web_html(year, info)

    status_code = request.status_code
    html = request.text
    if status_code == 200:
        print('파싱성공!!!')
        soup = BeautifulSoup(html, 'html.parser')
        # CSS Selector 를 통해 html 요소들을 찾아낸다.
        statistics_number = soup.select('#excel > table.TableType1')
        # statistics_percent = soup.select('#excel > table.TableType1')
        return get_dict_from_parsed_html(info, year, statistics_number)

    else:
        raise Exception('파싱에 실패하였습니다')


# TODO model 로 빼내기!!
def get_middle_school_info(name):
    json_data = open(BASE_DIR + '/school/school.json').read()
    data = json.loads(json_data)
    for item in data['schoolList03']:
        if name == item['SCHUL_NM']:
            return item


def get_school_code(info):
    return info['SCHUL_CODE']


def get_school_name(info):
    return info['SCHUL_NM']


def get_region_code(info):
    return info['ADRCD_ID']


def get_jibun(info):
    return info['ADRES_BRKDN'] + " #" + info['DTLAD_BRKDN']


def get_road(info):
    return info['SCHUL_RDNMA']
