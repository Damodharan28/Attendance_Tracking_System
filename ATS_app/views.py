from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import StudentRegistrationForm
from .forms import StudentLoginForm
from .forms import TeacherRegistrationForm
from .forms import TeacherLoginForm
from .forms import ParentRegistrationForm
from .forms import ParentLoginForm

from .models import PARENT
from .models import STUDENT
from .models import STUDENT_INFO
# from .models import TEACHER_INFO
from .models import SUBJECT
from .models import TEACHER
from .models import ATTENDANCE
from .models import ATTENDANCE_PER_HRS

from .resources import PARENTResource
from .resources import STUDENTResource
from .resources import STUDENT_INFOResource
from .resources import SUBJECTResource
from .resources import TEACHERResource
from .resources import ATTENDANCEResource
from .resources import ATTENDANCE_PER_HRSResource
from django.contrib import messages
from tablib import Dataset


#-----------------------------------------------------------------
def student_login(request):
        if request.method == 'POST':
            form = StudentLoginForm(request.POST)
            if form.is_valid():
                
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
                if '@' in username:
                    username1 = User.objects.get(email=username.lower()).username
                    user = authenticate(request, username=username1, password=password)

                else:
                    user = authenticate(request, username=username , password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "User Login Successful...")
                    return redirect('Student_Dashboard')
                else:
                    messages.info(request,"Invalid username or password !!!")
        else:
            # registerform = StudentRegistrationForm()
            form = StudentLoginForm()
        loginform = form
        return render(request,'student_login.html',{'loginform': loginform })
        
def student_register(request):
        if request.method == 'POST':
            form = StudentRegistrationForm(request.POST)
            if form.is_valid():
                email_id = form.cleaned_data['email_id']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                if password == confirm_password:    
                    student = STUDENT.objects.filter(EMAIL_ADDRESS=email_id).first()
                    if student is not None:
                        random_number = random.randint(100, 999)
                        username = student.FIRST_NAME + str(random_number)
                        user = User.objects.create_user(username=username, password=password, email=email_id, first_name=student.FIRST_NAME, last_name=student.LAST_NAME)
                        user.save()
                        messages.success(request, 'User created successfully.')
                        # return redirect('/student_login')  # Redirect to the login page
                    else:
                        messages.error(request, 'Student not found.')
                else:
                    messages.error(request, 'Passwords do not match.')
        else: 
            form = StudentRegistrationForm()
            # loginform = StudentLoginForm()
        registerform = form 
        return render(request,'student_register.html',{'registerform': registerform })

def parent_login(request):
        if request.method == 'POST':
            form = ParentLoginForm(request.POST)
            if form.is_valid():
                
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
                if '@' in username:
                    username1 = User.objects.get(email=username.lower()).username
                    user = authenticate(request, username=username1, password=password)

                else:
                    user = authenticate(request, username=username , password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "User Login Successful...")
                    return redirect('Parent_Dashboard')
                else:
                    messages.info(request,"Invalid username or password !!!")
        else:
            # registerform = StudentRegistrationForm()
            form = ParentLoginForm()
        loginform = form
        return render(request,'parent_login.html',{'loginform': loginform })
        
def parent_register(request):
    if request.method == 'POST':
            form = ParentRegistrationForm(request.POST)
            if form.is_valid():
                email_id = form.cleaned_data['email_id']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                if password == confirm_password:    
                    parent = PARENT.objects.filter(EMAIL_ADDRESS=email_id).first()
                    if parent is not None:
                        random_number = random.randint(100, 999)
                        username = parent.FIRST_NAME + str(random_number)
                        user = User.objects.create_user(username=username, password=password, email=email_id, first_name=parent.FIRST_NAME, last_name=parent.LAST_NAME)
                        user.save()
                        messages.success(request, 'User created successfully.')
                        # return redirect('/student_login')  # Redirect to the login page
                    else:
                        messages.error(request, 'parent not found.')
                else:
                    messages.error(request, 'Passwords do not match.')
    else: 
            form = ParentRegistrationForm()
            # loginform = StudentLoginForm()
    registerform = form 
    return render(request,'parent_register.html',{'registerform': registerform })

def teacher_login(request):
        if request.method == 'POST':
            form = TeacherLoginForm(request.POST)
            if form.is_valid():
                
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
                if '@' in username:
                    username1 = User.objects.get(email=username.lower()).username
                    user = authenticate(request, username=username1, password=password)

                else:
                    user = authenticate(request, username=username , password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "User Login Successful...")
                    return redirect('Teacher_Dashboard')
                else:
                    messages.info(request,"Invalid username or password !!!")
        else:
            # registerform = StudentRegistrationForm()
            form = TeacherLoginForm()
        loginform = form
        return render(request,'teacher_login.html',{'loginform': loginform })


def teacher_register(request):
        if request.method == 'POST':
            form = TeacherRegistrationForm(request.POST)
            if form.is_valid():
                email_id = form.cleaned_data['email_id']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']

                if password == confirm_password:    
                    teacher = TEACHER.objects.filter(EMAIL_ADDRESS=email_id).first()
                    if teacher is not None:
                        random_number = random.randint(100, 999)
                        username = teacher.FIRST_NAME + str(random_number)
                        user = User.objects.create_user(username=username, password=password, email=email_id, first_name=teacher.FIRST_NAME, last_name=teacher.LAST_NAME)
                        user.save()
                        messages.success(request, 'User created successfully.')
                        # return redirect('/student_login')  # Redirect to the login page
                    else:
                        messages.error(request, 'teacher not found.')
                else:
                    messages.error(request, 'Passwords do not match.')
        else: 
            form = TeacherRegistrationForm()
            # loginform = StudentLoginForm()
        registerform = form 
        return render(request,'teacher_register.html',{'registerform': registerform })

#--------------------------------------------------------------------------------

def PARENT_upload(request):
    if request.method == 'POST':
        PARENT_resource = PARENTResource()
        dataset = Dataset()
        new_PARENT = request.FILES['myfile']

        if not new_PARENT.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'attendance_entry.html')
        
        imported_data = dataset.load(new_PARENT.read(),format='xlsx')
        for data in imported_data:
            value = PARENT(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
            )
            value.save()
    return render(request,'attendance_entry.html')
    
# def STUDENT_upload(request):
#     if request.method == 'POST':
#         STUDENT_resource = STUDENTResource()
#         dataset = Dataset()
#         new_STUDENT = request.FILES['myfile']

#         if not new_STUDENT.name.endswith('xlsx'):
#             messages.info(request,'wrong format')
#             return render(request,'upload.html')
        
#         imported_data = dataset.load(new_STUDENT.read(),format='xlsx')
#         for data in imported_data:
#             value = STUDENT(
#                 data[0],
#                 data[1],
#                 data[2],
#                 data[3]
#             )
#             value.save()
#     return render(request,'upload.html')
    
# def STUDENT_INFO_upload(request):
#     if request.method == 'POST':
#         STUDENT_INFO_resource = STUDENT_INFOResource()
#         dataset = Dataset()
#         new_STUDENT_INFO = request.FILES['myfile']

#         if not new_STUDENT_INFO.name.endswith('xlsx'):
#             messages.info(request,'wrong format')
#             return render(request,'upload.html')
        
#         imported_data = dataset.load(new_STUDENT_INFO.read(),format='xlsx')
#         for data in imported_data:
#             value = STUDENT_INFO(
#                 data[0],
#                 data[1],
#                 data[2]
#             )
#             value.save()
#     return render(request,'upload.html')
    
# def SUBJECT_upload(request):
#     if request.method == 'POST':
#         SUBJECT_resource = SUBJECTResource()
#         dataset = Dataset()
#         new_SUBJECT = request.FILES['myfile']

#         if not new_SUBJECT.name.endswith('xlsx'):
#             messages.info(request,'wrong format')
#             return render(request,'upload.html')
        
#         imported_data = dataset.load(new_SUBJECT.read(),format='xlsx')
#         for data in imported_data:
#             value = SUBJECT(
#                 data[0],
#                 data[1],
#                 data[2]
#             )
#             value.save()
#     return render(request,'upload.html')
    
# def TEACHER_upload(request):
#     if request.method == 'POST':
#         TEACHER_resource = TEACHERResource()
#         dataset = Dataset()
#         new_TEACHER = request.FILES['myfile']

#         if not new_TEACHER.name.endswith('xlsx'):
#             messages.info(request,'wrong format')
#             return render(request,'upload.html')
        
#         imported_data = dataset.load(new_TEACHER.read(),format='xlsx')
#         for data in imported_data:
#             value = TEACHER(
#                 data[0],
#                 data[1],
#                 data[2]
#             )
#             value.save()
#     return render(request,'upload.html')
    
# def ATTENDANCE_upload(request):
#     if request.method == 'POST':
#         ATTENDANCE_resource = ATTENDANCEResource()
#         dataset = Dataset()
#         new_ATTENDANCE = request.FILES['myfile']

#         if not new_ATTENDANCE.name.endswith('xlsx'):
#             messages.info(request,'wrong format')
#             return render(request,'upload.html')
        
#         imported_data = dataset.load(new_ATTENDANCE.read(),format='xlsx')
#         for data in imported_data:
#             value = ATTENDANCE(
#                 data[0],
#                 data[1],
#                 data[2]
#             )
#             value.save()
#     return render(request,'upload.html')
    
# def ATTENDANCE_PER_HRS_upload(request):
#     if request.method == 'POST':
#         ATTENDANCE_PER_HRS_resource = ATTENDANCE_PER_HRSResource()
#         dataset = Dataset()
#         new_ATTENDANCE_PER_HRS = request.FILES['myfile']

#         if not new_ATTENDANCE_PER_HRS.name.endswith('xlsx'):
#             messages.info(request,'wrong format')
#             return render(request,'upload.html')
        
#         imported_data = dataset.load(new_ATTENDANCE_PER_HRS.read(),format='xlsx')
#         for data in imported_data:
#             value = ATTENDANCE_PER_HRS(
#                 data[0],
#                 data[1],
#                 data[2],
#                 data[3]
#             )
#             value.save()
#     return render(request,'upload.html')

#-----------------------------------------------------------------------------------------
def home(request):
    return render(request,'index.html')

def login_as(request):
    return render(request,'choicelogin.html')

def teacher_dashboard(request):
    return render(request,'teacher_page.html')

def parent_dashboard(request):
    return render(request,'parent_page.html')

def student_dashboard(request):
    return render(request,'student_page.html')

@login_required
def attendance_entry(request):
    return render(request, 'attendance_entry.html')

