from django.contrib import admin
from .models import PARENT
from .models import STUDENT
# from .models import TEACHER
from .models import STUDENT_INFO
# from .models import TEACHER_INFO
from .models import SUBJECT
from .models import ATTENDANCE
from .models import ATTENDANCE_PER_HRS
# from .models import ATTENDANCE_INFO

# Register your models here.
admin.site.register(PARENT)
admin.site.register(STUDENT)
admin.site.register(STUDENT_INFO)
# admin.site.register(TEACHER)
# admin.site.register(TEACHER_INFO)
admin.site.register(SUBJECT)
admin.site.register(ATTENDANCE)
admin.site.register(ATTENDANCE_PER_HRS)
# admin.site.register(ATTENDANCE_INFO)