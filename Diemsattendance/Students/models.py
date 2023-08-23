from django.db import models

# Create your models here.
class Student_Record(models.Model):
    sid = models.AutoField(primary_key=True)
    clg_prn=models.CharField(max_length=80)
    batu_prn=models.CharField(max_length=220)
    roll_no=models.CharField(max_length=220)
    full_name=models.CharField(max_length=240)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    address=models.TextField()
    year=models.CharField(max_length=200)
    student_branch=models.CharField(max_length=200)
    sem=models.CharField(max_length=200)
    div=models.CharField(max_length=200)
    batch=models.CharField(max_length=200)

class acdamic_year(models.Model):
    ac_id = models.AutoField(primary_key=True)
    year=models.CharField(max_length=80)
