from django.contrib.auth.models import User
from django.db import models

class Child(models.Model):
    unique_code = models.CharField(max_length=100, unique=True)  # A unique identifier code for each child
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="children")

    def __str__(self):
        return self.unique_code

class Location(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="locations")
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Location for {self.child.unique_code} at {self.timestamp}"

