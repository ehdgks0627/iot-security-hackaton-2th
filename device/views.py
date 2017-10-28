from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
# Create your views here.

@csrf_exempt
def create(request):
    print(request.body.decode("utf-8"))
    request = json.loads(request.body.decode("utf-8"))
    request_PK = request["PK"]
    print(request_PK)
    if request_PK == None:
        return HttpResponse(str({"PK": ""}).replace("'",'"'))
    else:
        if Device.objects.filter(PK=int(request_PK)):
            print("-", request_PK)
            return HttpResponse(str({"PK": request_PK}).replace("'",'"'))
        new_device = Device.objects.create(PK=request_PK)
        if new_device:
            print("a", request_PK)
            return HttpResponse(str({"PK": new_device.PK}).replace("'",'"'))
        else:
            print("b", request_PK)
            return HttpResponse(str({"PK": ""}).replace("'",'"'))
