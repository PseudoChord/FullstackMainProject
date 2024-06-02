from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=255)
    money = models.IntegerField(default=0)