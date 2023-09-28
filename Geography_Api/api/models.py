from django.db import models

# Create your models here.
class student_info(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    # Данные ученика:
    profile = models.CharField(max_length=40) # Профиль
    profile_num = models.IntegerField()       # Номер класса 7-11
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=25)
    geoposition = models.CharField(max_length=20)
