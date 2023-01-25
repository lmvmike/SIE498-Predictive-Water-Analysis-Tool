from django.db import models


class Waterorder(models.Model):
    grower = models.CharField(max_length=255)
    acreage = models.FloatField()
    croptype = models.CharField(max_length=255)
    lifecycle = models.CharField(max_length=255)
    cfs = models.IntegerField()
    hours= models.IntegerField()
    soiltype = models.CharField(max_length=255)