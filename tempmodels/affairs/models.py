from django.db import models

# Create your models here.


class myuser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Intake(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=20)
    sdate =models.DateField()
    edate =models.DateField()
    
class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50) 
    
     
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    bdate = models.DateField()
    intake = models.IntegerField()
    track = models.CharField(max_length=20)
    promotion = models.DecimalField(max_digits=5, decimal_places=1)

    
