import os
import json
from pprint import pprint

from django.db import models

# Create your models here.
from school_ranking.settings import STATICFILES_DIRS


class TransactedPrice:
    name = '국토부실거래가'
    service_key = os.environ.get('OPEN_API_SERVICE_KEY')

    def __init__(self):
        json_data = open(STATICFILES_DIRS[0] + '/trade_price.json').read()
        self.data = json.loads(json_data)[self.name]
        self.korean = self.data['korean']
        self.english = self.data['english']
        self.description = self.data['description']
        self.format = self.data['format']

    def __str__(self):
        return self.korean

    def 아파트매매(self):
        return self.data['아파트매매']

    def 연립다세대매매(self):
        return self.data['연립다세대매매']

    def 단독다가구매매(self):
        return self.data['단독다가구매매']

    def 오피스텔매매(self):
        return self.data['오피스텔매매']

    def 토지매매(self):
        return self.data['토지매매']

    def 아파트전월세(self):
        return self.data['아파트전월세']

    def 연립다세대전월세(self):
        return self.data['연립다세대전월세']

    def 아파트매매상세(self):
        return self.data['아파트매매상세']
