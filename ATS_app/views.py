from django.shortcuts import render
from django.http import HttpResponse

def login_as(request):
    return render(request,'choicelogin.html')

def home(request):
    return render(request,'index.html')