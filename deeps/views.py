from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

#model = load_model("model.h5")

@csrf_exempt
def check(request):
    req = json.loads(request.body.decode("utf-8"))
    PK = req["PK"]
    time = req["time"]
    features = req["features"]
    #request.POST("",data={})
    isInfacted = True
    return HttpResponse(str({"check": isInfacted, "time": time}).replace("'", '"').reaplce("True", "true").replace("False", "false"))


{"check": True}