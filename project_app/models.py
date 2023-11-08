from django.db import models
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(models.Model):
    First_Name=models.CharField( max_length=250)
    Last_Name=models.CharField( max_length=250)
    Email=models.EmailField( max_length=254, unique=True)
    Mobile=models.BigIntegerField()
    Password=models.CharField( max_length=250)
    Confirm_Password=models.CharField( max_length=250)

class ProjectTask(models.Model):
    Task_Name=models.CharField (max_length=250)
    TaskUserID=models.BigIntegerField()
    AssignUserID=models.BigIntegerField()
    TaskUserName=models.CharField( max_length=250)
    AssignUserName=models.CharField( max_length=250)
    