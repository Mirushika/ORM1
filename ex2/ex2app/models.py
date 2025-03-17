from django.db import models
from django.contrib import admin
class Employee (models.Model):
    eid=models.CharField(max_length=20,help_text="Employee ID")
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    qualification=models.CharField(max_length=100)



class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid','name','salary','age','email','qualification')
# Create your models here.
