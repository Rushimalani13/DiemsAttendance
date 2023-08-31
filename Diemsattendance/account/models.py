from django.db import models

# Create your models here.
class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=220)
    email=models.CharField(max_length=220)
    password=models.CharField(max_length=220)
    branch=models.CharField(max_length=220)
    acadmic_year=models.CharField(max_length=20)
    authority=models.CharField(max_length=220)

    def __str__(self):
        return self.username

 