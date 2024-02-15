from django.shortcuts import render
from django.http import HttpResponse

def ats(request):
    return HttpResponse("Attendance")

def home(request):
    return render(request,'sample.html' , {'name' : 'damo'})