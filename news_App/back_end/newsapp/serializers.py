from rest_framework import serializers
from .models import NewsUser
from userLocation_App.models import UserLocation




class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ['city', 'region', 'country', 'latitude', 'longitude']

class NewsUserSerializer(serializers.ModelSerializer):
    user_location = UserLocationSerializer()  # Include the user_location serializer
    class Meta:
        model = NewsUser
        fields = ['id', 'email', 'username', 'last_login', 'is_staff', 'date_joined', 'user_location']
    