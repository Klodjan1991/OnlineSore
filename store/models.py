from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Store(models.Model):

    name = models.CharField(max_length=30)
    generic = models.TextField()
    elements = models.TextField()
    facebook = models.CharField(default="-",max_length=30)
    twitter = models.CharField(default="-", max_length=30)
    dribbble = models.CharField(default="-", max_length=30)
    behance = models.CharField(default="-", max_length=30)
    tell = models.CharField(default="-", max_length=30)
    link = models.CharField(default="-", max_length=30)

    set_name = models.CharField(default="-", max_length=30)

    def __str__(self):
       return self.name + " | " + str(self.pk)