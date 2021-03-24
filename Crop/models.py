from django.db import models

# Create your models here.
class Yield(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=67)
    password=models.CharField(max_length=67)
    username=models.CharField(max_length=89)

class  CropData(models.Model):
    area=models.IntegerField()
    ha_yield=models.IntegerField()
    avg_rainfall_mm=models.IntegerField()
    pesticides_tonnes=models.IntegerField()
    avg_tem=models.IntegerField()