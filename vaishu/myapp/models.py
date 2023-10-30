from django.db import models
from django.contrib import admin
class FootballPlayer (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    experience=models.IntegerField()
    gender=models.CharField(max_length=100)
    height=models.IntegerField()

class FootballPlayerAdmin(admin.ModelAdmin):
    list_display=('name','age','experience','gender','height')