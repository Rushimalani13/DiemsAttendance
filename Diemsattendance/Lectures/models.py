from django.db import models

# Create your models here.
class Lecture_Record(models.Model):
    lid = models.AutoField(primary_key=True)
    Lecture_id=models.CharField(max_length=220)
    default_ltime=models.DateTimeField(auto_now_add=True)
    year=models.CharField(max_length=220)
    branch=models.CharField(max_length=200)
    sem=models.CharField(max_length=240)
    subject=models.CharField(max_length=220)
    stu_class=models.CharField(max_length=20)
    division=models.CharField(max_length=50)
    faculty=models.CharField(max_length=200)
    date_time=models.DateTimeField()
    
    def __str__(self):
        return self.Lecture_id

class Subject_Record(models.Model):
    subid = models.AutoField(primary_key=True)
    sub_code=models.CharField(max_length=220)
    year=models.CharField(max_length=220)
    branch=models.CharField(max_length=200)
    sem=models.CharField(max_length=240)
    subject_name=models.CharField(max_length=220)
    
    def __str__(self):
        return self.sub_code

class Subject_Assign_CSE(models.Model):
    assign_id = models.AutoField(primary_key=True)
    faculty_name=models.CharField(max_length=220)
    subject_name=models.CharField(max_length=220)
    acadmic_year=models.CharField(max_length=220)
    sem=models.CharField(max_length=240)
    stu_class=models.CharField(max_length=20)
    division=models.CharField(max_length=50)
    sub_type=models.CharField(max_length=200)
    batch_assign=models.CharField(max_length=200)
    
    def __str__(self):
        return self.faculty_name+subject_name
    
class Subject_Assign_AIML(models.Model):
    assign_id = models.AutoField(primary_key=True)
    faculty_name=models.CharField(max_length=220)
    subject_name=models.CharField(max_length=220)
    acadmic_year=models.CharField(max_length=220)
    sem=models.CharField(max_length=240)
    stu_class=models.CharField(max_length=20)
    division=models.CharField(max_length=50)
    sub_type=models.CharField(max_length=200)
    batch_assign=models.CharField(max_length=200)
    
    def __str__(self):
        return self.faculty_name+subject_name