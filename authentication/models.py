from datetime import datetime
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Classroom(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name

class TblStudents(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    iCap = models.BooleanField(default=False)
    date_birth = models.DateField()
    password = models.CharField(max_length=128, default=make_password('abc@123'))
    classrooms = models.ManyToManyField(Classroom, related_name='students', blank = True)

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class AttendanceSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='attendance_sessions')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.classroom.class_name} - {self.date} ({self.start_time} - {self.end_time})"

class Attendance(models.Model):
    session = models.ForeignKey(AttendanceSession, on_delete=models.CASCADE, related_name='attendances',null=True)
    student = models.ForeignKey(TblStudents, on_delete=models.CASCADE, related_name='attendances')
    attended = models.BooleanField(default=False)
    datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.session.classroom.class_name} - {self.session.date}"

    def save(self, *args, **kwargs):
        if not self.datetime:
            self.datetime = datetime .now()
        if not (self.session.start_time <= self.datetime.time() <= self.session.end_time):
            self.attended = False
        super().save(*args, **kwargs)
