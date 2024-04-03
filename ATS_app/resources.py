from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import PARENT
from .models import STUDENT
from .models import STUDENT_INFO
# from .models import TEACHER_INFO
# from .models import SUBJECT
from .models import TEACHER
# from .models import ATTENDANCE_INFO
from .models import ATTENDANCE_DATA
# from .models import ATTENDANCE_INFO

class StudentAndInfoResource(resources.ModelResource):
    student_id = fields.Field(attribute='STUDENT_ID', column_name='STUDENT_ID')
    first_name = fields.Field(attribute='FIRST_NAME', column_name='FIRST_NAME')
    last_name = fields.Field(attribute='LAST_NAME', column_name='LAST_NAME')
    parent_id = fields.Field(attribute='PARENT_ID', column_name='PARENT_ID', widget=ForeignKeyWidget(PARENT, 'PARENT_ID'))
    email = fields.Field(attribute='EMAIL_ADDRESS' , column_name='EMAIL_ADDRESS')
    department = fields.Field(attribute='DEPARTMENT', column_name='DEPARTMENT')
    section = fields.Field(attribute='SECTION', column_name='SECTION')

    def before_import_row(self, row, **kwargs):
        student_id = row.get('STUDENT_ID')
        student, created = STUDENT.objects.get_or_create(STUDENT_ID=student_id)
        student.FIRST_NAME = row.get('FIRST_NAME')
        student.LAST_NAME = row.get('LAST_NAME')
        # student.PARENT_ID = PARENT.objects.get(PARENT_ID=row.get('PARENT_ID'))
        # student.PARENT_ID = PARENT(PARENT_ID=row.get('PARENT_ID'))
        parent_id = row.get('PARENT_ID')
        
        # try:
        #     parent = PARENT.objects.get(PARENT_ID=parent_id)
        #     print("created")
        # except PARENT.DoesNotExist:
        #     parent = None
        parent = PARENT.objects.get(PARENT_ID=parent_id)
        student.PARENT_ID = parent
        student.save()

        # try:
        # student = STUDENT.objects.get(STUDENT_ID=student_id)
        # except STUDENT.DoesNotExist:
        #     student_info = STUDENT_INFO(STUDENT_ID=student_id)
        student_info, created = STUDENT_INFO.objects.get_or_create(STUDENT_ID=student)
        student_info.STUDENT_ID = student
        student_info.DEPARTMENT = row.get('DEPARTMENT')
        student_info.SECTION = row.get('SECTION')
        student_info.save()

    class Meta:
        model = STUDENT
        skip_unchanged = True
        report_skipped = False
        fields = ('student_id', 'first_name', 'last_name', 'parent_id', 'department', 'section')
        import_id_fields = ['student_id']

class PARENTResource(resources.ModelResource):
    class meta:
        model = PARENT
# class STUDENT_INFOResource(resources.ModelResource):
#     class meta:
#         model = STUDENT_INFO
# class SUBJECTResource(resources.ModelResource):
#     class meta:
#         model = SUBJECT
class TEACHERResource(resources.ModelResource):
    class meta:
        model = TEACHER
# class ATTENDANCEINFOResource(resources.ModelResource):
#     class meta:
#         model = ATTENDANCE_INFO
class ATTENDANCEResource(resources.ModelResource):
    class meta:
        model = ATTENDANCE_DATA

# class AttendanceAndHrsResource(resources.ModelResource):
#     attendance_id = fields.Field(attribute='ATTENDANCE_ID', column_name='ATTENDANCE_ID')
#     student_id = fields.Field(attribute='STUDENT_ID', column_name='STUDENT_ID', widget=ForeignKeyWidget(STUDENT, 'STUDENT_ID'))
#     date_of_attendance = fields.Field(attribute='DATE', column_name='DATE')
#     hour = fields.Field(attribute='HOUR', column_name='HOUR')
#     subject_id = fields.Field(attribute='SUBJECT_ID' , column_name='SUBJECT_ID')
#     status = fields.Field(attribute='STATUS', column_name='STATUS')

#     def before_import_row(self, row, **kwargs):
#         attendance_id = row.get('ATTENDANCE_ID')
#         attendance, created = ATTENDANCE.objects.get_or_create(ATTENDANCE_ID=attendance_id)
#         attendance.STUDENT_ID = STUDENT.objects.get(STUDENT_ID=row.get('STUDENT_ID'))
#         attendance.DATE = row.get('DATE')
#         attendance.HOUR = row.get('HOUR')
#         attendance.SUBJECT
        
#         # try:
#         #     parent = PARENT.objects.get(PARENT_ID=parent_id)
#         #     print("created")
#         # except PARENT.DoesNotExist:
#         #     parent = None
#         parent = PARENT.objects.get(PARENT_ID=parent_id)
#         attendance.PARENT_ID = parent
#         attendance.save()

#         # try:
#         # student = STUDENT.objects.get(STUDENT_ID=student_id)
#         # except STUDENT.DoesNotExist:
#         #     student_info = STUDENT_INFO(STUDENT_ID=student_id)
#         student_info, created = STUDENT_INFO.objects.get_or_create(STUDENT_ID=student)
#         student_info.STUDENT_ID = student
#         student_info.DEPARTMENT = row.get('DEPARTMENT')
#         student_info.SECTION = row.get('SECTION')
#         student_info.save()

#     class Meta:
#         model = STUDENT
#         skip_unchanged = True
#         report_skipped = False
#         fields = ('student_id', 'first_name', 'last_name', 'parent_id', 'department', 'section')
#         import_id_fields = ['student_id']
