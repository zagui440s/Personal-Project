# NewsUser VIEWS*******
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from django.contrib.auth import login, authenticate, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import NewsUser
from userLocation_App.models import UserLocation
from .serializers import NewsUserSerializer
import requests

class Sign_up(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        request.data["username"] = request.data["email"]
        try:
            user = NewsUser.objects.create_user(**request.data)
            token = Token.objects.create(user=user)
            location_data = get_location_from_ip(request)
            user_location = UserLocation(user=user, **location_data)
            user_location.full_clean()
            user_location.save()

            serialized_user = NewsUserSerializer(user).data

            return Response({"user": serialized_user, "token": token.key}, status=HTTP_201_CREATED)
        except Exception as e:
            print(f"Error during signup: {e}")
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)


# Helper function to get location from IP
def get_location_from_ip(request):
    ip = get_client_ip(request)
    print("get_location func within views.py LINE 48", ip)
    if ip:
        try:
            response = requests.get("https://ipinfo.io/75.49.124.40/json")
            if response.status_code == 200:
                data = response.json()
                city, region, country = data.get("city"), data.get("region"), data.get("country")
                latitude, longitude = map(float, data.get("loc", "0.0,0.0").split(","))
                return {
                    "city": city or "Unknown",
                    "region": region or "Unknown",
                    "country": country or "Unknown",
                    "latitude": latitude,
                    "longitude": longitude,
                }
        except Exception as e:
            print(f"Geolocation error: {e}")
    return {
        "city": "Unknown",
        "region": "Unknown",
        "country": "Unknown",
        "latitude": 0.0,
        "longitude": 0.0,
    }


# Helper function to get client's IP address
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')
    

        
     
class Log_in(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            user_location = UserLocation.objects.get(user=user)
            serialized_user = NewsUserSerializer(user).data
            return Response({"token": token.key, "user": serialized_user}, status=HTTP_200_OK)
        else:
            return Response({"error": "No user matching credentials, newsapp/ views.py, line 41"}, status=HTTP_404_NOT_FOUND)

class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # return Response({"email": request.user})
    
        serialized_user = NewsUserSerializer(request.user).data 
        return Response(serialized_user, status=HTTP_200_OK)

class Log_out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class UpdateProfile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = NewsUserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        user = request.user
        data = request.data
        serializer = NewsUserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = request.user
        data = request.data
        serializer = NewsUserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

