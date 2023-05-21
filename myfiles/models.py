from django.db import models

# Create your models here.

class Subscribe(models.Model):
    ism = models.CharField(max_length=30)
    familya = models.CharField(max_length=30)
    username = models.CharField(max_length=30,null=True,blank=True)
    tg_id = models.CharField(max_length=30,null=True,blank=True)
    ism = models.IntegerField(max_length=30,unique=True)
