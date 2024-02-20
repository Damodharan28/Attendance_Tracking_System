from django.db import models

# # 1
# class PARENT(models.Model):
#     PARENT_ID = models.IntegerField(primary_key=True)
#     FIRST_NAME = models.CharField(max_length=255)
#     LAST_NAME = models.CharField(max_length=255)
#     PHONE_NO = models.CharField(max_length=255)
#     EMAIL_ADDRESS = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.FIRST_NAME} {self.LAST_NAME}"
# # 2
# class STUDENT(models.Model):
#     STUDENT_ID = models.IntegerField(primary_key=True)
#     FIRST_NAME = models.CharField(max_length=255)
#     LAST_NAME = models.CharField(max_length=255)
#     PARENT_ID = models.ForeignKey('PARENT', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.FIRST_NAME} {self.LAST_NAME}"
# # 3
# class STUDENT_INFO(models.Model):
#     STUDENT_ID = models.OneToOneField(STUDENT, primary_key=True, on_delete=models.CASCADE)
#     DEPARTMENT = models.CharField(max_length=255)
#     SECTION = models.CharField(max_length=255)

#     def __str__(self):
#         return f"STUDENT_ID: {self.STUDENT_ID}, DEPARTMENT: {self.DEPARTMENT}, SECTION: {self.SECTION}"

# # 4 
# class TEACHER(models.Model):
#     TEACHER_ID = models.IntegerField(primary_key=True)
#     FIRST_NAME = models.CharField(max_length=255)
#     LAST_NAME = models.CharField(max_length=255)
#     PHONE_NO = models.CharField(max_length=255)
#     EMAIL_ADDRESS = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.FIRST_NAME} {self.LAST_NAME}"

# # 5
# class TEACHER_INFO(models.Model):
#     TEACHER_ID = models.OneToOneField(TEACHER, primary_key=True, on_delete=models.CASCADE)
#     DEPARTMENT = models.CharField(max_length=255)
#     SECTION = models.CharField(max_length=255)

#     def __str__(self):
#         return f"TEACHER: {self.TEACHER_ID}, DEPARTMENT: {self.DEPARTMENT}, SECTION: {self.SECTION}"

# # 6    
# class SUBJECT(models.Model):
#     SUBJECT_ID = models.IntegerField(primary_key=True)
#     SUBJECT_NAME = models.CharField(max_length=255)
#     TEACHER_ID = models.ForeignKey(TEACHER, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Subject ID: {self.SUBJECT_ID}, Teacher: {self.TEACHER_ID}"
    
# # 7
# class ATTENDANCE(models.Model):
#     ATTENDANCE_ID = models.IntegerField(primary_key=True)
#     STUDENT_ID = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
#     DATE = models.DateField()

#     def __str__(self):
#         return f"Attendance ID: {self.ATTENDANCE_ID}, Student ID: {self.STUDENT_ID}, Date: {self.DATE}"

# #8
# class ATTENDANCE_PER_HRS(models.Model):
#     ATTENDANCE_ID = models.OneToOneField(ATTENDANCE, primary_key=True, on_delete=models.CASCADE)
#     HOUR = models.IntegerField()
#     SUBJECT_ID = models.ForeignKey(SUBJECT, on_delete=models.CASCADE)
#     TEACHER_ID = models.ForeignKey(TEACHER, on_delete=models.CASCADE)
#     STATUS = models.CharField(max_length=255)

#     def __str__(self):
#         return f"Attendance ID: {self.ATTENDANCE_ID}, Hour: {self.HOUR}, Subject ID: {self.SUBJECT_ID}, Teacher ID: {self.TEACHER_ID}, Status: {self.STATUS}"

# #9
# class ATTENDANCE_INFO(models.Model):
#     ATTENDANCE_ID = models.OneToOneField(ATTENDANCE, primary_key=True, on_delete=models.CASCADE)
#     ABSENCE_REASON = models.CharField(max_length=255)
#     OD_REASON = models.CharField(max_length=255)
#     LATE_REASON = models.CharField(max_length=255)

#     def __str__(self):
#         return f"Attendance ID: {self.ATTENDANCE_ID}, Absence Reason: {self.ABSENCE_REASON}, OD Reason: {self.OD_REASON}, Late Reason: {self.LATE_REASON}"

class PARENT(models.Model):
    PARENT_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    PHONE_NO = models.CharField(max_length=255)
    EMAIL_ADDRESS = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.FIRST_NAME} {self.LAST_NAME}"

class STUDENT(models.Model):
    STUDENT_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    PARENT_ID = models.ForeignKey(PARENT, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.FIRST_NAME} {self.LAST_NAME}"

class STUDENT_INFO(models.Model):
    STUDENT_ID = models.OneToOneField(STUDENT, primary_key=True, on_delete=models.CASCADE)
    DEPARTMENT = models.CharField(max_length=255)
    SECTION = models.CharField(max_length=255)

    def __str__(self):
        return f"STUDENT_ID: {self.STUDENT_ID}, DEPARTMENT: {self.DEPARTMENT}, SECTION: {self.SECTION}"

class TEACHER(models.Model):
    TEACHER_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    PHONE_NO = models.CharField(max_length=255)
    EMAIL_ADDRESS = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.FIRST_NAME} {self.LAST_NAME}"

class TEACHER_INFO(models.Model):
    TEACHER_ID = models.OneToOneField(TEACHER,primary_key=True, on_delete=models.CASCADE)
    DEPARTMENT = models.CharField(max_length=255)
    SECTION = models.CharField(max_length=255)

    def __str__(self):
        return f"TEACHER: {self.TEACHER_ID}, DEPARTMENT: {self.DEPARTMENT}, SECTION: {self.SECTION}"

class SUBJECT(models.Model):
    SUBJECT_ID = models.IntegerField(primary_key=True)
    SUBJECT_NAME = models.CharField(max_length=255)
    TEACHER_ID = models.ForeignKey(TEACHER, on_delete=models.CASCADE)

    def __str__(self):
        return f"Subject ID: {self.SUBJECT_ID}, Teacher: {self.TEACHER_ID}"

class ATTENDANCE(models.Model):
    ATTENDANCE_ID = models.IntegerField(primary_key=True)
    STUDENT_ID = models.ForeignKey(STUDENT, on_delete=models.CASCADE)
    DATE = models.DateField()

    def __str__(self):
        return f"Attendance ID: {self.ATTENDANCE_ID}, Student ID: {self.STUDENT_ID}, Date: {self.DATE}"

class ATTENDANCE_PER_HRS(models.Model):
    ATTENDANCE_ID = models.OneToOneField(ATTENDANCE, primary_key=True, on_delete=models.CASCADE)
    HOUR = models.IntegerField()
    SUBJECT_ID = models.ForeignKey(SUBJECT, on_delete=models.CASCADE)
    TEACHER_ID = models.ForeignKey(TEACHER, on_delete=models.CASCADE)
    STATUS = models.CharField(max_length=255)

    def __str__(self):
        return f"Attendance ID: {self.ATTENDANCE_ID}, Hour: {self.HOUR}, Subject ID: {self.SUBJECT_ID}, Teacher ID: {self.TEACHER_ID}, Status: {self.STATUS}"

class ATTENDANCE_INFO(models.Model):
    ATTENDANCE_ID = models.OneToOneField(ATTENDANCE, on_delete=models.CASCADE,primary_key=True)
    ABSENCE_REASON = models.CharField(max_length=255)
    OD_REASON = models.CharField(max_length=255)
    LATE_REASON = models.CharField(max_length=255)

    def __str__(self):
        return f"Attendance ID: {self.ATTENDANCE_ID}, Absence Reason: {self.ABSENCE_REASON}, OD Reason: {self.OD_REASON}, Late Reason: {self.LATE_REASON}"
