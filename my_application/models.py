from django.db import models

# Create your models here.
class MyFileUpload(models.Model):
    file_name=models.CharField(max_length=50)
    myfile=models.FileField()