from django.db import models

# Create your models here.
class Branch_Record(models.Model):
    brid = models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=220)
    branch_code=models.CharField(max_length=200)
    branch_class=models.CharField(max_length=200)
    divisions=models.CharField(max_length=200)
    batches=models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
