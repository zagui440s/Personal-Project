from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import UserLocation
from newsapp.models import NewsUser
import requests  # Ensure requests is imported

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

def get_location_from_ip(ip):
    location_data = {
        "city": "Unknown",
        "region": "Unknown",
        "country": "Unknown",
        "latitude": 0.0,
        "longitude": 0.0,
    }

    try:
        # First try ip-api
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=country,region,city,lat,lon")
        if response.status_code == 200:
            data = response.json()
            location_data.update({
                "city": data.get("city", "Unknown"),
                "region": data.get("region", "Unknown"),
                "country": data.get("country", "Unknown"),
                "latitude": data.get("lat", 0.0),
                "longitude": data.get("lon", 0.0),
            })
        else:
            print(f"Error fetching location data from ip-api: {response.status_code}")

        # Try ipinfo.io to cross-check or as a fallback
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            city, region, country = data.get("city"), data.get("region"), data.get("country")
            latitude, longitude = map(float, data.get("loc", "0.0,0.0").split(","))
            location_data.update({
                "city": city or location_data["city"],
                "region": region or location_data["region"],
                "country": country or location_data["country"],
                "latitude": latitude or location_data["latitude"],
                "longitude": longitude or location_data["longitude"],
            })
        else:
            print(f"Error fetching location data from ipinfo.io: {response.status_code}")
    except requests.RequestException as e:
        print(f"Geolocation error: {e}")

    return location_data

class get_user_api_location(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_location = request.user.user_location
            location_data = {
                "city": user_location.city,
                "region": user_location.region,
                "country": user_location.country,
                "latitude": user_location.latitude,
                "longitude": user_location.longitude,
            }
            return JsonResponse(location_data, status=200)
        except UserLocation.DoesNotExist:
            return JsonResponse({"error": "Location not found"}, status=404)

    def post(self, request):
        try:
            ip = get_client_ip(request)
            location_data = get_location_from_ip(ip)
            user_location, created = UserLocation.objects.update_or_create(
                user=request.user,
                defaults=location_data
            )
            return JsonResponse({"message": "Location stored successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)