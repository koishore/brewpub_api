from django.db import models


class Brewery(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=100)
    state = models.CharField(max_length=25)
    def __str__(self):
        return self.name
