from django.db import models

#create your models here

class position(models.Model):
     title = models.CharField(max_length=50)
      
class crom(models.Model):
      fullname = models.CharField(max_length=100)
      crom_code = models.CharField(max_length=3)
      mobile = models.CharField(max_length=15)
      position = models.ForeignKey(position,on_delete=models.CASCADE)
