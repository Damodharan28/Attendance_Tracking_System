from django.shortcuts import render
from django.http import HttpResponse

def login_as(request):
    return render(request,'choicelogin.html')

def home(request):
    return render(request,'index.html')

def student_login(request):
    return render(request,'student_login.html')

def parent_login(request):
    return render(request,'parent_login.html')

def teacher_login(request):
    return render(request,'teacher_login.html')

def same(request):
    return render(request,'login.html#')