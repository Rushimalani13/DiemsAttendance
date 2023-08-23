from django.db import models

# Create your models here.
class Attendance_Record(models.Model):
    att_id = models.AutoField(primary_key=True)
    student_Id=models.CharField(max_length=220)
    Lecture_Id=models.CharField(max_length=200)
    Acadmic_year=models.CharField(max_length=220)
    default_att_Date=models.DateField(auto_now=False, auto_now_add=False)
    att_date=models.CharField(max_length=200)
    att_time=models.CharField(max_length=200)
    is_present=models.CharField(max_length=200)
    is_type=models.CharField(max_length=200)

    def __str__(self):
        return self.is_type
