from django.db import models
from django.utils import timezone


# Create your models here.

class EnrollHighSchool(models.Model):
    year = models.IntegerField(help_text="년도")
    school_name = models.CharField(max_length=50, default='', help_text="학교명")
    jibun = models.CharField(max_length=50, help_text="지번 주소")
    road = models.CharField(max_length=50, help_text="도로명 주소")
    school_code = models.CharField(max_length=50, help_text="학교코드")
    region_code = models.CharField(max_length=50, help_text="지역코드")

    graduate = models.FloatField(help_text="졸업자")
    foreigner = models.FloatField(help_text="진학자 특수목적고 외고국제고")
    science = models.FloatField(help_text="진학자 특수목적고 과학고")

    # sum
    private = models.FloatField(help_text="진학자 자율고 자율형사립고")
    public = models.FloatField(help_text="진학자 자율고 자율형공립고")

    # sum
    general = models.FloatField(help_text="진학자 일반고")
    etc = models.FloatField(help_text="진학자 기타")
    characterization = models.FloatField(help_text="진학자 특성화고")
    art = models.FloatField(help_text="진학자 특수목적고 예고체고")
    meister = models.FloatField(help_text="진학자 특수목적고 마이스터고")
    # sum
    job = models.FloatField(help_text="취업자")
    nothing = models.FloatField(help_text="무직 및 미상")

    data_type = models.CharField(max_length=5, help_text="수정일")
    created_at = models.DateTimeField(default=timezone.now, help_text="수정일")
    updated_at = models.DateTimeField(default=timezone.now, null=True, help_text="수정일")
    deleted_at = models.DateTimeField(null=True, help_text="수정일")

    column = [
        '졸업자',
        '진학자 일반고',
        '진학자 특성화고',
        '진학자 특수목적고 과학고',
        '진학자 특수목적고 외고국제고',

        '진학자 특수목적고 예고체고',
        '진학자 특수목적고 마이스터고',
        '',  # '진학자 특수목적고 소계',
        '진학자 자율고 자율형사립고',
        '진학자 자율고 자율형공립고',

        '',  # '진학자 자율고 소계',
        '진학자 기타',
        '',  # '진학자 진학자 계',
        '취업자',
        '무직 및 미상'
    ]

    @classmethod
    def create(cls, data):
        for col in cls.column:
            if col not in data:
                data.setdefault(col, 0.0)
        return cls(
            school_name=data['학교명'],
            jibun=data['지번'],
            road=data['도로명'],
            year=data['년도'],
            school_code=data['학교코드'],
            region_code=data['지역코드'],

            graduate=data[cls.column[0]],
            general=data[cls.column[1]],
            characterization=data[cls.column[2]],
            science=data[cls.column[3]],
            foreigner=data[cls.column[4]],

            art=data[cls.column[5]],
            meister=data[cls.column[6]],
            # sum
            private=data[cls.column[8]],
            public=data[cls.column[9]],

            # sum
            etc=data[cls.column[11]],
            # sum
            job=data[cls.column[13]],
            nothing=data[cls.column[14]],

            data_type=data['형태']
        )

    def __str__(self):
        return self.region_code
