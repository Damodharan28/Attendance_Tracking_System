from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,
                                                password=password,
                                                email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                print("user created")
                return redirect('/')
        else:
            print("password not matching")
            messages.info(request,"Password not matching...")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
    