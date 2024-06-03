from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    money = models.IntegerField(default=0)