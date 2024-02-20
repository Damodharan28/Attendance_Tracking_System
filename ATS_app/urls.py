from django.urls import path
from . import views

#config url
urlpatterns = [
    # string url, function name
    # chop off the app url and sends the 
    # remaining part
    path('attendance/', views.ats),
    path('', views.home)
]