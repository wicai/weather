from django.db import models

# Create your models here.
class Region(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

class Weather(models.Model):
    region = models.ForeignKey(Region)
    temperature = models.IntegerField()
    
class Tweets(models.Model):
    region = models.ForeignKey(Region)
    tweet = models.CharField(max_length = 200)

class Stats(models.Model):
    region = models.ForeignKey(Region)
    ratio = models.FloatField()
    trating = models.FloatField()



