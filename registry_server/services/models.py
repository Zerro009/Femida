from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255,)
    host = models.CharField(max_length=255,)
    port = models.IntegerField()

class Route(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    path = models.CharField(max_length=255,)
