from django.urls import path
from . import views

#config url
urlpatterns = [
    # string url, function name
    # chop off the app url and sends the 
    # remaining part
    path('', views.home),
    path('login_as/', views.login_as, name='login_as'),
    path('homepage/', views.home, name='homepage'),
    path('student_login/', views.student_login, name='student_login'),   
    path('parent_login/', views.parent_login, name='parent_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('student_register/',views.student_register, name="student_register"),
    path('teacher_register/',views.teacher_register, name="teacher_register"),
    path('parent_register/',views.parent_register, name="parent_register"),
    path('Teacher_Dashboard/',views.teacher_dashboard, name="Teacher_Dashboard"),
    path('Student_Dashboard',views.student_dashboard, name="Student_Dashboard"),
    path('Parent_Dashboard',views.parent_dashboard, name="Parent_Dashboard"),
    path('attendance_entry/',views.attendance_entry, name='attendance_entry'),
    path('parent_upload/',views.PARENT_upload, name='parent_upload'),
    path('student_upload/',views.StudentAndInfo_upload, name='student_upload'),
    # path('subject_upload/',views.SUBJECT_upload, name='subject_upload'),
    path('teacher_upload/',views.TEACHER_upload, name='teacher_upload'),
    # path('attendance_info_upload/',views.ATTENDANCEINFO_upload, name='attendanceinfo_upload'),
    path('attendance_upload/',views.ATTENDANCE_upload, name='attendance_upload'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('overall_attendance/',views.overall_attendance, name='overall_attendance'),
    path('add_attendance/',views.add_attendance,name='add_attendance'),
    path('daily_attendance',views.daily_attendance,name='daily_attendance'),
    path('attendance_status',views.attendance_status,name='attendance_status'),
    path('attendance_tracking',views.attendance_tracking,name='attendance_tracking'),
    path('attendance_summary',views.attendance_summary,name='attendance_summary'),
    path('fetch_students/', views.fetch_students, name='fetch_students'),
    path('help_support/', views.help_support, name='help_support'),
    path('about_us/', views.about_us, name='about_us'),
    path('direct_or_excel/', views.direct_or_excel, name='direct_or_excel'),
    path('generate_report/', views.generate_report, name='generate_report'),
]