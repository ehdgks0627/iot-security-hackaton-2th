from django.shortcuts import render
from django.http import HttpResponse
from keras.models import load_model
# Create your views here.

#model = load_model("model.h5")

def check(request):
    return HttpResponse("test~~")