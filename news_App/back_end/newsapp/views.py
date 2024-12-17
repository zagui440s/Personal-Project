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

class Sign_up(APIView):

    def post(self, request):
        request.data["username"] = request.data["email"]
        try:
            user = NewsUser.objects.create_user(**request.data)
            token = Token.objects.create(user=user)
            user_location = UserLocation(user=user, city="atx", region="texas", country="usa", latitude=22222222.222, longitude=22222222.22)
            user_location.full_clean()
            user_location.save()
            return Response({"user": user.email, "token": token.key}, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

class Log_in(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": user.email}, status=HTTP_200_OK)
        else:
            return Response({"error": "No user matching credentials, newsapp/ views.py, line 41"}, status=HTTP_404_NOT_FOUND)

class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email})

class Log_out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)


## adding comment before testing api