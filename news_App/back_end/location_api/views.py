from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
from django.http import JsonResponse

class get_user_location(APIView):
    # Apply token authentication and permission checking
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("heloo")
        # Return user information (email and age)
        user_info = {"email": request.user.email}
        try:
            response = requests.get("http://ip-api.com/json/?fields=61439")
            if response.status_code == 200:
                data = response.json()
                user_info.update(data)
                return JsonResponse(user_info, status=200)
            else:
                return JsonResponse({"error": "Unable to fetch location data"}, status=500)
        except requests.RequestException as e:
            return JsonResponse({"error": str(e)}, status=500)
        
