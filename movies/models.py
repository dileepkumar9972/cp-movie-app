from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    picture =  models.URLField(max_length=1000,default='https://drive.google.com/file/d/1TSn-u4Aj_rrcvRTX4YJF0bhe9krUCcgg/view?usp=sharing')
    rating = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    notes = models.TextField(max_length=3000,default='')


def __str__(self):
    return self.name