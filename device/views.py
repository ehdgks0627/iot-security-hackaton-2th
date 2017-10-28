from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def create(request):
    request_PK = request.GET.get("PK")
    if request_PK == None:
        return HttpResponse(str({"PK": ""}))
    else:
        if Device.objects.filter(PK=request_PK):
            return HttpResponse(str({"PK": request_PK}))
        new_device = Device.objects.create(PK=request_PK)
        if new_device:
            return HttpResponse(str({"PK": new_device.PK}))
        else:
            return HttpResponse(str({"PK": ""}))