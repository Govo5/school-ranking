from django.db import models


# Create your models here.

class EnrollHighSchool(models.Model):
    column = [
        '졸업자',
        '진학자 일반고',
        '진학자 특성화고',
        '진학자 특수목적고 과학고',
        '진학자 특수목적고 외고국제고',

        '진학자 특수목적고 예고체고',
        '진학자 특수목적고 마이스터고',
        # '진학자 특수목적고 소계',
        '진학자 자율고 자율형사립고',
        '진학자 자율고 자율형공립고',

        # '진학자 자율고 소계',
        '진학자 기타',
        '진학자 진학자 계',
        '취업자',
        '무직 및 미상'
    ]

    sido = None
    gugun = None
    year = None
    school_code = None
    region_code = None

    graduate = None
    general = None
    characterization = None
    science = None
    foreigner = None

    art = None
    meister = None
    # sum
    private = None
    public = None

    # sum
    etc = None
    # sum
    job = None
    nothing = None

    @classmethod
    def create(cls, data):
        enroll = cls(
            sido=data['sido'],
            gugun=data['gugun'],
            year=data['year'],
            school_code=data['school_code'],
            region_code=data['region_code'],

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
        )
        # do something with the book
        return enroll
