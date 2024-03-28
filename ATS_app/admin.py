from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import PARENT
from .models import STUDENT
from .models import TEACHER
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
admin.site.register(TEACHER)
# admin.site.register(TEACHER_INFO)
admin.site.register(SUBJECT)
admin.site.register(ATTENDANCE)
admin.site.register(ATTENDANCE_PER_HRS)
# admin.site.register(ATTENDANCE_INFO)

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import STUDENT, STUDENT_INFO

class StudentResource(resources.ModelResource):
    student_id = fields.Field(attribute='student_id', column_name='Student ID')
    first_name = fields.Field(attribute='first_name', column_name='First Name')
    last_name = fields.Field(attribute='last_name', column_name='Last Name')
    department = fields.Field(column_name='Department')
    section = fields.Field(column_name='Section')

    class Meta:
        model = STUDENT
        skip_unchanged = True
        report_skipped = False
        fields = ('student_id', 'first_name', 'last_name', 'department', 'section')
        import_id_fields = ['student_id']

    def before_import_row(self, row, **kwargs):
        # Create a STUDENT instance if it doesn't exist
        student_id = row.get('Student ID')
        student, created = STUDENT.objects.get_or_create(student_id=student_id)
        row['student'] = student

class StudentInfoResource(resources.ModelResource):
    student = fields.Field(
        column_name='Student ID',
        attribute='student',
        widget=ForeignKeyWidget(STUDENT, 'student_id')
    )
    department = fields.Field(attribute='department', column_name='Department')
    section = fields.Field(attribute='section', column_name='Section')

    class Meta:
        model = STUDENT_INFO
        skip_unchanged = True
        report_skipped = False
        fields = ('student', 'department', 'section')
        import_id_fields = ['student']

class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource

class StudentInfoAdmin(ImportExportModelAdmin):
    resource_class = StudentInfoResource

admin.site.register(STUDENT, StudentAdmin)
admin.site.register(STUDENT_INFO, StudentInfoAdmin)

class PARENTAdmin(ImportExportModelAdmin):
    list_display=('PARENT_ID','FIRST_NAME','LAST_NAME','PHONE_NO','EMAIL_ADDRESS')
class STUDENTAdmin(ImportExportModelAdmin):
    list_display=('STUDENT_ID','FIRST_NAME','LAST_NAME','PARENT_ID','DEPARTMENT','SECTION')

    def DEPARTMENT(self, obj):
        return obj.student_info.department

    def SECTION(self, obj):
        return obj.student_info.section
    
admin.site.register(STUDENT , STUDENTAdmin)
    
class STUDENT_INFOAdmin(ImportExportModelAdmin):
    list_display=('STUDENT_ID','DEPARTMENT','SECTION')
class TEACHERAdmin(ImportExportModelAdmin):
    list_display=('TEACHER_ID','PHONE_NO','EMAIL_ADDRESS')
class SUBJECTAdmin(ImportExportModelAdmin):
    list_display=('SUBJECT_ID','SUBJECT_NAME','DEPARTMENT')
class ATTENDANCEAdmin(ImportExportModelAdmin):
    list_display=('ATTENDANCE_ID','STUDENT_ID','DATE')
class ATTENDANCE_PER_HRSAdmin(ImportExportModelAdmin):
    list_display=('ATTENDANCE_ID','HOUR','SUBJECT_ID','STATUS')