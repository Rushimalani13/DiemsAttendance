from django.db import models

# Create your models here.
class Teacher_Record(models.Model):
    tid = models.AutoField(primary_key=True)
    teacher_id=models.CharField(max_length=220)
    full_name=models.CharField(max_length=240)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    
    def __str__(self):
        return self.teacher_id
    
class Faculty_Record_CSE(models.Model):
    tid = models.AutoField(primary_key=True)
    teacher_id=models.CharField(max_length=220)
    username=models.CharField(max_length=240)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    Authority=models.CharField(max_length=20)
     
    def __str__(self):
        return self.username
    
class Faculty_Record_AIML(models.Model):
    tid = models.AutoField(primary_key=True)
    teacher_id=models.CharField(max_length=220)
    username=models.CharField(max_length=240)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    Authority=models.CharField(max_length=20)
     
    def __str__(self):
        return self.username