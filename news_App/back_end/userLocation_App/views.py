from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import UserLocation
from newsapp.models import NewsUser

class get_user_api_location(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        location_data = request.body.copy()

    def get(self, request):
        # //body, data, make locations above 
        print("hellLLLOLOL**************")

        try:
            print(request.user)
            user_location = request.user.userlocation
            print(user_location)
            print("user DATATATATATAT")
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
        
        

    # POST: Save the user's location (e.g., after registration)
    def post(self, request):
        try:
            response = requests.get("http://ip-api.com/json/?fields=61439")
            if response.status_code == 200:
                data = response.json()
                # Save user location to the database
                user_location, created = UserLocation.objects.update_or_create(
                    user=request.user,
                    defaults={
                        'city': data.get('city', ''),
                        'region': data.get('regionName', ''),
                        'country': data.get('country', ''),
                        'latitude': data.get('lat', ''),
                        'longitude': data.get('lon', '')
                    }
                )
                return JsonResponse({"message": "Location stored successfully"}, status=201)
            else:
                return JsonResponse({"error": "Unable to fetch location data"}, status=500)
        except requests.RequestException as e:
            return JsonResponse({"error": str(e)}, status=500)

    # # PUT: Update the user's location (e.g., after changing location)
    # def put(self, request):
    #     try:
    #         user_location = UserLocation.objects.get(user=request.user)
    #         # Get updated location from request
    #         city = request.data.get('city', '')
    #         region = request.data.get('region', '')
    #         country = request.data.get('country', '')
    #         latitude = request.data.get('latitude', '')
    #         longitude = request.data.get('longitude', '')

    #         # Update the user's location
    #         user_location.city = city
    #         user_location.region = region
    #         user_location.country = country
    #         user_location.latitude = latitude
    #         user_location.longitude = longitude
    #         user_location.save()

    #         return JsonResponse({"message": "Location updated successfully"}, status=200)
    #     except UserLocation.DoesNotExist:
    #         return JsonResponse({"error": "Location not found"}, status=404)
