from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from ATS_app.models import STUDENT
from ATS_app.models import PARENT
from ATS_app.models import TEACHER
import random


def student_register(request):
    if request.method == 'POST':
        email_id = request.POST['email_id']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if STUDENT.objects.filter(EMAIL_ADDRESS=email_id).exists() and STUDENT.objects.filter(EMAIL_ADDRESS=email_id).count() == 0:
                student = STUDENT.objects.filter(EMAIL_ADDRESS=email_id).first()
                random_number = random.randint(100, 999)
                username= student.FIRST_NAME + str(random_number)
                user = User.objects.create_user(username=username,password=password,email_id=email_id,first_name=student.FIRST_NAME,last_name=student.LAST_NAME)
                user.save()
                return redirect('/')
            else:
                messages.info(request,'Email Not Correct')
                return redirect('/')
        else:
            messages.info(request,"Password not matching...")
            return redirect('register')
    else:
        return render(request,'register.html')
    
def teacher_register(request):
    if request.method == 'POST':
        email_id = request.POST['email_id']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if TEACHER.objects.filter(EMAIL_ADDRESS=email_id).exists() and TEACHER.objects.filter(EMAIL_ADDRESS=email_id).count() == 0:
                teacher = TEACHER.objects.filter(EMAIL_ADDRESS=email_id).first()
                random_number = random.randint(100, 999)
                username= teacher.FIRST_NAME + str(random_number)
                user = User.objects.create_superuser(username=username,password=password,email_id=email_id)
                user.save()
                return redirect('/')
            else:
                messages.info(request,'Email Not Correct')
                return redirect('/')
        else:
            messages.info(request,"Password not matching...")
            return redirect('register')
    else:
        return render(request,'register.html')
    
def parent_register(request):
    if request.method == 'POST':
        email_id = request.POST['email_id']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if PARENT.objects.filter(EMAIL_ADDRESS=email_id).exists() and PARENT.objects.filter(EMAIL_ADDRESS=email_id).count() == 0:
                parent = PARENT.objects.filter(EMAIL_ADDRESS=email_id).first()
                random_number = random.randint(100, 999)
                username= parent.FIRST_NAME + str(random_number)
                user = User.objects.create_user(username=username,password=password,email_id=email_id,first_name=parent.FIRST_NAME,last_name=parent.LAST_NAME)
                user.save()
                return redirect('/')
            else:
                messages.info(request,'Email Not Correct')
                return redirect('/')
        else:
            messages.info(request,"Password not matching...")
            return redirect('register')
    else:
        return render(request,'register.html')
