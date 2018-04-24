import os
import json
from pprint import pprint

from django.db import models

# Create your models here.
from school_ranking.settings import STATICFILES_DIRS


class TransactedApi:
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
        return TransactionPrice(self.data['아파트매매'])

    def 연립다세대매매(self):
        return TransactionPrice(self.data['연립다세대매매'])

    def 단독다가구매매(self):
        return TransactionPrice(self.data['단독다가구매매'])

    def 오피스텔매매(self):
        return TransactionPrice(self.data['오피스텔매매'])

    def 토지매매(self):
        return TransactionPrice(self.data['토지매매'])

    def 아파트전월세(self):
        return TransactionPrice(self.data['아파트전월세'])

    def 연립다세대전월세(self):
        return TransactionPrice(self.data['연립다세대전월세'])

    def 아파트매매상세(self):
        return TransactionPrice(self.data['아파트매매상세'])


class TransactionPrice:
    def __init__(self, transaction_api):
        self.version = transaction_api['version'],
        self.korean = transaction_api['korean'],
        self.english = transaction_api['english'],
        self.operation = transaction_api['operation'],
        self.description = transaction_api['description'],
        self.url = transaction_api['url'],
        self.parameters = transaction_api['parameters'],
        """
        "parameters": {
            "LAWD_CD": {
                "required": true,
                "type": "integer",
                "description": "지역코드",
                "example": "11110"
            },
            "DEAL_YMD": {
                "required": true,
                "type": "integer",
                "description": "지역코드",
                "example": "11110"
            }
        }
        """
    def get_parameters_list(self):
        """
        필수 파라미터 list 를 리턴
        :return:
        """
        pass

    def set_parameters(self):
        """
        get_parameters_list 에서 받은 필수 파라미터에 값을 할당함
        :return:
        """
        pass

    def is_able(self):
        """
        통긴가능한 상태인지 점검
        :return:
        """
        pass
