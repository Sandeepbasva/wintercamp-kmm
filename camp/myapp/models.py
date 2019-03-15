from django.db import models
import datetime
# Create your models here.

gender_list = [('M', 'Male'), ('F', 'Female')]


class Person(models.Model):
    name = models.CharField(max_length=120)
    gender = models.CharField(max_length=10, null=True, choices=gender_list)
    birthday = models.DateField(default=datetime.datetime.now())
    email = models.EmailField(max_length=120, unique=True)
    url = models.URLField(max_length=120)
    bio = models.TextField(max_length=420, blank=True)
    photo = models.FileField(blank=True)

    def __str__(self):
        return "%s" % self.name
