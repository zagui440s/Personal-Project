from rest_framework import serializers
from .models import Child, Location

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'parent']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['child', 'latitude', 'longitude', 'timestamp']
