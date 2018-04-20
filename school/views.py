from . import parser

from django.shortcuts import render
from django.http import HttpResponse

from school_ranking.settings import BASE_DIR


# Create your views here.

def index(request):
    data = parser.middle_school_parse(2017, '삼각산중학교')
    return HttpResponse(data)
