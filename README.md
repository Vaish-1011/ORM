# Ex02 Django ORM Web Application
## Date: 10/10/23

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

### model.py

```
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
```
### admin.py
```
from django.contrib import admin
from .models import FootballPlayer,FootballPlayerAdmin
admin.site.register(FootballPlayer,FootballPlayerAdmin)
```

## OUTPUT

![Alt text](<Screenshot 2023-10-30 204838.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
