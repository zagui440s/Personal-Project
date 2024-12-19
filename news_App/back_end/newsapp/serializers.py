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
        extra_kwargs = {
            'bio': {'required': False},
            'user_location': {'required': False}
        }
    
    def update(self, instance, validated_data):
        user_location_data = validated_data.pop('user_location', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if user_location_data:
            user_location_instance = instance.user_location
            for attr, value in user_location_data.items():
                setattr(user_location_instance, attr, value)
            user_location_instance.save()
        
        instance.save()
        return instance