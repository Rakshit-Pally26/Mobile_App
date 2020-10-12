from django.db import models

class Data(models.Model):
    first_name= models.CharField(max_length=100, null=True)
    last_name= models.CharField(max_length=100, null=True)
    email= models.EmailField(null=True)
    location = models.CharField(max_length=100, null=True)
    flood_depth = models.IntegerField(null=True)
    latitude= models.CharField(max_length=12, null=True)
    longitude= models.CharField(max_length=13, null=True)
    time_stamp= models.TimeField(null=True)
    date= models.DateField(null=True)
    additional_info= models.TextField(null=True)

# Create your models here.
