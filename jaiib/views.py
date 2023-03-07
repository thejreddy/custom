from django.shortcuts import render
from django.shortcuts import redirect
from user.models import User,Profile,brainjaiib
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import View
from random import randint
from django.http import JsonResponse
from .models import Question

# Create your views here.
def checkbrain(request):

    return render(request,"userinterface/testing.html")


def subscribejaiib(request):
    brainjaiib_obj = brainjaiib(
    username = request.user.username,
    role = request.user.Profile.role,)
    print("done bro")

class AjaxHandler(View):
    def get(self,request):
        scores= brainjaiib.objects.values().filter(user=request.user)
        scoresa=list(scores)
        a1011 = fetchquestion(request,1011)
        a1021 = fetchquestion(request,1021)
        a1031 = fetchquestion(request,1031)
        a1041 = fetchquestion(request,1041)
        a1051 = fetchquestion(request,1051)
        a1061 = fetchquestion(request,1061)
        a1071 = fetchquestion(request,1071)
        a1081 = fetchquestion(request,1081)
        a1091 = fetchquestion(request,1091)
        a1101 = fetchquestion(request,1101)
        a1111 = fetchquestion(request,1111)
        a1121 = fetchquestion(request,1121)
        a1131 = fetchquestion(request,1131)
        a1141= fetchquestion(request,1141)
        a1151 = fetchquestion(request,1151)


        return JsonResponse({'scoresa':scoresa, 'a1011':a1011, 'a1021':a1021, 'a1031':a1031, 'a1041':a1041, 'a1051':a1051, 'a1061':a1061, 'a1071':a1071, 'a1081':a1081, 'a1091':a1091, 'a1101':a1101, 'a1111':a1111, 'a1121':a1121, 'a1131':a1131, 'a1141':a1141, 'a1151':a1151})


def fetchquestion(request,subcode):
        question = Question.objects.filter(subcode=subcode).count()
        a = randint(10001,10000+question)
        question_fetch=Question.objects.values().filter(subcode=subcode,questcode=a)
        question_fetcha=list(question_fetch)
        return question_fetcha
