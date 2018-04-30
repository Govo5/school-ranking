import json
import os
# Create your models here.
import urllib
from pprint import pprint
from urllib.parse import urlencode

import xmltodict

from school_ranking.settings import STATICFILES_DIRS


class TransactApi:
    name = '국토부실거래가'

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
        return TransactionPrice(self.data['services']['아파트매매'])

    def 연립다세대매매(self):
        return TransactionPrice(self.data['services']['연립다세대매매'])

    def 단독다가구매매(self):
        return TransactionPrice(self.data['services']['단독다가구매매'])

    def 오피스텔매매(self):
        return TransactionPrice(self.data['services']['오피스텔매매'])

    def 토지매매(self):
        return TransactionPrice(self.data['services']['토지매매'])

    def 아파트전월세(self):
        return TransactionPrice(self.data['services']['아파트전월세'])

    def 연립다세대전월세(self):
        return TransactionPrice(self.data['services']['연립다세대전월세'])

    def 아파트매매상세(self):
        """

        :rtype:
        """
        return TransactionPrice(self.data['services']['아파트매매상세'])


class TransactionPrice:
    def __init__(self, transaction_api):
        self.service_key = os.environ.get('OPEN_API_SERVICE_KEY')
        self.version = transaction_api['version']
        self.korean = transaction_api['korean']
        self.english = transaction_api['english']
        self.operation = transaction_api['operation']
        self.description = transaction_api['description']
        self.url = transaction_api['url']
        self.parameters = transaction_api['parameters']
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
        :return: list
        """
        parameters = []
        for key, parameter in self.parameters.items():
            if parameter['required'] is True:
                parameters.append(key)
        return parameters

    def get_parameters_all_list(self):
        """
        모든 파라미터를 list 로 리턴
        :return: list
        """
        parameters = []
        for key, parameter in self.parameters.items():
            parameters.append(key)
        return parameters

    def set_parameters(self, parameters):
        """
        필수 파라미터에 값을 할당함
        :return:
        """
        for key, parameter in self.parameters.items():
            try:
                self.parameters[key].setdefault('value', parameters[key])
                if parameter['required'] is True and parameters[key] is None:
                    raise Exception('필수 파라미터 설정 에러!!!!!')
            except Exception as e:
                pprint(e)

    def get_content(self):
        param = {}
        for key, value in self.parameters.items():
            param[key] = value['value']
        pprint(self.parameters)

        full_url = self.url + "?" + urlencode(param) + "&serviceKey={SERVICE_KEY}".format(
            SERVICE_KEY=self.service_key)  # add service_key
        print(full_url)
        request = urllib.request.Request(full_url)
        response = urllib.request.urlopen(request)
        res_code = response.getcode()
        if res_code == 200:
            response_body = response.read()
            content = xmltodict.parse(response_body.decode('utf-8'))
            return json.dumps(content)
        else:
            return "Error Code:" + res_code

    def is_able(self):
        """
        통긴가능한 상태인지 점검
        :return:
        """
        pass
