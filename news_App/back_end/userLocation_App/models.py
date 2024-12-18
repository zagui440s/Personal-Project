from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from newsapp.models import NewsUser

class UserLocation(models.Model):
    user = models.OneToOneField(NewsUser, on_delete=models.CASCADE, related_name="user_location")
    city = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self): 
        return f"{self.city}, {self.region}, {self.country}"
