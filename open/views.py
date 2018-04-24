from django.shortcuts import render
from django.http import HttpResponse
from .models import TransactedPrice


# Create your views here.


def index(request):
    transaction_price = TransactedPrice()
    return HttpResponse(transaction_price)
