from django.db import models
from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r'^\d{10}$',
    message='Phone number must be exactly 10 digits.',
)

class PARENT(models.Model):
    PARENT_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    PHONE_NO = models.CharField(max_length=10, validators=[phone_number_validator], unique=True)
    EMAIL_ADDRESS = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.PARENT_ID}"

class STUDENT(models.Model):
    STUDENT_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    PARENT_ID = models.ForeignKey(PARENT, on_delete=models.CASCADE)
    EMAIL_ADDRESS = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.STUDENT_ID}"

class STUDENT_INFO(models.Model):
    STUDENT_ID = models.OneToOneField(STUDENT, primary_key=True, on_delete=models.CASCADE)
    DEPARTMENT = models.CharField(max_length=255)
    SECTION = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.STUDENT_ID}"

class TEACHER(models.Model):
    TEACHER_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    PHONE_NO = models.CharField(max_length=10, validators=[phone_number_validator],unique=True)
    EMAIL_ADDRESS = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.TEACHER_ID}"

class SUBJECT(models.Model):
    SUBJECT_ID = models.IntegerField(primary_key=True)
    SUBJECT_NAME = models.CharField(max_length=255)
    DEPARTMENT = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.SUBJECT_ID}"

class ATTENDANCE_INFO(models.Model):
    ATTENDANCE_ID = models.IntegerField(primary_key=True)
    STUDENT_ID = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
    STUDENT_NAME = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ATTENDANCE_ID}"

class ATTENDANCE(models.Model):
    ATTENDANCE_ID = models.ForeignKey(ATTENDANCE_INFO, on_delete=models.CASCADE, primary_key=True)
    DATE = models.DateField()
    HOUR = models.IntegerField()
    SUBJECT_ID = models.ForeignKey(SUBJECT, on_delete=models.CASCADE)
    STATUS = models.CharField(max_length=255)

    class Meta:
        unique_together = ('ATTENDANCE_ID', 'DATE')

    def __str__(self):
        return f"{self.ATTENDANCE_ID} - {self.DATE}"

# class ATTENDANCE_INFO(models.Model):
#     ATTENDANCE_ID = models.OneToOneField(ATTENDANCE, on_delete=models.CASCADE, primary_key=True)
#     ABSENCE_REASON = models.CharField(max_length=255)
#     OD_REASON = models.CharField(max_length=255)
#     LATE_REASON = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.ATTENDANCE_ID}"
