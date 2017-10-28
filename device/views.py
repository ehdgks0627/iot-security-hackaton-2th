from django.shortcuts import render
from .models import *
# Create your views here.

def create(request):
    request_PK = request.REQUEST.get("PK")
    a = Device.objects.create(PK=request_PK)
    print(a)