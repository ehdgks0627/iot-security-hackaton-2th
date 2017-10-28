from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from keras.models import load_model
import json

#model = load_model("model.h5")

@csrf_exempt
def check(request):
    x_data = json.loads(request.REQUEST.get("features"))
    #model.predict(x_data)
    #train here a
    return HttpResponse("test~~")
