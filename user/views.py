# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import updatescore
from .models import brainjaiib
from django.views.decorators.csrf import csrf_exempt
import json
from .serializers import jaiibserializer
import io
from rest_framework.parsers import JSONParser
from functools import reduce

def correctanswer(request):
    if request.method=="POST":
        subcode =request.POST.get('subcode')
        scoreobtained = request.POST.get('score')
        print(subcode)
        brainjaiib.objects.filter(user=request.user).update(**{subcode:"10"})
        return HttpResponse("/")

    else:
        print("I didnt pass")

@csrf_exempt
def jaffa(request):
    if (request.method=="POST"):
        stream=JSONParser().parse(request)
        print(stream)
        subcode=stream.get('subcode')
        score=stream.get('score')
        k=brainjaiib.objects.filter(user=request.user)[0]

        n = reduce( getattr, [ k ] + subcode.split("__" ) )
        print(n)
        print(subcode)
        lastDigit = int(repr(subcode)[-2])
        print(lastDigit)
        if(lastDigit==1):
            x = (float(n)*91.5+float(score)*9.5)/float(100);
            print(x)
        if(lastDigit==2):
            x = (float(n)*87.5+float(score)*12.5)/float(100);
        if(lastDigit==3):
            x = (float(n)*80+float(score)*20)/float(100);
        if subcode is not None:
            brainjaiib.objects.filter(user=request.user).update(**{subcode:x})
        return HttpResponse("/")
    return HttpResponse("/")
