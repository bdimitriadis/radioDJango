from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields.jsonb import JSONField

# Create your models here.   
class Location(models.Model):
    location = models.CharField(max_length=80)
#     images = ArrayField(models.CharField(max_length=100))
#     locUrl = models.URLField()
    
    def __str__(self):
        return self.location

class Genre(models.Model):
    genre = models.CharField(max_length=80)
    
    def __str__(self):
        return self.genre
    
class Area(models.Model):
    area = models.CharField(max_length=80)
    areaUrl = models.URLField()
    loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.area

    
# class LocArea(models.Model):
#     mlocation = models.ForeignKey(Location, on_delete=models.CASCADE)
#     marea = models.ForeignKey(Area, on_delete=models.CASCADE) 

class Station(models.Model):
    stationUrl = models.URLField()
    name = models.CharField(max_length=80)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    images = JSONField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name