from django.shortcuts import render
from django.http import HttpResponse
from .models import TransactedApi


# Create your views here.


def index(request):
    transaction_api = TransactedApi()
    return HttpResponse(transaction_api)
