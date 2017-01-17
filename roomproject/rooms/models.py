from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField()
    size = models.CharField(max_length=255, blank=True, default='')
    rent = models.IntegerField()
    date_available = models.DateField(auto_now=False, auto_now_add=False)
    bathroom = models.CharField(max_length=255, blank=True, default='')
    laundry = models.CharField(max_length=255, blank=True, default='')
    pets = models.CharField(max_length=255, blank=True, default='')
    location = models.CharField(max_length=255, blank=True, default='')
