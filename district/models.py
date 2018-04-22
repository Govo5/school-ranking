from django.db import models


# Create your models here.

class Code(models.Model):
    # 시도,시군구,행정구역명,행정동,법정동,     행정구역분류,행정기관코드,법정동코드,관할지역,행정동 영문명칭,      비고,,,,,,
    sido = models.CharField(max_length=50, default='', help_text="시도")
    sigungu = models.CharField(max_length=50, default='', help_text="시군구")
    administration = models.CharField(max_length=50, default='', help_text="행정구역명")
    administration_name = models.CharField(max_length=50, default='', help_text="행정동")
    legal_name = models.CharField(max_length=50, default='', help_text="법정동")

    administration_category = models.CharField(max_length=50, help_text="행정구역분류")
    administration_code = models.BigIntegerField(help_text="행정기관코드")
    legal_code = models.BigIntegerField(help_text="법정동코드")
    admin = models.CharField(max_length=50, default='', null=True, help_text="관할지역")
    english_administration_name = models.CharField(max_length=50, default='', help_text="행정동 영문명칭")

    memo = models.TextField(help_text="비고")

    column = {
        'sido': '시도',
        'sigungu': '시군구',
        'administration': '행정구역명',
        'administration_name': '행정동',
        'legal_name': '법정동',

        'administration_category': '행정구역분류',
        'administration_code': '행정기관코드',
        'legal_code': '법정동코드',
        'admin': '관할지역',
        'english_administration_name': '행정동 영문명칭',

        'memo': '비고',
        '': ''
    }

    @classmethod
    def create(cls, data):
        return cls(
            sido=data[cls.column['sido']],
            sigungu=data[cls.column['sigungu']],
            administration=data[cls.column['administration']],
            administration_name=data[cls.column['administration_name']],
            legal_name=data[cls.column['legal_name']],

            administration_category=data[cls.column['administration_category']],
            administration_code=data[cls.column['administration_code']],
            legal_code=data[cls.column['legal_code']],
            admin=data[cls.column['admin']],
            english_administration_name=data[cls.column['english_administration_name']],

            memo=data[cls.column['memo']]
        ).save()

    class Meta:
        unique_together = ('administration_code', 'administration_name', 'legal_code', 'legal_name',)

    def __str__(self):
        return self.legal_name
