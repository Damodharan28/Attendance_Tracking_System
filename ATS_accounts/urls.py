from django.urls import path
from . import views

#config url
urlpatterns = [
    # string url, function name
    # chop off the app url and sends the 
    # remaining part
    path('student_login', views.student_login, name="student_login"),
    path('teacher_login', views.teacher_login, name="teacher_login"),
    path('parent_login', views.parent_login, name="parent_login"),
    path('student_register',views.student_register, name="student_register"),
    path('teacher_register',views.teacher_register, name="teacher_register"),
    path('parent_register',views.parent_register, name="parent_register"),
]