from django.urls import path
from . import views

#config url
urlpatterns = [
    # string url, function name
    # chop off the app url and sends the 
    # remaining part
    path('', views.home),
    path('login_as/', views.login_as, name='login_as'),
    path('student_login/', views.student_login, name='student_login'),
    path('parent_login/', views.parent_login, name='parent_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('student_login/#/',views.same, name="same")
]