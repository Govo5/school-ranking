import csv

from django.test import TestCase

from school_ranking.settings import BASE_DIR
# Create your tests here.
from .models import Code


class DistrictModelTest(TestCase):
    def test_store_code_on_csv(self):
        """
        csv 파일을 파싱하여 데이터에 저장이 가능한지 테스트
        :return:
        """
        district = []
        with open(BASE_DIR + "/docs/법정동_행정동_맵핑.csv", encoding='utf-8') as region:
            reader = csv.DictReader(region)
            for row in reader:
                district.append(Code().create(row))
            self.assertTrue(len(district) > 0)
