from import_export import resources
from .models import PARENT
from .models import STUDENT
from .models import STUDENT_INFO
# from .models import TEACHER_INFO
from .models import SUBJECT
from .models import TEACHER
from .models import ATTENDANCE
from .models import ATTENDANCE_PER_HRS
# from .models import ATTENDANCE_INFO

class PARENTResource(resources.ModelResource):
    class meta:
        model = PARENT
class STUDENTResource(resources.ModelResource):
    class meta:
        model = STUDENT
class STUDENT_INFOResource(resources.ModelResource):
    class meta:
        model = STUDENT_INFO
class SUBJECTResource(resources.ModelResource):
    class meta:
        model = SUBJECT
class TEACHERResource(resources.ModelResource):
    class meta:
        model = TEACHER
class ATTENDANCEResource(resources.ModelResource):
    class meta:
        model = ATTENDANCE
class ATTENDANCE_PER_HRSResource(resources.ModelResource):
    class meta:
        model = ATTENDANCE_PER_HRS